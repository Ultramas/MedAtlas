from datetime import timezone, timedelta, date
from urllib import request

import self
from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from django.contrib.admin.widgets import AutocompleteSelect
from mysite import settings
from . import admin
from .models import Idea, OrderItem, EmailField, Item, Questionaire, StoreViewType, LotteryTickets, Meme, TradeOffer, \
    FriendRequest, Game, CurrencyOrder, UploadACard, Room, InviteCode, InventoryObject, CommerceExchange, ExchangePrize, \
    Trade_In_Cards, DegeneratePlaylistLibrary, DegeneratePlaylist, Choice, CATEGORY_CHOICES, CONDITION_CHOICES, \
    SPECIAL_CHOICES, QuickItem, SpinPreference, TradeItem, PrizePool, BattleParticipant, BattleGame, Monstrosity, \
    MonstrositySprite, Ascension, InventoryTradeOffer, VoteOption, Bet, GameChoice, MyPreferences, GiftCode, GiftCodeRedemption
from .models import UpdateProfile
from .models import VoteQuery
from .models import StaffApplication
from .models import PartnerApplication
from .models import PunishmentAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import Shuffler
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import Comment
from .models import Contact
from .models import BusinessMailingContact
from .models import ProfileDetails
from .models import UserProfile2
from .models import Support
from .models import SettingsModel
from .models import BackgroundImage
from .models import EBackgroundImage
from .models import ShowcaseBackgroundImage
from .models import ChatBackgroundImage
from .models import BilletBackgroundImage
from .models import BlogBackgroundImage
from .models import PostBackgroundImage
from .models import RuleBackgroundImage
from .models import AboutBackgroundImage
from .models import FaqBackgroundImage
from .models import StaffBackgroundImage
from .models import InformationBackgroundImage
from .models import TagBackgroundImage
from .models import UserBackgroundImage
from .models import StaffRanksBackgroundImage
from .models import MegaBackgroundImage
from .models import EventBackgroundImage
from .models import NewsBackgroundImage
from .models import BaseCopyrightTextField
from .models import Battle
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxSelectMultiple

# from .models import ProfileTwo
# from .models import PublicProfile
users = User.objects.filter()


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '150 Characters or fewer. Letters, digits and @/./+/-/_ only.'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your email address'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password must be at least 8 characters.'}),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please confirm your password.'}),
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use. Please use a different email address.")
        return email


CONTACT_PREFERENCE = [
    ('email', 'Email'),
    ('chat', 'Chat'),
    ('call', 'Call'),
]


class ContactForm(forms.ModelForm):
    prefered_contact = forms.MultipleChoiceField(choices=CONTACT_PREFERENCE, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Contact
        fields = '__all__'


class BusinessContactForm(forms.ModelForm):
    prefered_contact = forms.MultipleChoiceField(choices=CONTACT_PREFERENCE, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = BusinessMailingContact
        fields = '__all__'


class PostForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name.'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your profile description.'}))

    class Meta:
        model = UpdateProfile
        fields = ('name', 'description', 'image')
        # name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))

        # description = forms.CharField(widget = forms.EmailInput
        # (attrs={'placeholder':'Enter your email'}))


class Postit(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name.'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Choose a category you want your idea to affect.'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please share any ideas you may have.'}))

    class Meta:
        model = Idea
        fields = ('name', 'category', 'description', 'image')


class VoteQueryForm(forms.ModelForm):
    class Meta:
        model = VoteQuery
        fields = ['description', 'category']

VoteOptionFormSet = inlineformset_factory(
    VoteQuery,
    VoteOption,
    fields=('text',),
    extra=2,
    can_delete=False
)

# Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


"""class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Write Your Review Here"}))

    class Meta:
        model = ProductReview
        fields = '__all__'"""


class ShippingForm(forms.ModelForm):
    class Meta:
        model = UserProfile2
        fields = ('first_name', 'last_name', 'address', 'city', 'state', 'country', 'zip_code', 'phone_number', 'profile_picture')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ShippingForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False
        self.fields['profile_picture'].required = False
        self.user = user

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        user_profile.city = self.cleaned_data['city']
        user_profile.state = self.cleaned_data['state']
        user_profile.phone_number = self.cleaned_data['phone_number']
        user_profile.profile_picture = self.cleaned_data['profile_picture']
        if commit:
            if hasattr(self.user, 'userprofile2') and self.user.userprofile2.exists():
                user_profile.save()
            else:
                user_profile.user = self.user
                user_profile.save()
        return user_profile


class StaffJoin(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Lemon Sauce'}))
    role = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What role are you applying for?'}))
    I_have_no_strikes_on_my_account_currently = forms.BooleanField()
    Why_do_you_want_to_apply_for_staff = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Tell us why you want to be a Accomfort Staff Member. Be descriptive.'}),
        label='Why do you want to apply for staff?'
    )
    How_do_you_think_you_can_make_PokeTrove_better = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Tell us what you will do to make Accomfort better as a staff member.'}),
        label='How do you think you can make PokeTrove better?'
    )
    I_confirm_that_I_have_read_all_the_staff_requirements_and_meet_all_of_them = forms.BooleanField(
        label='I confirm that I have read all the staff requirements and meet all of them'
    )

    class Meta:
        model = StaffApplication
        fields = ('name', 'role', 'I_have_no_strikes_on_my_account_currently',
                  'Why_do_you_want_to_apply_for_staff',
                  'overall_time_check', 'previous_role_time_check',
                  'How_do_you_think_you_can_make_PokeTrove_better',
                  'I_confirm_that_I_have_read_all_the_staff_requirements_and_meet_all_of_them')


