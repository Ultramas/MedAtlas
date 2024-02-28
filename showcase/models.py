import string
import uuid
from uuid import uuid4
from venv import logger

from PIL import Image
# from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max, F, Count
from django.dispatch import receiver
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from pydantic import ValidationError
from django.contrib.auth.models import Group

# from image.utils import render

CATEGORY_CHOICES = (
    ('G', 'Gold'),
    ('P', 'Platinum'),
    ('E', 'Emerald'),
    ('D', 'Diamond'),
)

SPECIAL_CHOICES = (
    ('F', 'Featured'),
    ('P', 'Popular'),
    ('PR', 'Premium'),
    ('LE', 'Limited Edition'),
)

CONDITION_CHOICES = (
    ('M', 'Mint'),
    ('NM', 'Near Mint'),
    ('MP', 'Moderately Played'),
    ('HP', 'Heavily Played'),
    ('D', 'Damaged'),
)

LABEL_CHOICES = (
    ('N', 'New'),
    ('BS', 'Best Seller'),
    ('BV', 'Best Value'),
)

SHUFFLE_CHOICES = (
    ('L', 'Luck'),
    ('S', 'Skill'),
    ('G', 'Grade'),
)

AVALIABLE_CHOICES = (
    ('OP', 'One Player'),
    ('PVP', 'Player Versus Player'),
    ('MP', 'Multiple Players'),
    ('T', 'Tournament'),
    ('OE', 'Other Event'),
    ('L', 'Limited'),
    ('D', 'Drop'),
)

GAME_MODE = (
    ('STW', 'Spin The Wheel'),
    ('OB', 'Open Box'),
    ('OP', 'Open Pack'),
    ('SR', 'Spin Roulette'),
)

TYPE_CHOICES = (('S', 'Singles'), ('BP', 'Booster Pack'),
                ('BB', 'Booster Box'), ('PP', 'Pokemon Product'), ('O',
                                                                   'Other'))

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

BLOG_TYPE_CHOICES = (
    ('F', 'Featured'),
    ('N', 'New'),
    ('P', 'Popular'),
    ('EC', "Editor's Choice"),
)

HEAT = (
    ('M', 'Mild'),
    ('S', 'Spicy'),
    ('F', 'Fiery'),
    ('W', 'Wild'),
    ('E', 'Explosive'),
)

PRIVACY = (
    ('PUB', 'Public'),
    ('PRI', 'Private'),
)

LEVEL = (
    ('C', 'Common'),
    ('U', 'Uncommon'),
    ('R', 'Rare'),
    ('E', 'Epic'),
    ('M', 'Mythical'),
    ('T', 'Transcendent'),
    ('P', 'Primordial'),
    ('L', 'Legendary'),
    ('U', 'Ultimate'),
)

PRACTICE = (
    ('P', 'Practice'),
    ('R', 'Real'),
)

MEMBERSHIP_TIER = (
    ('S', 'Sapphire'),
    ('R', 'Ruby'),
    ('E', 'Emerald'),
    ('D', 'Diamond'),
    ('?', '???'),
)

BLACKJACK_OUTCOME = (
    ('W', 'Win'),
    ('L', 'Lose'),
    ('D', 'Draw'),
    ('B', 'BlackJack'),
)

GAMETYPE = (
    ('T', 'Traditional'),
    ('C', 'Club'),
)

GAMEHUB_CHOICES = (
    ('F', 'Featured'),
    ('P', 'Popular'),
    ('N', 'New'),
)


class Idea(models.Model):
    """Model for sharing ideas and getting user feedback"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Your name goes here.')
    category = models.CharField(max_length=100,
                                help_text='Choose a category you want your idea to affect (server layout, event idea, etc).')
    profile_number = models.PositiveIntegerField(default=0, editable=False)
    description = models.TextField(help_text='Please share any ideas you may have.')
    image = models.ImageField(help_text='Attach an image for your idea (scales to your picture`s dimensions).')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Idea"
        verbose_name_plural = "Ideas"

    def save(self, *args, **kwargs):
        if not self.pk:
            max_message_number = Idea.objects.aggregate(max_message_number=models.Max('profile_number'))[
                                     'max_message_number'] or 0

            # Increment the maximum message number to get the new message number
            self.profile_number = max_message_number + 1
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.user).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"http://127.0.0.1:8000/share/#{str(self.profile_number)}"

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class UpdateProfile(models.Model):
    """Update user profiles"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Your name goes here.')
    description = models.TextField(help_text='Your profile description goes here.')
    profile_number = models.PositiveIntegerField(default=0, editable=False)
    date_and_time = models.DateTimeField(null=True, verbose_name="time and date", auto_now_add=True)
    image = models.ImageField(help_text='Attach an image for your profile (scales to your picture`s dimensions.)')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "User Profile Post"
        verbose_name_plural = "User Profile Posts"

    def save(self, *args, **kwargs):
        if not self.pk:
            max_message_number = UpdateProfile.objects.aggregate(max_message_number=models.Max('profile_number'))[
                                     'max_message_number'] or 0

            # Increment the maximum message number to get the new message number
            self.profile_number = max_message_number + 1
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.user).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"http://127.0.0.1:8000/showcase/#{str(self.profile_number)}"

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class PrizePool(models.Model):
    prize_name = models.CharField(max_length=500, verbose_name="Prize Name")
    image = models.FileField(upload_to='images/', verbose_name="Prize Image")
    number = models.IntegerField(default=1, verbose_name="Number of Prize")
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.prize_name)

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"


class Choice(models.Model):
    """Used for voting on different new ideas"""
    # question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='Choice Text')
    file = models.FileField(null=True, verbose_name='File')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    votes = models.IntegerField(default=0)
    category = models.CharField(max_length=100,
                                help_text='Category of choice (Pokemon, trainers, etc.).')
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    tier = models.CharField(choices=LEVEL, max_length=1, blank=True, null=True)
    rarity = models.DecimalField(max_digits=7, decimal_places=4, help_text="Rarity of choice in percent (optional).",
                                 blank=True, null=True, verbose_name="Rarity (%)")
    prizes = models.ForeignKey(PrizePool, on_delete=models.CASCADE, blank=True, null=True)
    lower_nonce = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        validators=[MaxValueValidator(999999), MinValueValidator(0)],
        help_text="Lower bound nonce of Choice",
        blank=True,
        null=True
    )
    upper_nonce = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        validators=[MaxValueValidator(999999), MinValueValidator(0)],
        help_text="Upper bound nonce of Choice",
        blank=True,
        null=True
    )
    nodes = models.IntegerField(help_text="Number of the choice included", blank=True, null=True, )
    value = models.DecimalField(max_digits=12, decimal_places=2, help_text="Value of item in Rubicoins.", blank=True,
                                null=True, verbose_name="Value (Rubicoins)")
    number = models.IntegerField(help_text="Position in rarity (ordered by value)")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        if self.prizes:
            return str(self.choice_text) + ' with prize ' + str(self.prizes)
        else:
            return str(self.choice_text)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"


class PollQuestion(models.Model):
    question_text = models.CharField(max_length=500, verbose_name="Question")
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.question_text)

    class Meta:
        verbose_name = "Poll Question"
        verbose_name_plural = "Poll Questions"


class Inventory(models.Model):
    """Model for sharing ideas and getting user feedback"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Inventory Name",
                            help_text="Name your inventory. Leave blank to use (your name)'s inventory", blank=True,
                            null=True)
    image = models.ImageField(help_text='Inventory Image.')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.user}'s inventory"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Player Inventory"
        verbose_name_plural = "Player Inventories"


class InventoryObject(models.Model):
    """Model for sharing ideas and getting user feedback"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=True, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='Choice Text', blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.user) + "'s " + str(self.choice)

    def save(self, *args, **kwargs):
        if self.choice:
            self.choice_text = self.choice.choice_text
            self.image = self.choice.file
            self.image_length = self.choice.image_length
            self.image_width = self.choice.image_width
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Player Inventory Object"
        verbose_name_plural = "Player Inventory Objects"


class Vote(models.Model):
    """Used for voting on different new ideas"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Your name goes here.')
    description = models.TextField()
    category = models.CharField(max_length=100,
                                help_text='Type the category that you are voting on (server layout, event idea, administration position, etc).')
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.user).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class EmailField(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True,
                              help_text="Sign up for our newsletter to get the latest news and gossip! We will never share your personal information with anyone without your explicit permission. Unsubscribe at any time. ")
    confirmation = models.BooleanField(
        help_text="By clicking this box, I agree to receive emails, coupons and discounts from PokeTrove. I also understand that I may unsubscribe at any time and PokeTrove will not share my personal information with anyone without my explicit permission.")
    # username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"


class Product(models.Model):
    """A product in the storefront"""
    name = models.CharField(max_length=200)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")
    description = models.TextField()
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1000)  # can use for cataloging products
    mfg_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=[('b', 'Bad'), ('a', 'Average'), ('e', 'Excellent')])

    def __str__(self):
        return self.name

    def show_desc(self):
        return self.description[:50]


class City(models.Model):
    """Not currently used. NEEDS TO BE DELETED"""
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class SearchResult(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()


class StaffApplication(models.Model):
    """For applying for staff"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, help_text='Your full name goes here.')
    strikes_check = models.BooleanField(
        verbose_name="I have no strikes on my account currently",
        default=False,
        choices=((True, 'Yes'), (False, 'No'))
    )
    role = models.TextField(help_text='What role are you applying for?', verbose_name="Roles")
    resume = models.FileField(help_text='Your Resume', verbose_name="Resume")
    why = models.TextField(
        help_text='Tell us why you want to be an Accomfort Staff Member. Be descriptive.',
        verbose_name="Why do you want to apply for staff?"
    )
    how_better = models.TextField(
        help_text='Tell us what you will do to make Accomfort better as a staff member.',
        verbose_name="How do you think you can make Accomfort better?"
    )
    read_requirements = models.BooleanField(
        verbose_name="I confirm that I have read all the staff requirements and meet all of them.",
        default=False,
        choices=((True, 'Yes'), (False, 'No'))
    )
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.role + " submitted by " + str(self.user)

    class Meta:
        verbose_name = "Staff Application"
        verbose_name_plural = "Staff Applications"


