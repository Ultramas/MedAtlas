from django import forms
from .models import Post
from .models import ShowcasePost
from .models import Poste
from .models import MyModel
from .models import StaffApplication
from .models import Partner
from .models import PunishAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import Comment                
from .models import Contact
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
from .models import TextField
from .models import TextField2
from .models import TextField3
from .models import TextField4
from .models import TextField5
from .models import TextField6
from .models import TextField7
from .models import TextField8
from .models import BilletTextField
from .models import BilletTextField2
from .models import BilletTextField3
from .models import BilletTextField4
from .models import BilletTextField5
from .models import BilletTextField6
from .models import BilletTextField7
from .models import BilletTextField8
from .models import AboutTextField
from .models import AboutTextField2
from .models import AboutTextField3
from .models import AboutTextField4
from .models import AboutTextField5
from .models import AboutTextField6
from .models import AboutTextField7
from .models import AboutTextField8
from .models import BaseCopyrightTextField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import ProfileTwo
#from .models import PublicProfile

users = User.objects.filter()


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':
            '150 Characters or fewer. Letters, digits and @/./+/-/_ only.'
        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email address'}))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your password must be at least 8 characters.'}), label = 'Password')
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Please confirm your password.'}), label = 'Confirm Password')
   

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


CONTACT_PREFERENCE = [
    ('email', 'Email'),
    ('chat', 'Chat'),
    ('call', 'Call'),
]


class ContactForm(forms.ModelForm):
    prefered_contact = forms.MultipleChoiceField(
        choices=CONTACT_PREFERENCE, widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Contact
        fields = '__all__'


class MyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a catagory you want your idea to affect.'
        }))    
    image = forms.ImageField(widget=forms.TextInput(
        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = MyModel
        fields = '__all__'


class PostForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Choose a catagory you want your idea to affect.'
        }))
    image = forms.URLField(widget=forms.TextInput(
        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = ShowcasePost
        fields = '__all__'
        #name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))

        #description = forms.CharField(widget = forms.EmailInput
        #(attrs={'placeholder':'Enter your email'}))


class Postit(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a catagory you want your idea to affect.'
        }))
    image = forms.URLField(widget=forms.TextInput(
        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = Post    
        fields = '__all__'


class PosteForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a catagory you want your idea to affect.'
        }))
    image = forms.URLField(widget=forms.TextInput(
        attrs={'placeholder': 'Link an image url for your post.'}))

    class Meta:
        model = Poste
        fields = '__all__'



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

class StaffJoin(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Lime#6510'}))
    role = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'What role are you applying for?'
        }))
    I_have_been_in_MC_for_at_least_2_months = forms.BooleanField()
    I_have_been_in_a_previous_role_for_at_least_1_month = forms.BooleanField()
    I_can_attend_at_least_half_of_the_staff_meetings = forms.BooleanField()
    I_have_no_strikes_on_my_account_currently = forms.BooleanField()
    Why_do_you_want_to_apply_for_staff = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tell us why you want to be a MegaClan Staff Member. Be descriptive.'}))
    How_do_you_think_you_can_make_MC_better = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Tell us what you will do to make MC better as a staff member.'}))
    I_confirm_that_I_have_read_all_the_staff_requiernments_and_meet_all_of_them = forms.BooleanField()  

    class Meta:
        model = StaffApplication
        fields = '__all__'


class Server_Partner(forms.ModelForm):
  name = forms.CharField(max_length = 100, help_text='Your server name goes here.')
  catagory = forms.CharField(widget=forms.TextInput(
        attrs={
           'placeholder': 'Pick a catagory you feel your server represents (gaming, community, etc).'
        }))
  description = forms.CharField(help_text='Describe your server. Tell potential members why they should join.')
  server_invite = forms.URLField(help_text='Post your server invite link here.')
     
  class Meta:
      model = Partner
      fields = '__all__'

class Support(forms.ModelForm):
  name = forms.CharField(max_length = 100, help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
  catagory = forms.CharField(max_length = 200, help_text='Please let us know what type of issue you are dealing with.')
  issue = forms.CharField(help_text='Describe your issue in detail. We will try to get back to you as soon as possible.')
  Additional_comments = forms.CharField(help_text='Put any additional comments you may have here.')
  image = forms.URLField(help_text='Please attach a screenshot of your issue.')

     
  class Meta:
      model = Support
      fields = '__all__'
    
class PunishAppeal(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    Rule_broken = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tell us the numbers of the rule(s) you broke. Refer to our rules page to see the rules and their corresponding numbers.'
        }))
    Why_I_should_have_my_punishment_revoked = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Tell us why we should revoke your punishment, and what you can do to fix your mistake. If you think your punishment is a mistake, tell us why.'}))
    
    Additional_comments = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Put any additional evidence or comments you may have here.'}))

    class Meta:
        model = PunishAppeal
        fields = '__all__'

class BanAppeal(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    Rule_broken = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tell us the numbers of the rule(s) you broke. Refer to our rules page to see the rules and their corresponding numbers.'
        }))
    Why_I_should_have_my_punishment_revoked = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Tell us why we should revoke your ban, and what you can do to fix your mistake. If you think your ban is a mistake, tell us why.'}))
    
    Additional_comments = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Put any additional evidence or comments you may have here.'}))

    class Meta:
        model = BanAppeal
        fields = '__all__'