class Server_Partner(forms.ModelForm):
    class Meta:
        model = PartnerApplication
        fields = (
            'user', 'name', 'category', 'multi_category', 'description', 'resume', 'requirement_check', 'policy_check',
            'voucher',)


class SupportForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name.'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please let us know what type of issue you are dealing with.'}))
    issue = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Describe your issue in detail. We will get back to you ASAP.'}))
    additional_comments = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Put any additional comments you may have here.'}))

    class Meta:
        model = Support
        fields = ('name', 'category', 'issue', 'Additional_comments', 'image',)


class PunishAppeale(forms.ModelForm):
    class Meta:
        model = PunishmentAppeal
        fields = ('name', 'Rule_broken', 'Why_I_should_have_my_punishment_revoked', 'Additional_comments',)


class BanAppeale(forms.ModelForm):
    class Meta:
        model = BanAppeal
        fields = ('name', 'Rule_broken', 'Why_I_should_have_my_ban_revoked', 'Additional_comments',)


class ReportIssues(forms.ModelForm):
    class Meta:
        model = ReportIssue
        fields = ('name', 'category', 'issue', 'Additional_comments', 'image',)


class News_Feed(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please let us know what form of news this is.'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write the news here.'}))
    image = forms.FileField(widget=forms.TextInput(attrs={'placeholder': 'Please provide a cover image for the news.'}))

    class Meta:
        model = NewsFeed
        fields = '__all__'


class Staffprofile(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    position = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please let us know what staff position you serve currently.'}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Write whatever you want on your profile here (within regulations).'}))
    staff_feats = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Let us know of your transcendental feats of making MegaClan a better place.'}))
    image = forms.FileField(
        widget=forms.TextInput(attrs={'placeholder': 'Please provide a cover image for your profile.'}))

    class Meta:
        model = StaffProfile
        fields = '__all__'


class Eventform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The event name goes here'}))
    category = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Please let us know what type of event this is (tournament, stage night, etc).'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Give a brief description of the event.'}))
    date_and_time = forms.DateTimeField()
    image = forms.FileField(
        widget=forms.TextInput(attrs={'placeholder': 'Please provide a cover image for the event.'}))

    class Meta:
        model = Event
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'post', 'name', 'email', 'body', 'active'


from django import forms
from django.forms import inlineformset_factory
from .models import Game, Choice


# used when the user wants to use their own cards; PokeTrove gets commission
class PlayerInventoryGameForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=PrizePool.objects.filter(is_active=1),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Available Prizes"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quantity_fields = {}
        for prize in PrizePool.objects.filter(is_active=1):
            field_name = f"quantity_{prize.id}"
            self.fields[field_name] = forms.IntegerField(
                label=f"Quantity for {prize.prize_name}",
                min_value=0,
                max_value=prize.number,
                required=False,
            )
            self.quantity_fields[prize.id] = field_name

    class Meta:
        model = Game
        fields = ['name', 'cost', 'discount_cost', 'type', 'category', 'image', 'power_meter', 'items']


# used when the user wants to use cards owned by PokeTrove; user gets commission

class InventoryGameForm(forms.ModelForm):
    choices = forms.ModelMultipleChoiceField(
        queryset=Choice.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Game
        fields = [
            'name', 'cost', 'discount_cost', 'type', 'category', 'image',
        ]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['rarity', 'lower_nonce', 'upper_nonce', 'number_of_choice']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

ChoiceFormSet = modelformset_factory(
    Choice,
    form=ChoiceForm,
    extra=0,
)


from django.utils.safestring import mark_safe

class TypeaheadSelectWidget(forms.Select):
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css',)
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js',
        )

    def render(self, name, value, attrs=None, renderer=None):
        # Render the default select widget.
        output = super().render(name, value, attrs, renderer)
        # Use the element's id to initialize Select2.
        element_id = attrs.get('id', 'id_%s' % name)
        js = f'''
        <script type="text/javascript">
            (function($) {{
                $(document).ready(function(){{
                    $('#{element_id}').select2({{
                        width: 'resolve',
                        placeholder: 'Select a choice',
                        allowClear: true
                    }});
                }});
            }})(django.jQuery);
        </script>
        '''
        return mark_safe(output + js)


class GameChoiceForm(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.all(),
        widget=TypeaheadSelectWidget,
        required=True
    )

    class Meta:
        model = GameChoice
        fields = '__all__'

class ToggleFavoriteForm(forms.Form):
    game_id = forms.IntegerField(widget=forms.HiddenInput())


