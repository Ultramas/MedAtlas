from django.contrib import admin
from .models import UpdateProfile, Questionaire
from .models import Idea
from .models import Vote
from .models import Product
from .models import City
from .models import StaffApplication
from .models import PartnerApplication
from .models import PunishmentAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import Feedback
from .models import Blog
from .models import Preference
from .models import PostLikes
from .models import Idea, Comment
from .models import Profile
from .models import HyperlinkBase
from .models import Room, Message
from .models import SupportMessage
from .models import ProfileDetails
from .models import UserProfile
from .models import UserProfile2
from .models import SettingsModel
from .models import Support
#from .models import ConvertBackgroundImage
#from .models import BackgroundImage
#from .models import BackgroundImage2a
from .models import EBackgroundImage
from .models import ShowcaseBackgroundImage
from .models import ChatBackgroundImage
from .models import SupportChatBackgroundImage
from .models import BilletBackgroundImage
from .models import BlogBackgroundImage
from .models import PostBackgroundImage
from .models import RuleBackgroundImage
from .models import AboutBackgroundImage
from .models import FaqBackgroundImage
from .models import StaffBackgroundImage
from .models import InformationBackgroundImage
from .models import TagBackgroundImage
from .models import StaffRanksBackgroundImage
from .models import MegaBackgroundImage
from .models import UserBackgroundImage
from .models import EventBackgroundImage
from .models import NewsBackgroundImage
from .models import DonorBackgroundImage
from .models import ContentBackgroundImage
from .models import PartnerBackgroundImage
from .models import WhyBackgroundImage
from .models import SettingsBackgroundImage
from .models import PerksBackgroundImage
from .models import FaviconBase
from .models import LogoBase
from .models import BackgroundImageBase
from .models import TextBase
from .models import Titled
from .models import NavBar
from .models import NavBarHeader
from .models import ImageCarousel
from .models import BaseCopyrightTextField
from .models import AdvertisementBase
#from .models import ResizeImageMixin
from .models import ImageBase
from .models import DonateIcon
from .models import Coupon
from .models import (Item, OrderItem, Order, CheckoutAddress, Payment)
from .models import OrderItemField
from .models import Contact
from .models import BusinessMailingContact
from .models import Feedback
from .models import Order
from .models import Donate
from .models import EmailField
from .models import AdminRoles
from .models import AdminTasks
from .models import AdminPages
from django.contrib.auth.models import Group
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy


class categoryAdmin(admin.ModelAdmin):
    pass


class publisherAdmin(admin.ModelAdmin):
    pass


class detailsAdmin(admin.ModelAdmin):
    pass


class authorAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(UpdateProfile, categoryAdmin)
admin.site.register(Idea, categoryAdmin)
admin.site.register(Vote, authorAdmin)
admin.site.register(StaffApplication, authorAdmin)
admin.site.register(PartnerApplication)
admin.site.register(PunishmentAppeal)
admin.site.register(BanAppeal)
admin.site.register(ReportIssue)
admin.site.register(NewsFeed)
admin.site.register(StaffProfile)
admin.site.register(Profile)
admin.site.register(SettingsModel)
#admin.site.register(SettingsBackgroundImage)
#admin.site.register(ConvertBackgroundImage)
admin.site.register(NavBar)
admin.site.register(NavBarHeader)
admin.site.register(UserProfile)
admin.site.register(UserProfile2)
admin.site.register(Support)
admin.site.register(Preference)
admin.site.register(PostLikes)
#admin.site.register(BackgroundImage)
#admin.site.register(BackgroundImage2a)
#admin.site.register(EBackgroundImage)
#admin.site.register(ShowcaseBackgroundImage)
#admin.site.register(ChatBackgroundImage)
#admin.site.register(SupportChatBackgroundImage)
#admin.site.register(BilletBackgroundImage)
#admin.site.register(PostBackgroundImage)
#admin.site.register(RuleBackgroundImage)
#admin.site.register(AboutBackgroundImage)
#admin.site.register(FaqBackgroundImage)
#admin.site.register(StaffBackgroundImage)
#admin.site.register(InformationBackgroundImage)
#admin.site.register(TagBackgroundImage)
#admin.site.register(StaffRanksBackgroundImage)
#admin.site.register(MegaBackgroundImage)
#admin.site.register(UserBackgroundImage)
#admin.site.register(EventBackgroundImage)
#admin.site.register(NewsBackgroundImage)
#admin.site.register(DonorBackgroundImage)
#admin.site.register(ContentBackgroundImage)
#admin.site.register(PartnerBackgroundImage)
#admin.site.register(WhyBackgroundImage)
#admin.site.register(PerksBackgroundImage)
admin.site.register(FaviconBase)
admin.site.register(BackgroundImageBase)
admin.site.register(ImageCarousel)
admin.site.register(Titled)
admin.site.register(BaseCopyrightTextField)
#admin.site.register(ResizeImageMixin)
admin.site.register(ImageBase)
admin.site.register(DonateIcon)
admin.site.register(Contact)
admin.site.register(BusinessMailingContact)
#admin.site.register(BackgroundImages)
admin.site.register(Coupon)
#admin.site.register(Feedback)
admin.site.register(EmailField)
admin.site.register(AdminRoles)
admin.site.register(AdminTasks)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .models import User, SecurityQuestions, ProxyUser

