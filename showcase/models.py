from django.db import models
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.conf import settings

from uuid import uuid4

STATUS = ((0, "Draft"), (1, "Publish"))

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
# from showcase.models import Project
# new_group, created = Group.objects.get_or_create(name='new_group')
# Code to add permission to group ???
# ct = ContentType.objects.get_for_model(Project)

# Now what - Say I want to add 'Can add project' permission to new_group?
# permission = Permission.objects.create(codename='can_add_project',
#                                   name='Can add project',
#                                   content_type=ct)
# new_group.permissions.add(permission)

from django.contrib.auth.models import Group


# class Administrators(Group):
#    pass

#    class Meta:
#        app_label = 'authentication'

# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#    ...

#    class Meta:
#        db_table = 'Users'

# class SecurityQuestions(models.Model):
#    ...

#    class Meta:
#        app_label = 'auth'
#        db_table = 'Security_Questions'
#        verbose_name = 'Security Question'
#        verbose_name_plural = 'Security Questions'

# class ProxyUser(User):
#    pass

#    class Meta:
#        app_label = 'auth'
#        proxy = True
#        verbose_name = 'User'
#        verbose_name_plural = 'Users'

# class MarkActive(models.Model):
#      is_active = models.IntegerField(default=1,
#                              blank=True,
#                              null=True,
#                              help_text='1->Active, 0->Inactive',
#                              choices=((1, 'Active'), (0, 'Inactive')))


class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.SlugField()


class PatreonBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Patreon Background Image"
        verbose_name_plural = "Patreon Background Images"


class Patreon(models.Model):
    patreon_username = models.CharField(max_length=100, verbose_name='Patreon`s Username',
                                        help_text='The patreon`s username goes here.')
    description = models.TextField(help_text='Description of Patreon`s patreonage.')
    image = models.ImageField(
        help_text=
        'The patreon`s avatar goes here.')

    # change rest to either imagefields or urlfields (has to be uniform throughout the form)

    # widget=form.TextInput, help_text='Your name goes here.')
    class Meta:
        verbose_name = "Patreon"
        verbose_name_plural = "Patreons"


class Post(models.Model):
    name = models.CharField(max_length=100, help_text='Your name goes here.')
    catagory = models.CharField(
        max_length=100,
        help_text=
        'Choose a catagory you want your idea to affect (server layout, event idea, etc).'
    )
    description = models.TextField(
        help_text='Please share any ideas you may have.')
    image = models.URLField(
        help_text=
        'Link a URL for your idea (scales to your picture`s dimensions.)')

    class Meta:
        verbose_name = "Idea"
        verbose_name_plural = "Ideas"


class ShowcasePost(models.Model):
    name = models.CharField(max_length=100, help_text='Your name goes here.')
    description = models.TextField(help_text='Post your profile here.')
    image = models.ImageField(
        help_text=
        'Link a URL for your profile (scales to your picture`s dimensions.)')

    # change rest to either imagefields or urlfields (has to be uniform throughout the form)

    # widget=form.TextInput, help_text='Your name goes here.')
    class Meta:
        verbose_name = "User Profile Post"
        verbose_name_plural = "User Profile Posts"


"""class Post(models.Model):
    name = models.CharField(max_length=100, help_text='Your name goes here.')
    catagory = models.CharField(
        max_length=100,
        help_text=
        'Choose a catagory you want your idea to affect (server layout, event idea, etc).'
    )
    description = models.TextField(
        help_text='Please share any ideas you may have.')
    image = models.URLField(
        help_text=
        'Link a URL for your idea (scales to your picture`s dimensions.)')

    class Meta:
        verbose_name = "Idea"
        verbose_name_plural = "Ideas"
        """


class Poste(models.Model):
    name = models.CharField(max_length=100, help_text='Your name goes here.')
    catagory = models.CharField(
        max_length=100,
        help_text=
        'Type the catagory that you are voting on (server layout, event idea, administration position, etc).'
    )
    description = models.TextField(
        help_text='Please share any ideas you may have.')
    image = models.URLField(
        help_text=
        'Link a URL for your profile (scales to your picture`s dimensions.)')
    mfg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"


Rating = [('b', 'Bad'), ('a', 'Average'), ('e', 'Excellent')]