class PartnerApplication(models.Model):
    """Application to partner with the server"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, help_text='Your server name goes here.')
    category = models.CharField(
        max_length=100,
        help_text='Pick a category you feel your server represents (gaming, community, etc).'
    )
    description = models.TextField(help_text='Describe your server. Tell potential members why they should join.')
    server_invite = models.URLField(help_text='Idea your server invite link here.')
    is_active = models.IntegerField(
        default=1,
        blank=True,
        null=True,
        help_text='1->Active, 0->Inactive',
        choices=((1, 'Active'), (0, 'Inactive')),
        verbose_name="Set active?"
    )

    class Meta:
        verbose_name = "Partner Application"
        verbose_name_plural = "Partner Applications"

    def __str__(self):
        return self.name + "'s website at: " + self.server_invite


class PunishmentAppeal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Your name and tag go here.')
    Rule_broken = models.CharField(max_length=200,
                                   help_text='Tell us the numbers of the rule(s) you broke. Refer to our rules page to see the rules and their corresponding numbers.',
                                   verbose_name="rule broken")
    Why_I_should_have_my_punishment_revoked = models.TextField(
        help_text='Tell us why we should revoke your punishment, and what you can do to fix your mistake. If you think your punishment is a mistake, tell us why.',
        verbose_name="Why I should have my punishment revoked")
    Additional_comments = models.TextField(help_text='Put any additional evidence or comments you may have here.',
                                           verbose_name="additional comments")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.Why_I_should_have_my_punishment_revoked + " submitted by " + str(self.user)

    class Meta:
        verbose_name = "Punishment Appeal"
        verbose_name_plural = "Punishment Appeals"


class BanAppeal(models.Model):
    name = models.CharField(max_length=100, help_text='Your name and tag go here.')
    Rule_broken = models.CharField(max_length=200,
                                   help_text='Tell us the numbers of the rule(s) you broke. Refer to our rules page to see the rules and their corresponding numbers.')
    Why_I_should_have_my_ban_revoked = models.TextField(
        help_text='Tell us why we should unban you, and tell us you can do to fix your mistake. If you think your punishment is a mistake, tell us why.',
        verbose_name="Why I should have my ban revoked.")
    Additional_comments = models.TextField(
        help_text='Put any additional evidence or comments you may have here.')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.Why_I_should_have_my_ban_revoked + " submitted by " + str(self.name)

    class Meta:
        verbose_name = "Ban Appeal"
        verbose_name_plural = "Ban Appeals"


class ReportIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,
                            help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
    category = models.CharField(max_length=200, help_text='Please let us know what type of issue this is.')
    issue = models.TextField(help_text='Describe the issue in detail. We will try to get to it as soon as possible.')
    Additional_comments = models.TextField(help_text='Put any additional comments you may have here.',
                                           verbose_name="additional comments")
    image = models.ImageField(help_text='Please put a screenshot of the issue.')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    anonymous = models.BooleanField(default=False, help_text="Report issue anonymously?")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.issue + " reported by " + str(self.user)

    # class Changelog(models.Model):
    #  name = models.CharField(max_length = 100, help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
    #  category = models.CharField(max_length = 200, help_text='Please let us know what type of issue this is.')
    #  issue = models.TextField(help_text='Describe the issue in detail. We will try to get to it as soon as possible.')
    #  Additional_comments = models.TextField(help_text='Put any additional evidence or comments you may have here.')
    #  image = models.FileField(help_text='Please put a screenshot of the issue.')

    class Meta:
        verbose_name = "Report Issue"
        verbose_name_plural = "Report Issues"

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.user).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class Support(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,
                            help_text='Your name and tag go here.')
    category = models.CharField(max_length=200, help_text='Please let us know what type of issue you are dealing with.')
    issue = models.TextField(
        help_text='Describe your issue in detail. We will try to get back to you as soon as possible.')
    Additional_comments = models.TextField(help_text='Put any additional comments you may have here.',
                                           verbose_name="additional comments")
    image = models.ImageField(help_text='Please attach a screenshot of your issue.', null=True, blank=True)
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.issue + " submitted by " + str(self.user)

    class Meta:
        verbose_name = "Customer Support"
        verbose_name_plural = "Customer Support"


class NewsFeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,
                            help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
    title = models.TextField(help_text='Write the news headline here.', verbose_name="News Headline")
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=200, help_text='Please let us know what form of news this is.')
    description = models.TextField(help_text='Write the news here.')
    image = models.ImageField(help_text='Please provide a cover image for the news.')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    date_and_time = models.DateTimeField(null=True, verbose_name="time and date")
    position = models.IntegerField(verbose_name="Image Position", default=1)
    anonymous = models.BooleanField(default=False, help_text="Remain anonymous? (not recommended)")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title + " authored by " + str(self.user)

    class Meta:
        verbose_name = "News Feed"
        verbose_name_plural = "News Feed"

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the associated ProfileDetails for the user
            profile = ProfileDetails.objects.filter(user=self.user).first()

            # Set the position to the position value from the associated ProfileDetails
            # if profile:
            # self.position = profile.position

        print("Position before save:", self.position)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):

    # return reverse("showcase:news", kwargs={"slug": str(self.slug)})

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class StaffProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,
                            help_text='Your name goes here. If you wish to stay anonymous, put "Anonymous".')
    role_position = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Position")
    description = models.TextField(help_text='Write whatever you want on your profile here (within regulations).')
    staff_feats = models.TextField(
        help_text='Let us know of your transcendental feats of making PokeTrove a better place.',
        verbose_name="Staff feats")
    date_and_time = models.DateTimeField(null=True, verbose_name="Time and date of Staff Profile Creation")
    image = models.ImageField(help_text='Please provide a cover image for your profile.')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Staff Profile"
        verbose_name_plural = "Staff Profiles"

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.user).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        # If a profile already exists for this user, update it
        try:
            existing = StaffProfile.objects.get(user=self.user)
            self.pk = existing.pk  # set this instance's pk to the existing profile's pk
        except StaffProfile.DoesNotExist:
            pass  # No existing profile, so we're creating a new one

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class SocialMedia(models.Model):
    social = models.TextField(verbose_name="Social Media Platform", help_text="Follow format 'logo-{platform name}'",
                              blank=True, null=True)
    icon = models.ImageField(verbose_name="Social Media Logo", blank=True, null=True)
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Width of the image (in percent relative).',
                                              verbose_name="image width")
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Length of the image (in percent relative).',
                                               verbose_name="image length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resize Width")
    height_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resize Height")
    image_position = models.IntegerField(help_text='Positioning of the image.', verbose_name='Position', blank=True,
                                         null=True)
    alternate = models.TextField(verbose_name="Alternate Text", blank=True, null=True)
    page = models.TextField(verbose_name="Page Name")
    hyperlink = models.URLField(verbose_name="Hyperlink")
    staff_profile = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.social + " in " + self.page

    def save(self, *args, **kwargs):
        if not self.page.endswith('.html'):
            self.page += '.html'
        if not self.pk:  # Check if this is a new object
            self.image_position = SocialMedia.objects.filter(page=self.page).count() + 1
        if self.icon and not self.alternate:  # Check if an image exists and alternate text is not set
            self.alternate = str(self.icon)  # Set the alternate text to the string version of the image name
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"


class FrequentlyAskedQuestions(models.Model):
    question = models.TextField()
    position = models.IntegerField(help_text='Positioning of the image within the carousel.',
                                   verbose_name='position', default=1)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Frequently-Asked Question"
        verbose_name_plural = "Frequently-Asked Questions"


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Event name goes here.')
    category = models.CharField(max_length=200,
                                help_text='Please let us know what type of event this is (tournament, stage night, etc).')
    numeric_quantifier = models.FloatField()
    qualitative_qualifier = models.CharField(max_length=500)
    description = models.TextField(help_text='Give a brief description of the event.')
    date = models.DateField(null=True, help_text='Event date (day, date, and month)')
    time = models.TimeField(null=True, help_text='Event time (hour/minute)')
    date_and_time = models.DateTimeField(null=True, verbose_name="Time and date of Event Creation")
    section = models.IntegerField(verbose_name="Page Section", blank=True, null=True)
    page = models.TextField(verbose_name="Page Name")
    slug = models.SlugField()
    anonymous = models.BooleanField(default=False, help_text="Remain anonymous? (not recommended)")
    image = models.ImageField(help_text='Please provide a cover image for the event.', upload_to='images/')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.name + " hosted by " + str(self.user)

    def save(self, *args, **kwargs):
        if not self.page.endswith('.html'):
            self.page += '.html'
        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.user).first()
            self.section = Event.objects.filter(page=self.page).count() + 1

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position
        super().save(*args, **kwargs)

    def get_profile_url(self):
        return reverse('showcase:eventmore', args=[str(self.slug)])

    def get_profile_url2(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class BusinessMessageBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Business Message Background Image"
        verbose_name_plural = "Business Message Background Images"


class MemberHomeBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Member Home Background Image"
        verbose_name_plural = "Member Home Background Images"


class PatreonBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Patreon Background Image"
        verbose_name_plural = "Patreon Background Images"


class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Your username goes here.')
    category = models.CharField(max_length=100,
                                help_text='Pick a category you feel your server represents (gaming, community, etc).')
    description = models.TextField(help_text='Describe your server. Tell potential members why they should join.')
    server_invite = models.URLField(help_text='Post your server invite link here.')
    anonymous = models.BooleanField(default=False, help_text="Remain anonymous? (not recommended)")

    def __str__(self):
        return str(self.user) + " " + self.server_invite

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.user).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class Patreon(models.Model):
    patreon_username = models.CharField(max_length=100, verbose_name='Patreon`s Username',
                                        help_text='The patreon`s username goes here.')
    description = models.TextField(help_text='Description of Patreon`s patreonage.')
    image = models.ImageField(
        help_text=
        'The patreon`s avatar goes here.')

    # change rest to either imagefields or urlfields (has to be uniform throughout the form)

    # widget=form.TextInput, help_text='Your name goes here.'
    class Meta:
        verbose_name = "Patreon"
        verbose_name_plural = "Patreons"


class BlogHeader(models.Model):
    category = models.CharField(max_length=200, verbose_name="Category")
    image = models.ImageField(upload_to='images/')
    position = models.IntegerField(verbose_name="Position", default=1)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    class Meta:
        verbose_name = "Blog Header"
        verbose_name_plural = "Blog Headers"

    def __str__(self):
        return self.category


from django.template.defaultfilters import slugify, random, date


class BlogFilter(models.Model):
    blog_filter = models.CharField(verbose_name="Hashtag filters", max_length=200, blank=True, null=True)
    clicks = models.IntegerField(verbose_name="Popularity", blank=True, null=True)
    image = models.ImageField(verbose_name="Filter Image", blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.blog_filter

    class Meta:
        verbose_name = "Blog Filter"
        verbose_name_plural = "Blog Filters"


class Blog(models.Model):
    """Each blog post"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(choices=BLOG_TYPE_CHOICES, max_length=2, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True, verbose_name="updated on: ")
    content = models.TextField()
    filters = models.ForeignKey(BlogFilter, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name="Hashtag filters")
    created_on = models.DateTimeField(auto_now_add=True)
    position = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(BlogHeader, verbose_name="Category", on_delete=models.CASCADE, blank=True, null=True,
                                 help_text="Optional")
    minute_read = models.IntegerField(verbose_name="Time to read (in minutes)", blank=True, null=True)
    status = models.IntegerField(choices=((0, "Draft"), (1, "Publish")), default=0)
    image = models.ImageField(upload_to='images/')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    likes = models.ManyToManyField(User, blank=True, verbose_name='post likes')
    # likes = models.IntegerField(default=0)
    dislikes = models.ManyToManyField(User, blank=True, verbose_name='post dislikes', related_name="post_dislikes")
    # url = models.SlugField(max_length=200, unique=True, blank=True)
    # blogbackgroundimage
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ['-created_on']

    #    def save(self, *args, **kwargs):
    #        self.url = slugify(self.title)
    #        super(Blog, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)

        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.author_id).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position
            max_position = Blog.objects.all().aggregate(Max('position'))['position__max']
            if max_position is None:  # if there are no other blog posts
                self.position = 1
            else:
                self.position = max_position + 1
        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.author_id).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("showcase:post_detail", kwargs={"slug": str(self.slug)})

    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    def view_count(self):
        return Blog.objects.filter(post=self).count()

    # def number_of_likes(self):
    #    return self.likes.count()
    def delete(self, *args, **kwargs):
        # Get all Blog objects with a position greater than the one being deleted
        blogs_to_update = Blog.objects.filter(position__gt=self.position)

        # Delete the object
        super().delete(*args, **kwargs)

        # Decrement the position of each remaining object
        for i, blog in enumerate(blogs_to_update.order_by('position')):
            blog.position = self.position + i
            blog.save()


