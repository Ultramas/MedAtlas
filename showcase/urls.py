"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from .views import HomePageView, SearchResultsView, EcommerceSearchResultsView

# remove this:
# from . import settings
#####
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
# add this:
from . import views
#####

from .views import ProfileView

from .views import contactView, successView

from .views import profile

# from django.chatbot.views import web_hook

# from changelog.views import ChangelogView

from .views import (
    remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    remove_single_item_from_cart,
    AddCouponView,
    RequestRefundView,
    ItemDetailView,
    BackgroundView,
    EBackgroundView,
    BilletBackgroundView,
    ChatBackgroundView,
    SupportChatBackgroundView,
    ShowcaseBackgroundView,
    BlogBackgroundView,
    PostBackgroundView,
    RuleBackgroundView,
    AboutBackgroundView,
    FaqBackgroundView,
    StaffBackgroundView,
    InformationBackgroundView,
    TagBackgroundView,
    UserBackgroundView,
    StaffRanksBackgroundView,
    MegaBackgroundView,
    EventBackgroundView,
    NewsBackgroundView,
    BaseView,
    EBaseView,
    MemberBaseView,
    DonateBaseView,
    #SubmitFeedbackView,
    PostingView,
    DonorView,
    DonationsView,
    ContributorBackgroundView,
    ContentBackgroundView,
    PartnerBackgroundView,
    ShareBackgroundView,
    DonateIconView,
    PostView,
    PostList,
    PosteView,
    BlogComment,
    BlogBackgroundView,
    BlogBaseView,
    RoomView,
    FeedbackView,
    ContactViewe,
    BusinessMailingView,
    BusinessEmailViewe,
    WhyBackgroundView,
    StaffApplyBackgroundView,
    ConvertBackgroundView,
    ReasonsBackgroundView,
    ContactSuccessView,
    BusinessSuccessMailingView,
    SignupView,
    ChangePasswordView,
    PerksBackgroundView,
    IssueBackgroundView,
    AdminRolesView,
    AdminTasksView,
    AdminPagesView,
    AdministrationView,
    SettingsView,
    SettingsBackgroundView,
    DonateView,
    DonateHistoryView,
    PatreonedView,
    OrderHistory,
    submit_feedback,
    detail_post_view,
    postpreference,
    getMessages,
    AdvertisementView,
    MemberHomeBackgroundView,

)

from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)

app_name = 'showcase'

from django.contrib.auth import views as auth_views