#admin.site.register(ProxyUser, UserAdmin)
#admin.site.register(SecurityQuestions)


class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy('MegaClan Administration')

    # Text to put in each page's <h1> (and above login form).
    site_header = gettext_lazy('〖𐌑𐌂〗 Administration')

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('Webite Administration')


admin_site = MyAdminSite()


# Admin Action Functions
def change_rating(modeladmin, request, queryset):
    queryset.update(rating='e')


# Action description
change_rating.short_description = "Mark Selected Products as Excellent"


# ModelAdmin Class
class ProductA(admin.ModelAdmin):
    list_display = ('name', 'description', 'mfg_date', 'rating')
    list_filter = (
        'name',
        'description',
        'mfg_date',
    )
    actions = [change_rating]


admin.site.register(Product, ProductA)


class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "state",
    )


admin.site.register(City, CityAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status", )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}


#admin.site.register(Blog, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Room)
admin.site.register(SupportMessage)
admin.site.register(Message)
#admin.site.register(OrderItem)
admin.site.register(OrderItemField)
admin.site.register(Order)
admin.site.register(CheckoutAddress)
admin.site.register(Payment)
admin.site.register(Questionaire)

from django.contrib import messages
from .models import State


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_on')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True

    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=1)
        messages.success(
            request, "Selected Record(s) Marked as Active Successfully !!")

    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=0)
        messages.success(
            request, "Selected Record(s) Marked as Inactive Successfully !!")

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")


admin.site.register(State, StateAdmin)

#from .models import ExtendUser
# Register your models here.
#admin.site.register(ExtendUser)

#from .models import Group
from .forms import GroupAdminForm

# Unregister the original Group admin.
admin.site.unregister(Group)


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)

from .models import Feedback
from .forms import FeedbackForm

class FeedbackAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Feedback Information', {
            'fields': ('item', 'order', 'star_rating', 'comment', 'image')
        }),
        ('Feedback Information - Read-only Fields', {
            'fields': ('slug', 'username'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Feedback, FeedbackAdmin)

class HyperlinkBaseAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Hyperlink Information - Text Display', {
            'fields': ('display_text',),
            'classes': ('collapse',),
        }),
        ('Hyperlink Information - Image Display', {
            'fields': ('display_image', 'alternate', 'image_length', 'image_width', 'length_for_resize', 'width_for_resize',),
            'classes': ('collapse',),
        }),
        ('Hyperlink Information', {
            'fields': ('hyperlink', 'section', 'page', 'hyperlink_type', 'is_active'),
        }),
    )

admin.site.register(HyperlinkBase, HyperlinkBaseAdmin)

class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Item Information - Categorical Descriptions', {
            'fields': ('title', 'category', 'label', 'slug', 'description', 'is_active',),
            'classes': ('collapse-open',),  # Open by default
        }),
        ('Item Information - Prices', {
            'fields': ('price', 'discount_price',),
            'classes': ('collapse',),  # Open by default
        }),
        ('Item Information - Image', {
            'fields': ('image', 'image_length', 'image_width', 'length_for_resize', 'width_for_resize',),
            'classes': ('collapse-open',),  # Open by default
        }),
        ('Item Information - Related Items', {
            'fields': ('relateditems',),
            'classes': ('collapse-open',),  # Open by default
        }),
    )

    class Media:
        js = ('admin-collapse-default.js',)
        css = {
            'all': ('admin-collapse-default.css',)
        }