class Currency(models.Model):
    name = models.CharField(default='Rubiaces', max_length=200)
    flavor_text = models.CharField(max_length=200)
    file = models.FileField(null=True, verbose_name='Sprite')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "PokeTrove Currency"
        verbose_name_plural = "PokeTrove Currencies"


class CurrencyMarket(models.Model):
    name = models.CharField(max_length=200)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    unit_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deal = models.BooleanField(default=False)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1000, blank=True,
                             null=True)  # can use for cataloging products
    flavor_text = models.CharField(max_length=200)
    file = models.FileField(null=True, verbose_name='Sprite')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("showcase:currencyproduct", kwargs={'slug': self.slug})

    def currency_get_add_to_cart_url(self):
        return reverse("showcase:currency-add-to-cart", kwargs={'slug': self.slug})

    def currency_get_remove_from_cart_url(self):
        return reverse("showcase:currency-remove-from-cart", kwargs={'slug': self.slug})

    def get_profile_url(self):
        return reverse('showcase:product', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if self.amount != 0:  # Avoid division by zero
            self.unit_ratio = self.price / self.amount
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Currency Market"
        verbose_name_plural = "Currency Markets"


class CurrencyOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()
    items = models.OneToOneField(CurrencyMarket, on_delete=models.CASCADE)
    itemhistory = models.ForeignKey(CurrencyMarket, on_delete=models.CASCADE, verbose_name="Order history", null=True,
                                    related_name='currency_item_history')
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('Address', related_name='currency_shipping_address', on_delete=models.SET_NULL,
                                         blank=True, null=True)
    billing_address = models.ForeignKey('Address', related_name='currency_billing_address', on_delete=models.SET_NULL,
                                        blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    id = uuid4()
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active order?")
    '''
   1. Item added to cart
   2. Adding a billing address
   (Failed checkout)
   3. Payment
   (Preprocessing, processing, packaging etc.)
   4. Being delivered
   5. Received
   6. Refunds
   '''

    def __str__(self):
        return self.user.username
        if not self.id:  # Newly created object, so set slug
            self.slug = slugify(self.market.slug)
        super(CurrencyOrder, self).save(*args, **kwargs)

    def get_total_item_price(self):
        if self.items.discount_price:
            return self.quantity * self.get_discount_item_price()
        return self.quantity * self.items.price

    def get_discount_item_price(self):
        return self.quantity * self.items.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def currency_get_add_to_cart_url(self):
        return reverse("showcase:currency-add-to-cart", kwargs={'slug': self.slug})

    def currency_get_remove_from_cart_url(self):
        return reverse("showcase:currency-remove-from-cart", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.items.discount_price:
            self.amount = self.items.discount_price
        else:
            self.amount = self.items.price
        super().save(*args, **kwargs)

    def get_total_price(self):
        total = 0
        total += self.items.price  # or another field representing the item's price
        if self.coupon:
            if self.coupon.percentDollars:
                total *= 1 - (0.01 * self.coupon.amount)
            else:
                total -= self.coupon.amount
        return total

    def get_final_price(self):
        if self.items.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()

    def get_profile_url(self):
        return reverse('showcase:profile', args=[str(self.slug)])

    def get_profile_url2(self):
        return reverse('showcase:currencymarket', args=[str(self.slug)])

    class Meta:
        verbose_name = "Individiual Currency Order"
        verbose_name_plural = "Individiual Currency Orders"


class CurrencyFullOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(CurrencyOrder)
    itemhistory = models.ForeignKey(CurrencyMarket, on_delete=models.CASCADE, verbose_name="Order history", null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    # billing_address = models.ForeignKey('Address', related_name='billing-address', on_delete=models.SET_NULL,
    #                                    blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    id = uuid4()
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active order?")
    '''
   1. Item added to cart
   2. Adding a billing address
   (Failed checkout)
   3. Payment
   (Preprocessing, processing, packaging etc.)
   4. Being delivered
   5. Received
   6. Refunds
   '''

    def __str__(self):
        return self.user.username

    def get_final_price(self):
        if self.items.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()

    def get_discount_item_price(self):
        return self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            if self.coupon.percentDollars:
                total *= 1 - (0.01 * self.coupon.amount)
            else:
                total -= self.coupon.amount
        return total

    def get_profile_url(self):
        return reverse('showcase:profile', args=[str(self.slug)])

    def get_profile_url2(self):
        return reverse('showcase:currencyproducts', args=[str(self.slug)])

    class Meta:
        verbose_name = "Total Currency Order"
        verbose_name_plural = "Total Currency Orders"


class GameHub(models.Model):
    name = models.CharField(max_length=200, verbose_name="Game Name")
    type = models.CharField(choices=GAMETYPE, max_length=1, blank=True, null=True)
    filter = models.CharField(choices=GAMEHUB_CHOICES, max_length=1, blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Game Hub"
        verbose_name_plural = "Game Hub"


class BlackJack(models.Model):
    name = models.CharField(max_length=200, verbose_name="BlackJack Game Name")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "BlackJack Game"
        verbose_name_plural = "BlackJack Games"


class SellerApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.DateField(verbose_name='Date of birth')
    identification = models.FileField(
        help_text="Please provide a valid government-issued id (Passport, Driver's License, Birth Certificate, etc)")
    email = models.EmailField(help_text="Please input your email", unique=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Seller Application"
        verbose_name_plural = "Seller Applications"


class Preference(models.Model):
    DoesNotExist = None  # added outside tutorial
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_posts')
    value = models.IntegerField(help_text="1->Like, 2->Dislike")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ':' + str(self.post) + ':' + str(self.value)

    class Meta:
        unique_together = ("user", "post", "value")
        verbose_name = "Blog Like"
        verbose_name_plural = "Blog Likes"


class Comment(models.Model):
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name="Post comment?")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)

        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.commentator).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position
        super().save(*args, **kwargs)

    def get_profile_url(self):
        return reverse('showcase:profile', args=[str(self.slug)])

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("showcase:post_detail", kwargs={"slug": self.post.slug})


class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    post = models.ForeignKey(Idea, on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Post Like"
        verbose_name_plural = "Post Likes"


class Profile(models.Model):
    about_me = models.TextField()
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.user)


class FaviconBase(models.Model):
    favicontitle = models.TextField(verbose_name="Favicon Title")
    faviconcover = models.ImageField(upload_to='images/', verbose_name="Favicon")
    favicon_length = models.PositiveIntegerField(blank=True, null=True, default="100",
                                                 help_text='Original length of the favicon (use for original ratio).',
                                                 verbose_name="favicon length")
    favicon_width = models.PositiveIntegerField(blank=True, null=True, default="100",
                                                help_text='Original width of the favicon (use for original ratio).',
                                                verbose_name="favicon width")
    length_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Width")
    faviconpage = models.TextField(verbose_name="Page Name")
    faviconurl = models.URLField(verbose_name="Page URL")
    faviconlink = models.URLField(verbose_name="Favicon Link")
    faviconsizes = models.TextField(verbose_name="Favicon Sizes", help_text="example: 180x180")
    faviconrelationship = models.TextField(verbose_name="Favicon Relationship", help_text="example: icon")
    favicontype = models.TextField(verbose_name="Favicon Type", help_text="example: ico")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.favicontitle

    class Meta:
        verbose_name = "Favicon"
        verbose_name_plural = "Favicons"


class LogoBase(models.Model):
    title = models.TextField(verbose_name="Background Title")
    logocover = models.ImageField(upload_to='images/', verbose_name="Logo")
    hyperlink = models.TextField(verbose_name="Hyperlink")
    section = models.IntegerField(verbose_name="Page Section", default=1)
    page = models.TextField(verbose_name="Page Name")
    alternate = models.TextField(verbose_name="Alternate Text")
    logo_length = models.PositiveIntegerField(blank=True, null=True, default="100",
                                              help_text='Original length of the advertisement (use for original ratio).',
                                              verbose_name="logo length")
    logo_width = models.PositiveIntegerField(blank=True, null=True, default="100",
                                             help_text='Original width of the advertisement (use for original ratio).',
                                             verbose_name="logo width")
    length_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new object
            self.section = LogoBase.objects.filter(page=self.page).count() + 1
        if not self.page.endswith('.html'):
            self.page += '.html'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logos"


class HyperlinkBase(models.Model):
    display_text = models.TextField(verbose_name="Text Display", blank=True, null=True, help_text="Display text")
    display_image = models.ImageField(upload_to='images/', verbose_name="Image Display", blank=True, null=True,
                                      help_text="Display an image")
    hyperlink = models.TextField(verbose_name="Hyperlink")
    section = models.IntegerField(verbose_name="Page Section")
    page = models.TextField(verbose_name="Page Name")
    alternate = models.TextField(verbose_name="Alternate Text", blank=True, null=True,
                                 help_text="Alternate text for Display Image")
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    length_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Width")
    hyperlink_type = models.IntegerField(default=4,
                                         blank=True,
                                         null=True,
                                         help_text='Pick the type of hyperlink (optional)',
                                         choices=((4, 'Home Hyperlink'), (3, 'Member Hyperlink'),
                                                  (2, 'Administration Hyperlink'), (2, 'Form Hyperlink'),
                                                  (1, 'Store Hyperlink'), (0, 'Other')), verbose_name="Hyperlink Type")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.hyperlink

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new object
            self.section = HyperlinkBase.objects.filter(page=self.page).count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Hyperlink Base"
        verbose_name_plural = "Hyperlink Base"


class BackgroundImageBase(models.Model):
    backgroundtitle = models.TextField(verbose_name="Background Title", blank=True, null=True)
    cover = models.ImageField(blank=True, null=True, upload_to='images/', verbose_name="Images")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Width of the image (in percent relative).',
                                              verbose_name="image width")
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Length of the image (in percent relative).',
                                               verbose_name="image length")
    file = models.FileField(blank=True, null=True, upload_to='images/', verbose_name="Non-image File")
    alternate = models.TextField(verbose_name="Alternate Text", blank=True, null=True)
    page = models.TextField(verbose_name="Page Name")
    url = models.CharField(verbose_name="Page URL", max_length=250, blank=True, null=True)
    position = models.IntegerField(verbose_name="Image Position", blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.backgroundtitle + " in " + self.page + " at Section " + str(self.position)

    def save(self, *args, **kwargs):
        if not self.url and self.page == "index":
            self.url = 'http://127.0.0.1:8000/'
        elif not self.url and self.page == "login":
            self.url = 'http://127.0.0.1:8000/accounts/login'
        elif not self.url:
            self.url = f'http://127.0.0.1:8000/{self.page}'
        elif not self.url.startswith('http://127.0.0.1:8000/'):
            self.url = f'http://127.0.0.1:8000/{self.url}'
        if not self.page.endswith('.html'):
            self.page += '.html'
        if not self.pk:  # Check if this is a new object
            self.position = BackgroundImageBase.objects.filter(page=self.page).count() + 1
            self.backgroundtitle = f'background {self.position}'  # Set the title here
        if self.cover and not self.alternate:  # Check if an image exists and alternate text is not set
            self.alternate = str(self.cover)  # Set the alternate text to the string version of the image name
        elif self.file and not self.alternate:
            self.alternate = str(self.file)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Background Image Base"
        verbose_name_plural = "Background Image Base"

    def set_image_position(image_id, xposition, yposition):
        # Retrieve the Image object from the database
        image = ImageBase.objects.get(id=image_id)
        print("Current coordinates: x={image.x}, y={image.y}")

        # Set the x and y positions to the desired values
        image.x = xposition
        image.y = yposition

        # Save the updated Image object back to the database
        image.save()


class StoreViewType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    VIEW_TYPE_CHOICES = (
        ('stream', 'Streamlined View'),
        ('detail', 'Detailed View'),
    )
    type = models.CharField(blank=True, null=True, choices=VIEW_TYPE_CHOICES, default='stream', max_length=6)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.type + "filter set by " + str(self.user)

    def save(self, *args, **kwargs):
        if self.user_id is not None:
            # If a StoreViewType for this user already exists, delete it
            StoreViewType.objects.filter(user=self.user).delete()

            # Now save the new StoreViewType
            super().save(*args, **kwargs)
        else:
            view_type_choice = 'stream'  # replace with the view type the user wants

            # Create a StoreViewType instance without saving it to the database
            store_view_type = StoreViewType(type=view_type_choice)

            # Now you can use store_view_type as needed
            print(store_view_type.type)

    class Meta:
        verbose_name = "Store View Type"
        verbose_name_plural = "Store View Types"


class TextBase(models.Model):
    TEXT_MEASUREMENT_CHOICES = (
        ('px', 'Pixels'),
        ('%', 'Percent'),
        ('vh', 'View Height'),
        ('em', 'em'),
        ('rem', 'Root em'),
        ('pt', 'Points'),
        ('pc', 'Picas'),
    )
    text = models.TextField(verbose_name="Text")
    page = models.TextField(verbose_name="Page Name")
    url = models.URLField(verbose_name="Page URL", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    text_color = models.CharField(blank=True, null=True, default="white", verbose_name="Text Color",
                                  help_text="Color of the text (accepts color names, hex codes or RGBA values in format (R, G, B, A))",
                                  max_length=200)
    header_or_textfield = models.BooleanField(verbose_name="Header or Body Text", default=1,
                                              choices=((1, 'Header'), (0, 'Body')))
    section = models.IntegerField(verbose_name="Text Section", help_text="Section Number of Text", default="1")
    exists = models.BooleanField(verbose_name="Section Taken", help_text="Is this section taken?", default=1,
                                 choices=((1, 'Yes'), (0, 'No')))
    hyperlink = models.TextField(blank=True, null=True, verbose_name="Hyperlink")
    text_size = models.IntegerField(default=0,
                                    help_text='6->Body 3, 5->Body 2, 4->Body 1, 3-> Heading 3,2-> Heading 2, 1-> Heading 1,',
                                    choices=(
                                        (6, 'H6'), (5, 'H5'), (4, 'H4'), (3, 'H3'), (2, 'H2'), (1, 'H1'), (0, 'p')),

                                    verbose_name="Text Type")
    font_size = models.IntegerField(blank=True, null=True, verbose_name="Font Size")
    font_measurement = models.CharField(blank=True, null=True, choices=TEXT_MEASUREMENT_CHOICES, max_length=3)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.text + " in " + self.page + " at Section " + str(self.section)

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = 'http://127.0.0.1:8000/'
        if not self.page.endswith('.html'):
            self.page += '.html'
        elif not self.url.startswith('http://127.0.0.1:8000/'):
            self.url = f'http://127.0.0.1:8000/{self.url}'
        if not self.pk:  # Check if this is a new object
            self.section = TextBase.objects.filter(page=self.page).count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Text Base"
        verbose_name_plural = "Text Base"


class BackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    page = models.TextField()
    is_active = models.IntegerField(
        default=1,
        blank=True,
        null=True,
        help_text='1->Active, 0->Inactive',
        choices=((1, 'Active'), (0, 'Inactive')),
        verbose_name="Set active?"
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = self.slug

        super().save(*args, **kwargs)

    def get_profile_url(self):
        return reverse('showcase:profile', args=[str(self.slug)])

    class Meta:
        verbose_name = "Background Image"
        verbose_name_plural = "Background Images"


class ContentBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Content Background Image"
        verbose_name_plural = "Content Background Images"


class SupportBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Support Background Image"
        verbose_name_plural = "Support Background Images"


class ProductBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Background Image"
        verbose_name_plural = "Product Background Images"


class NavBar(models.Model):
    text = models.TextField()
    url = models.TextField(blank=True, null=True)
    row = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    opennew = models.BooleanField(verbose_name="Open In New Tab?", default=False,
                                  choices=((True, 'Yes'), (False, 'No')))
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.text + " at Row " + str(self.row) + ", Position " + str(self.position)

    def save(self, *args, **kwargs):
        if not self.url.startswith('http'):
            self.url = f'http://127.0.0.1:8000/{self.url}'
        if not self.pk:  # Check if this is a new object
            self.position = NavBar.objects.filter(row=self.row).count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Navigational Bar Dropdown"
        verbose_name_plural = "Navigational Bar Dropdowns"


class NavBarHeader(models.Model):
    text = models.TextField(help_text='This is a header.')
    section = models.TextField(max_length=200,
                               blank=True,
                               null=True,
                               help_text='ID Section of page.')
    row = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new object
            self.row = NavBarHeader.objects.count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Navigational Bar Header"
        verbose_name_plural = "Navigational Bar Headers"


class FeaturedNavigationBar(models.Model):
    default_header = models.TextField(help_text="Only set if occupying 1'st position", blank=True, null=True,
                                      default='IntelleX', verbose_name='Heading')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(verbose_name="Navigational image", blank=True, null=True)
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Width of the image (in percent relative).',
                                              verbose_name="image width")
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Length of the image (in percent relative).',
                                               verbose_name="image length")
    url = models.TextField(blank=True, null=True)
    position = models.IntegerField()
    opennew = models.BooleanField(verbose_name="Open In New Tab?", default=False,
                                  choices=((True, 'Yes'), (False, 'No')))
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        if self.text:
            return self.text
        elif self.image:
            return self.image.url
        else:
            return self.default_header

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new object
            self.position = FeaturedNavigationBar.objects.count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Featured Navigation Bar"
        verbose_name_plural = "Featured Navigation Bar"


class SettingsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='settings')
    username = models.CharField(help_text='Your username', max_length=200)
    password = models.CharField(help_text='Your password', max_length=200)
    email = models.EmailField(help_text='Your password', max_length=200, blank=True, null=True)
    coupons = models.BooleanField(verbose_name="Send me coupons", default=True, blank=True, null=True,
                                  choices=((True, 'Yes'), (False, 'No')))
    news = models.BooleanField(verbose_name="Keep me in the loop", default=True, blank=True, null=True,
                               choices=((True, 'Yes'), (False, 'No')))
    # connects to email
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"


class Donate(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)

    # Add more fields if needed

    # ForeignKey to link each donation to a specific user (donor)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymous = models.BooleanField(default=False, help_text="Donate anonymously?")
    # position = models.IntegerField(
    #    default=0,
    #    help_text="Position for sorting",
    #    editable=False,  # This makes the field non-editable in forms
    # )
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return f"Donation by {self.donor} ({self.amount} USD)"

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.donor).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.donor).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donations"


class DonorBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    donor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Donors Background Image"
        verbose_name_plural = "Donors Background Images"


class ContributorBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contributors Background Image"
        verbose_name_plural = "Contributors Background Images"


class SettingsBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Settings Background Image"
        verbose_name_plural = "Settings Background Images"


class DonateIcon(models.Model):
    row = models.IntegerField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Donation Icon"
        verbose_name_plural = "Donation Icons"


class Titled(models.Model):
    overtitle = models.TextField(verbose_name="Title")
    page = models.TextField(verbose_name="Page Name", blank=True, null=True, )
    url = models.URLField(verbose_name="Page URL", blank=True, null=True, )
    position = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.overtitle + " at " + self.page

    class Meta:
        verbose_name = "Page Title"
        verbose_name_plural = "Page Titles"

    def save(self, *args, **kwargs):
        if not self.url and self.page == "index":
            self.url = 'http://127.0.0.1:8000/'
        elif not self.url and self.page == "login":
            self.url = 'http://127.0.0.1:8000/accounts/login'
        elif not self.url:
            self.url = f'http://127.0.0.1:8000/{self.page}'
        elif not self.url.startswith('http://127.0.0.1:8000/'):
            self.url = f'http://127.0.0.1:8000/{self.url}'
        if not self.page.endswith('.html'):
            self.page += '.html'
        super().save(*args, **kwargs)


class Meme(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,
                             verbose_name="Meme Creator")
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    font_size = models.IntegerField(blank=True, null=True, verbose_name="Font Size")
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")

    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    class Meta:
        verbose_name = "Meme Text"
        verbose_name_plural = "Meme Texts"