urlpatterns = [

    re_path(r'^(id)/$', detail_post_view, name='like'),
    path(r'blogpost-like/<str:post_name>/preference/<like_or_dislike>/', postpreference, name='preference'),
    # path(r'blogpost-like/<slug:slug>/preference/<like_or_dislike>/', postpreference, name='preference'),
    # path('preference/<int:like_or_dislike>/', postpreference, name='preference'),

    # add these
    path('showcase/', views.ShowcaseBackgroundView.as_view(), name='showcase'),
    path('memberhome/', views.MemberHomeBackgroundView.as_view(), name='memberhome'),
    path('post_edit/', views.PostingView.as_view(), name='post_edit'),
    # path('post_edit/', views.PostBackgroundView.as_view(), name='post_edit'),
    # works at the cost of the post display
    path('blog/', views.PostList.as_view(), name='blog'),
    # works at the cost of the blog display
    path('users/', views.UserBackgroundView.as_view(), name='users'),
    path('voting/', views.votingview.as_view(), name='voting'),
    path('partners/', views.PartnerBackgroundView.as_view(), name='partners'),
    # path('newsfeed/', views.newsfeedview.as_view(), name='newsfeed'),
    # path('staff/', views.staffview.as_view(), name='staff'),
    # path('events/', views.eventview.as_view(), name='events'),
    path('events/', views.EventBackgroundView.as_view(), name='events'),
    # path('blog/', views.BlogBackgroundView, name='blog'),
    path('featuredproducts/', views.Featured.as_view(), name='featuredproducts'),
    # path('post_edit/', views.post_new, name='post_edit'),
    path('vote/', views.PosteView.as_view(), name='vote'),
    # path('share/, views.post, name='share'),
    path('share/', views.ShareBackgroundView.as_view(), name='share'),
    path('ideas/', views.PostView.as_view(), name='ideas'),
    path('cv-form/', views.SignupView.as_view(), name='cv-form'),
    path('staffapplications/', views.StaffApplyBackgroundView.as_view(), name='staffapplications'),
    path('punishapps/', views.PunishAppsBackgroundView.as_view(), name='punishapps'),
    path('banappeals/', views.BanAppealBackgroundView.as_view(), name='banappeals'),
    path('issues/', views.IssueBackgroundView.as_view(), name='issues'),
    #    path('profile/', views.phome, name='profile'),

    # changed name to cv-form, is that what you want?
    #####
    path('supportissues/', views.supportview.as_view(), name='supportissues'),
    path('', views.BackgroundView.as_view(), name='index'),
    path('ehome/', views.EBackgroundView.as_view(), name='ehome'),
    path('ehome/<int:page>/', views.EBackgroundView.as_view(), name='ehome'),
    path('home/', views.ChatBackgroundView.as_view(), name='home'),
    path('billets/', views.BilletBackgroundView.as_view(), name='billets'),
    # path('', views.Background2aView.as_view(), name='index'),
    path('supportissues/', TemplateView.as_view(template_name='supportissues.html'), name='supportissues'),
    path('supportchat/', views.SupportChatBackgroundView.as_view(), name='supportchat'),
    path('privateroom/', TemplateView.as_view(template_name='privateroom.html'), name='privateroom'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('', TemplateView.as_view(template_name='index.html'), name = 'index'),
    path('website/', TemplateView.as_view(template_name='website.html'), name='website'),
    path('about/', views.AboutBackgroundView.as_view(), name='about'),
    path('commitment/', TemplateView.as_view(template_name='commitment.html'), name='commitment'),
    path('faq/', views.FaqBackgroundView.as_view(), name='faq'),
    path('servers/', TemplateView.as_view(template_name='servers.html'), name='servers'),
    path('notloggedin/', TemplateView.as_view(template_name='notloggedin.html'), name='notloggedin'),
    path('pricing/', TemplateView.as_view(template_name='pricing.html'), name='pricing'),
    path('whydonate/', views.WhyBackgroundView.as_view(), name='whydonate'),
    path('users/', TemplateView.as_view(template_name='users.html'), name='users'),
    path('share/', TemplateView.as_view(template_name='share.html'), name='share'),
    #path('events/', TemplateView.as_view(template_name='events.html'), name='events'),
    path('newsfeed/', views.NewsBackgroundView.as_view(), name='newsfeed'),
    path('staff/', views.StaffBackgroundView.as_view(), name='staff'),
    path('admin/', TemplateView.as_view(template_name='admin.html'), name='admin'),
    path('voting/', TemplateView.as_view(template_name='voting.html'), name='voting'),
    # path('contact/', TemplateView.as_view(template_name='email.html'), name='contact'),
    path('ao/', TemplateView.as_view(template_name='ao.html'), name='ao'),
    path('contributors/', views.ContributorBackgroundView.as_view(), name='contributors'),
    path('mantenience/', TemplateView.as_view(template_name='mantenience.html'), name='mantenience'),
    path('cost/', TemplateView.as_view(template_name='cost.html'), name='cost'),
    path('tiers/', TemplateView.as_view(template_name='tiers.html'), name='tiers'),
    path('perks/', views.PerksBackgroundView.as_view(), name='perks'),
    path('morecontent/', views.ContentBackgroundView.as_view(), name='morecontent'),
    path('lordsmonkey/', TemplateView.as_view(template_name='lordsmonkey.html'), name='lordsmonkey'),
    #path('myaccount/', TemplateView.as_view(template_name='myaccount.html'), name='myaccount'),
    path('myaccount', views.SettingsView.as_view(), name='myaccount'),
    path('settings', views.SettingsBackgroundView.as_view(), name='settings'),
    path('addons/', TemplateView.as_view(template_name='addons.html'), name='addons'),
    path('rules/', views.RuleBackgroundView.as_view(), name='rules'),
    path('staffapplications/', TemplateView.as_view(template_name='staffapplications.html'), name='staffapplications'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('social-auth/sociallogin', TemplateView.as_view(template_name='sociallogin.html'), name='sociallogin'),
    path('password_reset/', TemplateView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', TemplateView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/', TemplateView.as_view(template_name='password_reset_confirm.html.html'),
         name='password_reset_confirm.html'),
    path('password_reset_complete/', TemplateView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('email/', TemplateView.as_view(template_name='email.html'), name='email'),
    path('profilehome/', TemplateView.as_view(template_name='profilehome.html'), name='home'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    #path('blog/<int:pk>/', views.ProfileDetails.as_view(), name='profile'),
    path('profile/edit/<int:pk>', views.edit_profile, name="edit_profile"),
    #path('profile/', views.profile, name="profile"),
    path('like/<username>/', profile, name='like'), #consider making it views.profile
    path('administration/', AdministrationView.as_view(), name='administration'),
    path('administrativeroles/', AdminRolesView.as_view(), name='administrativeroles'),
    path('administrativetasks/', AdminTasksView.as_view(), name='administrativetasks'),
    path('administrativepages/', AdminPagesView.as_view(), name='administrativepages'),
    path('issues/', TemplateView.as_view(template_name='issues.html'), name='issues'),
    path('punishapps/', TemplateView.as_view(template_name='punishapps.html'), name='punishapps'),
    path('banappeals/', TemplateView.as_view(template_name='banappeals.html'), name='banappeals'),
    path('information/', views.InformationBackgroundView.as_view(), name='information'),
    path('invite/', TemplateView.as_view(template_name='invite.html'), name='invite'),
    path('partners/', TemplateView.as_view(template_name='partners.html'), name='partners'),
    path('tag/', views.TagBackgroundView.as_view(), name='tag'),
    path('originalmembers/', TemplateView.as_view(template_name='originalmembers.html'), name='originalmembers'),
    path('staffranks/', views.StaffRanksBackgroundView.as_view(), name='staffranks'),
    path('boosts/', TemplateView.as_view(template_name='boosts.html'), name='boosts'),
    path('donors/', views.DonationsView.as_view(), name='donors'),
    path('megacoins/', views.MegaBackgroundView.as_view(), name='megacoins'),
    path('main/', TemplateView.as_view(template_name='main.html'), name='main'),
    path('staffdone/', TemplateView.as_view(template_name='staffdone.html'), name='staffdone'),
    path('issuedone/', TemplateView.as_view(template_name='issuedone.html'), name='issuedone'),
    path('bandone/', TemplateView.as_view(template_name='bandone.html'), name='bandone'),
    path('punishdone/', TemplateView.as_view(template_name='punishdone.html'), name='punishdone'),
    path('memberbase/', TemplateView.as_view(template_name='memberbase.html'), name='memberbase'),
    # path('billets/', TemplateView.as_view(template_name='billets.html'), name = 'billets'),
    path('ad/', TemplateView.as_view(template_name='ad.html'), name='ad'),
    path('giveaways/', TemplateView.as_view(template_name='giveaways.html'), name='giveaways'),
    path('hostgiveaway/', TemplateView.as_view(template_name='hostgiveaway.html'), name='hostgiveaway'),
    # path('changelog/', ChangelogView.as_view(), name='changelog'),
    path('blogbase/', BlogBaseView.as_view(), name='blogbase'),
    path('base/', BaseView.as_view(), name='base'),
    path('sidebar/', TemplateView.as_view(template_name='sidebar.html'), name='sidebar'),
    path('quantumentangling/', TemplateView.as_view(template_name='quantumentangling.html'), name='quantumentangling'),
    path('featuredproducts/', TemplateView.as_view(template_name='featuredproducts.html'), name='featuredproducts'),
    path('ecommercesearch/', EcommerceSearchResultsView.as_view(), name='ecommercesearch_results'),
    path('i2/', TemplateView.as_view(template_name='i2.html'), name='i2'),

    # might try to switch to using slug filter format like the below comment rather than primary key filter format
    # path('product/<slug>/', views.ProductView.as_view(), name='product'),
    re_path(r'^thanks/$', views.thanks),
    # re_path(r'^create/$', views.create_company),
    path('review_detail/<slug>/', views.FeedbackView.as_view(), name='review_detail'),
    path('reviews/', views.review, name='review'),
    #path('create_review/<int:orderitem_id>/', views.SubmitFeedbackView.as_view(), name='create_review'),
    path('create_review/<int:item_id>/', views.submit_feedback, name='create_review'),
    #might cause issues due to the implementation of an integer rather than the foreignkey

    path('order_history/<str:username>/', views.OrderHistory.as_view(), name='order_history'),
    #path('create_review/', views.submit_feedback, name='create_review'),
    #path('create_review/<int:item_id>/', views.submit_feedback, name='create_review'),
    #possibly consider making wireframes to see where the create feedback form based on bought products url would look like
    path('feedbackfinish/', TemplateView.as_view(template_name='feedbackfinish.html'), name='feedbackfinish'),
    path('feedbackfinish/<slug:slug>/', views.FeedbackView.as_view(), name='feedbackfinish'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),

    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),

    # path("password_reset", views.password_reset_request, name="password_reset"),

    # new

    # path('contact/', contactView, name='contact'),

    # path('success/', successView, name='success'),

    # Change Password
    # Forget Password
    # Change Password
    # path('change-password/', auth_views.PasswordChangeView.as_view(
    #            template_name='registration/change-password.html',
    #            success_url = '/'
    #        ),
    #        name='change_password'
    #    ),

    # path('password-reset/',
    #         auth_views.PasswordResetView.as_view(
    #             template_name='templates/password-reset/password_reset.html',
    #             subject_template_name='templates/password-reset/password_reset_subject.txt',
    #             email_template_name='registration/password-reset/password_reset_email.html',
    #             success_url='/login/'
    #         ),
    #         name='password_reset'),
    #    path('password-reset/done/',
    #         auth_views.PasswordResetDoneView.as_view(
    #             template_name='registration/password-reset/password_reset_done.html'
    #         ),
    #         name='password_reset_done'),
    #    path('password-reset-confirm/<uidb64>/<token>/',
    #         auth_views.PasswordResetConfirmView.as_view(
    #             template_name='registration/password-reset/password_reset_confirm.html'
    #         ),
    #         name='password_reset_confirm'),
    #    path('password-reset-complete/',
    #         auth_views.PasswordResetCompleteView.as_view(
    #             template_name='registration/password-reset/password_reset_complete.html'
    #         ),
    #         name='password_reset_complete'),

    #    path('password_reset_form/',
    #         auth_views.PasswordResetCompleteView.as_view(
    #             template_name='registration/password_reset_form.html'
    #         ),
    #         name='password_reset_form'),

    path('contact/', views.ContactViewe.as_view(), name='contact'),
    # path('success/', successView, name='success'),
    path('success/', views.ContactSuccessView.as_view(), name='success'),
    path('contactbase/', views.TemplateView.as_view(template_name='contactbase.html'), name='contactbase'),
    path('email/', TemplateView.as_view(template_name='email.html'), name='email'),
    path('businessemail/', views.BusinessMailingView.as_view(), name='businessemail'),
    path('businessmailingsuccess', views.BusinessEmailSuccessView.as_view(), name='businessmailingsuccess'),
    # path('<slug:slug>/', views.BlogComment.as_view(), name='post_detail'),
    # path('blogpost-like/<int:pk>/', views.BlogPostLike, name='blogpost_like'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('home/<str:room>/', views.RoomView.as_view(), name='room'),
    path('home/checkview', views.checkview, name='checkview'),
    path('home/send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    # path('supportchat/', views.Support, name='supportchat'),
    path('supportchat/room', views.supportroom, name='supportroom'),
    # path('supportchat/<str:room>/', views.room, name='room'),
    path('user.username/<str:room>/', views.room, name='room'),
    path('supportchat/checkview', views.supportcheckview, name='supportcheckview'),
    path('supportchat/send', views.supportsend, name='supportsend'),
    path('supportgetMessages/<str:room>/', views.supportgetMessages, name='supportgetMessages'),
    path('supportchat/<str:supportroom>/', views.supportroom, name='supportroom'),
    # change url <str:room> to use user username for added security
    path('product/<slug>/', views.ProductView.as_view(), name='product'),
    path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity-item/<slug>/', reduce_quantity_item, name='reduce-quantity-item'),
    path('ebase/', EBaseView.as_view(), name='ebase'),
    path("backgroundimagechange/", BackgroundView.as_view(), name="backgroundimagechange"),
    path("ebackgroundimagechange/", EBackgroundView.as_view(), name="ebackgroundimagechange"),
    path("showcasebackgroundimagechange/", ShowcaseBackgroundView.as_view(), name="showcasebackgroundimagechange"),
    path("chatbackgroundimagechange/", ChatBackgroundView.as_view(), name="chatbackgroundimagechange"),
    path("billetbackgroundimagechange/", BilletBackgroundView.as_view(), name="billetbackgroundimagechange"),
    path("blogbackgroundimagechange/", BlogBackgroundView.as_view(), name="blogbackgroundimagechange"),
    # path("imagechange/", PostBackgroundView.as_view(), name="postbackgroundimagechange"),
    path("rulebackgroundimagechange/", RuleBackgroundView.as_view(), name="rulebackgroundimagechange"),
    path("aboutbackgroundimagechange/", AboutBackgroundView.as_view(), name="aboutbackgroundimagechange"),
    path("faqbackgroundimagechange/", FaqBackgroundView.as_view(), name="faqbackgroundimagechange"),
    path("eventbackgroundimagechange/", EventBackgroundView.as_view(), name="eventbackgroundimagechange"),
    path("newsbackgroundimagechange/", NewsBackgroundView.as_view(), name="newsbackgroundimagechange"),
    # path("webhook/", web_hook, name="webhook"),
    # path('order-summary/', TemplateView.as_view(template_name='order-summary.html'), name = 'order-summary'),
    # path('checkout/', TemplateView.as_view(template_name='checkout.html'), name = 'checkout'),
    path('navbase/', TemplateView.as_view(template_name='navbase.html'), name='navbase'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    # path('edit_profile/', UserRegisterView.as_view(), name='edit_profile'),
    # path("user", views.userpage, name = "userpage"),
    path('theories/', TemplateView.as_view(template_name='theories.html'), name='theories'),
    path('donatebase/', DonateBaseView.as_view(), name='donatebase'),
    #path('donate/', views.donate, name='donate'),
    path('donate/', views.DonateView.as_view(), name='donate'),
    path('mydonationhistory/', views.DonateHistoryView.as_view(), name='donationhistory'),
    path('charge/', views.charge, name='charge'),
    path('patreoned/<str:args>/', views.PatreonedView.as_view(), name='patreoned'),
    # (r'^accounts/update/(?P<pk>[\-\w]+)/$', views.edit_user, name='account_update'),
    path('support/', views.SupportBackgroundView.as_view(), name="support"),
    path('accounts/change-password/', views.change_password, name="accounts/change-password"),
    # path('accounts/change-password/', views.ChangePasswordView.as_view(), name="accounts/change-password"),
    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name="register"),
    # register = regform
    path("convert/", views.ConvertBackgroundView.as_view(), name='convert'),
    path("reasons-to-convert/", views.ReasonsBackgroundView.as_view(), name='reasons_to_convert'),
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='commons/password-reset/password_reset.html',
                                              subject_template_name='commons/password-reset/password_reset_subject.txt',
                                              email_template_name='commons/password-reset/password_reset_email.html',
                                              success_url='/login/'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='commons/password-reset/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='commons/password-reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='commons/password-reset/password_reset_complete.html'),
         name='password_reset_complete')
]

# remove these
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)