from django.contrib import admin
from .models import ShowcasePost
from .models import Post
from .models import Poste
from .models import Product
from .models import City
from .models import StaffApplication
from .models import Partner
from .models import PunishAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import Patreon
from .models import Blog
from .models import Post, Comment
from .models import Profile
from .models import Room, Message
#from .models import ProfileDetails
from .models import UserProfile
from .models import UserProfile2
from .models import SettingsModel
from .models import ConvertBackgroundImage
from .models import BackgroundImage
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
from .models import FaviconBase
from .models import BackgroundImageBase
from .models import TextBase
from .models import Titled
from .models import NavBar
from .models import NavBarHeader
from .models import ImageCarousel
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
from .models import FaqTextField
from .models import FaqTextField2
from .models import FaqTextField3
from .models import FaqTextField4
from .models import FaqTextField5
from .models import FaqTextField6
from .models import FaqTextField7
from .models import FaqTextField8
from .models import FaqTextField9
from .models import FaqTextField10
from .models import FaqTextField11
from .models import FaqTextField12
from .models import FaqTextField13
from .models import FaqTextField14
from .models import FaqTextField15
from .models import FaqTextField16
from .models import FaqTextField17
from .models import FaqTextField18
from .models import StaffRanksTextField
from .models import StaffRanksTextField2
from .models import StaffRanksTextField3
from .models import StaffRanksTextField4
from .models import StaffRanksTextField5
from .models import StaffRanksTextField6
from .models import StaffRanksTextField7
from .models import StaffRanksTextField8
from .models import StaffRanksTextField9
from .models import StaffRanksTextField10
from .models import StaffRanksTextField11
from .models import StaffRanksTextField12
from .models import StaffRanksTextField13
from .models import StaffRanksTextField14
from .models import StaffRanksTextField15
from .models import StaffRanksTextField16
from .models import StaffRanksTextField17
from .models import StaffRanksTextField18
from .models import MegaCoinsTextField
from .models import MegaCoinsTextField2
from .models import MegaCoinsTextField3
from .models import MegaCoinsTextField4
from .models import MegaCoinsTextField5
from .models import MegaCoinsTextField6
from .models import MegaCoinsTextField7
from .models import MegaCoinsTextField8
from .models import InformationTextField
from .models import InformationTextField2
from .models import InformationTextField3
from .models import InformationTextField4
from .models import InformationTextField5
from .models import InformationTextField6
from .models import InformationTextField7
from .models import InformationTextField8
from .models import InformationTextField9
from .models import RuleTextField
from .models import RuleTextField2
from .models import BaseCopyrightTextField
from .models import DonateIcon
from .models import Coupon
#from  django.contrib.auth.models import BackgroundImages
from .models import (Item, OrderItem, Order, CheckoutAddress, Payment)
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
admin.site.register(ShowcasePost, categoryAdmin)
admin.site.register(Post, categoryAdmin)
admin.site.register(Poste, authorAdmin)
admin.site.register(StaffApplication, authorAdmin)
admin.site.register(Partner)
admin.site.register(PunishAppeal)
admin.site.register(BanAppeal)
admin.site.register(ReportIssue)
admin.site.register(NewsFeed)
admin.site.register(StaffProfile)
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Patreon)
admin.site.register(SettingsModel)
admin.site.register(SettingsBackgroundImage)
admin.site.register(ConvertBackgroundImage)
admin.site.register(NavBar)
admin.site.register(NavBarHeader)
#admin.site.register(ProfileDetails)
admin.site.register(UserProfile)
admin.site.register(UserProfile2)
admin.site.register(BackgroundImage)
#admin.site.register(BackgroundImage2a)
admin.site.register(EBackgroundImage)
admin.site.register(ShowcaseBackgroundImage)
admin.site.register(ChatBackgroundImage)
admin.site.register(SupportChatBackgroundImage)
admin.site.register(BilletBackgroundImage)
admin.site.register(BlogBackgroundImage)
admin.site.register(PostBackgroundImage)
admin.site.register(RuleBackgroundImage)
admin.site.register(AboutBackgroundImage)
admin.site.register(FaqBackgroundImage)
admin.site.register(StaffBackgroundImage)
admin.site.register(InformationBackgroundImage)
admin.site.register(TagBackgroundImage)
admin.site.register(StaffRanksBackgroundImage)
admin.site.register(MegaBackgroundImage)
admin.site.register(UserBackgroundImage)
admin.site.register(EventBackgroundImage)
admin.site.register(NewsBackgroundImage)
admin.site.register(DonorBackgroundImage)
admin.site.register(ContentBackgroundImage)
admin.site.register(PartnerBackgroundImage)
admin.site.register(WhyBackgroundImage)
admin.site.register(FaviconBase)
admin.site.register(BackgroundImageBase)
admin.site.register(TextBase)
admin.site.register(ImageCarousel)
admin.site.register(Titled)
admin.site.register(TextField)
admin.site.register(TextField2)
admin.site.register(TextField3)
admin.site.register(TextField4)
admin.site.register(TextField5)
admin.site.register(TextField6)
admin.site.register(TextField7)
admin.site.register(TextField8)
admin.site.register(BilletTextField)
admin.site.register(BilletTextField2)
admin.site.register(BilletTextField3)
admin.site.register(BilletTextField4)
admin.site.register(BilletTextField5)
admin.site.register(BilletTextField6)
admin.site.register(BilletTextField7)
admin.site.register(BilletTextField8)
admin.site.register(AboutTextField)
admin.site.register(AboutTextField2)
admin.site.register(AboutTextField3)
admin.site.register(AboutTextField4)
admin.site.register(AboutTextField5)
admin.site.register(AboutTextField6)
admin.site.register(AboutTextField7)
admin.site.register(AboutTextField8)
admin.site.register(FaqTextField)
admin.site.register(FaqTextField2)
admin.site.register(FaqTextField3)
admin.site.register(FaqTextField4)
admin.site.register(FaqTextField5)
admin.site.register(FaqTextField6)
admin.site.register(FaqTextField7)
admin.site.register(FaqTextField8)
admin.site.register(FaqTextField9)
admin.site.register(FaqTextField10)
admin.site.register(FaqTextField11)
admin.site.register(FaqTextField12)
admin.site.register(FaqTextField13)
admin.site.register(FaqTextField14)
admin.site.register(FaqTextField15)
admin.site.register(FaqTextField16)
admin.site.register(FaqTextField17)
admin.site.register(FaqTextField18)
admin.site.register(StaffRanksTextField)
admin.site.register(StaffRanksTextField2)
admin.site.register(StaffRanksTextField3)
admin.site.register(StaffRanksTextField4)
admin.site.register(StaffRanksTextField5)
admin.site.register(StaffRanksTextField6)
admin.site.register(StaffRanksTextField7)
admin.site.register(StaffRanksTextField8)
admin.site.register(StaffRanksTextField9)
admin.site.register(StaffRanksTextField10)
admin.site.register(StaffRanksTextField11)
admin.site.register(StaffRanksTextField12)
admin.site.register(StaffRanksTextField13)
admin.site.register(StaffRanksTextField14)
admin.site.register(StaffRanksTextField15)
admin.site.register(StaffRanksTextField16)
admin.site.register(StaffRanksTextField17)
admin.site.register(StaffRanksTextField18)
admin.site.register(MegaCoinsTextField)
admin.site.register(MegaCoinsTextField2)
admin.site.register(MegaCoinsTextField3)
admin.site.register(MegaCoinsTextField4)
admin.site.register(MegaCoinsTextField5)
admin.site.register(MegaCoinsTextField6)
admin.site.register(MegaCoinsTextField7)
admin.site.register(MegaCoinsTextField8)
admin.site.register(InformationTextField)
admin.site.register(InformationTextField2)
admin.site.register(InformationTextField3)
admin.site.register(InformationTextField4)
admin.site.register(InformationTextField5)
admin.site.register(InformationTextField6)
admin.site.register(InformationTextField7)
admin.site.register(InformationTextField8)
admin.site.register(InformationTextField9)
admin.site.register(RuleTextField)
admin.site.register(RuleTextField2)
admin.site.register(BaseCopyrightTextField)
admin.site.register(DonateIcon)
#admin.site.register(BackgroundImages)
admin.site.register(Coupon)

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


admin.site.register(Blog, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(CheckoutAddress)
admin.site.register(Payment)

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