class MemeTextField(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE, related_name='text_fields')
    text = models.TextField(null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.text

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    class Meta:
        verbose_name = "Meme Text Field"
        verbose_name_plural = "Meme Texts Fields"


class BaseCopyrightTextField(models.Model):
    copyright = models.TextField(verbose_name="Copyright Field", help_text="Copyright And Year")
    page = models.TextField(verbose_name="Page Name")
    hyperlink = models.TextField(verbose_name="Hyperlink")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.copyright

    def save(self, *args, **kwargs):
        if not self.page.endswith('.html'):
            self.page += '.html'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Base Text Field Copyright"
        verbose_name_plural = "Base Text Field Copyright"


class ShowcaseBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Showcase Background Image"
        verbose_name_plural = "Showcase Background Images"


class BilletBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Billet Background Image"
        verbose_name_plural = "Billet Background Images"


class BlogBackgroundImage(models.Model):
    title = models.TextField(verbose_name="Title")
    cover = models.ImageField(upload_to='images/', verbose_name="Cover")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Background Image"
        verbose_name_plural = "Blog Background Images"


class PostBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    # name = models.CharField(max_length=100, help_text='Your name goes here.')
    # description = models.TextField(help_text='Idea your profile here.')
    # image = models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Idea Background Image"
        verbose_name_plural = "Idea Background Images"


class PosteBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    # name = models.CharField(max_length=100, help_text='Your name goes here.')
    # description = models.TextField(help_text='Idea your profile here.')
    # image = models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Idea Background Image"
        verbose_name_plural = "Idea Background Images"


class VoteBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    # name = models.CharField(max_length=100, help_text='Your name goes here.')
    # description = models.TextField(help_text='Idea your profile here.')
    # image = models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vote Background Image"
        verbose_name_plural = "Vote Background Images"


class RuleBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Rule Background Image"
        verbose_name_plural = "Rule Background Images"


class AboutBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Background Image"
        verbose_name_plural = "About Background Images"


class FaqBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "FAQ Background Image"
        verbose_name_plural = "FAQ Background Images"


class StaffBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Staff Background Image"
        verbose_name_plural = "Staff Background Images"


class StaffApplyBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Staff Application Background Image"
        verbose_name_plural = "Staff Application Background Images"


class InformationBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Information Background Image"
        verbose_name_plural = "Information Background Images"


class TagBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag Background Image"
        verbose_name_plural = "Tag Background Images"


class UserBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "User Background Image"
        verbose_name_plural = "Users Background Images"


class StaffRanksBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Staff Ranks Background Image"
        verbose_name_plural = "Staff Ranks Background Images"


class MegaBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mega Background Image"
        verbose_name_plural = "Mega Background Images"


# megacoins.html


class EventBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Event Background Image"
        verbose_name_plural = "Event Background Images"


class NewsBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News Background Image"
        verbose_name_plural = "News Background Images"


class ShareBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Share Background Image"
        verbose_name_plural = "Share Background Images"


class WhyBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Why Background Image"
        verbose_name_plural = "Why Background Images"


class WebsiteBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Website Background Image"
        verbose_name_plural = "Website Background Images"


class PerksBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Perks Background Image"
        verbose_name_plural = "Perks Background Images"


class CommitmentBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Commitment Background Image"
        verbose_name_plural = "Commitment Background Images"


class PriceBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Price Background Image"
        verbose_name_plural = "Price Background Images"


class ServerBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Server Background Image"
        verbose_name_plural = "Server Background Images"


class ContactBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact Background Image"
        verbose_name_plural = "Contact Background Images"


class MantenienceBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mantenience Background Image"
        verbose_name_plural = "Mantenience Background Images"


class CostBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cost Background Image"
        verbose_name_plural = "Cost Background Images"


class TiersBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tiers Background Image"
        verbose_name_plural = "Tiers Background Images"


class AccountBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Account Background Image"
        verbose_name_plural = "Account Background Images"


class AddonsBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Addons Background Image"
        verbose_name_plural = "Addons Background Images"


class PunishAppsBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Punishment Applications Background Image"
        verbose_name_plural = "Punishment Applications Background Images"


class BanAppealBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ban Appliciations Background Image"
        verbose_name_plural = "Ban Applications Background Images"


# class Background2aImage(models.Model):
#  image = models.URLField(help_text='Upload a background image for the Introduction Section (section 2a).')

#  def get_absolute_url(self):
#    return self.image

#  class Meta:
#    verbose_name = "Background Image"
#    verbose_name_plural = "Background Images"

# class Background2aImage(models.Model):
#  image = models.URLField(help_text='Upload a background image for the Introduction Section (section 2a).')

#  def get_absolute_url(self):
#    return self.image

#  class Meta:
#    verbose_name = "Background Image"
#    verbose_name_plural = "Background Images"

from django.db.models.signals import post_save, post_delete, pre_delete

# class PublicProfile(models.Model):
# user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
# photo = models.ImageField(verbose_name=("Profile Picture"),
#                  upload_to = 'profiles', #"main.PublicProfile.photo"
#                  format="Image", max_length=255, null=True, blank=True)
# website = models.URLField(default='', blank=True)
# username = models.CharField(max_length=100)
# bio = models.TextField(default='', blank=True)
# phone = models.CharField(max_length=20, blank=True, default='')
# city = models.CharField(max_length=100, default='', blank=True)
# country = models.CharField(max_length=100, default='', blank=True)
# organization = models.CharField(max_length=100, default='', blank=True)

# def create_profile(sender, **kwargs):
# user = kwargs["instance"]
# if kwargs["created"]:
# user_profile = UserProfile(user=user, bio='my bio') #website='http://poketrove.com')
# user_profile.save()
# post_save.connect(create_profile, sender=User)

from django.contrib.auth import get_user_model

# link the profiledetails page to settings
from django.db.models import Q


def get_friends(self):
    from .models import FriendRequest  # Import here to avoid circular import
    accepted_friend_requests = FriendRequest.objects.filter(
        Q(sender=self, status=FriendRequest.ACCEPTED) | Q(receiver=self, status=FriendRequest.ACCEPTED))
    friends = set()
    for friend_request in accepted_friend_requests:
        if friend_request.sender == self:
            friends.add(friend_request.receiver)
        else:
            friends.add(friend_request.sender)
    print('friends here')
    return friends


# Add the get_friends method to the User model
User.add_to_class('get_friends', get_friends)


class FriendRequest(models.Model):
    PENDING = 0
    ACCEPTED = 1
    DECLINED = 2

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined'),
    )

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f'{self.sender.username} -> {self.receiver.username}: {self.get_status_display()}'

    def get_profile_url(self, current_user):
        if current_user == self.sender or current_user == self.receiver:
            profile = ProfileDetails.objects.filter(user=current_user).first()
            if profile:
                return reverse('showcase:profile', args=[str(profile.pk)])

    # Handle the case where the current user is neither the sender nor the receiver

    class Meta:
        verbose_name = "Friend Request"
        verbose_name_plural = "Friend Requests"
        unique_together = ('sender', 'receiver')


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " is friends with " + str(self.friend) + "!"

    @receiver(post_save, sender=FriendRequest)
    def handle_friend_request(sender, instance, created, **kwargs):
        if instance.status == FriendRequest.ACCEPTED:
            Friend.objects.get_or_create(user=instance.sender, friend=instance.receiver)
        elif instance.status == FriendRequest.DECLINED:
            Friend.objects.filter(
                (Q(user=instance.sender) & Q(friend=instance.receiver)) |
                (Q(user=instance.receiver) & Q(friend=instance.sender))
            ).delete()

    post_save.connect(handle_friend_request, sender=FriendRequest)

    class Meta:
        unique_together = ('user', 'friend')


class Room(models.Model):
    name = models.CharField(max_length=1000)
    signed_in_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='room',
                                       verbose_name="Room Creator")

    time = models.DateTimeField(default=timezone.now, blank=True)
    public = models.BooleanField(default=False, verbose_name="Make Public?")
    logo = models.FileField(blank=True, null=True, verbose_name="Logo")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        if self.name:
            return str(self.name)
        else:
            return str('Guest')

    def user_can_join(self, user):
        if self.public:
            print('public server')
            return True
        else:
            print('private server')
            # Only allow signed-in users to join if the room is not public
            if user.is_authenticated:
                # Allow the room creator to join the room
                if self.signed_in_user == user:
                    return True

                # Check if there's an accepted friend request between the user and the room creator
                return FriendRequest.objects.filter(
                    Q(sender=self.signed_in_user, receiver=user, status=FriendRequest.ACCEPTED) |
                    Q(sender=user, receiver=self.signed_in_user, status=FriendRequest.ACCEPTED)
                ).exists()
            else:
                return False

    def get_absolute_url(self):
        # Construct the URL for the room detail page
        if self.name == '':
            return reverse("showcase:room", kwargs={'room': ''})

        room_url = reverse("showcase:room", kwargs={'room': self.name})

        # Construct the query parameters with the username
        final_url = f"{room_url}?username={self.name}"

        return final_url


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=1000000, verbose_name="Username")
    signed_in_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='messages',
                                       verbose_name="User")
    room = models.CharField(max_length=1000000)
    message_number = models.PositiveIntegerField(default=0, editable=False)
    file = models.FileField(upload_to='images/', null=True, blank=True)
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        if self.value:
            return str(self.value) + " in " + str(self.room)
        else:
            return "blank message in " + str(self.room)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the current maximum message number
            max_message_number = Message.objects.aggregate(max_message_number=models.Max('message_number'))[
                                     'max_message_number'] or 0

            # Increment the maximum message number to get the new message number
            self.message_number = max_message_number + 1
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    def get_absolute_url(self):

        # Construct the URL for the room detail page
        room_url = reverse("showcase:room", kwargs={'room': str(self.room)})

        # Construct the query parameters
        final_url = f"{room_url}?username={self.signed_in_user.username}"

        return final_url

        """
   def _get_current_user(self):
       # Logic to retrieve the currently signed-in user
       # You can modify this according to your authentication mechanism
       return User.objects.get(username='example_user')

   def get_profile_url(self):
       return reverse('showcase:profile', args=[str(self.signed_in_user_id)])
   #def get_profile_url(self):
   #    return f"http://127.0.0.1:8000/profile/{self.signed_in_user_id}/"
"""


# is_active is new

# Create your models here.
class SupportChat(models.Model):
    name = models.CharField(max_length=1000)
    signed_in_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,
                                       verbose_name="User")  # room should be based on the signed-in user
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    # datetime.now()
    # api_time = models.DateTimeField()

    def __str__(self):
        return str(self.signed_in_user)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    def get_absolute_url(self):
        # Construct the URL for the room detail page
        room_url = reverse('showcase:supportroom', args=[str(self.signed_in_user)])
        return room_url

    class Meta:
        verbose_name = "Support Chat"
        verbose_name_plural = "Support Chat"


class SupportMessage(models.Model):
    value = models.CharField(max_length=1000000)
    # now = datetime.datetime.now()
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=1000000)
    signed_in_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,
                                       related_name='support_messages',
                                       verbose_name="User")
    room = models.CharField(max_length=1000000)  # newly added unique=True
    avatar = models.ImageField(upload_to='profile_image', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.value)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    def get_absolute_url(self):
        # Construct the URL for the room detail page
        room_url = reverse('showcase:supportroom', args=[str(self.signed_in_user)])
        return room_url

    class Meta:
        verbose_name = "Support Message"
        verbose_name_plural = "Support Messages"


# support live chat below, support thread above (requires refresh)