class Product(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))
    description = models.TextField()
    mfg_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=Rating)

    def __str__(self):
        return self.name

    def show_desc(self):
        return self.description[:50]


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.email


class StaffApplication(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Your name & tag go here.')
    I_have_been_in_MC_for_at_least_2_months = models.BooleanField(
        verbose_name="I have been in MC for at least 2 months", default=False, choices=((True, 'Yes'), (False, 'No')))
    I_have_been_in_a_previous_role_for_at_least_1_month = models.BooleanField(
        verbose_name="I have been in MC for at least 1 month", default=False, choices=((True, 'Yes'), (False, 'No')))
    I_can_attend_at_least_half_of_the_staff_meetings = models.BooleanField(
        verbose_name="I can attend at least half of the staff meetings.", default=False,
        choices=((True, 'Yes'), (False, 'No')))
    I_have_no_strikes_on_my_account_currently = models.BooleanField(
        verbose_name="I have no strikes on my account currently", default=False, choices=((True, 'Yes'), (False, 'No')))
    role = models.TextField(
        help_text='What role are you applying for?',
        verbose_name="Roles")
    Why_do_you_want_to_apply_for_staff = models.TextField(
        help_text='Tell us why you want to be a MegaClan Staff Member. Be descriptive.',
        verbose_name="Why do you want to apply for staff?")
    How_do_you_think_you_can_make_MC_better = models.TextField(
        help_text=
        'Tell us what you will do to make MC better as a staff member.',
        verbose_name="How do you think you can make MC better?")
    I_confirm_that_I_have_read_all_the_staff_requiernments_and_meet_all_of_them = models.BooleanField(
        verbose_name="I confirm that I have read all the staff requiernments and meet all of them.", default=False,
        choices=((True, 'Yes'), (False, 'No'))
    )

    class Meta:
        verbose_name = "Staff Application"
        verbose_name_plural = "Staff Applications"


class Partner(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Your server name goes here.')
    catagory = models.CharField(
        max_length=100,
        help_text=
        'Pick a catagory you feel your server represents (gaming, community, etc).'
    )
    description = models.TextField(
        help_text=
        'Describe your server. Tell potential members why they should join.')
    server_invite = models.URLField(
        help_text='Post your server invite link here.')


class PunishAppeal(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Your name and tag go here.')
    Rule_broken = models.CharField(
        max_length=200,
        help_text=
        'Tell us the numbers of the rule(s) you broke. Refer to our rules page to see the rules and their corresponding numbers.'
    )
    Why_I_should_have_my_punishment_revoked = models.TextField(
        help_text=
        'Tell us why we should revoke your punishment, and what you can do to fix your mistake. If you think your punishment is a mistake, tell us why.',
        verbose_name="Why I should have my punishment revoked.")
    Additional_comments = models.TextField(
        help_text='Put any additional evidence or comments you may have here.')

    class Meta:
        verbose_name = "Punish Appeal"
        verbose_name_plural = "Punishment Appeals"


class BanAppeal(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Your name and tag go here.')
    Rule_broken = models.CharField(
        max_length=200,
        help_text=
        'Tell us the numbers of the rule(s) you broke. Refer to our rules page to see the rules and their corresponding numbers.'
    )
    Why_I_should_have_my_ban_revoked = models.TextField(
        help_text=
        'Tell us why we should unban you, and tell us you can do to fix your mistake. If you think your punishment is a mistake, tell us why.',
        verbose_name="Why I should have my ban revoked.")
    Additional_comments = models.TextField(
        help_text='Put any additional evidence or comments you may have here.')

    class Meta:
        verbose_name = "Ban Appeal"
        verbose_name_plural = "Ban Appeals"


class ReportIssue(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=
        'Your name and tag go here. If you wish to stay anonymous, put "Anonymous".'
    )
    catagory = models.CharField(
        max_length=200,
        help_text='Please let us know what type of issue this is.')
    issue = models.TextField(
        help_text=
        'Describe the issue in detail. We will try to get to it as soon as possible.'
    )
    Additional_comments = models.TextField(
        help_text='Put any additional comments you may have here.')
    image = models.FileField(help_text='Please put a screenshot of the issue.')

    # class Changelog(models.Model):
    #  name = models.CharField(max_length = 100, help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
    #  catagory = models.CharField(max_length = 200, help_text='Please let us know what type of issue this is.')
    #  issue = models.TextField(help_text='Describe the issue in detail. We will try to get to it as soon as possible.')
    #  Additional_comments = models.TextField(help_text='Put any additional evidence or comments you may have here.')
    #  image = models.FileField(help_text='Please put a screenshot of the issue.')

    class Meta:
        verbose_name = "Report Issue"
        verbose_name_plural = "Report Issues"


class Support(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=
        'Your name and tag go here. If you wish to stay anonymous, put "Anonymous".'
    )
    catagory = models.CharField(
        max_length=200,
        help_text='Please let us know what type of issue you are dealing with.'
    )
    issue = models.TextField(
        help_text=
        'Describe your issue in detail. We will try to get back to you as soon as possible.'
    )
    Additional_comments = models.TextField(
        help_text='Put any additional comments you may have here.')
    image = models.URLField(
        help_text='Please attach a screenshot of your issue.')

    # class Changelog(models.Model):
    #  name = models.CharField(max_length = 100, help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
    #  catagory = models.CharField(max_length = 200, help_text='Please let us know what type of issue this is.')
    #  issue = models.TextField(help_text='Describe the issue in detail. We will try to get to it as soon as possible.')
    #  Additional_comments = models.TextField(help_text='Put any additional evidence or comments you may have here.')
    #  image = models.FileField(help_text='Please put a screenshot of the issue.')

    class Meta:
        verbose_name = "Customer Support"
        verbose_name_plural = "Customer Support"


class NewsFeed(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=
        'Your name and tag go here. If you wish to stay anonymous, put "Anonymous".'
    )
    catagory = models.CharField(
        max_length=200,
        help_text='Please let us know what form of news this is.')
    description = models.TextField(help_text='Write the news here.')
    image = models.FileField(
        help_text='Please provide a cover image for the news.')

    class Meta:
        verbose_name = "News Feed"
        verbose_name_plural = "News Feed"


class StaffProfile(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=
        'Your name and tag go here. If you wish to stay anonymous, put "Anonymous".'
    )
    position = models.CharField(
        max_length=200,
        help_text='Please let us know what staff position you serve currently.'
    )
    description = models.TextField(
        help_text=
        'Write whatever you want on your profile here (within regulations).')
    staff_feats = models.TextField(
        help_text=
        'Let us know of your transcendental feats of making MegaClan a better place.'
    )
    image = models.FileField(
        help_text='Please provide a cover image for your profile.')

    class Meta:
        verbose_name = "Staff Profile"
        verbose_name_plural = "Staff Profiles"


class Event(models.Model):
    name = models.CharField(max_length=100, help_text='Event name goes here.')
    catagory = models.CharField(
        max_length=200,
        help_text=
        'Please let us know what type of event this is (tournament, stage night, etc).'
    )
    description = models.TextField(
        help_text='Give a brief description of the event.')
    date_and_time = models.DateTimeField(null=True)
    image = models.FileField(
        help_text='Please provide a cover image for your profile.')


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/')
    # blogbackgroundimage
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(Blog,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Profile(models.Model):
    about_me = models.TextField()
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class FaviconBase(models.Model):
    favicontitle = models.TextField(verbose_name="Favicon Title")
    faviconcover = models.ImageField(upload_to='images/', verbose_name="Cover")
    faviconpage = models.TextField(verbose_name="Page Name")
    faviconurl = models.URLField(verbose_name="Page URL")
    faviconlink = models.TextField(verbose_name="Favicon Link")
    faviconsizes = models.TextField(verbose_name="Favicon Sizes", help_text="example: 180x180")
    faviconrelationship = models.TextField(verbose_name="Favicon Relationship", help_text="example: icon")
    favicontype = models.TextField(verbose_name="Favicon Type", help_text="example: .ico")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.favicontitle

    class Meta:
        verbose_name = "Favicon"
        verbose_name_plural = "Favicons"


class BackgroundImageBase(models.Model):
    backgroundtitle = models.TextField(verbose_name="Background Title")
    cover = models.ImageField(upload_to='images/')
    page = models.TextField(verbose_name="Page Name")
    url = models.URLField(verbose_name="Page URL")
    position = models.IntegerField(verbose_name="Positioning of Image")
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.backgroundtitle

    class Meta:
        verbose_name = "Background Image Base"
        verbose_name_plural = "Background Image Base"


class TextBase(models.Model):
    text = models.TextField(verbose_name="Text")
    page = models.TextField(verbose_name="Page Name")
    url = models.URLField(verbose_name="Page URL")
    header_or_textfield = models.BooleanField(verbose_name="Header or Body Text", default=1,
                                              choices=((1, 'Header'), (0, 'Body')))
    section = models.IntegerField(verbose_name="Text Section", help_text="Section Number of Text")
    exists = models.BooleanField(verbose_name="Section Taken", help_text="Is this section taken?", default=1,
                                 choices=((1, 'Yes'), (0, 'No')))
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Base"
        verbose_name_plural = "Text Base"


class BackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.title

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


class NavBar(models.Model):
    text = models.TextField()
    url = models.TextField(blank=True, null=True)
    row = models.IntegerField()
    position = models.IntegerField()
    opennew = models.BooleanField(verbose_name="Open In New Tab?", default=False,
                                  choices=((True, 'Yes'), (False, 'No')))
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Navigational Bar Dropdown"
        verbose_name_plural = "Navigational Bar Dropdowns"


class NavBarHeader(models.Model):
    text = models.TextField(help_text='This is a header.')
    section = models.TextField(max_length=200,
                               blank=True,
                               null=True,
                               help_text='ID Section of page.')
    row = models.IntegerField()
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Navigational Bar Header"
        verbose_name_plural = "Navigational Bar Headers"


class Settings(models.Model):
    username = models.CharField(help_text='Your username', max_length=200)
    password = models.CharField(help_text='Your password', max_length=200)
    coupons = models.BooleanField(verbose_name="Send me coupons", default=True, blank=True, null=True,
                                  choices=((True, 'Yes'), (False, 'No')))
    news = models.BooleanField(verbose_name="Keep me in the loop", default=True, blank=True, null=True,
                               choices=((True, 'Yes'), (False, 'No')))
    # connects to email
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"


"""class Convert(models.Model):
    username = models.TextField(help_text='Your username')
    coupons = models.BooleanField(verbose_name="Send me coupons", default=True, blank=True, null=True, choices=((True, 'Yes'), (False, 'No')))
    news = models.BooleanField(verbose_name="Keep me in the loop", default=True, blank=True, null=True, choices=((True, 'Yes'), (False, 'No')))
    #connects to email
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Convert"
        verbose_name_plural = "Converts"""


class ContentTextField(models.Model):
    text = models.TextField()
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Content Text Field Title 1"
        verbose_name_plural = "Content Text Field Titles 1"


class ContentTextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Content Text Field Description 2"
        verbose_name_plural = "Content Text Field Descriptions 2"


class ContentTextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Content Text Field Title 3"
        verbose_name_plural = "Content Text Field Titles 3"


class ContentTextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Content Text Field Description 4"
        verbose_name_plural = "Content Text Fields Descriptions 4"


class ContentTextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Content Text Field Title 5"
        verbose_name_plural = "Content Text Field Titles 5"


class ContentTextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Content Text Field Description 6"
        verbose_name_plural = "Content Text Field Descriptions 6"


class ContentTextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Content Text Field Title 7"
        verbose_name_plural = "Content Text Field Titles 7"


class ContentTextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Content Text Field Description 8"
        verbose_name_plural = "Content Text Fields Descriptions 8"


class TextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Field Title 1"
        verbose_name_plural = "Text Field Titles 1"


class TextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Field Description 2"
        verbose_name_plural = "Text Field Descriptions 2"


class TextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Field Title 3"
        verbose_name_plural = "Text Field Titles 3"


class TextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Field Description 4"
        verbose_name_plural = "Text Fields Descriptions 4"


class TextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Field Title 5"
        verbose_name_plural = "Text Field Titles 5"


class TextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Field Description 6"
        verbose_name_plural = "Text Field Descriptions 6"


class TextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Field Title 7"
        verbose_name_plural = "Text Field Titles 7"


class TextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Text Field Description 8"
        verbose_name_plural = "Text Fields Descriptions 8"


class BilletTextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Billet Text Field Title 1"
        verbose_name_plural = "Billet Text Field Titles 1"


class BilletTextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Billet Text Field Description 2"
        verbose_name_plural = "Billet Text Field Descriptions 2"


class BilletTextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Billet Text Field Title 3"
        verbose_name_plural = "Billet Text Field Titles 3"


class BilletTextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Billet Text Field Description 4"
        verbose_name_plural = "Billet Text Fields Descriptions 4"


class BilletTextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Billet Text Field Title 5"
        verbose_name_plural = "Billet Text Field Titles 5"


class BilletTextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Billet Text Field Description 6"
        verbose_name_plural = "Billet Text Field Descriptions 6"


class BilletTextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Billet Text Field Title 7"
        verbose_name_plural = "Billet Text Field Titles 7"


class BilletTextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Billet Text Field Description 8"
        verbose_name_plural = "Billet Text Fields Descriptions 8"


class AboutTextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "About Text Field Title 1"
        verbose_name_plural = "About Text Field Titles 1"


class AboutTextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "About Text Field Description 2"
        verbose_name_plural = "About Text Field Descriptions 2"


class AboutTextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "About Text Field Title 3"
        verbose_name_plural = "About Text Field Titles 3"


class AboutTextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "About Text Field Description 4"
        verbose_name_plural = "About Text Fields Descriptions 4"


class AboutTextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "About Text Field Title 5"
        verbose_name_plural = "About Text Field Titles 5"


class AboutTextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "About Text Field Description 6"
        verbose_name_plural = "About Text Field Descriptions 6"


class AboutTextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "About Text Field Title 7"
        verbose_name_plural = "About Text Field Titles 7"


class AboutTextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "About Text Field Description 8"
        verbose_name_plural = "About Text Fields Descriptions 8"


class FaqTextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 1"
        verbose_name_plural = "FAQ Text Field Titles 1"


class FaqTextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 2"
        verbose_name_plural = "FAQ Text Field Descriptions 2"


class FaqTextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 3"
        verbose_name_plural = "FAQ Text Field Titles 3"


class FaqTextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 4"
        verbose_name_plural = "FAQ Text Fields Descriptions 4"


class FaqTextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 5"
        verbose_name_plural = "FAQ Text Field Titles 5"


class FaqTextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 6"
        verbose_name_plural = "FAQ Text Field Descriptions 6"


class FaqTextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 7"
        verbose_name_plural = "FAQ Text Field Titles 7"


class FaqTextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 8"
        verbose_name_plural = "FAQ Text Fields Descriptions 8"


class FaqTextField9(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 9"
        verbose_name_plural = "FAQ Text Field Titles 9"


class FaqTextField10(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 10"
        verbose_name_plural = "FAQ Text Field Descriptions 10"


class FaqTextField11(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 11"
        verbose_name_plural = "FAQ Text Field Titles 11"


class FaqTextField12(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 12"
        verbose_name_plural = "FAQ Text Fields Descriptions 12"


class FaqTextField13(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 13"
        verbose_name_plural = "FAQ Text Field Titles 13"


class FaqTextField14(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 14"
        verbose_name_plural = "FAQ Text Field Descriptions 14"


class FaqTextField15(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 15"
        verbose_name_plural = "FAQ Text Field Titles 15"


class FaqTextField16(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 16"
        verbose_name_plural = "FAQ Text Field Descriptions 16"


class FaqTextField17(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Title 17"
        verbose_name_plural = "FAQ Text Field Titles 17"


class FaqTextField18(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "FAQ Text Field Description 18"
        verbose_name_plural = "FAQ Text Field Descriptions 18"


class StaffRanksTextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 1"
        verbose_name_plural = "StaffRanks Text Field Titles 1"


class StaffRanksTextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 2"
        verbose_name_plural = "StaffRanks Text Field Descriptions 2"


class StaffRanksTextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 3"
        verbose_name_plural = "StaffRanks Text Field Titles 3"


class StaffRanksTextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 4"
        verbose_name_plural = "StaffRanks Text Fields Descriptions 4"


class StaffRanksTextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 5"
        verbose_name_plural = "StaffRanks Text Field Titles 5"


class StaffRanksTextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 6"
        verbose_name_plural = "StaffRanks Text Field Descriptions 6"


class StaffRanksTextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 7"
        verbose_name_plural = "StaffRanks Text Field Titles 7"


class StaffRanksTextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 8"
        verbose_name_plural = "StaffRanks Text Fields Descriptions 8"


class StaffRanksTextField9(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 9"
        verbose_name_plural = "StaffRanks Text Field Titles 9"


class StaffRanksTextField10(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 10"
        verbose_name_plural = "StaffRanks Text Field Descriptions 10"


class StaffRanksTextField11(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 11"
        verbose_name_plural = "StaffRanks Text Field Titles 11"


class StaffRanksTextField12(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 12"
        verbose_name_plural = "StaffRanks Text Fields Descriptions 12"


class StaffRanksTextField13(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 13"
        verbose_name_plural = "StaffRanks Text Field Titles 13"


class StaffRanksTextField14(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 14"
        verbose_name_plural = "StaffRanks Text Field Descriptions 14"


class StaffRanksTextField15(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 15"
        verbose_name_plural = "StaffRanks Text Field Titles 15"


class StaffRanksTextField16(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 16"
        verbose_name_plural = "StaffRanks Text Field Descriptions 16"


class StaffRanksTextField17(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Title 17"
        verbose_name_plural = "StaffRanks Text Field Titles 17"


class StaffRanksTextField18(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "StaffRanks Text Field Description 18"
        verbose_name_plural = "StaffRanks Text Field Descriptions 18"


class MegaCoinsTextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "MegaCoins Text Field Title 1"
        verbose_name_plural = "MegaCoins Text Field Titles 1"


class MegaCoinsTextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "MegaCoins Text Field Description 2"
        verbose_name_plural = "MegaCoins Text Field Descriptions 2"


class MegaCoinsTextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "MegaCoins Text Field Title 3"
        verbose_name_plural = "MegaCoins Text Field Titles 3"


class MegaCoinsTextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "MegaCoins Text Field Description 4"
        verbose_name_plural = "MegaCoins Text Fields Descriptions 4"


class MegaCoinsTextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "MegaCoins Text Field Title 5"
        verbose_name_plural = "MegaCoins Text Field Titles 5"


class MegaCoinsTextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "MegaCoins Text Field Description 6"
        verbose_name_plural = "MegaCoins Text Field Descriptions 6"


class MegaCoinsTextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "MegaCoins Text Field Title 7"
        verbose_name_plural = "MegaCoins Text Field Titles 7"


class MegaCoinsTextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "MegaCoins Text Field Description 8"
        verbose_name_plural = "MegaCoins Text Fields Descriptions 8"


class InformationTextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Title 1"
        verbose_name_plural = "Information Text Field Titles 1"


class InformationTextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Description 2"
        verbose_name_plural = "Information Text Field Descriptions 2"


class InformationTextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Title 3"
        verbose_name_plural = "Information Text Field Titles 3"


class InformationTextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Description 4"
        verbose_name_plural = "Information Text Fields Descriptions 4"


class InformationTextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Title 5"
        verbose_name_plural = "Informations Text Field Titles 5"


class InformationTextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Description 6"
        verbose_name_plural = "Information Text Field Descriptions 6"


class InformationTextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Title 7"
        verbose_name_plural = "Information Text Field Titles 7"


class InformationTextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Description 8"
        verbose_name_plural = "Information Text Fields Descriptions 8"


class InformationTextField9(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Information Text Field Description 9"
        verbose_name_plural = "Information Text Fields Descriptions 9"


class RuleTextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Title 1"
        verbose_name_plural = "Rules Text Field Titles 1"


class RuleTextField2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Description 2"
        verbose_name_plural = "Rules Text Field Descriptions 2"


class RuleTextField3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Title 3"
        verbose_name_plural = "Rules Text Field Titles 3"


class RuleTextField4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Description 4"
        verbose_name_plural = "Rules Text Field Descriptions 4"


class RuleTextField5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Title 5"
        verbose_name_plural = "Rules Text Field Titles 5"


class RuleTextField6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Description 6"
        verbose_name_plural = "Rules Text Field Descriptions 6"


class RuleTextField7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Title 7"
        verbose_name_plural = "Rules Text Field Titles 7"


class RuleTextField8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Description 8"
        verbose_name_plural = "Rules Text Field Descriptions 8"


class RuleTextField9(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Title 9"
        verbose_name_plural = "Rules Text Field Titles 9"


class RuleTextField10(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Description 10"
        verbose_name_plural = "Rules Text Field Descriptions 10"


class RuleTextField11(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Title 11"
        verbose_name_plural = "Rules Text Field Titles 11"


class RuleTextField12(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Rules Text Field Description 12"
        verbose_name_plural = "Rules Text Field Descriptions 12"


class DonorBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

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
    page = models.TextField(verbose_name="Page Name")
    url = models.URLField(verbose_name="Page URL")
    position = models.IntegerField()
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.overtitle

    class Meta:
        verbose_name = "Page Title"
        verbose_name_plural = "Page Titles"


class BaseCopyrightTextField(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

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
    # description = models.TextField(help_text='Post your profile here.')
    # image = models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post Background Image"
        verbose_name_plural = "Post Background Images"


class PosteBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    # name = models.CharField(max_length=100, help_text='Your name goes here.')
    # description = models.TextField(help_text='Post your profile here.')
    # image = models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post Background Image"
        verbose_name_plural = "Post Background Images"


class VoteBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    # name = models.CharField(max_length=100, help_text='Your name goes here.')
    # description = models.TextField(help_text='Post your profile here.')
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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

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
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Addons Background Image"
        verbose_name_plural = "Addons Background Images"


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

from django.db.models.signals import post_save

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

from django.utils import timezone
import pytz
from django.utils.timezone import make_aware

from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)


# Create your models here.
class SupportChat(models.Model):
    name = models.CharField(max_length=1000)

    # datetime.now()
    # api_time = models.DateTimeField()


class SupportMessage(models.Model):
    value = models.CharField(max_length=1000000)
    # now = datetime.datetime.now()
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)


# from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField

CATEGORY_CHOICES = (
    ('G', 'Gold'),
    ('P', 'Platinum'),
    ('E', 'Emerald'),
    ('D', 'Diamond'),
)

LABEL_CHOICES = (
    ('N', 'New'),
    ('BS', 'Best Seller'),
    ('BV', 'Best Value'),
)

TYPE_CHOICES = (('S', 'Singles'), ('BP', 'Booster Pack'),
                ('BB', 'Booster Box'), ('PP', 'Pokemon Product'), ('O',
                                                                   'Other'))

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    # related name could be a possible solution
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class ProfileDetails(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_image',
                                        null=True,
                                        blank=True)
    about_me = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


# link the profiledetails page to settings


"""class Settings(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    #password =
    full_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Settings"
        """


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1000)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    relateditems = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("showcase:product", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("showcase:add-to-cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("showcase:remove-from-cart", kwargs={'slug': self.slug})


class EBackgroundImage(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    items = Item.objects.all()
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))

    def __str__(self):
        return self.title

    # def __str__(self):
    #    return self.__annotations__title

    class Meta:
        verbose_name = "Ecommerce Background Image"
        verbose_name_plural = "Ecommerce Background Images"


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


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

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

    class Meta:
        verbose_name_plural = 'Order Items'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('Address',
                                         related_name='shipping_address',
                                         on_delete=models.SET_NULL,
                                         blank=True,
                                         null=True)
    billing_address = models.ForeignKey('Address',
                                        related_name='billing_address',
                                        on_delete=models.SET_NULL,
                                        blank=True,
                                        null=True)
    payment = models.ForeignKey('Payment',
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True)
    coupon = models.ForeignKey('Coupon',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    id = uuid4()
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


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1000, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=150)
    amount = models.FloatField()
    percentDollars = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


class Contact(models.Model):
    from_email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100,
                               help_text='Subject of your message.')
    message = models.TextField(help_text='Your message goes here.')

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Checkout Addresses'


from django.utils import timezone


class State(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')))
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


# from tinymce.models import HTMLField
# from django.dispatch import receiver
# from django.db.models.signals import post_save

# Create your models here.

# class ProfileTwo(models.Model):
# user = models.OneToOneField(User, on_delete=models.CASCADE)
# products = models.ManyToManyField(Product)

# @receiver(post_save, sender=User) #add this
# def create_user_profile(sender, instance, created, **kwargs):
# if created:
# ProfileTwo.objects.create(user=instance)

# @receiver(post_save, sender=User) #add this
# def save_user_profile(sender, instance, **kwargs):
# instance.profile.save()


class UserProfile2(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_image',
                                        null=True,
                                        blank=True)

    class Meta:
        verbose_name = "Edit Profile"
        verbose_name_plural = "Edit Profiles"


def create_profile(sender, **kwargs):
    if (kwargs['created']):
        user_profile = UserProfile2.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