class MyPreferencesForm(forms.ModelForm):
    class Meta:
        model = MyPreferences
        fields = ['spintype',]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MyPreferencesForm, self).__init__(*args, **kwargs)

        if self.user and not self.instance.pk:
            try:
                preferences = MyPreferences.objects.get(user=self.user)
                self.initial['spintype'] = preferences.spintype
                self.instance = preferences
            except MyPreferences.DoesNotExist:
                pass

class AscensionCreateForm(forms.ModelForm):
    class Meta:
        model = Ascension
        fields = []


class CardUploading(forms.ModelForm):
    class Meta:
        model = Choice
        fields = 'choice_text', 'file', 'category', 'tier', 'rarity', 'total_number_of_choice', 'value', 'number'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CardUploading, self).__init__(*args, **kwargs)


ChoiceFormSet = inlineformset_factory(Game, Choice, form=CardUploading, extra=1)


class GameAdminForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        daily = cleaned_data.get("daily")
        unlocking_level = cleaned_data.get("unlocking_level")

        if daily and not unlocking_level:
            raise ValidationError("An unlocking level must be set for daily games.")

        return cleaned_data


class BattleCreationForm(forms.ModelForm):
    game_values = forms.CharField(
        widget=forms.Textarea(attrs={'readonly': 'readonly'}),
        required=False,
        label="Game Quantities and Values"
    )
    total_value = forms.DecimalField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}),
        required=False,
        label="Total Value"
    )
    slots = forms.ChoiceField(
        choices=Battle.BATTLE_SLOTS,  # Use the model's defined choices
        widget=forms.RadioSelect,
        label="Battle Slots",
        initial='2'  # Default option
    )
    type = forms.ChoiceField(
        choices=Battle.BATTLE_TYPE,  # Use the model's defined choices
        widget=forms.RadioSelect,
        label="Battle Type",
        initial='Free For All'
    )

    class Meta:
        model = Battle
        fields = ['battle_name', 'chests', 'min_human_participants', 'slots', 'type', 'bets_allowed', 'game_values',
                  'total_value']
        widgets = {
            'chests': forms.SelectMultiple(attrs={'id': 'id_chests'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.initial['type'] = 'Free For All'

    def clean(self):
        cleaned_data = super().clean()
        chests = cleaned_data.get('chests')
        quantities = {}

        for game in chests:
            quantity_key = f'quantity-{game.id}'
            quantity = self.data.get(quantity_key, 1)  # Default to 1 if not provided
            if not quantity.isdigit() or int(quantity) < 1:
                raise forms.ValidationError(f"Invalid quantity for {game.name}.")
            quantities[game.id] = int(quantity)

        # Store quantities for use in save()
        self.cleaned_data['quantities'] = quantities
        return cleaned_data

    def save(self, commit=True):
        # Save the Battle instance first
        battle = super().save(commit=commit)
        quantities = self.cleaned_data.get('quantities', {})

        # Update or create BattleGame instances with the provided quantities
        for game in self.cleaned_data.get('chests'):
            qty = quantities.get(game.id, 1)
            # Use get_or_create to ensure that a BattleGame instance exists for this game/battle pair
            battle_game, created = BattleGame.objects.get_or_create(battle=battle, game=game)
            if battle_game.quantity != qty:
                battle_game.quantity = qty
                battle_game.save()

        # Optionally, recalc the total price (if using total_game_values in the template)
        battle.price = battle.total_game_values
        battle.save()

        return battle

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ('amount',)

    def __init__(self, *args, **kwargs):
        battle = kwargs.pop('battle', None)
        super().__init__(*args, **kwargs)

        if not battle:
            battle_id = getattr(self.instance, 'battle_id', None)
            if battle_id:
                battle = self.instance.battle
            elif 'battle' in self.initial:
                try:
                    battle = Battle.objects.get(pk=self.initial['battle'])
                except Battle.DoesNotExist:
                    battle = None

        if battle and (battle.type == 'teams' or battle.type == 'team_fight'):
            self.fields['winning_team'] = forms.ModelChoiceField(
                queryset=User.objects.all(),
                label="Winning Team",
                required=True
            )
        else:
            self.fields['winning_user'] = forms.ModelChoiceField(
                queryset=User.objects.all(),
                label="Winning User",
                required=True
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.instance.user
        if commit:
            instance.save()
        return instance


BattleGameFormSet = inlineformset_factory(
    parent_model=Battle,
    model=BattleGame,
    fields=['game', 'quantity'],
    extra=1,
    can_delete=True,
    widgets={
        'game': forms.Select(attrs={'class': 'form-control'}),
        'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
    }
)



class BattleJoinForm(forms.ModelForm):
    class Meta:
        model = BattleParticipant
        fields = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.battle = kwargs.pop('battle', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        # Ensure the user isn't already a participant in the battle
        if BattleParticipant.objects.filter(user=self.user, battle=self.battle).exists():
            raise forms.ValidationError("You are already a participant in this battle.")

        return cleaned_data

    def save(self, commit=True):
        # Create or retrieve the participant instance
        participant = super().save(commit=False)
        participant.user = self.user
        participant.battle = self.battle

        if commit:
            participant.save()
            # Add the participant to the battle's participants ManyToMany field
            self.battle.participants.add(participant)

        return participant


class MoveToTradeForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    fees = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    specialty = forms.ChoiceField(choices=SPECIAL_CHOICES, required=False)
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, initial="M", required=False)
    label = forms.CharField(max_length=1000, required=False)
    slug = forms.SlugField(required=False)
    value = forms.IntegerField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)
    image_length = forms.IntegerField(required=False)
    image_width = forms.IntegerField(required=False)
    length_for_resize = forms.IntegerField(required=False)
    width_for_resize = forms.IntegerField(required=False)

    class Meta:
        model = TradeItem
        fields = '__all__'


class AddTradeForm(forms.ModelForm):
    class Meta:
        model = InventoryObject
        fields = ('trade_locked',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddTradeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['add_trade_item'].queryset = InventoryObject.objects.filter(user=user)


class Trade_In_Form(forms.ModelForm):
    class Meta:
        model = Trade_In_Cards
        fields = ('card_name', 'card_image', 'card_condition',)


# class EditProfileForm(forms.Form):
# username = forms.CharField()
# about_me = forms.CharField(widget=forms.Textarea())
# image = forms.ImageField(required=False)


class SettingsForm(forms.ModelForm):
    class Meta:
        model = SettingsModel
        fields = ('username', 'password', 'email', 'coupons', 'news')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.instance.user
        if commit:
            instance.save()
        return instance


class BaseCopyrightTextFielde(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BaseCopyrightTextField
        fields = '__all__'


class BackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BackgroundImage
        fields = '__all__'


class BackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BackgroundImage
        fields = '__all__'


class EBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = EBackgroundImage
        fields = '__all__'


class ChatBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = ChatBackgroundImage
        fields = '__all__'


class ShowcaseBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = ShowcaseBackgroundImage
        fields = '__all__'


class BlogBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BlogBackgroundImage
        fields = '__all__'


class PostBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = PostBackgroundImage
        fields = '__all__'


class RuleBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = RuleBackgroundImage
        fields = '__all__'


class AboutBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = AboutBackgroundImage
        fields = '__all__'


class FaqBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = FaqBackgroundImage
        fields = '__all__'


class StaffBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = StaffBackgroundImage
        fields = '__all__'


class InformationBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = InformationBackgroundImage
        fields = '__all__'


class TagBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = TagBackgroundImage
        fields = '__all__'


class UserBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = UserBackgroundImage
        fields = '__all__'


class StaffRanksBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = StaffRanksBackgroundImage
        fields = '__all__'


class MegaBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = MegaBackgroundImage
        fields = '__all__'


class EventBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = EventBackgroundImage
        fields = '__all__'


class NewsBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = NewsBackgroundImage
        fields = '__all__'


class RoomSettings(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['public', 'logo']


class UploadCardsForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name of the card.'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UploadCardsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UploadACard
        fields = ('name', 'image', 'public',)


class InviteCodeForm(forms.ModelForm):
    class Meta:
        model = InviteCode
        fields = ['code', 'user', 'expire_time', 'permalink']  # Assuming these are your fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the current user if logged in
        user = self.request.user
        if user.is_authenticated:
            self.initial['user'] = user


from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
    ('C', 'Card')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(required=False,
                                                                              widget=CountrySelectWidget(attrs={
                                                                                  'class': 'custom-select d-block w-100'}))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(required=False, widget=CountrySelectWidget(
        attrs={'class': 'custom-select d-block w-100'}))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES, required=True)

    def __init__(self, *args, **kwargs):
        all_items_currency_based = kwargs.pop('all_items_currency_based', False)
        super(CheckoutForm, self).__init__(*args, **kwargs)
        if all_items_currency_based:
            self.fields['payment_option'].required = False
            self.fields['payment_option'].widget = forms.HiddenInput()


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo Code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))



class GiftCodeForm(forms.Form):
    code = forms.CharField(max_length=64)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get("code")

        try:
            gift_code = GiftCode.objects.get(code=code)
        except GiftCode.DoesNotExist:
            raise forms.ValidationError("Invalid gift code.")

        if gift_code.is_active != 1:
            raise forms.ValidationError("This gift code is inactive.")

        if gift_code.expiration_date and gift_code.expiration_date < timezone.now():
            gift_code.is_active = 0
            gift_code.save()
            raise forms.ValidationError("This gift code has expired.")

        redemptions = GiftCodeRedemption.objects.filter(user=self.user, gift_code=gift_code).count()
        if redemptions >= gift_code.uses:
            raise forms.ValidationError("You have already redeemed this gift code the maximum number of times.")

        return cleaned_data

class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    number = forms.IntegerField(required=False)
    exp_month = forms.IntegerField(required=False)
    expiry = forms.CharField(required=False)
    exp_year = forms.IntegerField(required=False)
    cvc = forms.IntegerField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class PaypalPaymentForm(forms.Form):
    # number = forms.IntegerField(required=True)
    number = forms.CharField(required=True)
    exp_month = forms.IntegerField(required=True)
    expiry = forms.CharField(required=True)
    exp_year = forms.IntegerField(required=True)
    cvc = forms.IntegerField(required=True)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class CurrencyCheckoutForm(forms.Form):
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CurrencyPaymentForm(forms.Form):
    number = forms.IntegerField(required=False)
    exp_month = forms.IntegerField(required=False)
    expiry = forms.CharField(required=False)
    exp_year = forms.IntegerField(required=False)
    cvc = forms.IntegerField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class CurrencyPaypalPaymentForm(forms.Form):
    # number = forms.IntegerField(required=True)
    number = forms.CharField(required=True)
    exp_month = forms.IntegerField(required=True)
    expiry = forms.CharField(required=True)
    exp_year = forms.IntegerField(required=True)
    cvc = forms.IntegerField(required=True)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


from .models import Withdraw

from django import forms
from .models import Withdraw, InventoryObject


class WithdrawForm(forms.ModelForm):
    selected_cards = forms.ModelMultipleChoiceField(
        queryset=InventoryObject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Withdraw
        fields = ['number_of_cards', 'shipping_state', 'fees', 'status', 'is_active']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['selected_cards'].queryset = InventoryObject.objects.filter(user=user)


class DegeneratePlaylistForm(forms.ModelForm):
    class Meta:
        model = DegeneratePlaylist
        fields = ['user', 'song', 'audio_file', 'audio_img', 'is_active', ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['song'].queryset = DegeneratePlaylistLibrary.objects.filter(user=user)


class TradeProposalForm(forms.ModelForm):
    class Meta:
        model = TradeOffer
        fields = ['title', 'trade_items', 'estimated_trading_value', 'user2', 'message', 'quantity', ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TradeProposalForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['trade_items'].queryset = TradeItem.objects.filter(user=user)


class InventoryTradeOfferResponseForm(forms.ModelForm):
    class Meta:
        model = InventoryTradeOffer
        fields = ['status']
        widgets = {
            'status': forms.RadioSelect(choices=[('accepted', 'Accept'), ('declined', 'Decline')]),
        }


class ExchangePrizesForm(forms.ModelForm):
    usercard = forms.ModelMultipleChoiceField(
        queryset=InventoryObject.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Items to Trade"
    )
    exchangeprizes = forms.ModelMultipleChoiceField(
        queryset=ExchangePrize.objects.filter(is_active=1),  # Only active prizes
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select Prizes"
    )

    class Meta:
        model = CommerceExchange  # Ensure this is the correct model
        fields = ['usercard', 'exchangeprizes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extract the user from kwargs
        super().__init__(*args, **kwargs)
        if user:
            self.fields['usercard'].queryset = InventoryObject.objects.filter(user=user)

        # Customize the label display for the usercard and exchangeprizes fields
        self.fields['usercard'].label_from_instance = self.get_usercard_label
        self.fields['exchangeprizes'].label_from_instance = self.get_exchangeprize_label

    def get_usercard_label(self, obj):
        """Define how InventoryObject details are displayed in the form."""
        return f"{obj.choice_text} - {obj.category} - ${obj.price} ({obj.condition})"

    def get_exchangeprize_label(self, obj):
        """Define how ExchangePrize details are displayed in the form."""
        return f"{obj.name} - ${obj.value} ({obj.condition})"

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('usercard') and not cleaned_data.get('exchangeprizes'):
            raise forms.ValidationError("You must select at least one item to trade or exchange.")
        return cleaned_data

    def save(self, commit=True):
        selected_usercards = self.cleaned_data.get('usercard', [])
        selected_exchangeprizes = self.cleaned_data.get('exchangeprizes', [])

        # Calculate total value of usercards and exchangeprizes
        total_usercard_value = sum([card.price for card in selected_usercards])
        total_exchangeprize_value = sum([prize.value for prize in selected_exchangeprizes])

        # Calculate the difference
        difference = total_usercard_value - total_exchangeprize_value

        # Get the user's ProfileDetails instance
        profile = ProfileDetails.objects.get(user=self.instance.user)

        # If the difference is positive, update the currency_amount
        if difference > 0:
            profile.currency_amount += difference
            profile.save()

        # Delete usercards from the inventory
        for usercard in selected_usercards:
            usercard.delete()

        # Add the selected prizes to the user's inventory
        for exchangeprize in selected_exchangeprizes:
            InventoryObject.objects.create(
                user=self.instance.user,  # Ensure the user is set
                choice=exchangeprize.prize,  # Assuming the ExchangePrize has a related prize Choice
                choice_text=exchangeprize.name,
                category=exchangeprize.prize.category,  # Assuming prize has a category field
                currency=exchangeprize.currency,
                price=exchangeprize.value,
                condition=exchangeprize.condition,
                image=exchangeprize.image,
                image_length=exchangeprize.image_length,
                image_width=exchangeprize.image_width,
                is_active=1,  # Set active by default
            )

        if commit:
            self.instance.save()  # Save the CommerceExchange instance
        return self.instance


class InventoryTradeForm(forms.ModelForm):
    trading_user = forms.ModelChoiceField(
        queryset=User.objects.none(),
        required=True,
        label="Select a User to Trade With"
    )
    usercard = forms.ModelMultipleChoiceField(
        queryset=TradeItem.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'usercard-checkbox'}),
        required=True,
        label="Select Your Items to Trade"
    )
    exchangeprizes = forms.ModelMultipleChoiceField(
        queryset=TradeItem.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'exchangeprizes-checkbox'}),
        required=True,
        label="Select Their Items to Trade"
    )

    class Meta:
        model = CommerceExchange
        fields = ['trading_user', 'usercard', 'exchangeprizes']

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Populate trading_user field with users who have active trade items
        self.fields['trading_user'].queryset = User.objects.filter(
            tradeitem__is_active=True
        ).distinct().exclude(id=current_user.id)

        # Populate usercard with current user's active trade items
        self.fields['usercard'].queryset = TradeItem.objects.filter(user=current_user, is_active=True)

        # Populate exchangeprizes with all active trade items
        self.fields['exchangeprizes'].queryset = TradeItem.objects.filter(is_active=True)


class AddMonstrosityForm(forms.ModelForm):
    class Meta:
        model = Monstrosity
        fields = ['monstrositysprite', 'monstrositys_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set a custom widget for displaying monstrositysprite options
        self.fields['monstrositysprite'].queryset = MonstrositySprite.objects.filter(is_active=1)
        self.fields['monstrositysprite'].widget = forms.RadioSelect(
            choices=[(sprite.id, sprite) for sprite in self.fields['monstrositysprite'].queryset],
        )


class FeedMonstrosityForm(forms.ModelForm):
    class Meta:
        model = Monstrosity
        fields = ['feed_amount',]

    def clean_currency_amount(self):
        currency_amount = self.cleaned_data['currency_amount']
        if currency_amount <= 0:
            raise forms.ValidationError("Currency amount must be positive.")
        return currency_amount


from .models import Endowment


class EndowmentForm(forms.Form):
    user = forms.CharField(widget=forms.HiddenInput())  # or use forms.ModelChoiceField if needed
    target = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name of Endowed Individual'}))
    order = forms.IntegerField(widget=forms.HiddenInput())  # Adjust widget/field type as needed

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if self.request:
            self.fields['user'].initial = self.request.user.username  # if using a CharField for username
            self.fields['target'].initial = User.objects.exclude(pk=self.request.user.pk).first().username
            # You can set an initial value for order if available

    def clean_user(self):
        username = self.cleaned_data.get('user')
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError('Invalid username. Please enter a valid user.')

    def save(self, commit=True):
        # Convert the 'user' field value to an actual user instance using clean_user.
        user = self.clean_user()
        # You might need to adjust target if it's a username or process it accordingly.
        instance = Endowment(
            user=user,
            target=self.cleaned_data['target'],
            order=self.cleaned_data['order']
        )
        if commit:
            instance.save()
        return instance


class HitStandForm(forms.Form):
    action = forms.ChoiceField(choices=[('hit', 'Hit'), ('stand', 'Stand')], label='Action')


class CreateChest(forms.ModelForm):
    class Meta:
        model = Shuffler
        fields = ('question', 'choice_text', 'file', 'choices', 'category', 'heat', 'shuffletype', 'demonstration',
                  'total_number_of_choice', 'cost',)
        readonly_fields = ('mfg_date',)


from .models import SellerApplication


class SellerApplicationForm(forms.ModelForm):
    class Meta:
        model = SellerApplication
        fields = ['first_name', 'last_name', 'age', 'identification', 'email']

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('age')
        today = date.today()
        if (today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))) < 18:
            raise ValidationError('You need to be 18 or older to apply to sell!')
        return dob


class ProfileDetail(forms.ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ('email', 'avatar', 'alternate', 'about_me')


class StoreViewTypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = StoreViewType
        fields = ('type',)

    def save(self, commit=True):

        user = self.request.user if self.request.user.is_authenticated else None

        storeviewtype = super().save(commit=False)

        # Set the user, star rating, and slug if available
        if user and isinstance(user, User):  # Check if user is a User instance
            storeviewtype.user = user
        else:
            storeviewtype.user = None  # Set to None if user is not a valid User instance

        if commit:
            storeviewtype.save()
        return storeviewtype


# class PublicForm(forms.ModelForm):
# class Meta:
# model = PublicProfile
# fields = ['username']


# class NewUserForm(UserCreationForm):
# ...

# class UserForm(forms.ModelForm):
# ...

# class ProfileForm(forms.ModelForm):
# class Meta:
# model = ProfileTwo
# fields = ('products',)


from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data["new_password1"]

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password',)


class BilletBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a category you want your idea to affect.'
        }))
    image = forms.ImageField(widget=forms.TextInput(
        attrs={'placeholder': 'Attach an image for your post.'}))

    class Meta:
        model = BilletBackgroundImage
        fields = '__all__'


class TagBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a category you want your idea to affect.'
        }))
    image = forms.ImageField(widget=forms.TextInput(
        attrs={'placeholder': 'Attach an image for your post.'}))

    class Meta:
        model = TagBackgroundImage
        fields = '__all__'


class StaffRanksBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Choose a category you want your idea to affect.'}))
    image = forms.ImageField(widget=forms.TextInput(attrs={'placeholder': 'Attach an image for your post.'}))

    class Meta:
        model = StaffRanksBackgroundImage
        fields = '__all__'


class MegaBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Choose a category you want your idea to affect.'}))
    image = forms.ImageField(widget=forms.TextInput(attrs={'placeholder': 'Attach an image for your post.'}))

    class Meta:
        model = MegaBackgroundImage
        fields = '__all__'


from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group

User = get_user_model()


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance


from django.core.mail import send_mail


class ContactForme(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {"name", "email", "inquiry", "message"}

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'e.g. Marinara Sauce'}),
            "email": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'e.g. Intellex@gmail.com'}),
            "inquiry": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Subject of your message.'}),
            "message": forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Your message.'})
        }

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg, from_email

    def send(self):
        subject, msg, from_email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=from_email,
            recipient_list=[settings.EMAIL_HOST_USER]
        )


class BusinessMailingForm(forms.ModelForm):
    class Meta:
        model = BusinessMailingContact
        fields = {"name", "email", "inquiry", "message"}

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'e.g. Liam Mannara'}),
            # get this instead of Contact.name in views
            "email": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'e.g. Intellex@gmail.com'}),
            "inquiry": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Your inquiry goes here.'}),
            "message": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Your message goes here.'})
        }

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg, from_email

    def send(self):
        subject, msg, to_email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email]
        )