class SupportInterface(models.Model):
    name = models.CharField(max_length=1000, null=True)
    room = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='supportinterfaceroom',
                             verbose_name="Room Creator")
    date = models.DateTimeField(default=timezone.now, blank=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        if self.name:
            return str(self.name)
        else:
            return str('Guest')

    def get_absolute_url(self):
        # Construct the URL for the room detail page
        if self.name == '':
            return reverse("showcase:supportline", kwargs={'room': ''})

        room_url = reverse("showcase:supportline", kwargs={'room': self.name})

        # Construct the query parameters with the username
        final_url = f"{room_url}?username={self.name}"

        return final_url

    class Meta:
        verbose_name = "Administration Chat Thread"
        verbose_name_plural = "Administration Chat Thread"


class SupportLine(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    signed_in_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,
                                       related_name='supportlinemessages',
                                       verbose_name="User")
    room = models.CharField(max_length=1000000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_number = models.PositiveIntegerField(default=0, editable=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.value)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Get the current maximum message number
            max_message_number = SupportLine.objects.aggregate(max_message_number=models.Max('message_number'))[
                                     'max_message_number'] or 0

            # Increment the maximum message number to get the new message number
            self.message_number = max_message_number + 1
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    def get_absolute_url(self):

        # Construct the URL for the room detail page
        room_url = reverse("showcase:room", kwargs={'room': str(self.room)})

        # Construct the query parameters
        final_url = f"{room_url}?username={self.signed_in_user.username}"

        return final_url

    class Meta:
        verbose_name = "Administration Thread Message"
        verbose_name_plural = "Administration Thread Messages"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    # related name could be a possible solution
    one_click_purchasing = models.BooleanField(default=False)
    currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, null=True)  # Adjust model name if needed
    currency_amount = models.IntegerField(default=0, verbose_name='Currency Amount')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


from django.db.models import signals
from django.db.transaction import atomic


class Wager(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Bet Amount')
    outcome = models.CharField(max_length=1, choices=BLACKJACK_OUTCOME, default=None, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print('bet: ' + str(self.amount))
        print('currency: ' + str(self.user_profile.currency_amount))
        with atomic():
            # Check for negative bets and insufficient funds
            if self.amount <= 0:
                print('put a positive amount')
                raise ValidationError("Bet amount must be positive.")
            if self.user_profile.currency_amount < self.amount:
                print('insufficient funds')
                raise ValidationError("Insufficient funds for this bet. You have {}, but the bet is {}.".format(
                    self.user_profile.currency_amount, self.amount))

            # Deduct amount from user currency (within atomic block)
            self.user_profile.currency_amount -= self.amount
            self.user_profile.save()  # Save user profile first for potential integrity checks

            # Save wager after user profile (for cleaner error handling)
            super().save(*args, **kwargs)

    def resolve(self, outcome):
        self.outcome = outcome
        win_multiplier = 1.5 if outcome == 'B' else 1.0  # Handle Blackjack bonus
        if outcome in ('W', 'B'):  # Update currency only on wins (including Blackjack)
            self.user_profile.currency_amount += self.amount * win_multiplier
        elif outcome == 'D':  # Refund on ties
            self.user_profile.currency_amount += self.amount
        self.user_profile.save()
        self.save()


# Connect pre-save signal to print `self.amount` before atomic block
def print_amount_before_save(sender, instance, **kwargs):
    print("Wager amount before atomic block:", instance.amount)


signals.pre_save.connect(print_amount_before_save, sender=Wager)

"""class Settings(models.Model):
 username = models.OneToOneField(User, on_delete=models.CASCADE)
 #password =
 full_name = models.CharField(max_length=200, blank=True, null=True)

 class Meta:
     verbose_name_plural = "Settings"
     """
from django.db.models.signals import pre_save

from django.http import JsonResponse
from django.core import serializers


class ItemFilter(models.Model):
    product_filter = models.CharField(verbose_name="Hashtag filters", max_length=200, blank=True, null=True)
    clicks = models.IntegerField(verbose_name="Popularity", blank=True, null=True)
    image = models.ImageField(verbose_name="Filter Image", blank=True, null=True)
    category = models.IntegerField(default=0, blank=True,
                                   null=True, verbose_name='Make the Filter a Category?', help_text='1->Yes, 0->No',
                                   choices=((1, 'Yes'), (0, 'No')))
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.product_filter

    class Meta:
        verbose_name = "Item Filter"
        verbose_name_plural = "Item Filters"


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    specialty = models.CharField(blank=True, null=True, choices=SPECIAL_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1000)  # can use for cataloging products
    slug = models.SlugField()  # might change to automatically get the slug
    status = models.IntegerField(choices=((0, "Draft"), (1, "Publish")), default=1)
    description = models.TextField()
    image = models.ImageField()
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    length_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Width")
    # hyperlink = models.TextField(verbose_name = "Hyperlink", blank=True, null=True, help_text="Feedbacks will use this hyperlink as a link to this product.") #might change to automatically get the hyperlink by means of item filtering
    relateditems = models.ManyToManyField("self", blank=True, verbose_name="Related Items:")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Out of stock?")

    def __str__(self):
        if self.user:
            return self.title + " by " + self.user.username
        else:
            return self.title + " by PokeTrove"

    def get_absolute_url(self):
        return reverse("showcase:product", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("showcase:add-to-cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("showcase:remove-from-cart", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = self.slug
        super().save(*args, **kwargs)

    def get_profile_url(self):
        return reverse('showcase:product', args=[str(self.slug)])

    # used to get the user;s profile url
    def get_profile_url2(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])


class EBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    items = Item.objects.filter(is_active=1)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.title

    # def __str__(self):
    #    return self.__annotations__title

    class Meta:
        verbose_name = "Ecommerce Background Image"
        verbose_name_plural = "Ecommerce Background Images"


from django.utils.crypto import get_random_string


class TradeItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    specialty = models.CharField(blank=True, null=True, choices=SPECIAL_CHOICES, max_length=2)
    condition = models.CharField(choices=CONDITION_CHOICES, default="M", max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1000)  # can use for cataloging products
    slug = models.SlugField()  # might change to automatically get the slug
    status = models.IntegerField(choices=((0, "Draft"), (1, "Publish")), default=1)
    description = models.TextField()
    image = models.ImageField()
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    length_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Width")
    # hyperlink = models.TextField(verbose_name = "Hyperlink", blank=True, null=True, help_text="Feedbacks will use this hyperlink as a link to this product.") #might change to automatically get the hyperlink by means of item filtering
    relateditems = models.ManyToManyField("self", blank=True, verbose_name="Related Items:")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Out of stock?")

    def __str__(self):
        if self.user:
            return self.title + " by " + self.user.username
        else:
            return self.title + " by PokeTrove"

    class Meta:
        verbose_name = "Trade Item"
        verbose_name_plural = "Trade Items"


class TradeOfferManager(models.Manager):
    def get_queryset(self, request):
        return super().get_queryset().select_related('trade_items').filter(trade_items__user=request.user)


from django.utils.text import slugify


class TradeOffer(models.Model):
    PENDING = 0
    ACCEPTED = 1
    DECLINED = 2

    TRADE_STATUS = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined')
    )
    title = models.CharField(max_length=100, help_text="Name of your trade offer.")
    trade_items = models.ManyToManyField(TradeItem)
    estimated_trading_value = models.DecimalField(
        help_text="Estimated Market Price of Trade Item (will be displayed to potential traders)", decimal_places=2,
        max_digits=12)
    message = models.CharField(max_length=2000, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Trader')
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Receiver', blank=True,
                              null=True, help_text="Optional", verbose_name="Recipient")
    trade_status = models.IntegerField(choices=TRADE_STATUS, default=PENDING)
    slug = models.SlugField(unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Out of stock?")

    def __str__(self):
        item_titles = ", ".join([item.title for item in self.trade_items.all()])
        if self.user and self.user2:
            return f'Offer: {item_titles} between {self.user.username} and {self.user2.username}'
        elif self.user:
            return f'Offer: {item_titles} offered by {self.user.username}'
        else:
            return f'Offer: {item_titles} fulfilled by PokeTrove'

    def get_profile_url(self):
        return reverse('showcase:directedtradeoffers', args=[str(self.pk)])

    def get_absolute_url(self):

        return reverse('showcase:directedtradeoffers', args=[str(self.pk)])


    class Meta:
        verbose_name = "Trade Offer"
        verbose_name_plural = "Trade Offers"


class RespondingTradeOffer(models.Model):
    PENDING = 0
    ACCEPTED = 1
    DECLINED = 2

    TRADE_STATUS = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined')
    )
    wanted_trade_items = models.ManyToManyField(TradeItem)
    offered_trade_items = models.ForeignKey(TradeOffer, on_delete=models.CASCADE, blank=True, null=True)
    estimated_trading_value = models.DecimalField(
        help_text="Estimated Market Price of Trade Item (will be displayed to potential traders)", decimal_places=2,
        max_digits=12)
    message = models.CharField(max_length=2000, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Dealer', blank=True, null=True)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Recipient', blank=True,
                              null=True, help_text="Optional", verbose_name="Recipient")
    slug = models.SlugField(unique=True, editable=False, blank=True, null=True)
    trade_status = models.IntegerField(choices=TRADE_STATUS, default=PENDING)
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Out of stock?")


    class Meta:
        verbose_name = "Trade Offer Response"
        verbose_name_plural = "Response Trade Offer Responses"


class Trade(models.Model):
    trade_offers = models.ManyToManyField(TradeOffer)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='traders')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Out of stock?")

    def __str__(self):
        offer_titles = " & ".join([str(offer) for offer in self.trade_offers.all()])
        user_names = " & ".join([user.username for user in self.users.all()])
        return f'{offer_titles} by {user_names}'

    def get_profile_url(self):
        return [reverse('showcase:profile', args=[str(user.pk)]) for user in self.users.all()]

    class Meta:
        verbose_name = "Trade"
        verbose_name_plural = "Trades"


class ChatBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    # items = Item.objects.all()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Chat Background Image"
        verbose_name_plural = "Chat Background Images"


class SupportChatBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    # items = Item.objects.all()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Support Chat Background Image"
        verbose_name_plural = "Support Chat Background Images"


class PartnerBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Partner Background Image"
        verbose_name_plural = "Partner Background Images"


class ConvertBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Convert Background Image"
        verbose_name_plural = "Convert Background Images"


class ReasonsBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Reasons Background Image"
        verbose_name_plural = "Reasons Background Images"


class OrderBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Order Background Image"
        verbose_name_plural = "Order Background Images"


class CheckoutBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Checkout Background Image"
        verbose_name_plural = "Checkout Background Images"


class SignupBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Signup Background Image"
        verbose_name_plural = "SignupBackground Images"


class ChangePasswordBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Change Password Background Image"
        verbose_name_plural = "Change Password Background Images"


class FeedbackBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Feedback Background Image"
        verbose_name_plural = "Feedback Background Images"


class IssueBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Issue Background Image"
        verbose_name_plural = "Issue Background Images"


import uuid


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # order_number = models.IntegerField()
    slug = models.SlugField(max_length=200, blank=True, null=True,
                            help_text="Leave blank to use corresponding product slug.")  # apply unique=True parameter after slugs are actually implemented
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField()
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Order date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        if self.item.discount_price:
            return self.quantity * self.get_discount_item_price()
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()

    # used to get the url of the item
    def get_profile_url(self):
        order = OrderItem.objects.filter(user=self.user).first()
        if order:
            return reverse('showcase:product', args=[str(self.slug)])

    # used to get the user;s profile url
    def get_profile_url2(self):
        profile = ProfileDetails.objects.filter(user=self.user).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.item.slug
        if not self.image:
            self.image = self.item.image
        super().save(*args, **kwargs)
        OrderItemField.objects.create(
            user=self.user,
            ordered=self.ordered,
            # order_number=self.order_number,
            slug=self.slug,
            item=self.item,
            image=self.image,
            orderitem_id=self,
            quantity=self.quantity,
            is_active=self.is_active,
        )

    class Meta:
        verbose_name_plural = 'Order Items'


""" def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.item.slug)
       super().save(*args, **kwargs)"""


class OrderItemField(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    # order_number = models.IntegerField()
    slug = models.SlugField(max_length=200, blank=True, null=True,
                            help_text="Leave blank to use corresponding product slug.")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField()
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    quantity = models.IntegerField(default=1)
    orderitem_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE, verbose_name="Order item id", null=True)
    is_active = models.IntegerField(default=1, blank=True, null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    class Meta:
        verbose_name_plural = 'Order Item Fields'


class AdminRoles(models.Model):
    role = models.CharField(max_length=30, verbose_name="Administration role")
    role_description = models.TextField(verbose_name="Role Overview", blank='True', null='True')
    # role_hyperlink = models.CharField(max_length=100, verbose_name="Role hyperlink", help_text='Only add if necessary',
    #                             blank='True', null='True')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')),
                                    verbose_name="Is this role currently active?")

    def __str__(self):
        return self.role

    class Meta:
        verbose_name_plural = 'Administrative Roles'


class AdminTasks(models.Model):
    task = models.CharField(max_length=30, verbose_name="Administration tasks")
    hyperlink = models.CharField(max_length=100, verbose_name="Task hyperlink", help_text='Only add if necessary',
                                 blank='True', null='True')
    opennew = models.BooleanField(verbose_name="Open In New Tab?", default=False,
                                  choices=((True, 'Yes'), (False, 'No')),
                                  help_text="Please note all Administration Interface Pages should open in a new tab.")
    section = models.IntegerField(help_text='Position of the page link.', verbose_name='position')
    page_name = models.TextField(verbose_name="Page Name", blank="True", null="True")
    image = models.ImageField(verbose_name="Task image")
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    length_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Width")
    alternate = models.TextField(verbose_name="Alternate text")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')),
                                    verbose_name="Is this task currently active?")

    def __str__(self):
        return self.task

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new object
            self.section = AdminTasks.objects.filter(page_name=self.page_name).count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Administrative Tasks'


class AdminPages(models.Model):
    pages = models.CharField(max_length=30, verbose_name="Administration pages")
    description = models.TextField(help_text='Page description', default='')
    hyperlink = models.CharField(max_length=100, verbose_name="Page hyperlinks")
    opennew = models.BooleanField(verbose_name="Open In New Tab?", default=False,
                                  choices=((True, 'Yes'), (False, 'No')),
                                  help_text="Please note all Administration Interface Pages should open in a new tab.")
    section = models.IntegerField(help_text='Position of the page link.',
                                  verbose_name='position')
    page_name = models.TextField(verbose_name="Page Name", blank="True", null="True")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active page?")

    def __str__(self):
        return self.pages

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new object
            self.section = AdminPages.objects.filter(page_name=self.page_name).count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Administrative Pages'


class Questionaire(models.Model):
    RADIO_CHOICES = (
        ('option1', 'Multiple Choice'),
        ('option2', 'Short Answer'),
        ('option3', 'True or False'),
        ('option4', 'Free Response'),
        ('option5', 'Image Field'),
        ('option6', 'Integer Field'),
        ('option7', 'Decimal Field'),
        ('option8', 'Other'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    form_name = models.TextField(verbose_name="Form Name")
    form_type = models.CharField(max_length=10, choices=RADIO_CHOICES)
    text = models.TextField(verbose_name="Question")
    image = models.TextField(verbose_name="Image", blank=True, null=True)

    # answer_choices = models.JSONField(default=list, blank=True)
    answer_choices = models.CharField(max_length=255, blank=True, null=True)

    # Add fields to store correct answers for different question types
    correct_answer_multiple_choice = models.CharField(max_length=255, blank=True, null=True)
    correct_answer_short_answer = models.CharField(max_length=255, blank=True, null=True)
    correct_answer_true_false = models.BooleanField(blank=True, null=True)
    correct_answer_free_response = models.TextField(blank=True, null=True)
    correct_answer_image_field = models.ImageField(upload_to='correct_answers/', blank=True, null=True)
    correct_answer_integer_field = models.IntegerField(blank=True, null=True)
    correct_answer_decimal_field = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    correct_answer_infinite_decimal_field = models.FloatField(blank=True, null=True)
    correct_answer_other = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active order?")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Question Form Base'


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questionaire, on_delete=models.CASCADE)

    # Fields for different response types
    multiple_choice_response = models.CharField(max_length=100, null=True, blank=True)
    short_answer_response = models.TextField(null=True, blank=True)
    true_or_false_response = models.BooleanField(null=True, blank=True)
    free_response_response = models.TextField(null=True, blank=True)
    image_field_response = models.ImageField(upload_to='responses/', null=True, blank=True)
    integer_field_response = models.IntegerField(null=True, blank=True)
    decimal_field_response = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_response = models.TextField(null=True, blank=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active order?")

    def __str__(self):
        return f"{self.user.username}'s answer to '{self.question.text}'"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    itemhistory = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Order history", null=True)
    feedback_url = models.URLField(blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL,
                                         blank=True, null=True)
    billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL,
                                        blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    id = uuid4()
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active order?")
    '''
   1. Item added to cart
   2. Adding a billing address
   (Failed checkout)
   3. Payment
   (Preprocessing, processing, packaging etc.)
   4. Being delivered
   5. Received
   6. Refunds
   '''

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            if self.coupon.percentDollars:
                total *= 1 - (0.01 * self.coupon.amount)
            else:
                total -= self.coupon.amount
        return total

    def get_profile_url(self):
        return reverse('showcase:profile', args=[str(self.slug)])

    def get_profile_url2(self):
        return reverse('showcase:products', args=[str(self.slug)])


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1000, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active address?")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=150)
    amount = models.FloatField()
    percentDollars = models.BooleanField(default=False, verbose_name="Percent-off Coupon")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active coupon?")

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active refund?")

    def __str__(self):
        return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField(max_length=200, verbose_name="Recipient")
    inquiry = models.CharField(max_length=100, verbose_name="Subject")
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


class BusinessMailingContact(models.Model):
    name = models.TextField()
    email = models.EmailField(max_length=200, verbose_name="Recipient")
    inquiry = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Business Mailing Message"
        verbose_name_plural = "Business Mailing Messages"


class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active address?")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Checkout Addresses'


from django.db import IntegrityError


class ImageCarousel(models.Model):
    carouseltitle = models.CharField(max_length=100, help_text='Title of the image.', verbose_name="title", blank=True,
                                     null=True)
    carouselcaption = models.TextField(help_text='Caption for the image.', verbose_name="caption")
    carouselimage = models.ImageField(help_text='Upload an image for the carousel.)',
                                      upload_to='images/', verbose_name='image')
    carouselimage_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                                       help_text='Original length of the image (use for original ratio).',
                                                       verbose_name="image length")
    carouselimage_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                                      help_text='Original width of the image (use for original ratio).',
                                                      verbose_name="image width")
    length_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Width")
    associated_product = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True,
                                           verbose_name="Associated Product")
    specialty = models.CharField(blank=True, null=True, choices=SPECIAL_CHOICES, max_length=2)
    carouselnumber = models.IntegerField(help_text='What carousel number is this?.',
                                         verbose_name='Carousel number')
    carouselposition = models.IntegerField(help_text='Positioning of the image within the carousel.',
                                           verbose_name='position', blank=True, null=True)
    carouseltotal = models.IntegerField(help_text='Total number of images within the carousel.',
                                        verbose_name='total images', default=9)
    carouselpage = models.TextField(verbose_name="Page Name")
    hyperlink = models.TextField(verbose_name="Hyperlink")
    alternate = models.TextField(verbose_name="Alternate Text", blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return self.carouseltitle

    class Meta:
        verbose_name = "Image Carousel Post"
        verbose_name_plural = "Image Carousel Posts"

    def save(self, *args, **kwargs):

        if not self.carouselpage.endswith('.html'):
            self.carouselpage += '.html'
        if not self.pk:  # Check if this is a new object
            self.carouselposition = ImageCarousel.objects.filter(carouselpage=self.carouselpage,
                                                                 carouselnumber=self.carouselnumber).count() + 1
            self.carouseltitle = f'background {self.carouselposition}'  # Set the title here
        if self.carouselimage and not self.alternate:  # Check if an image exists and alternate text is not set
            self.alternate = str(self.carouselimage)  # Set the alternate text to the string version of the image name
        # Set the specialty based on the associated product
        if self.associated_product and self.associated_product.specialty:
            self.specialty = self.associated_product.specialty
        try:
            super().save(*args, **kwargs)
        except IntegrityError as e:
            # Handle any IntegrityError exceptions that may occur during save
            # Print or log the error for debugging
            print(f"IntegrityError during save: {e}")
        super().save(*args, **kwargs)


class AdvertisementBase(models.Model):
    advertisementtitle = models.CharField(max_length=100, help_text='Advertisement title.',
                                          verbose_name="advertisement title")
    advertisement = models.ImageField(help_text='Image of the advertisement.', upload_to='images/',
                                      height_field="advertisement_width",
                                      width_field="advertisement_length")  # the variable usage of advertisement_width & advertisement_height prevent those fields from being edited
    advertisement_file = models.FileField(blank=True, null=True, upload_to='images/', verbose_name="Non-image File")
    advertisement_length = models.PositiveIntegerField(blank=True, null=True, default="100",
                                                       help_text='Original length of the advertisement (use for original ratio).',
                                                       verbose_name="advertisement length")
    advertisement_width = models.PositiveIntegerField(blank=True, null=True, default="100",
                                                      help_text='Original width of the advertisement (use for original ratio).',
                                                      verbose_name="advertisement width")
    length_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Length")
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resized Width")
    advertisement_position = models.IntegerField(help_text='Positioning of the advertisement.', verbose_name='Position')
    page = models.TextField(verbose_name="Page Name")
    xposition = models.IntegerField(help_text='x-position.', verbose_name="x-position")
    yposition = models.IntegerField(help_text='x-position.', verbose_name="y-position")
    relevance = models.TextField(help_text='Relevance of advertisement')
    correlating_product = models.OneToOneField(Item, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, help_text='Type of product.')
    advertisement_hyperlink = models.TextField(verbose_name="Hyperlink")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    class Meta:
        verbose_name = "Advertisement Base"
        verbose_name_plural = "Advertisement Base"

        def __unicode__(self):
            return self.advertisementtitle

    def save(self, *args, **kwargs):
        if not self.id:  # object is being created for the first time
            super().save(*args, **kwargs)
            img = Image.open(self.advertisement.path)
            img = img.resize((self.width_for_resize, self.length_for_resize), Image.LANCZOS)
            self.advertisement_length, self.advertisement_width = img.size
            super().save(*args, **kwargs)
        else:  # object already exists and is being updated
            img = Image.open(self.advertisement.path)
            img = img.resize((self.width_for_resize, self.length_for_resize), Image.LANCZOS)
            self.advertisement_width, self.advertisement_length = img.size
            super().save(*args, **kwargs)
        if not self.pk:  # Check if this is a new object
            self.advertisement_position = AdvertisementBase.objects.filter(page=self.page).count() + 1
        super().save(*args, **kwargs)


class Advertising(AdvertisementBase):
    pass


class ImageBase(models.Model):
    IMAGE_MEASUREMENT_CHOICES = (
        ('px', 'Pixels'),
        ('%', 'Percent'),
        ('vh', 'View Height'),
        ('em', 'em'),
        ('rem', 'Root em'),
        ('pt', 'Points'),
        ('pc', 'Picas'),
    )
    title = models.CharField(max_length=100, help_text='title.', blank=True, null=True,
                             verbose_name="title")
    image = models.ImageField(blank=True, null=True, help_text='Image of the advertisement.', upload_to='images/',
                              height_field="image_length",
                              width_field="image_width")  # the variable usage of advertisement_width & advertisement_height prevent those fields from being edited
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Width of the image (in percent relative).',
                                              verbose_name="image width")
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Length of the image (in percent relative).',
                                               verbose_name="image length")
    image_ratio = models.FloatField(blank=True, null=True, default=1.0,
                                    help_text='Length to Width Ratio of the Image (Length/Width).',
                                    verbose_name="image ratio")

    file = models.FileField(blank=True, null=True, upload_to='images/', verbose_name="Non-image File")
    image_measurement = models.CharField(blank=True, null=True, choices=IMAGE_MEASUREMENT_CHOICES, max_length=3)
    width_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resize Width")
    height_for_resize = models.PositiveIntegerField(default=100, verbose_name="Resize Height")
    image_position = models.IntegerField(help_text='Positioning of the image.', verbose_name='Position', blank=True,
                                         null=True)
    alternate = models.TextField(verbose_name="Alternate Text", blank=True, null=True)
    page = models.TextField(verbose_name="Page Name")
    xposition = models.IntegerField(help_text='x-position.', verbose_name="x-position", default="0")
    yposition = models.IntegerField(help_text='x-position.', verbose_name="y-position", default="0")
    relevance = models.TextField(help_text='Relevance of image')
    correlating_product = models.OneToOneField(Item, blank=True, null=True, on_delete=models.CASCADE)
    # try incorporating other models in addition to Item
    type = models.CharField(max_length=200, help_text='Type of image.')
    hyperlink = models.TextField(verbose_name="Hyperlink", blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    class Meta:
        # Add verbose name
        verbose_name = 'Image Base'
        verbose_name_plural = 'Image Base'

    def __str__(self):
        return self.title + " in " + self.page + " at Image Position " + str(self.image_position)

    def image_save(self, *args, **kwargs):
        if not self.id:  # Object is being created for the first time
            super().save(*args, **kwargs)
        else:  # Object already exists and is being updated
            # Retrieve the image
            img = Image.open(self.image.path)

            # Resize the image
            img = img.resize((self.width_for_resize, self.height_for_resize), Image.ANTIALIAS)

            # Update image dimensions and ratio
            self.image_length, self.image_width = img.size
            if self.image_width and self.image_length:
                self.image_ratio = self.image_length / self.image_width
                print("the ratio is: " + str(self.image_ratio))

            super().save(*args, **kwargs)

    def set_image_position(image_id, xposition, yposition):
        # Retrieve the Image object from the database
        image = ImageBase.objects.get(id=image_id)
        print("Current coordinates: x={image.x}, y={image.y}")

        # Set the x and y positions to the desired values
        image.x = xposition
        image.y = yposition

        # Save the updated Image object back to the database
        image.save()

    def save(self, *args, **kwargs):
        if not self.page.endswith('.html'):
            self.page += '.html'
        if not self.pk:  # Check if this is a new object
            self.image_position = ImageBase.objects.filter(page=self.page).count() + 1
            self.title = f'background {self.image_position}'  # Set the title here
        if self.image and not self.alternate:  # Check if an image exists and alternate text is not set
            self.alternate = str(self.image)  # Set the alternate text to the string version of the image name
        elif self.file and not self.alternate:
            self.alternate = str(self.file)
        super().save(*args, **kwargs)


class State(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.IntegerField(default=1, blank=True, null=True, help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now,
                                      null=True,
                                      blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'state'
        # Add verbose name
        verbose_name = 'Website'


class FileBase(models.Model):
    file_field = models.FileField(blank=True, null=True, verbose_name="File Field")


class UserProfile2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_image', null=True, blank=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    class Meta:
        verbose_name = "Edit Profile"
        verbose_name_plural = "Edit Profiles"


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile2.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Feedback(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True,
                             null=True)  # might want to replace item with order
    """orderitem = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)"""  # might want to replace item with order
    order = models.OneToOneField(OrderItem, on_delete=models.CASCADE)
    # order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    """order = models.OneToOneField(OrderItem, on_delete=models.CASCADE, related_name='feedback', null=True)"""
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # hyperlink = models.CharField(max_length=200,
    #                            help_text="Leave field blank, hyperlink will automatically fill with the link to the associated product.")

    comment = models.TextField()
    feedbackpage = models.TextField(verbose_name="Page Name", blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True,
                            help_text="Leave blank to use corresponding product slug.")  # get the actual item slug
    # unique=True prevents saving, but does not prevent the IntegrityError at /create_review/1/ UNIQUE constraint failed: showcase_feedback.slug
    star_rating = models.IntegerField(verbose_name='Star Rating',
                                      validators=[MinValueValidator(1), MaxValueValidator(5)])
    showcase = models.IntegerField(default=0, blank=True,
                                   null=True, verbose_name='Showcase on Cover Page?', help_text='1->Yes, 0->No',
                                   choices=((1, 'Yes'), (0, 'No')))
    image = models.ImageField(verbose_name="Images", upload_to='images/', help_text='Please upload any product images',
                              blank=True, null=True)
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the image (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the image (use for original ratio).',
                                              verbose_name="image width")
    timestamp = models.DateTimeField(default=timezone.now)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return "%s %s" % (self.username, self.order)

    def get_current_username(self):
        User = get_user_model()
        return User.objects.get(pk=self.request.user.pk).username

    def get_profile_url(self):
        return reverse('showcase:review_detail', args=[str(self.slug)])

    def get_profile_url2(self):
        profile = ProfileDetails.objects.filter(user=self.username).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    def get_absolute_url(self):

        return reverse('showcase:review_detail', args=[str(self.slug)])

    @property
    def item_name(self):
        if self.item:
            return self.item.name
        elif self.order and self.order.item:
            return self.order.item.name
        return ""

    # Define a property to get the related item's slug
    @property
    def item_slug(self):
        if self.item:
            return self.item.slug
        elif self.order and self.order.item:
            return self.order.item.slug
        return ""


@receiver(pre_save, sender=Feedback)
def set_slug(sender, instance, *args, **kwargs):
    # Check if instance.slug is not already set before updating it
    if not instance.slug and instance.item:
        instance.slug = instance.item.slug


class ShuffleType(models.Model):
    name = models.CharField(default="Pack Opening", max_length=200)
    type = models.CharField(choices=SHUFFLE_CHOICES, default='L',
                            max_length=1)  # skill-based are usually reserved for tournament-type scenarios
    circumstance = models.CharField(choices=AVALIABLE_CHOICES, default='OP', max_length=3)
    game_mode = models.CharField(choices=GAME_MODE, default="STP", max_length=3)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Shuffle Type"
        verbose_name_plural = "Shuffle Types"


class PlayerVersusPlayer(models.Model):
    name = models.CharField(default="Pack Opening", max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    privacy = models.CharField(choices=PRIVACY, max_length=3)
    locked_in = models.BooleanField(default=0,
                                    help_text='0->Open, 1->Locked In',
                                    verbose_name="Open or Locked In?")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Player Versus Player"
        verbose_name_plural = "Player Versus Players"


class Shuffler(models.Model):
    """Used for voting on different new ideas"""
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    file = models.FileField(null=True, verbose_name='File')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    choices = models.ManyToManyField(Choice, blank=True)
    category = models.CharField(max_length=100,
                                help_text='Type the category of product getting shuffled.')
    heat = models.CharField(choices=HEAT, max_length=2, blank=True, null=True)
    shuffletype = models.ForeignKey(ShuffleType, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="Shuffle Type")
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    demonstration = models.CharField(choices=PRACTICE, max_length=2, blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True, default=0.0)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.question)

    # Signal receiver function
    @receiver(post_save, sender=Choice)
    def update_shuffler(sender, instance, **kwargs):
        shufflers = Shuffler.objects.filter(choices=instance)
        for shuffler in shufflers:
            shuffler.tier = instance.tier
            shuffler.rarity = instance.rarity
            shuffler.value = instance.value
            shuffler.number = instance.number
            shuffler.save()

    class Meta:
        verbose_name = "Shuffle Choice"
        verbose_name_plural = "Shuffle Choices"


import random


def create_unique_lottery_number():
    return str(random.randint(1000000000, 9999999999))


class Lottery(models.Model):
    name = models.CharField(default='Daily Lotto', max_length=200)
    flavor_text = models.CharField(max_length=200)
    file_path = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    file = models.FileField(null=True, verbose_name='Sprite')
    profile_number = models.PositiveIntegerField(default=0, editable=False)
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.pk:
            max_message_number = Lottery.objects.aggregate(max_message_number=models.Max('profile_number'))[
                                     'max_message_number'] or 0
            self.profile_number = max_message_number + 1

        if not self.slug:
            if self.name != "Daily Lotto" and self.name != "Daily Lottery" and self.name != "daily lotto" and self.name != "daily lottery":
                self.slug = slugify(self.name)

        self.file_path = reverse('showcase:lottery', kwargs={'slug': self.slug})

        super().save(*args, **kwargs)  # Call the "real" save() method.

    def select_winner(self):
        # Get all tickets associated with this lottery
        tickets = list(self.tickets.all())

        # Count the number of tickets
        count = len(tickets)

        if count == 0:
            # No tickets sold for this lottery
            return None

        # Select a random ticket
        random_index = random.randint(0, count - 1)
        winner_ticket = tickets[random_index]

        return winner_ticket.user

    class Meta:
        verbose_name = "Lottery"
        verbose_name_plural = "Lotteries"


class LotteryTickets(models.Model):
    name = models.CharField(default='Daily Lotto', max_length=200)
    flavor_text = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(null=True, verbose_name='Sprite')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
    lottery_number = models.CharField(
        max_length=10,
        unique=True,
        default=create_unique_lottery_number
    )
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name) + " #" + str(self.lottery_number) + " - " + str(self.user)

    class Meta:
        verbose_name = "Lottery Ticket"
        verbose_name_plural = "Lottery Tickets"


class Membership(models.Model):
    name = models.CharField(default='Rubiaces', max_length=200)
    tier = models.CharField(choices=MEMBERSHIP_TIER, max_length=2, blank=True, null=True)
    file = models.FileField(null=True, verbose_name='Sprite')
    image_length = models.PositiveIntegerField(blank=True, null=True, default=100,
                                               help_text='Original length of the advertisement (use for original ratio).',
                                               verbose_name="image length")
    image_width = models.PositiveIntegerField(blank=True, null=True, default=100,
                                              help_text='Original width of the advertisement (use for original ratio).',
                                              verbose_name="image width")
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Membership Tier"
        verbose_name_plural = "Membership Tiers"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership_tier = models.ForeignKey(Membership, on_delete=models.CASCADE)
    mfg_date = models.DateTimeField(auto_now_add=True, verbose_name="date")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"


class Level(models.Model):
    level = models.IntegerField(default=1)
    level_name = models.CharField(max_length=200)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.level_name) + " " + str(self.level)

    def save(self, *args, **kwargs):
        if not self.pk:  # if the object is being created, not updated
            last_level = Level.objects.all().order_by('-level').first()
            if last_level:
                self.level = last_level.level + 1
            # if there is no last_level, self.level will be 1 by default
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"
        ordering = ['level']


class ProfileDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_image', null=True, blank=True, verbose_name="Profile picture")
    alternate = models.TextField(verbose_name="Alternate text")
    about_me = models.TextField(blank=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default="")
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    currency_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    seller = models.BooleanField(default=False, null=True)
    position = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="Position for sorting",
    )
    # link_to_profile = models.URLField(default=1, blank=True, null=True, verbose_name="Link to profile") #possibly consider making this automatically fill with the link to the user's profile
    # consider making a randomized pk that is assigned to each invididual user and can be attached to the end of the default profile url like in this schema: "http://127.0.0.1:8000/profile/pk/
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('showcase:profile', kwargs={'pk': self.pk})

    def add_currency(self, amount):
        self.currency_amount += amount
        self.save()

    def subtract_currency(self, amount):
        if self.currency_amount >= amount:
            self.currency_amount -= amount
            self.save()
        else:
            raise ValueError("Not enough currency")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            default_level = Level.objects.first()  # or set this to whatever you want the default to be
            default_currency = Currency.objects.first()  # or set this to whatever you want the default to be
            ProfileDetails.objects.create(user=instance, currency=default_currency, level=default_level)

    post_save.connect(create_user_profile, sender=User)

    class Meta:
        verbose_name = "Account Profile"
        verbose_name_plural = "Account Profiles"