admin.site.register(Item, ItemAdmin)
class LogoBaseAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Logo Information - Categorical Descriptions', {
            'fields': ('title', 'hyperlink', 'section', 'page', 'is_active',),
            'classes': ('collapse-open',),  # Open by default
        }),
        ('Logo Information - Image', {
            'fields': ('logocover', 'logo_length', 'logo_width', 'length_for_resize', 'width_for_resize',),
            'classes': ('collapse-open',),  # Open by default
        }),
    )

    class Media:
        js = ('admin-collapse-default.js',)  # Include the custom JavaScript file
        css = {
            'all': ('admin-collapse-default.css',)
        }

admin.site.register(LogoBase, LogoBaseAdmin)

class BlogAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Blog Information - Categorical Descriptions', {
            'fields': ('title', 'slug', 'author', 'content', 'status', 'is_active',),
            'classes': ('collapse-open',),  # Open by default
        }),
        ('Blog Information - Image', {
            'fields': ('image', 'image_length', 'image_width',),
            'classes': ('collapse-open',),  # Open by default
        }),

        ('Blog Information - Likes/Dislikes', {
            'fields': ('likes', 'dislikes',),
            'classes': ('collapse-open',),  # Open by default
        }),
    )

    class Media:
        js = ('admin-collapse-default.js',)  # Include the custom JavaScript file
        css = {
            'all': ('admin-collapse-default.css',)
        }

admin.site.register(Blog, BlogAdmin)


class TextBaseAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Text Base Information - Categorical Descriptions', {
            'fields': ('text', 'page', 'url', 'is_active',),
            'classes': ('collapse-open',),  # Open by default
        }),
        ('Text Base  Information - Attributes', {
            'fields': ('header_or_textfield', 'section', 'text_size', 'hyperlink'),
            'classes': ('collapse-open',),  # Open by default
        }),
    )

    class Media:
        js = ('admin-collapse-default.js',)  # Include the custom JavaScript file
        css = {
            'all': ('admin-collapse-default.css',)
        }

admin.site.register(TextBase, TextBaseAdmin)

class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Event Information - Categorical Descriptions', {
            'fields': ('user', 'name', 'category', 'description', 'image',),
            'classes': ('collapse-open',),  # Open by default
        }),
        ('Event  Information - Attributes', {
            'fields': ('date_and_time','slug', 'anonymous', 'is_active',),
            'classes': ('collapse-open',),  # Open by default
        }),
    )
    class Media:
        js = ('admin-collapse-default.js',)  # Include the custom JavaScript file
        css = {
            'all': ('admin-collapse-default.css',)
        }

admin.site.register(Event, EventAdmin)

class AdvertisementBaseAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Advertisement Base Information - Categorical Descriptions', {
            'fields': ('advertisementtitle', 'page', 'type',),
            'classes': ('collapse-open',),  # Open by default
        }),
        ('Advertisement Base Information - Advertisement', {
            'fields': ('advertisement', 'advertisement_length', 'advertisement_width', 'length_for_resize', 'width_for_resize', 'xposition', 'yposition',),
            'classes': ('collapse-open',),  # Open by default
        }),
        ('Advertisement Base  Information - Attributes', {
            'fields': ('advertisement_position','relevance', 'correlating_product', 'advertisement_hyperlink', 'is_active',),
            'classes': ('collapse-open',),  # Open by default
        }),
    )

    class Media:
        js = ('admin-collapse-default.js',)  # Include the custom JavaScript file
        css = {
            'all': ('admin-collapse-default.css',)
        }

admin.site.register(AdvertisementBase, AdvertisementBaseAdmin)

class ProfileDetailsAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Profile Information', {
            'fields': ('user', 'email', 'avatar', 'alternate', 'about_me', 'is_active')
        }),
    )
    readonly_fields = ('position',)

admin.site.register(ProfileDetails, ProfileDetailsAdmin)

class AdministrationPagesAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Administration Pages Information', {
            'fields': ('pages', 'hyperlink', 'opennew',)
        }),
        ('Administration Pages Information - Attributes', {
            'fields': ('section', 'page_name', 'is_active',)
        }),
    )

admin.site.register(AdminPages, AdministrationPagesAdmin)

admin.site.register(Donate)