class ReportIssues(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Please let us know what type of issue this is.'
        })
        )
    issue = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Describe the issue in detail. We will try to get to it as soon as possible.'}))
    
    additional_comments = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Put any additional comments you may have here.'}))
    
    image = forms.FileField(help_text='Please put a screenshot of the issue.')

    class Meta:
        model = ReportIssue
        fields = '__all__'        


class News_Feed(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Please let us know what form of news this is.'
        }))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Write the news here.'}))
    
    image = forms.FileField(widget=forms.TextInput(
        attrs={'placeholder': 'Please provide a cover image for the news.'}))

    class Meta:
        model = NewsFeed
        fields = '__all__'        
        
class Staffprofile(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    position = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Please let us know what staff position you serve currently.'
        }))    
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Write whatever you want on your profile here (within regulations).'}))
    staff_feats = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Let us know of your transcendental feats of making MegaClan a better place.'
        })) 
    image = forms.FileField(widget=forms.TextInput(
        attrs={'placeholder': 'Please provide a cover image for your profile.'}))

    class Meta:
        model = StaffProfile
        fields = '__all__'


class Eventform(forms.ModelForm):

  name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'The event name goes here'}))
  catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Please let us know what type of event this is (tournament, stage night, etc).'}))
  description = forms.CharField(widget=forms.TextInput(
        attrs={
          'placeholder': 'Give a brief description of the event.'
          }))
  date_and_time = forms.DateTimeField( )
  image = forms.FileField(widget=forms.TextInput(
        attrs={'placeholder': 'Please provide a cover image for the event.'}))
        
  class Meta:
    model = Event
    fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'post', 'name', 'email', 'body', 'active'

#class EditProfileForm(forms.Form):
    #username = forms.CharField()
    #about_me = forms.CharField(widget=forms.Textarea())
    #image = forms.ImageField(required=False)

class SettingsForm(forms.ModelForm):     

    class Meta:
      model = SettingsModel
      fields = 'username', 'password', 'coupons', 'news'
      
class TextFielde(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = TextField
      fields = '__all__'

class TextFielde2(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = TextField2
      fields = '__all__'

class TextFielde3(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = TextField3
      fields = '__all__'

class TextFielde4(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = TextField4
      fields = '__all__'

class TextFielde5(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = TextField5
      fields = '__all__'

class TextFielde6(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = TextField6
      fields = '__all__'

class TextFielde7(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = TextField7
      fields = '__all__'

class TextFielde8(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = TextField8
      fields = '__all__'


class BilletTextFielde(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = BilletTextField
      fields = '__all__'

class BilletTextFielde2(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = BilletTextField2
      fields = '__all__'

class BilletTextFielde3(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = BilletTextField3
      fields = '__all__'

class BilletTextFielde4(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = BilletTextField4
      fields = '__all__'

class BilletTextFielde5(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = BilletTextField5
      fields = '__all__'

class BilletTextFielde6(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = BilletTextField6
      fields = '__all__'

class BilletTextFielde7(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = BilletTextField7
      fields = '__all__'

class BilletTextFielde8(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = BilletTextField8
      fields = '__all__'


class AboutTextFielde(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = AboutTextField
      fields = '__all__'

class AboutTextFielde2(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = AboutTextField2
      fields = '__all__'

class AboutTextFielde3(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = AboutTextField3
      fields = '__all__'

class AboutTextFielde4(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = AboutTextField4
      fields = '__all__'

class AboutTextFielde5(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = AboutTextField5
      fields = '__all__'

class AboutTextFielde6(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = AboutTextField6
      fields = '__all__'

class AboutTextFielde7(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = AboutTextField7
      fields = '__all__'

class AboutTextFielde8(forms.ModelForm):
#    image = forms.ImageField(widget=forms.TextInput(
#        attrs={'placeholder': 'Link an image for your post.'}))
  
    class Meta:
      model = AboutTextField8
      fields = '__all__'

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

from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    number = forms.IntegerField(required=False)
    exp_month = forms.IntegerField(required=False)
    expiry = forms.CharField(required=False)
    exp_year = forms.IntegerField(required=False)
    cvc = forms.IntegerField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class ProfileDetail(forms.Form):
 
    class Meta:
        model = ProfileDetails
        fields = '__all__'




#class PublicForm(forms.ModelForm):
    #class Meta:
        #model = PublicProfile
        #fields = ['username']


#class NewUserForm(UserCreationForm):
    #...

#class UserForm(forms.ModelForm):
   #...

#class ProfileFormv(forms.ModelForm):
	#class Meta: 
		#model = ProfileTwo
		#fields = ('products',)



from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields =(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit=False)
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
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )


class BilletBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a catagory you want your idea to affect.'
        }))
    image = forms.URLField(widget=forms.TextInput(
        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BilletBackgroundImage        
        fields = '__all__'


class TagBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a catagory you want your idea to affect.'
        }))
    image = forms.URLField(widget=forms.TextInput(
        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = TagBackgroundImage        
        fields = '__all__'

class StaffRanksBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a catagory you want your idea to affect.'
        }))
    image = forms.URLField(widget=forms.TextInput(
        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = StaffRanksBackgroundImage        
        fields = '__all__'

class MegaBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    catagory = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a catagory you want your idea to affect.'
        }))
    image = forms.URLField(widget=forms.TextInput(
        attrs={'placeholder': 'Link an image for your post.'}))

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