from .models import Feedback

from django.contrib import admin
from django.contrib.auth.models import User


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('user', 'item', 'quantity', 'slug')
        # might want to replace item with order (check models)
        widgets = {
            # 'slug': forms.TextInput(attrs={'readonly': 'readonly'})
        }


class OrderItemAdmin(admin.ModelAdmin):
    form = OrderItemForm
    # readonly_fields = ('user', 'slug', 'item', 'quantity')


admin.site.register(OrderItem, OrderItemAdmin)

from .models import Wager


class WagerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Wager
        fields = ['amount']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if self.user_profile and self.user_profile.currency_amount < amount:
            raise forms.ValidationError("Insufficient funds for this bet.")
        return amount


class DirectedTradeOfferForm(forms.ModelForm):
    class Meta:
        model = TradeOffer
        fields = ['trade_status']  # or any other fields you want in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trade_status'].widget = forms.RadioSelect(choices=TradeOffer.TRADE_STATUS)

    def clean_direct_trade_offer(self):
        user = self.instance.user
        return user


class TradeOfferAcceptanceForm(forms.ModelForm):
    class Meta:
        model = TradeOffer
        fields = ['user', 'user2']


from django.core.exceptions import ValidationError


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'title', 'price', 'discount_price', 'specialty', 'label', 'slug', 'description', 'image')
        widgets = {
            # 'slug': forms.TextInput(attrs={'readonly': 'readonly'})
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        user = self.instance.user
        if Item.objects.filter(title=title, user=user).exists():
            raise ValidationError("You have already created an item with this title.")
        return title

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        discount_price = cleaned_data.get('discount_price')

        if discount_price is not None:
            fees = discount_price * 0.07
        else:
            fees = price * 0.07

        cleaned_data['fees'] = fees

        return cleaned_data


class QuickItemForm(forms.ModelForm):
    class Meta:
        model = QuickItem
        fields = ['image', 'image_length', 'image_width']


from .models import TradeItem

from .models import TradeOffer


class TradeItemForm(forms.ModelForm):
    class Meta:
        model = TradeItem
        fields = ['title', 'category', 'specialty', 'condition', 'slug', 'status', 'description', 'image']

    def __init__(self, *args, **kwargs):
        inventory_object = kwargs.pop('inventory_object', None)
        super().__init__(*args, **kwargs)

        # Pre-fill fields based on the provided InventoryObject
        if inventory_object:
            self.fields['title'].initial = inventory_object.title
            self.fields['category'].initial = inventory_object.category
            self.fields['specialty'].initial = inventory_object.specialty
            self.fields['condition'].initial = inventory_object.condition
            self.fields['description'].initial = inventory_object.description
            self.fields['image'].initial = inventory_object.image


class TradeProposalForm(forms.ModelForm):
    class Meta:
        model = TradeOffer
        fields = ['title', 'trade_items', 'estimated_trading_value', 'user2', 'message', 'quantity', ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TradeProposalForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['trade_items'].queryset = TradeItem.objects.filter(user=user)


class FriendRequestForm(forms.ModelForm):
    receiver = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'You can add friends with their username.'}))

    class Meta:
        model = FriendRequest
        fields = ['receiver']  # or any other fields you want in the form

    def clean_receiver(self):
        receiver_username = self.cleaned_data['receiver']
        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            raise ValidationError("User with this username does not exist.")
        return receiver


class FriendRequestAcceptanceForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ['sender', 'receiver']


from django import forms
from .models import RespondingTradeOffer, TradeOffer

from django.contrib.auth.decorators import login_required

# forms.py
from django import forms
from .models import TradeItem, RespondingTradeOffer

from .fields import UserRestrictedModelMultipleChoiceField


class RespondingTradeOfferForm(forms.ModelForm):
    offered_trade_items = UserRestrictedModelMultipleChoiceField(user=None, required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['offered_trade_items'].queryset = TradeItem.objects.filter(user=user)
        self.fields['offered_trade_items'].user = user

    class Meta:
        model = RespondingTradeOffer
        fields = ['estimated_trading_value', 'offered_trade_items', 'wanted_trade_items', 'message']


from django.utils import timezone


class TicketRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TicketRequestForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        user = self.user

        # Get the current time and the time at 5pm of the previous day
        now = timezone.now()  # Use timezone.now() instead of datetime.timezone.now()
        reset_time = now.replace(hour=17, minute=0, second=0)
        if now.hour < 17:
            reset_time -= timedelta(days=1)

        # Check if the user has already submitted a form since the reset time
        if LotteryTickets.objects.filter(user=user, mfg_date__gte=reset_time).exists():
            raise forms.ValidationError("You have already collected your daily ticket. Please try again after 5pm.")

        return cleaned_data

    class Meta:
        model = LotteryTickets
        fields = ('name',)


from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import get_user_model
from .models import Feedback

"""class FeedbackForm(forms.ModelForm):
    star_rating = forms.ChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Outstanding!'}))
    order = forms.ModelChoiceField(queryset=None)
    image = forms.ImageField(required=False)

    class Meta:
        model = Feedback
        fields = ('order', 'star_rating', 'comment', 'slug', 'image')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(initial=self.request.user.username)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['order'].queryset = OrderItem.objects.filter(user=self.request.user)

"""

from django import forms
from .models import Feedback
from .models import OrderItem

from django import forms
from django.utils.text import slugify
from django import forms
from .models import Feedback
from django import forms

from django import forms
from .models import Feedback

from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Feedback
        fields = ('order', 'star_rating', 'comment', 'slug', 'image')

    def save(self, commit=True):
        # Get the user who created the feedback
        user = self.request.user if self.request.user.is_authenticated else None

        # Create an instance of the Feedback model
        feedback = super().save(commit=False)

        if feedback.order and feedback.order.item:
            feedback.item = feedback.order.item
        if feedback.order:
            feedback.slug = feedback.order.slug

        # Set the user, star rating, and slug if available
        if user and isinstance(user, User):  # Check if user is a User instance
            feedback.username = user
        else:
            feedback.username = None  # Set to None if user is not a valid User instance

        if 'star_rating' in self.cleaned_data:
            feedback.star_rating = self.cleaned_data['star_rating']
        if 'slug' in self.cleaned_data:
            feedback.slug = self.cleaned_data['slug']

        # Set the 'image' field if an image file is provided
        if 'image' in self.cleaned_data:
            feedback.image = self.cleaned_data['image']

        if commit:
            feedback.save()
        return feedback


class FeedForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('order', 'star_rating', 'comment', 'slug', 'image')


class EmailForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'style': 'height: 50px;'}))

    class Meta:
        model = EmailField
        fields = ('email', 'confirmation')

    def clean_confirmation(self):
        confirmation = self.cleaned_data.get('confirmation')
        if not confirmation:
            raise forms.ValidationError("You must agree to the terms to continue.")
        return confirmation
        # name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))

        # description = forms.CharField(widget = forms.EmailInput
        # (attrs={'placeholder':'Enter your email'}))


class SpinPreferenceForm(forms.ModelForm):
    class Meta:
        model = SpinPreference
        fields = ['quick_spin']


class QuestionForm(forms.Form):
    text = forms.CharField(max_length=255)

    answer_choices = forms.MultipleChoiceField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'dynamic-input'}),
        choices=[],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a field for answer choices when the question type is 'Multiple Choice'
        if self.instance.form_type == 'option1':
            self.fields['answer_choices'] = forms.CharField(
                label='Answer Choices (comma-separated)',
                required=True,
                widget=forms.TextInput(attrs={'placeholder': 'Choice 1, Choice 2, ...'}),
            )


class QuestionCountForm(forms.Form):
    num_questions = forms.IntegerField(label="Number of Questions", )
    form_name = forms.CharField()

    class Meta:
        model = Questionaire
        fields = {"form_name", "form_text", "text"}


from .models import Answer


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', [])
        super(AnswerForm, self).__init__(*args, **kwargs)

        for question in questions:
            field_name = f'answer_{question.id}'
            self.fields[field_name] = forms.CharField(
                label=question.text,
                required=True,
                widget=forms.TextInput(attrs={'class': 'form-control'})
            )


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['title', 'image']