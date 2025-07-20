import pprint
from urllib import request
from venv import logger
import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin

from decimal import Decimal

import pytz
from celery import shared_task
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError

import django
import self
from django.contrib.messages import get_messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.views.generic import ListView
import stripe
from social_core.backends.stripe import StripeOAuth2
from django.utils.text import slugify
from urllib.parse import quote, urlparse
from django.db import close_old_connections
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
import math
from django.contrib.auth.models import AnonymousUser
from paypalrestsdk import Payment as PayPalPayment
from django.test import RequestFactory

from . import models
from .models import UpdateProfile, EmailField, Answer, FeedbackBackgroundImage, TradeItem, TradeOffer, Shuffler, \
    PrizePool, CurrencyMarket, CurrencyOrder, SellerApplication, Meme, CurrencyFullOrder, Currency, Wager, GameHub, \
    InventoryObject, Inventory, Trade, FriendRequest, Friend, RespondingTradeOffer, TradeShippingLabel, \
    Game, UploadACard, Withdraw, ExchangePrize, CommerceExchange, SecretRoom, Transaction, Outcome, GeneralMessage, \
    SpinnerChoiceRenders, DefaultAvatar, Achievements, QuickItem, SpinPreference, Battle, \
    BattleParticipant, Monstrosity, MonstrositySprite, Product, Level, BattleGame, Notification, InventoryTradeOffer, \
    UserNotification, TopHits, Card, Clickable, GameChoice, Robot, MyPreferences, UserClickable, GiftCodeRedemption, \
    GiftCode, IndividualChestStatistics, FavoriteChests, Season, Tier, ChangeLog, FavoriteCurrency
from .models import Idea
from .models import VoteQuery
from .models import StaffApplication
from .models import Contact
from .models import BusinessMailingContact
from .models import PartnerApplication
from .models import PunishmentAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import City, VoteQuery, UpdateProfile, Idea, PartnerApplication
from .models import ItemFilter
from .models import Support
from .models import CheckoutAddress
from .models import Item
from .models import FaviconBase
from .models import BackgroundImage
from .models import EBackgroundImage
from .models import ShowcaseBackgroundImage
from .models import ChatBackgroundImage
from .models import SupportChatBackgroundImage
from .models import BilletBackgroundImage
from .models import PatreonBackgroundImage
from .models import BusinessMessageBackgroundImage
from .models import Patreon
from .models import StoreViewType
from .models import BlogBackgroundImage
from .models import PostBackgroundImage
from .models import PosteBackgroundImage
from .models import VoteBackgroundImage
from .models import RuleBackgroundImage
from .models import AboutBackgroundImage
from .models import FaqBackgroundImage
from .models import StaffBackgroundImage
from .models import InformationBackgroundImage
from .models import TagBackgroundImage
from .models import UserBackgroundImage
from .models import StaffRanksBackgroundImage
from .models import StaffApplyBackgroundImage
from .models import MegaBackgroundImage
from .models import EventBackgroundImage
from .models import NewsBackgroundImage
from .models import DonorBackgroundImage
from .models import ContributorBackgroundImage
from .models import ContentBackgroundImage
from .models import PartnerBackgroundImage
from .models import ShareBackgroundImage
from .models import WhyBackgroundImage
from .models import ProductBackgroundImage
from .models import SettingsModel
from .models import ImageCarousel
from .models import PostLikes
from .models import ConvertBackgroundImage
from .models import ReasonsBackgroundImage
from .models import SettingsBackgroundImage
from .models import PunishAppsBackgroundImage
from .models import BanAppealBackgroundImage
from .models import SupportBackgroundImage
from .models import OrderBackgroundImage
from .models import CheckoutBackgroundImage
from .models import SignupBackgroundImage
from .models import PerksBackgroundImage
from .models import ChangePasswordBackgroundImage
from .models import IssueBackgroundImage
from .models import BackgroundImageBase
from .models import TextBase
from .models import LogoBase
from .models import FrequentlyAskedQuestions
from .models import MemberHomeBackgroundImage
from .models import NavBar
from .models import NavBarHeader
from .models import FeaturedNavigationBar
from .models import DonateIcon
from .models import Donate
from .models import Titled
from .models import AdvertisementBase
from .models import ImageBase
from .models import SocialMedia
from .models import AdminRoles
from .models import AdminTasks
from .models import AdminPages
from .models import Ascension
from .models import (Item, OrderItem, Order, Address, Payment, Coupon, Refund,
                     UserProfile)

from .forms import CouponForm, RefundForm, PaymentForm, CurrencyViewTypeForm

from .forms import VoteQueryForm, EmailForm, AnswerForm, ItemForm, TradeItemForm, TradeProposalForm, \
    SellerApplicationForm, \
    MemeForm, CurrencyCheckoutForm, CurrencyPaymentForm, CurrencyPaypalPaymentForm, HitStandForm, WagerForm, \
    DirectedTradeOfferForm, FriendRequestForm, RespondingTradeOfferForm, ShippingForm, EndowmentForm, UploadCardsForm, \
    RoomSettings, WithdrawForm, ExchangePrizesForm, AddTradeForm, InventoryGameForm, PlayerInventoryGameForm, \
    CardUploading, MoveToTradeForm, \
    SpinPreferenceForm, BattleCreationForm, BattleJoinForm, AddMonstrosityForm, AscensionCreateForm, InventoryTradeForm, \
    InventoryTradeOfferResponseForm, BetForm, MyPreferencesForm, ProfileViewTypeForm
from .forms import PostForm
from .forms import Postit
from .forms import StaffJoin
from .forms import Server_Partner
from .forms import SignUpForm
from .forms import News_Feed
from .forms import PunishAppeale
from .forms import ReportIssues
from .forms import BanAppeale
from .forms import Staffprofile
from .forms import Eventform
from .forms import ProfileDetail
from .forms import SupportForm
from .forms import SettingsForm
from .forms import BackgroundImagery
from .forms import EBackgroundImagery
from .forms import ShowcaseBackgroundImagery
from .forms import ChatBackgroundImagery
from .forms import BilletBackgroundImagery
from .forms import BlogBackgroundImagery
from .forms import PostBackgroundImagery
from .forms import RuleBackgroundImagery
from .forms import AboutBackgroundImagery
from .forms import FaqBackgroundImagery
from .forms import StaffBackgroundImagery
from .forms import InformationBackgroundImagery
from .forms import TagBackgroundImagery
from .forms import UserBackgroundImagery
from .forms import StaffRanksBackgroundImagery
from .forms import MegaBackgroundImagery
from .forms import EventBackgroundImagery
from .forms import NewsBackgroundImagery
from .forms import PaypalPaymentForm
from .forms import BaseCopyrightTextField
from .forms import ContactForme
from .forms import SignUpForm
from .forms import StoreViewTypeForm
from .forms import GiftCodeForm

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.db.models import Q, Sum
from django.views import generic
from django.views.generic import TemplateView, ListView

from django.urls import reverse_lazy, is_valid_path
from django.views.generic import UpdateView
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Blog
from .models import BlogHeader
from .models import BlogFilter
from django.views.generic.edit import FormMixin

import pdb
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseNotFound, \
    HttpResponseBadRequest, Http404
from .forms import ContactForm
from .forms import BusinessContactForm
from .forms import BusinessMailingForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404

from .models import Room, Message
from .models import SupportChat, SupportMessage
from .models import SupportLine
from .models import SupportInterface
from django.http import JsonResponse
import os

from django.contrib.auth.decorators import login_required

from guest_user.mixins import RegularUserRequiredMixin

from guest_user.decorators import allow_guest_user

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from datetime import datetime, timedelta
from django.utils import timezone
from .forms import CheckoutForm

from django.views.decorators.csrf import csrf_exempt

from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.decorators.http import require_POST
from django.db.models import Prefetch

stripe.api_key = settings.STRIPE_SECRET_KEY

class SignupView(FormMixin, ListView):
    model = SignupBackgroundImage
    template_name = "cv-form.html"
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup'] = SignupBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        print('signup')
        if request.method == 'POST':
            print('post')
            form = SignUpForm(request.POST)
            if form.is_valid():
                print('is_valid')
                user = form.save()
                user.refresh_from_db()

                user.save()
                raw_password = form.cleaned_data.get('password')

                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                subject = "Welcome to IntelleX!"
                message = 'Hello {user.username}, thank you for becoming a member of the IntelleX Community!'
                email_from = settings.EMAIL_HOST_USER
                recipent_list = [user.email, ]
                send_mail(subject, message, email_from, recipent_list)

                return redirect('showcase:showcase')
                messages.info(request, "You have signed up successfully! Welcome!")
        else:
            form = SignUpForm()
        return render(request, 'cv-form.html', {'form': form})


class TotalView(ListView):
    model = BackgroundImageBase

    def _context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['TextFielde'] = TextBase.objects.filter(is_active=1).order_by("section")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class LogoView(ListView):
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter('page')
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

from .models import Advertising

class AdvertisementView(ListView):
    model = AdvertisementBase

    def display_advertisement(request, advertisement_id):
        advertising = Advertising.objects.get(id=advertising_id)
        context = {'advertising': advertising}
        return render(request, 'index.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Advertisement'] = AdvertisementBase.objects.filter(page=self.template_name, is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

"""    def handle_uploaded_image(i):

       imagefile  = StringIO.StringIO(i.read())
       imageImage = Image

       (width, height) = imageImage.size
       (width, height) = scale_dimensions(width, height, longest_side=240)

       resizedImage = imageImage.resize((width, height))

       imagefile = StringIO.StringIO()
       resizedImage.save(imagefile,'JPEG')"""

def set_image_position(image_id, xposition, yposition):

    image = ImageBase.objects.get(id=image_id)
    print("Current coordinates: x={image.x}, y={image.y}")

    image.x = xposition
    image.y = yposition

    image.save()

class ImageView(ListView):
    model = ImageBase

    def post(self, request, *args, **kwargs):

        image_id = request.POST.get('image_id')
        xposition = request.POST.get('xposition')
        yposition = request.POST.get('yposition')

        set_image_position(image_id, xposition, yposition)

        return HttpResponse('Image position updated.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BaseView(ListView):
    template_name = "base.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        print(f'User: {user.username}, is_authenticated: {user.is_authenticated}, is_staff: {user.is_staff}')

        if user.is_authenticated and user.is_staff:
            print('Staff is presently present')
            context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        else:

            print('User is not staff')
            context['Header'] = NavBarHeader.objects.filter(is_active=1).exclude(
                text__icontains="Admin"
            ).order_by("row")

            print('Headers:')
            for header in context['Header']:
                print(header.text)

        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class EBaseView(ListView):
    template_name = "ebase.html"
    model = NavBar

    def get_context_data(self, **kwargs):

        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logos'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BlogBaseView(ListView):
    template_name = "blogbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from .models import Preference

def detail_post_view(request, id=None):
    eachpost = get_object_or_404(Post, id=id)

    context = {'eachpost': eachpost}

    return render(request, 'showcase:likes.html', context)

@login_required
def postpreference(request, post_name, like_or_dislike):
    if request.method == "POST":
        eachpost = get_object_or_404(Blog, slug=post_name)

        if request.user in eachpost.likes.iterator():
            eachpost.likes.remove(request.user)
        if request.user in eachpost.dislikes.iterator():
            eachpost.dislikes.remove(request.user)

        if int(like_or_dislike) == 1:
            eachpost.likes.add(request.user)
        else:
            eachpost.dislikes.add(request.user)

        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'likes.html', context)

    else:
        eachpost = get_object_or_404(Blog, slug=post_name)
        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'showcase:likes.html', context)

from django.contrib.admin.views.decorators import staff_member_required
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(staff_member_required, name='dispatch')
class AdminRolesView(BaseView):
    template_name = "administrativeroles.html"
    model = AdminRoles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Roles'] = AdminRoles.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTasksView(ListView):
    template_name = "administrativetasks.html"
    model = AdminTasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Tasks'] = AdminTasks.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminPagesView(ListView):
    template_name = "administrativepages.html"
    model = AdminPages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Pages'] = AdminPages.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@method_decorator(staff_member_required, name='dispatch')
class AdministrationView(ListView):
    template_name = "administration.html"
    model = AdminPages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Pages'] = AdminPages.objects.filter(is_active=1)
        context['Tasks'] = AdminTasks.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class DonateBaseView(ListView):
    template_name = "donatebase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class MemberBaseView(ListView):
    template_name = "memberbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class usersview(ListView):
    paginate_by = 10
    template_name = 'users.html'

    def get_queryset(self):
        return Idea.objects.all()

"""
class PostList(BaseView):
    model = BlogBackgroundImage

    paginate_by = 10
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        print(124)
        context = super().get_context_data(**kwargs)
        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['TextFielde'] = TextBase.objects.filter(is_active=1)
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)

        blog_posts = Blog.objects.filter(status=1).order_by('-created_on')

        context['BlogPosts'] = blog_posts

        for blog_post in context['BlogPosts']:
            author = blog_post.author
            profile = ProfileDetails.objects.filter(user=author).first()
            if profile:
                blog_post.author_profile_picture_url = profile.avatar.url
                blog_post.author_profile_url = blog_post.get_profile_url()

                print('imgsrcimg')

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get_queryset(self):
        return Blog.objects.filter(status=1).order_by('-created_on')

"""

"""
class votingview(ListView):
    model = VoteBackgroundImage
    paginate_by = 10
    template_name = 'voting.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['VoteQuery'] = VoteQuery.objects.all()

        newprofile = VoteQuery.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get_queryset(self):
        return VoteQuery.objects.all()
"""

class partnerview(ListView):
    paginate_by = 10
    template_name = 'partners.html'

    def get_queryset(self):
        return PartnerApplication.objects.all()

class newsfeedview(ListView):
    paginate_by = 10
    template_name = 'newsfeed.html'

    def get_queryset(self):
        return NewsFeed.objects.all()

class Issueview(ListView):
    paginate_by = 10
    template_name = 'issues.html'

    def get_queryset(self):
        return ReportIssue.objects.all()

class staffview(ListView):
    paginate_by = 10
    template_name = 'staff.html'

    def get_queryset(self):
        return StaffProfile.objects.all()

class eventview(ListView):
    paginate_by = 10
    template_name = 'events.html'

    def get_queryset(self):
        return Event.objects.all()

class supportview(ListView):
    paginate_by = 10
    template_name = 'supportissues.html'

    def get_queryset(self):
        return Support.objects.all()

class MemberHomeBackgroundView(ListView):
    model = MemberHomeBackgroundImage
    template_name = "memberhome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['MemberHomeBackgroundImage'] = MemberHomeBackgroundImage.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PatreonBackgroundView(ListView):
    model = Patreon
    template_name = "patreon.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BlogComment(generic.DetailView):
    model = Blog
    paginate_by = 10
    template_name = 'blog_comment.html'

    def post(self, request, slug, *args, **kwargs):
        most_recent = Blog.objects.order_by('-created_on')[:3]

        post = get_object_or_404(Blog, slug=slug)
        category_count = post.likes

        form = CommentForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.instance.user = request.user
                form.instance.post = post
                form.save()
                return redirect(reverse("blog_comment", kwargs={
                    'id': post.pk
                }))
        context = {
            'form': form,
            'post': post,
            'most_recent': most_recent,
            'category_count': category_count,
            'form': form
        }
        return render(request, 'blog_comment.html', context)

from django.views.generic import ListView, CreateView

class FaviconBaseView(ListView):
    model = FaviconBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicons'] = FaviconBase.objects.filter('faviconpage')
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BackgroundBaseView(ListView):
    model = BackgroundImageBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BackgroundImages'] = BackgroundImageBase.objects.filter('page').order_by('position')
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class TextBaseView(ListView):
    model = TextBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(is_active=1).order_by("section")
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        return render(context)

class ImageCarouselView(BaseView):
    model = ImageCarousel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Carousel'] = ImageCarousel.objects.filter(is_active=1).order_by('position')
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.views.generic import TemplateView
from .models import BackgroundImage

class BackgroundStyleView(TemplateView):
    template_name = "style.css"
    content_type = "text/css"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        background_image = BackgroundImageBase.objects.first()

        context['Background'] = background_image
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def dynamic_css(request):
    background_objects = BackgroundImageBase.objects.filter(page='index').order_by("position")

    context = {
        'background_objects': background_objects,
    }

    return render(request, 'dynamic_css.css', context, content_type='text/css')

class CreatePostView(CreateView):
    model = BackgroundImage
    form_class = BackgroundImagery
    template_name = "backgroundimagechange.html"
    success_url = reverse_lazy("index")


class ECreatePostView(CreateView):
    model = EBackgroundImage
    form_class = EBackgroundImagery
    template_name = "ebackgroundimagechange.html"
    success_url = reverse_lazy("ehome")


class ShowcaseBackgroundView(BaseView):
    model = ShowcaseBackgroundImage
    template_name = "showcase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class ShowcaseCreatePostView(CreateView):
    model = ShowcaseBackgroundImage
    form_class = ShowcaseBackgroundImagery
    template_name = "showcasebackgroundimagechange.html"
    success_url = reverse_lazy("showcase")


def create_responding_tradeoffer(request, tradeoffer_pk):
    related_offer = TradeOffer.objects.get(pk=tradeoffer_pk)
    if request.method == 'POST':
        form = RespondingTradeOfferForm(request.POST, related_offer=related_offer)
        if form.is_valid():
            form.save()

    else:
        form = RespondingTradeOfferForm(related_offer=related_offer)
    return render(request, 'tradingcentral.html', {'form': form})


class ChatBackgroundView(BaseView):
    model = ChatBackgroundImage
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['Friends'] = Friend.objects.filter(user=self.request.user)

            current_user = self.request.user
            newprofile = UserProfile2.objects.filter(is_active=1, user=current_user)
            context['Profiles'] = newprofile

            for newprofile in context['Profiles']:
                user = newprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    newprofile.newprofile_profile_picture_url = profile.avatar.url
                    newprofile.newprofile_profile_url = newprofile.get_profile_url()

            onlineprofile = Friend.objects.filter(is_active=1, user=current_user)
            context['OnlineProfiles'] = onlineprofile

            for onlineprofile in context['OnlineProfiles']:
                friend = onlineprofile.friend
                activeprofile = ProfileDetails.objects.filter(user=friend).first()
                if activeprofile:
                    onlineprofile.author_profile_picture_url = profile.avatar.url
                    onlineprofile.friend_profile_picture_url = activeprofile.avatar.url
                    onlineprofile.author_profile_url = onlineprofile.get_profile_url()
                    onlineprofile.friend_name = onlineprofile.friend.username
                    print('activeprofile exists')

            friends = Friend.objects.filter(user=self.request.user)
            friends_data = []

            for friend in friends:
                profile = ProfileDetails.objects.filter(user=friend.friend).first()
                if profile:
                    friends_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': profile.avatar.url,
                        'profile_url': reverse('showcase:profile', args=[str(profile.pk)]),
                        'currently_active': friend.currently_active,
                        'user_profile_url': friend.get_profile_url2()
                    })

            context['friends_data'] = friends_data

            search_term = self.request.GET.get('search', '')
            if search_term:
                context = self.search_friends(context)
        else:
            context['Friends'] = []
            context['Profiles'] = []
            context['OnlineProfiles'] = []
            context['friends_data'] = []
            context['search_results'] = []

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def search_friends(self, context):
        search_term = self.request.GET.get('search', '')
        if search_term:
            item_list = Friend.objects.filter(
                Q(friend__username__icontains=search_term)
            ).prefetch_related('friend')

            search_results_data = []
            current_user = self.request.user

            for friend in item_list:
                profile = ProfileDetails.objects.filter(user=friend.friend).first()
                if profile:
                    search_results_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': profile.avatar.url if profile else None,
                        'profile_url': reverse('showcase:profile', args=[str(profile.pk)]),
                        'currently_active': friend.currently_active,
                    })
                    print('the friend does have a profile')
                else:
                    search_results_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': None,
                        'profile_url': reverse('showcase:profile', args=[str(friend.friend.pk)]),
                        'currently_active': friend.currently_active,
                    })
                    print('no profile on the friend')

            context['search_results'] = search_results_data
        else:
            context['search_results'] = []

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.views.generic import ListView


class FriendSearchResultsView(ListView):
    model = Friend
    template_name = 'friendssearchresultview.html'

    def get_queryset(self):
        search_term = self.request.GET.get('search', '')
        if search_term:
            item_list = Friend.objects.filter(
                Q(friend_username__icontains=search_term)
            )
            print('item_list contains' + str(item_list))
        else:
            item_list = Friend.objects.none()
            print('item_list is empty')
        return item_list


def friendlysearchresultview(request):
    search_term = request.GET.get('search', '')
    if search_term:
        item_list = Friend.objects.filter(
            Q(friend__username__icontains=search_term)
        )
    else:
        item_list = Friend.objects.none()
    context = {'item_list': item_list}
    return render(request, 'friendssearchresultview.html', context)


class SupportChatBackgroundView(BaseView):
    model = SupportChatBackgroundImage
    template_name = "supportchat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class PlaceWagerView(FormView):
    template_name = 'template_name.html'
    form_class = WagerForm
    success_url = reverse_lazy('showcase')

    def form_valid(self, form):
        wager = form.save(commit=False)
        wager.user_profile = self.request.user.userprofile
        wager.save()
        return super().form_valid(form)

from django.core.exceptions import ValidationError

@csrf_exempt
def update_wager(request, wager_id):
    if request.method == 'POST':
        outcome = request.POST.get('outcome')
        wager = get_object_or_404(Wager, pk=wager_id)

        valid_outcomes = ('W', 'L', 'D', 'B')
        if outcome not in valid_outcomes:
            raise ValidationError("Invalid outcome submitted")

        wager.outcome = outcome
        wager.save()

        return JsonResponse({'success': True, 'message': 'Wager updated successfully'})

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def create_spinner_choice_render_automatically(request):
    nonce = random.randint(0, 1000000)
    choice = Choice.objects.filter(Q(lower_nonce__lte=nonce) & Q(upper_nonce__gte=nonce)).first()

    if choice:
        game = choice.game
        game_hub = GameHub.objects.first()

        spinner_choice_render = SpinnerChoiceRenders.objects.create(
            user=choice.user,
            value=choice.value,
            ratio=choice.rarity,
            type=game_hub,
            image=choice.file,
            color=choice.color,
            game=game,
            choice=choice,
            nonce=nonce,
            is_active=1
        )
        return redirect('spinner_choice_render_list')
    else:
        return render(request, 'error.html', {'message': 'No choice found for the generated nonce'})


def spinner_choice_render_list(request):
    spinner_choice_renders = SpinnerChoiceRenders.objects.all()
    return render(request, 'spinner_choice_render_list.html', {'spinner_choice_renders': spinner_choice_renders})


def spinner_choice_render_list(request):
    spinner_choice_renders = SpinnerChoiceRenders.objects.filter(game=self.game)
    return render(request, 'game.html', {'spinner_choice_renders': spinner_choice_renders})


class ChestBackgroundView(BaseView):
    model = UserProfile
    template_name = "blackjack.html"

    def post(self, request, *args, **kwargs):
        form = WagerForm(request.POST, user_profile=request.user.user_profile)
        if form.is_valid():
            wager = form.save(commit=False)
            wager.user_profile = request.user.user_profile
            wager.save()

            return JsonResponse({'wager_id': wager.id})
        else:

            return self.get(request, *args, **kwargs)

    @csrf_exempt
    def update_wager(request):
        if request.method == 'POST':
            wager_id = request.POST.get('wager_id')
            outcome = request.POST.get('outcome')
            try:
                wager = Wager.objects.get(id=wager_id)
                wager.resolve(outcome)
                return JsonResponse({'status': 'success'})
            except Wager.DoesNotExist:
                return JsonResponse({'error': 'Wager not found.'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Invalid request method.'}, status=405)

        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('../accounts/login')
            return super().dispatch(request, *args, **kwargs)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
            context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
            context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")

            user = self.request.user
            user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
            context['SentProfile'] = user_profile
            user_cash = user_profile.currency_amount

            context = {
                'user_cash': user_cash,
            }

            context['Money'] = Currency.objects.filter(is_active=1).first()
            context['wager_form'] = WagerForm()
            context['tophit'] = TopHits.objects.filter(game=game, is_active=True).order_by('-mfg_date')[:8]
            newprofile = UpdateProfile.objects.filter(is_active=1)

            context['Profiles'] = newprofile

            for newprofile in context['Profiles']:
                user = newprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    newprofile.newprofile_profile_picture_url = profile.avatar.url
                    newprofile.newprofile_profile_url = newprofile.get_profile_url()

            return context

class PokeChestBackgroundView(BaseView):
    model = UserProfile
    template_name = "pokechests.html"

    def post(self, request, *args, **kwargs):
        form = WagerForm(request.POST, user_profile=request.user.user_profile)
        if form.is_valid():
            wager = form.save(commit=False)
            wager.user_profile = request.user.user_profile
            wager.save()
            return redirect('showcase:blackjack')
        else:
            return self.get(request, *args, **kwargs)

    @csrf_exempt
    def update_wager(request):
        if request.method == 'POST':
            wager_id = request.POST.get('wager_id')
            outcome = request.POST.get('outcome')
            try:
                wager = Wager.objects.get(id=wager_id)
                wager.resolve(outcome)
                return JsonResponse({'status': 'success'})
            except Wager.DoesNotExist:
                return JsonResponse({'error': 'Wager not found.'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Invalid request method.'}, status=405)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['games'] = Game.objects.filter(is_active=1)
        context['wager_form'] = WagerForm()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def find_choice(request):
    generated_nonce = random.randint(0, 1000000)

    choice = Choice.objects.filter(lower_nonce__lte=generated_nonce, upper_nonce__gte=generated_nonce).first()

    context = {
        'generated_nonce': generated_nonce,
        'choice': choice
    }

    return render(request, 'game.html', context)

class FindChoiceView(View):
    template_name = 'game.html'

    def get(self, request, *args, **kwargs):
        generated_nonce = random.randint(0, 1000000)

        choice = Choice.objects.filter(lower_nonce__lte=generated_nonce, upper_nonce__gte=generated_nonce).first()

        context = {
            'generated_nonce': generated_nonce,
            'choice': choice
        }

        return render(request, self.template_name, context)


def generate_nonce():
    return random.randint(1, 1000000)


@csrf_exempt
def create_outcome(request, slug):
    if request.method == 'POST':
        try:
            django.db.close_old_connections()

            with transaction.atomic():
                body = json.loads(request.body)
                game_id = body.get('game_id')
                button_id = body.get('button_id')
                user = request.user

                if not game_id:
                    return JsonResponse({'status': 'error', 'message': 'Game ID is required.'})

                game = Game.objects.get(id=game_id, slug=slug)
                nonce = random.randint(1, 1000000)

                game_choice_instance = GameChoice.objects.filter(
                    game=game,
                    lower_nonce__lte=nonce,
                    upper_nonce__gte=nonce
                ).first()

                if game_choice_instance:
                    choice = game_choice_instance.choice
                else:
                    choices = Choice.objects.filter(
                        game=game,
                        lower_nonce__lte=nonce,
                        upper_nonce__gte=nonce
                    )
                    if not choices.exists():
                        return JsonResponse(
                            {'status': 'error', 'message': 'No valid choice found for the given nonce.'})
                    choice = choices.order_by('?').first()

                color = game.get_color(choice)
                choice.color = color
                choice.save()

                demonstration_flag = True if button_id == "start2" else False

                outcome_data = {
                    'game': game,
                    'choice': choice,
                    'color': choice.color,
                    'nonce': nonce,
                    'value': choice.value,
                    'ratio': random.randint(1, 10),
                    'type': game.type,
                    'demonstration': demonstration_flag
                }
                if user.is_authenticated and button_id == "start":
                    outcome_data['user'] = user
                else:
                    outcome_data['user'] = None


                outcome = Outcome.objects.create(**outcome_data)

            return JsonResponse({
                'status': 'success',
                'outcome': outcome.id,
                'nonce': outcome.nonce,
                'choice_id': choice.id,
                'choice_value': choice.value,
                'choice_text': choice.choice_text,
                'choice_color': choice.color,
                'choice_file': choice.file.url if choice.file else None,
                'demonstration': outcome.demonstration
            })

        except Game.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Game not found.'})
        except Exception as e:

            django.db.close_old_connections()
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


@csrf_exempt
def battle_create_outcome(request, battle_id, game_id):
    if request.method != 'POST':
        return JsonResponse({'status':'error','message':'POST required'}, status=405)

    battle = get_object_or_404(Battle, id=battle_id)
    if battle.status != "O":
        return JsonResponse({'status':'error','message':'Cannot create outcome: battle is not open.'}, status=400)

    bg = get_object_or_404(BattleGame, battle=battle, game_id=game_id)
    if bg.outcome_created:
        return JsonResponse({'status':'error','message':'Outcome already generated for this game in this battle.'}, status=400)

    if request.method == 'POST':
        try:
            django.db.close_old_connections()
            with transaction.atomic():
                body = json.loads(request.body)
                game_id = body.get('game_id')
                button_id = body.get('button_id')
                user = request.user

                if not game_id:
                    return JsonResponse({'status': 'error', 'message': 'Game ID is required.'}, status=400)

                game = Game.objects.get(id=game_id)
                nonce = random.randint(1, 1000000)

                game_choice_instance = GameChoice.objects.filter(
                    game=game,
                    lower_nonce__lte=nonce,
                    upper_nonce__gte=nonce
                ).first()

                if game_choice_instance:
                    choice = game_choice_instance.choice
                else:
                    choices = Choice.objects.filter(
                        game=game,
                        lower_nonce__lte=nonce,
                        upper_nonce__gte=nonce
                    )
                    if not choices.exists():
                        return JsonResponse(
                            {'status': 'error', 'message': 'No valid choice found for the given nonce.'})
                    choice = choices.order_by('?').first()

                color = game.get_color(choice)
                choice.color = color
                choice.save()

                demonstration_flag = True if button_id == "start2" else False

                outcome_data = {
                    'game': game,
                    'choice': choice,
                    'color': choice.color,
                    'nonce': nonce,
                    'value': choice.value,
                    'ratio': random.randint(1, 10),
                    'type': game.type,
                    'demonstration': demonstration_flag
                }
                if user.is_authenticated:
                    outcome_data['user'] = user
                bg.outcome_created = True
                bg.save(update_fields=['outcome_created'])

                print(f"[BattleCreateOutcome] Outcome#{outcome.pk} → Game={game.slug}, User={user.username if user.is_authenticated else 'anon'}")

                outcome = Outcome.objects.create(**outcome_data)

            return JsonResponse({
                'status': 'success',
                'outcome': outcome.id,
                'nonce': outcome.nonce,
                'choice_id': choice.id,
                'choice_value': choice.value,
                'choice_text': choice.choice_text,
                'choice_color': choice.color,
                'choice_file': choice.file.url if choice.file else None,
                'demonstration': outcome.demonstration
            })

        except Game.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Game not found.'})
        except Exception as e:

            django.db.close_old_connections()
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})




def game_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if game.daily:
        cost = 0
    else:
        cost = game.discount_cost if game.discount_cost else game.cost

    context = {
        'game': game,
        'cost_threshold_80': cost * 0.8,
        'cost_threshold_100': cost,
        'cost_threshold_200': cost * 2,
        'cost_threshold_500': cost * 5,
        'cost_threshold_10000': cost * 100,
    }

    return render(request, 'game.html', context)

def game_view(request, slug):
    game = get_object_or_404(Game, slug=slug)
    context = {
        'game': game,
        'games': Game.objects.all(),
        'cost_threshold_80': game.cost * 0.8,
        'cost_threshold_100': game.cost,
        'cost_threshold_200': game.cost * 2,
        'cost_threshold_500': game.cost * 5,
        'cost_threshold_10000': game.cost * 100,
    }

    if request.method == 'POST':
        num_nonces = random.randint(500, 1000)
        nonces = [random.randint(0, 1000000) for _ in range(num_nonces)]

        matching_choices = []
        for nonce in nonces:
            choices = Choice.objects.filter(lower_nonce__lte=nonce, upper_nonce__gte=nonce, game=game)
            for choice in choices:
                matching_choices.append((nonce, choice))

        random.shuffle(matching_choices)

        choices_data = [{
            'nonce': nonce,
            'choice_text': choice.choice_text,
            'value': choice.value,
            'file_url': choice.file.url
        } for nonce, choice in matching_choices]

        return JsonResponse({
            'status': 'success',
            'choices': choices_data
        })

    nonce = random.randint(1, 1000000)
    return render(request, 'game.html', {'game': game, 'nonce': nonce})

def save_spin_preference(request):
    if request.method == "POST" and request.is_ajax():
        quick_spin = request.POST.get('quick_spin') == 'true'
        spinpreference, created = SpinPreference.objects.get_or_create(user=request.user)
        spinpreference.quick_spin = quick_spin
        spinpreference.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def display_choices(request, game_id, slug):
    game = get_object_or_404(Game, id=game_id, slug=slug)
    choices = Choice.objects.filter(game=game)

    for choice in choices:
        if choice.lower_nonce is None or choice.upper_nonce is None:
            choice.lower_nonce = random.randint(0, 1000000)
            choice.upper_nonce = random.randint(0, 1000000)
            choice.save()

    return render(request, 'game.html', {'game': game, 'choices': choices})

@login_required
def get_user_cash(request):
    profile = ProfileDetails.objects.filter(user=request.user).first()
    user_cash = profile.currency_amount if profile else 0
    return JsonResponse({'user_cash': user_cash})

import json
from django.http import JsonResponse
from json.decoder import JSONDecodeError
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from .models import InventoryObject, Transaction, ProfileDetails

@csrf_exempt
def bulk_sell_view(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request method"}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "Invalid JSON payload"}, status=400)

    items = data.get("items", [])
    if not items:
        return JsonResponse({"success": False, "error": "No items provided"}, status=400)

    sold_count = 0
    total_added = 0
    items_to_update = []
    transactions_to_create = []

    user_profile = get_object_or_404(ProfileDetails, user=request.user)
    for item in items:
        inv_pk = item.get("inventory_pk")
        if not inv_pk:
            continue

        inventory_object = get_object_or_404(InventoryObject, pk=inv_pk)
        if inventory_object.user != request.user:
            return JsonResponse({"success": False, "error": f"Permission denied for item {inv_pk}"}, status=403)

        inventory_object.user = None
        inventory_object.inventory = None
        items_to_update.append(inventory_object)

        transactions_to_create.append(
            Transaction(
                inventory_object=inventory_object,
                user=request.user,
                currency=inventory_object.currency,
                amount=inventory_object.price
            )
        )
        total_added += inventory_object.price
        sold_count += 1

    with transaction.atomic():
        Transaction.objects.bulk_create(transactions_to_create)
        for inv_obj in items_to_update:
            inv_obj.save()
        user_profile.currency_amount += total_added
        user_profile.save()

    stock_count = InventoryObject.objects.filter(is_active=1, user=request.user).count()
    stock_count2 = InventoryObject.objects.filter(is_active=1, user=request.user).count()
    return JsonResponse({
        "success": True,
        "sold_count": sold_count,
        "stock_count": stock_count,
        "stock_count2": stock_count2,
        "currency_amount": user_profile.currency_amount
    })

@csrf_exempt
def sell_game_inventory_object(request, pk):
    print('sell direct started in the outside')
    if request.method != "POST":
        return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

    inventory_object = get_object_or_404(InventoryObject, pk=pk)

    if inventory_object.user != request.user:
        return JsonResponse({'success': False, 'message': 'Unauthorized'}, status=403)

    try:
        data = json.loads(request.body)
        items = data.get("items", [])

        if not items:
            return JsonResponse({'success': False, 'message': 'No items provided'}, status=400)

        total_sale_value = sum(float(item["price"]) for item in items if "price" in item)

        django.db.close_old_connections()
        with transaction.atomic():
            for item in items:
                item_pk = item.get("inventory_pk")
                item_inventory = get_object_or_404(InventoryObject, pk=item_pk)

                item_inventory.user = None
                item_inventory.inventory = None
                item_inventory.save()

                Transaction.objects.create(
                    inventory_object=item_inventory,
                    user=request.user,
                    currency=item.get("currencySymbol", ""),
                    amount=float(item.get("price", 0))
                )

            user_profile = get_object_or_404(ProfileDetails, user=request.user)
            user_profile.currency_amount += total_sale_value
            user_profile.save()
            print('sold an item directly using outside sell_game_inventory_object method')

        stock_count = InventoryObject.objects.filter(is_active=1, user=request.user).count()
        stock_count2 = InventoryObject.objects.filter(is_active=1, user=request.user).count()

        return JsonResponse({
            'success': True,
            'stock_count': stock_count,
            'stock_count2': stock_count2,
            'currency_amount': user_profile.currency_amount,
            'message': f"Sold {len(items)} items for {total_sale_value} currency."
        })

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON data'}, status=400)

@csrf_exempt
def create_top_hit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        required_fields = ['choice_id', 'game_id']
        button_id = data.get('button_id')

        print(f"Top Hits Button ID: {button_id}")
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return JsonResponse({'error': f'Missing fields: {", ".join(missing_fields)}'}, status=400)

        try:
            choice = Choice.objects.get(id=data['choice_id'])

            try:
                game = Game.objects.get(id=data['game_id'])
            except Game.DoesNotExist:
                return JsonResponse({'error': 'Invalid game_id. Game does not exist.'}, status=400)

            try:
                top_hit = TopHits.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    game=game,
                    choice=choice,
                    color=choice.color,
                    file=choice.file if hasattr(choice, 'file') else None,
                )
                print(
                    f"Creating TopHits with data: user={request.user}, game={game}, choice={choice}, color={choice.color}, file={choice.file}"
                )
            except Exception as e:
                print(f"Error while creating TopHits: {str(e)}")
                raise

            return JsonResponse({'message': 'Top Hit created successfully', 'id': top_hit.id})
        except Choice.DoesNotExist:
            return JsonResponse({'error': 'Invalid choice_id. Choice does not exist.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

class TopHitsListView(ListView):
    model = TopHits
    template_name = 'top_hits_list.html'
    context_object_name = 'top_hits'

    def get_queryset(self):
        return TopHits.objects.filter(is_active=True).order_by('-mfg_date')

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string('partials/top_hits_partial.html', context, request=self.request)
            return JsonResponse({'html': html})
        return super().render_to_response(context, **response_kwargs)

class MyPreferencesView(FormMixin, LoginRequiredMixin, ListView):
    model = MyPreferences
    form_class = MyPreferencesForm
    template_name = 'mypreferences.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        user = self.request.user

        if not user.is_authenticated:
            if is_ajax:
                return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=401)
            else:
                messages.error(request, 'You must be logged in to update preferences.')
                return redirect('login')

        preference_instance, created = MyPreferences.objects.get_or_create(user=user)
        form = MyPreferencesForm(request.POST, instance=preference_instance, user=user)

        if form.is_valid():
            try:
                preference = form.save(commit=False)
                preference.user = user
                preference.save()

                if is_ajax:
                    return JsonResponse({'status': 'success', 'spintype': preference.spintype})
                else:
                    messages.success(request, 'Spin preferences updated successfully!')
                    return redirect('showcase:mypreferences')
            except IntegrityError:
                if is_ajax:
                    return JsonResponse({'status': 'error', 'errors': {'general': 'Database error occurred'}}, status=400)
                else:
                    messages.error(request, 'Database error occurred')
                    return self.form_invalid(form)
        else:
            if is_ajax:
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
            else:
                return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            try:
                preferences = MyPreferences.objects.get(user=request.user)
                data = {
                    'spintype': preferences.spintype,
                    'is_active': preferences.is_active,
                    'spintype_display': preferences.get_spintype_display()
                }
                return JsonResponse({'status': 'success', 'preferences': data})
            except MyPreferences.DoesNotExist:
                return JsonResponse({'status': 'success', 'preferences': {'spintype': 'C', 'is_active': 1}})
        else:
            return super().get(request, *args, **kwargs)

class PreferencesDoneView(ListView):
    model = MyPreferences
    template_name = 'mypreferencesdone.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        user = self.request.user
        if user.is_authenticated:
            try:
                context['SentProfile'] = ProfileDetails.objects.get(user=self.request.user)
            except ObjectDoesNotExist:
                context['SentProfile'] = None
        else:
            context['SentProfile'] = None
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1).first()
        context['GameRoom'] = Game.objects.filter(is_active=1, daily=True).first()
        context['form'] = EmailForm()

        newprofile = Game.objects.filter(is_active=1, daily=True)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class TierView(BaseView):
    model = Tier
    template_name = "tiers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
        context['Tiers'] = Tier.objects.filter(is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class ClickableView(BaseView):
    model = Clickable
    template_name = "clickable.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
        context['Tiers'] = Tier.objects.filter(is_active=1)
        context['clickables'] = Clickable.objects.filter(is_active=1)


        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class DailyRoomView(BaseView):
    model = GameHub
    template_name = "dailyroom.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "dailyroom.html", {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        user = self.request.user
        if user.is_authenticated:
            try:
                context['SentProfile'] = ProfileDetails.objects.get(user=self.request.user)
            except ObjectDoesNotExist:
                context['SentProfile'] = None
        else:
            context['SentProfile'] = None
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1).first()
        context['GameRoom'] = Game.objects.filter(is_active=1, daily=True).first()
        context['form'] = EmailForm()

        newprofile = Game.objects.filter(is_active=1, daily=True)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


def get_next_5pm_pst():

    pst = pytz.timezone('US/Pacific')
    now = datetime.now(pst)

    next_5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)
    if now >= next_5pm:
        next_5pm += timedelta(days=1)

    return next_5pm


class DailyChestView(BaseView):
    template_name = "game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['slug'] = slug

        game = get_object_or_404(Game, slug=slug)

        context['game'] = game

        user = self.request.user
        if user.is_authenticated:
            try:
                context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
            except UserProfile.DoesNotExist:
                context['SentProfile'] = None
        else:
            context['SentProfile'] = None

        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['wager_form'] = WagerForm()

        context['tophit'] = TopHits.objects.filter(game=game, is_active=True).order_by('-mfg_date')[:8]
        game = get_object_or_404(Game, slug=slug)
        context['games'] = game
        choices = Choice.objects.filter(game=game)
        spinner_choice_renders = SpinnerChoiceRenders.objects.filter(game=game)
        context['spinner_choice_renders'] = spinner_choice_renders
        if game.daily:
            cost = 0
        else:
            cost = game.discount_cost if game.discount_cost else game.cost
        context.update({
            'cost_threshold_80': cost * 0.8,
            'cost_threshold_100': cost,
            'cost_threshold_200': cost * 2,
            'cost_threshold_500': cost * 5,
            'cost_threshold_10000': cost * 100,
        })

        newprofile = UpdateProfile.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        user_profile = None
        if game.user:

            user_profile, created = UserProfile.objects.get_or_create(user=game.user)

        context['SentProfile'] = user_profile
        if game.user:
            user_cash = user_profile.currency_amount

            context = {
                'user_cash': user_cash,
            }

        context['Money'] = Currency.objects.filter(is_active=1).first()

        spinpreference = None

        if user.is_authenticated:
            try:
                spinpreference = SpinPreference.objects.get(user=user)
            except SpinPreference.DoesNotExist:
                spinpreference = SpinPreference(user=user, quick_spin=False)
                spinpreference.save()

            context['quick_spin'] = spinpreference.quick_spin
        else:
            context['quick_spin'] = False

        context['spinpreference'] = spinpreference

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if spinpreference:
            spinform = SpinPreferenceForm(instance=spinpreference)
        else:
            spinform = SpinPreferenceForm()
        context['spin_preference_form'] = spinform

        if user.is_authenticated:
            if spinpreference.quick_spin:
                random_amount = random.randint(500, 1000)
            else:
                random_amount = random.randint(150, 300)
        else:
            random_amount = random.randint(150, 300)

        context['random_amount'] = random_amount
        context['range_random_amount'] = range(random_amount)
        print(str('the random amount is ') + str(random_amount))

        random_nonces = [random.randint(0, 1000000) for _ in range(random_amount)]
        context['random_nonces'] = random_nonces

        choices_with_nonce = []
        for nonce in random_nonces:
            for choice in choices:
                if choice.lower_nonce <= nonce <= choice.upper_nonce:
                    choices_with_nonce.append({
                        'choice': choice,
                        'nonce': nonce,
                        'lower_nonce': choice.lower_nonce,
                        'upper_nonce': choice.upper_nonce,
                        'file_url': choice.file.url if choice.file else '',
                        'currency': {
                            'symbol': choice.currency.name if choice.currency else '💎',
                            'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                        }
                    })
                    break

        context['choices_with_nonce'] = choices_with_nonce

        game_id = self.kwargs.get('slug')

        game = get_object_or_404(Game, slug=slug)

        choices = Choice.objects.filter(game=game)

        context['game'] = game
        context['choices'] = choices

        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        print(context['Background'])

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['next_5pm'] = get_next_5pm_pst()
        context['is_daily'] = game.daily
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def game_detail(request, slug):
        game = get_object_or_404(Game, slug=slug)
        choices = game.choices.all()
        return render(request, 'game_detail.html', {'game': game, 'choices': choices})

    def display_choices(request, game_id, slug):
        game = get_object_or_404(Game, id=game_id, slug=slug)
        choices = Choice.objects.filter(game=game)

        for choice in choices:
            if choice.lower_nonce is None or choice.upper_nonce is None:
                choice.lower_nonce = random.randint(0, 1000000)
                choice.upper_nonce = random.randint(0, 1000000)
                choice.save()

        return render(request, 'game.html', {'game': game, 'choices': choices})

    def take_spinner_slot(user, game, choice):
        SpinnerChoiceRenders.take_up_slot(user=user, game=game, choice=choice, value=100, ratio=2,
                                          type=game.type,
                                          image=choice.image.url, color=choice.color)

    def save_spin_preference(request):
        if request.method == "POST" and request.is_ajax():
            quick_spin = request.POST.get('quick_spin') == 'true'
            spinpreference, created = SpinPreference.objects.get_or_create(user=request.user)
            spinpreference.quick_spin = quick_spin
            spinpreference.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)

    def wager(self, request, *args, **kwargs):
        form = WagerForm(request.POST, user_profile=request.user.user_profile)
        if form.is_valid():
            wager = form.save(commit=False)
            wager.user_profile = request.user.user_profile
            wager.save()
            return redirect('showcase:blackjack')
        else:
            return self.get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            quick_spin = request.POST.get('quick_spin') == 'true'
            spinpreference, created = SpinPreference.objects.get_or_create(user=request.user)
            spinpreference.quick_spin = quick_spin
            spinpreference.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)



@csrf_exempt
def spin_game(request):
    if request.method != "POST":
        return JsonResponse(
            {"success": False, "error": "Invalid request method."},
            status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"success": False, "error": "Invalid JSON."},
            status=400
        )

    game_id = data.get("game_id")
    spin_multiplier = int(data.get("spin_multiplier", 1))
    game = get_object_or_404(Game, id=game_id)

    profile = ProfileDetails.objects.filter(user=request.user).first()
    if not profile:
        return JsonResponse(
            {"success": False, "error": "User profile not found."},
            status=404
        )

    effective_cost = game.get_effective_cost()
    total_cost = effective_cost * spin_multiplier

    if game.daily:
        # daily spin: no charge, no contribution
        message = "Daily spin—no charge."
    else:
        # charge the user
        if profile.currency_amount < total_cost:
            return JsonResponse(
                {"success": False, "error": "Insufficient currency."},
                status=400
            )
        profile.currency_amount -= total_cost
        profile.save()

        lotto = get_object_or_404(Lottery, name="Daily Lotto")
        increment = int(total_cost / 250)
        lotto.prize += increment
        lotto.save()

        message = f"Spin charged {total_cost} {profile.currency.name}"

    lotto = get_object_or_404(Lottery, name="Daily Lotto")
    return JsonResponse({
        "success": True,
        "message": message,
        "updated_currency_amount": profile.currency_amount,
        "currency_name": profile.currency.name,
        "daily": game.daily,
        "lottery_prize": lotto.prize,
    })



def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    choices = Choice.objects.filter(game=game)

    context = {
        'game': game,
        'choices': choices,
    }

    return render(request, 'game.html', context)

from django.http import JsonResponse

@csrf_exempt
def create_card_instance(request):
    print("View called")

    if request.method == 'POST':
        data = json.loads(request.body)
        print(f"Received data: {data}")

        selected_nonce = data.get('nonce')
        if selected_nonce:
            print(f"Selected nonce: {selected_nonce}")

        return JsonResponse({'success': True, 'message': 'Debugging response'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})


class OpenBattleListView(ListView):
    model = Battle
    template_name = "battle.html"
    context_object_name = "open_battles"

    def get_queryset(self):
        return Battle.objects.filter(status='O').order_by('-time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        active_games = Game.objects.filter(is_active=1)
        if active_games.exists():
            context['game'] = random.choice(active_games)
        else:
            context['game'] = None

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['game_values'] = self.request.session.pop('game_values', '')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        battle_id = request.POST.get('battle_id')
        try:
            battle = Battle.objects.get(id=battle_id)
        except Battle.DoesNotExist:
            messages.error(request, "Battle not found.")
            return redirect('showcase:battle')

        if battle.participants.count() >= int(battle.slots.split('v')[-1]):
            messages.error(request, 'This battle is full. You cannot join.')
            battle.status = '0'
            return redirect('showcase:battle_detail', battle_id=battle.id)

        if battle.status != 'O':
            messages.error(request, 'This battle is not currently open for participants.')
            return redirect('showcase:battle_detail', battle_id=battle.id)

        if request.user in battle.participants.all():
            messages.error(request, 'You are already a participant in this battle.')
            return redirect('showcase:battle_detail', battle_id=battle.id)

        form = BattleJoinForm(request.POST, user=request.user, battle=battle)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully joined the battle!')
            return redirect('showcase:battle_detail', battle_id=battle.id)
        else:
            messages.error(request, 'There was an error joining the battle. Please try again.')
            return redirect('showcase:battle_detail', battle_id=battle.id)
        return self.get(request, *args, **kwargs)


class SingleBattleListView(DetailView):
    model = Battle
    template_name = "battle_detail.html"
    context_object_name = "battle"

    def get_object(self):
        battle_id = self.kwargs.get('battle_id')
        return get_object_or_404(Battle, id=battle_id)

    def dispatch(self, request, *args, **kwargs):
        battle = self.get_object()
        redirect_url = None
        if battle.is_full():
            if battle.status == 'O':
                battle.status = 'R'
                battle.save(update_fields=['status'])
            print('battle is full, starting battle')
            redirect_url = reverse('showcase:actualbattle', kwargs={'battle_id': battle.id})
            redirect_url += '?auto_spin=true'
            print('the url is: ' + redirect_url)
            return redirect(redirect_url)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        battle = self.get_object()

        battle_games = battle.battle_games.all().order_by('order')
        ordered_games = [bg.game for bg in battle_games]
        context['battle_game_data'] = battle_games
        context['bet_form'] = BetForm(battle=battle)
        context['ordered_games'] = ordered_games
        context['default_game'] = ordered_games[0] if ordered_games else None
        related_games = Game.objects.filter(game_battles__battle=battle).distinct()
        context['related_games'] = related_games
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
        context["battle_absolute_url"] = self.request.build_absolute_uri(battle.get_absolute_url())
        context['auto_spin'] = self.request.GET.get('auto_spin') == 'true'

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        user = self.request.user
        context['is_participant'] = battle.participants.filter(user=user).exists()

        total_capacity = battle.get_total_capacity()

        participants = list(battle.participants.all())

        grid = [participants[i] if i < len(participants) else None for i in range(total_capacity)]

        user_ids = [p.user.id for p in grid if p and p.user]
        profiles = ProfileDetails.objects.filter(user_id__in=user_ids)
        profile_map = {p.user_id: p for p in profiles}

        # Attach profile to each slot (if it exists)
        for slot in grid:
            if slot and slot.user:
                slot.profile = profile_map.get(slot.user.id)

        context['grid'] = grid
        context['is_full'] = len(participants) >= total_capacity
        context['SentProfile'] = UserProfile.objects.filter(user=user).first() if user.is_authenticated else None
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['wager_form'] = WagerForm()

        cost = sum(game.discount_cost or game.cost for game in related_games)
        context.update({
            'cost_threshold_80': cost * 0.8,
            'cost_threshold_100': cost,
            'cost_threshold_200': cost * 2,
            'cost_threshold_500': cost * 5,
            'cost_threshold_10000': cost * 100,
        })

        spinpreference = None
        if user.is_authenticated:
            spinpreference, _ = SpinPreference.objects.get_or_create(
                user=user, defaults={'quick_spin': False}
            )
            random_amount = random.randint(500, 1000) if spinpreference.quick_spin else random.randint(150, 300)
        else:
            random_amount = random.randint(150, 300)
        context['random_amount'] = random_amount
        context['range_random_amount'] = range(random_amount)
        context['random_nonces'] = [random.randint(0, 1000000) for _ in range(random_amount)]

        choices = Choice.objects.filter(game__in=related_games)
        choices_with_nonce = [
            {
                'choice': choice,
                'nonce': nonce,
                'lower_nonce': choice.lower_nonce,
                'upper_nonce': choice.upper_nonce,
                'file_url': choice.file.url if choice.file else None,
                'currency': {
                    'symbol': choice.currency.name if choice.currency else '💎',
                    'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                }
            }
            for nonce in context['random_nonces']
            for choice in choices
            if choice.lower_nonce <= nonce <= choice.upper_nonce
        ]
        context['choices_with_nonce'] = choices_with_nonce

        user_profiles = ProfileDetails.objects.filter(user=user) if user.is_authenticated else None
        context['Profiles'] = user_profiles or [
            {'newprofile_profile_picture_url': 'static/css/images/a.jpg', 'newprofile_profile_url': None}
        ]
        context['spin_preference_form'] = SpinPreferenceForm(
            instance=spinpreference) if spinpreference else SpinPreferenceForm()

        game_id = self.kwargs.get('game_id')
        if game_id:
            game = get_object_or_404(Game, id=game_id)
            context['game'] = game

        if user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                profile = ProfileDetails.objects.filter(user=userprofile.user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if hasattr(self, 'object') and self.object is not None and self.request.user.is_authenticated:
            battle = self.object
            context['is_participant'] = battle.participants.filter(user=user).exists()
            context['is_creator'] = (battle.creator == user)
            context['is_full'] = battle.is_full() if hasattr(battle, 'is_full') else False
        else:
            context['is_participant'] = False
            context['is_creator'] = False
            context['is_full'] = False

        if 'bet_form' not in context:
            context['bet_form'] = BetForm(initial={'battle': battle.pk})

        if 'join_form' not in context:
            context['join_form'] = BattleJoinForm(user=user, battle=battle)

        sound_url = self.request.session.pop('robot_sound_url', None)
        if sound_url:
            context['robot_sound_url'] = sound_url

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        battle = self.object
        if 'join_battle_submit' in request.POST:
            if battle.status != 'O':
                messages.error(request, 'This battle is not currently open for participants.')
                return redirect('showcase:battle_detail', battle_id=battle.id)
            if request.user in battle.participants.all():
                messages.error(request, 'You are already a participant in this battle.')
                return redirect('showcase:battle_detail', battle_id=battle.id)
            redirect_url = None
            if battle.is_full():
                battle.status = 'R'
                battle.save()
                messages.error(request, 'This battle is now full and has started.')
                print('reached a full battle')
                redirect_url = reverse('showcase:actualbattle', kwargs={'battle_id': battle.id})
                redirect_url += '?auto_spin=true'
                print('the url is: ' + redirect_url)
                return redirect(redirect_url)
            join_form = BattleJoinForm(request.POST, user=request.user, battle=battle)
            if join_form.is_valid():
                join_form.save()
                if battle.is_full():
                    battle.status = 'R'
                    battle.save()
                    messages.success(request, 'You have successfully joined the battle, and it is now running!')
                else:
                    messages.success(request, 'You have successfully joined the battle!')
                return redirect('showcase:battle_detail', battle_id=battle.id)
            else:
                messages.error(request, 'There was an error joining the battle. Please try again.')
                context = self.get_context_data(join_form=join_form)
                return self.render_to_response(context)

        elif 'bet_form_submit' in request.POST:
            is_creator = (request.user == battle.creator)
            is_participant = battle.participants.filter(user=request.user).exists()

            if not battle.bets_allowed:
                messages.error(request, 'Bets are not allowed in this battle.')
                return redirect('showcase:battle_detail', battle_id=battle.id)

            bet_form = BetForm(request.POST, is_creator==True or is_participant==True, battle=battle)
            if bet_form.is_valid():
                bet_form.instance.battle = battle
                bet_form.instance.user   = request.user
                bet_form.save()
                messages.success(request, 'Bet placed successfully.')
                return redirect('showcase:battle_detail', battle_id=battle.id)

            context = self.get_context_data(bet_form=bet_form)
            return self.render_to_response(context)

        messages.error(request, 'Invalid form submission.')
        return redirect('showcase:battle_detail', battle_id=battle.id)


from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.core.paginator import Paginator

from .models import (
    Battle, Game, GameChoice, Choice,
    ProfileDetails, SpinPreference, UserProfile,
    BackgroundImageBase, BaseCopyrightTextField,
    Titled, NavBarHeader, NavBar, LogoBase,
    InventoryObject
)

from .forms import (
    MyPreferencesForm, WagerForm,
    SpinPreferenceForm
)


class ActualBattleView(DetailView):
    model = Battle
    template_name = "actualbattle.html"
    context_object_name = "battle"

    def get_object(self):
        return get_object_or_404(
            Battle.objects.prefetch_related(
                Prefetch(
                    'chests',
                    queryset=Game.objects.prefetch_related(
                        Prefetch(
                            'gamechoice_set',
                            queryset=GameChoice.objects.select_related('choice'),
                            to_attr='gamechoice_links'
                        )
                    ),
                    to_attr='games_with_choices'
                )
            ),
            id=self.kwargs['battle_id']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        battle = self.object
        all_participants = BattleParticipant.objects.filter(battle=battle)

        humans = [bp.user for bp in all_participants if not bp.is_bot and bp.user]
        bots = [bp.robot for bp in all_participants if bp.is_bot and bp.robot]

        context['players'] = [('human', h) for h in humans] + [('robot', b) for b in bots]
        context['battle_games'] = [
            {
                'id': bg.game.id,
                'slug': bg.game.slug,
                'quantity': bg.quantity,
                'name': bg.game.name,
                'image_url': bg.game.image.url if bg.game.image else '',
                'battle_id': self.object.id
            }
            for bg in self.object.battle_games.all()
        ]
        context['battle_games_json'] = mark_safe(
            json.dumps(context['battle_games'])
        )

        # 1) Grab all prefetched games
        games = getattr(battle, 'games_with_choices', [])
        if not games:
            raise Http404("No games found for this battle.")

        # 2) Prepare detailed context for ALL games
        context['all_games_data'] = []
        for game in games:
            # Choices
            inline_choices = game.choice_fk_set.all()
            m2m_choices = game.choices.all()
            combined = {c.pk: c for c in list(inline_choices) + list(m2m_choices)}

            through_qs = GameChoice.objects.filter(game=game).select_related('choice')
            through_data = {}
            for gc in through_qs:
                c = gc.choice
                through_data[c.pk] = {
                    'lower_nonce': gc.lower_nonce or c.lower_nonce,
                    'upper_nonce': gc.upper_nonce or c.upper_nonce,
                    'value':       gc.value or c.value,
                    'rarity':      gc.rarity or c.rarity,
                    'file_url':    c.file.url if c.file else '',
                    'category':    c.category or '',
                    'currency': {
                        'symbol':   c.currency.name if c.currency else '💎',
                        'file_url': c.currency.file.url if c.currency and c.currency.file else None
                    }
                }

            all_choices = []
            for pk, choice in combined.items():
                info = through_data.get(pk, {
                    'lower_nonce': choice.lower_nonce,
                    'upper_nonce': choice.upper_nonce,
                    'value':       choice.value,
                    'rarity':      choice.rarity,
                    'file_url':    choice.file.url if choice.file else '',
                    'category':    choice.category or '',
                    'currency': {
                        'symbol':   choice.currency.name if choice.currency else '💎',
                        'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                    }
                })
                all_choices.append({
                    'choice':      choice,
                    'choice_text': choice.choice_text,
                    **info,
                    'image_width':  getattr(choice, 'image_width', None),
                    'image_length': getattr(choice, 'image_length', None),
                    'get_color_display': choice.get_color_display(),
                    'get_tier_display':  choice.get_tier_display(),
                })

            # Randomization logic
            rand_amt = random.randint(500, 1000) if context.get('quick_spin') else random.randint(150, 300)
            random_nonces = [random.randint(0, 1_000_000) for _ in range(rand_amt)]

            choices_with_nonce = []
            for nonce in random_nonces:
                for cd in all_choices:
                    if cd['lower_nonce'] <= nonce <= cd['upper_nonce']:
                        choices_with_nonce.append({
                            'choice':     cd['choice'],
                            'nonce':      nonce,
                            'lower_nonce':cd['lower_nonce'],
                            'upper_nonce':cd['upper_nonce'],
                            'rarity':     cd['rarity'],
                            'file_url':   cd['file_url'],
                            'currency':   cd['currency']
                        })
                        break

            context['all_games_data'].append({
                'game': game,
                'choices_with_nonce': choices_with_nonce,
                'random_nonces': random_nonces,
            })

        # 3) For backwards compatibility: pick a “primary” game for single‐game logic
        primary_game = games[0]
        context['game'] = primary_game
        context['auto_spin'] = self.request.GET.get('auto_spin') == 'true'

        # 4) User & profile info
        user = self.request.user
        if user.is_authenticated:
            profile = ProfileDetails.objects.filter(user=user).first()
            context['user_cash'] = profile.currency_amount if profile else 0
            context['total_cost'] = primary_game.get_effective_cost()
            # MyPreferences form
            pref_inst = getattr(user, 'mypreferences', None)
            context['preferenceform'] = (
                MyPreferencesForm(instance=pref_inst, user=user)
                if pref_inst else
                MyPreferencesForm(user=user)
            )
            # SpinPreference
            spin_pref = SpinPreference.objects.get_or_create(user=user, defaults={'quick_spin': False})[0]
            context['quick_spin'] = spin_pref.quick_spin
            context['spinpreference'] = spin_pref
            context['spin_preference_form'] = SpinPreferenceForm(instance=spin_pref)
        else:
            context.update({
                'user_cash': None,
                'total_cost': None,
                'quick_spin': False,
                'spinpreference': None,
                'spin_preference_form': SpinPreferenceForm(),
                'preferenceform': MyPreferencesForm()
            })

        # 5) Random nonces for your spinner logic
        rand_amt = random.randint(500, 1000) if context.get('quick_spin') else random.randint(150, 300)
        context['random_amount'] = rand_amt
        context['range_random_amount'] = range(rand_amt)
        context['random_nonces'] = [random.randint(0, 1_000_000) for _ in range(rand_amt)]

        # 6) Choice‐generation logic (unchanged)
        inline_choices = primary_game.choice_fk_set.all()
        m2m_choices = primary_game.choices.all()
        combined = {c.pk: c for c in list(inline_choices) + list(m2m_choices)}

        through_qs = GameChoice.objects.filter(game=primary_game).select_related('choice')
        through_data = {}
        for gc in through_qs:
            c = gc.choice
            through_data[c.pk] = {
                'lower_nonce': gc.lower_nonce or c.lower_nonce,
                'upper_nonce': gc.upper_nonce or c.upper_nonce,
                'value':       gc.value or c.value,
                'rarity':      gc.rarity or c.rarity,
                'file_url':    c.file.url if c.file else '',
                'category':    c.category or '',
                'currency': {
                    'symbol':   c.currency.name if c.currency else '💎',
                    'file_url': c.currency.file.url if c.currency and c.currency.file else None
                }
            }

        all_choices = []
        for pk, choice in combined.items():
            info = through_data.get(pk, {
                **through_data.get(pk, {}),
                'lower_nonce': choice.lower_nonce,
                'upper_nonce': choice.upper_nonce,
                'value':       choice.value,
                'rarity':      choice.rarity,
                'file_url':    choice.file.url if choice.file else '',
                'category':    choice.category or '',
                'currency': {
                    'symbol':   choice.currency.name if choice.currency else '💎',
                    'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                }
            })
            all_choices.append({
                'choice':      choice,
                'choice_text': choice.choice_text,
                **info,
                'image_width':  getattr(choice, 'image_width', None),
                'image_length': getattr(choice, 'image_length', None),
                'get_color_display': choice.get_color_display(),
                'get_tier_display':  choice.get_tier_display(),
            })

        context['choices'] = all_choices

        # 7) Matching nonces → choice objects
        with_nonce = []
        for nonce in context['random_nonces']:
            for cd in all_choices:
                if cd['lower_nonce'] <= nonce <= cd['upper_nonce']:
                    with_nonce.append({
                        'choice':     cd['choice'],
                        'nonce':      nonce,
                        'lower_nonce':cd['lower_nonce'],
                        'upper_nonce':cd['upper_nonce'],
                        'rarity':     cd['rarity'],
                        'file_url':   cd['file_url'],
                        'currency':   cd['currency']
                    })
                    break
        context['choices_with_nonce'] = with_nonce

        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
        if user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=user).order_by("created_at")
        print(battle.participants.all())

        newprofile = ProfileDetails.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for profile in context['Profiles']:
            user = profile.user
            profile.newprofile_profile_picture_url = profile.avatar.url if profile.avatar else None
            profile.newprofile_profile_url = profile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()
        return context


from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta


def active_users_count(request):
    now = timezone.now()
    window = now - timedelta(seconds=10)
    sessions = Session.objects.filter(expire_date__gt=now)
    count = 0

    for session in sessions:
        data = session.get_decoded()
        ts = data.get('last_activity')
        if not ts:
            continue
        last_seen = timezone.datetime.fromisoformat(ts)
        if last_seen > window:
            count += 1

    return JsonResponse({'count': count})


class BattleCreationView(CreateView):
    login_url = reverse_lazy('login')
    model = Battle
    form_class = BattleCreationForm
    template_name = "battlecreator.html"

    def get_success_url(self):
        return reverse_lazy('showcase:battle_detail', kwargs={'battle_id': self.object.id})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['chests'].queryset = Game.objects.filter(daily=False)
        return form

    def form_valid(self, form):
        form.instance.creator = self.request.user
        response = super().form_valid(form)
        battle = form.instance

        battle.game_values = form.cleaned_data.get('game_values', '')
        battle.save(update_fields=['game_values'])

        battle.price = battle.total_game_values
        battle.save(update_fields=['price'])

        BattleParticipant.objects.get_or_create(user=self.request.user, battle=battle)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        games = Game.objects.filter(daily=False)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        context['games_json'] = json.dumps([
            {
                'id': game.id,
                'name': game.name,
                'cost': game.get_effective_cost()
            }
            for game in games
        ])

        if hasattr(self, 'object') and self.object is not None:
            battle = self.object
            context['is_participant'] = battle.participants.filter(user=self.request.user).exists()
            context['is_creator'] = (battle.creator == self.request.user)
            context['is_full'] = battle.is_full() if hasattr(battle, 'is_full') else False
        else:
            context['is_participant'] = False
            context['is_creator'] = False
            context['is_full'] = False

        return context


def create_outcomes_for_battle(battle):
    """
    For every (Game × User) in this battle, make one Outcome.
    """
    # 1) all non-bot, authenticated participants
    participants = BattleParticipant.objects.filter(
        battle=battle,
        is_bot=False,
        user__isnull=False
    ).select_related('user')

    # 2) all the games in the battle
    games = battle.chests.all().prefetch_related('choice_fk_set', 'choices')

    for game in games:
        # pick a default choice for this game (you can customize this)
        default_choice = (
            game.choice_fk_set.first()    or
            game.choices.first()
        )
        for bp in participants:
            outcome = Outcome.objects.create(
                game=game,
                user=bp.user,
                type=game.type,
                choice=default_choice
            )
            print(
                f"[BattleStart] Outcome #{outcome.pk} → "
                f"Game={game.slug}, User={bp.user.username}"
            )


def load_game_wrapper(request, game_id, battle_id):
    game = get_object_or_404(Game, id=game_id)
    battle = get_object_or_404(Battle, id=battle_id)
    battle_game = get_object_or_404(BattleGame, game=game, battle=battle)
    quantity = battle_game.quantity

    all_participants = BattleParticipant.objects.filter(battle=battle)
    humans = [bp.user for bp in all_participants if not bp.is_bot and bp.user]
    bots = [bp.robot for bp in all_participants if bp.is_bot and bp.robot]
    players = [('human', h) for h in humans] + [('robot', b) for b in bots]

    # Auth-related profile context
    user = request.user
    if user.is_authenticated:
        profile = ProfileDetails.objects.filter(user=user).first()
        user_cash = profile.currency_amount if profile else 0
        spin_pref = SpinPreference.objects.get_or_create(user=user, defaults={'quick_spin': False})[0]
        quick_spin = spin_pref.quick_spin
    else:
        user_cash = None
        quick_spin = False

    # Choices
    inline_choices = game.choice_fk_set.all()
    m2m_choices = game.choices.all()
    combined = {c.pk: c for c in list(inline_choices) + list(m2m_choices)}

    through_qs = GameChoice.objects.filter(game=game).select_related('choice')
    through_data = {}
    for gc in through_qs:
        c = gc.choice
        through_data[c.pk] = {
            'lower_nonce': gc.lower_nonce or c.lower_nonce,
            'upper_nonce': gc.upper_nonce or c.upper_nonce,
            'value':       gc.value or c.value,
            'rarity':      gc.rarity or c.rarity,
            'file_url':    c.file.url if c.file else '',
            'category':    c.category or '',
            'currency': {
                'symbol':   c.currency.name if c.currency else '💎',
                'file_url': c.currency.file.url if c.currency and c.currency.file else None
            }
        }

    all_choices = []
    for pk, choice in combined.items():
        info = through_data.get(pk, {
            'lower_nonce': choice.lower_nonce,
            'upper_nonce': choice.upper_nonce,
            'value':       choice.value,
            'rarity':      choice.rarity,
            'file_url':    choice.file.url if choice.file else '',
            'category':    choice.category or '',
            'currency': {
                'symbol':   choice.currency.name if choice.currency else '💎',
                'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
            }
        })
        all_choices.append({
            'choice':      choice,
            'choice_text': choice.choice_text,
            **info,
            'image_width':  getattr(choice, 'image_width', None),
            'image_length': getattr(choice, 'image_length', None),
            'get_color_display': choice.get_color_display(),
            'get_tier_display':  choice.get_tier_display(),
        })

    # Randomization logic
    rand_amt = random.randint(500, 1000) if quick_spin else random.randint(150, 300)
    random_nonces = [random.randint(0, 1_000_000) for _ in range(rand_amt)]

    choices_with_nonce = []
    for nonce in random_nonces:
        for cd in all_choices:
            if cd['lower_nonce'] <= nonce <= cd['upper_nonce']:
                choices_with_nonce.append({
                    'choice':     cd['choice'],
                    'nonce':      nonce,
                    'lower_nonce':cd['lower_nonce'],
                    'upper_nonce':cd['upper_nonce'],
                    'rarity':     cd['rarity'],
                    'file_url':   cd['file_url'],
                    'currency':   cd['currency']
                })
                break

    context = {
        'game': game,
        'battle': battle,
        'players': players,
        'quantity': quantity,
        'choices_with_nonce': choices_with_nonce,
        'user_cash': user_cash,
        'quick_spin': quick_spin,
        'random_nonces': random_nonces,
    }

    return render(request, "partials/game_wrapper.html", context)


def join_battle(request):
    battle_id = request.POST.get('battle_id')
    battle = Battle.objects.get(id=battle_id)

    if battle.status != 'O':
        messages.error(request, 'This battle is not currently open for participants.')
        return redirect('home')

    if BattleParticipant.objects.filter(user=request.user, battle=battle).exists():
        messages.error(request, 'You are already a participant in this battle.')
        return redirect('battle_detail', battle_id=battle.id)

    if battle.participants.count() >= int(battle.slots.split('v')[-1]):
        messages.error(request, 'This battle is full. You cannot join.')
        return redirect('battle_detail', battle_id=battle.id)

    if request.method == 'POST':
        form = BattleJoinForm(request.POST, user=request.user, battle=battle)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully joined the battle!')
            return redirect('battle_detail', battle_id=battle.id)
        else:
            messages.error(request, 'There was an error joining the battle. Please try again.')
    else:
        form = BattleJoinForm(user=request.user, battle=battle)

    return render(request, 'showcase/join_battle.html', {'form': form, 'battle': battle})


def add_robot(request, battle_id):
    battle = get_object_or_404(Battle, id=battle_id)

    if request.user != battle.creator:
        messages.error(request, "Only the battle creator can add robots.")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'error': "Only the battle creator can add robots."}, status=403)
        return redirect('showcase:battle_detail', battle_id=battle.id)

    used_robot_ids = battle.participants.filter(robot__isnull=False).values_list('robot_id', flat=True)
    available_robots = Robot.objects.filter(is_active=1).exclude(id__in=used_robot_ids)
    if not available_robots.exists():
        messages.error(request, "No available robots to add.")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'error': "No available robots to add."}, status=400)
        return redirect('showcase:battle_detail', battle_id=battle.id)

    selected_robot = random.choice(available_robots)
    BattleParticipant.objects.create(
        user=None,
        is_bot=True,
        robot=selected_robot,
        battle=battle
    )

    # Build the sound URL (if any)
    sound_url = None
    if selected_robot.sound:
        sound_url = selected_robot.sound.url

    # Check if the battle is now full
    is_now_full = battle.is_full()
    redirect_url = None
    if is_now_full:
        print('battle is now full, starting')
        rf = RequestFactory()
        for game in battle.chests.all():
            payload = json.dumps({
                'game_id': game.id,
                'button_id': 'start2'  # or whatever flag you need
            })
            fake_req = rf.post(
                path='/',  # path doesn’t actually matter
                data=payload,
                content_type='application/json'
            )
            fake_req.user = request.user

            battle_create_outcome(fake_req, battle.id, game.id)
        print('started battle trigger')
        redirect_url = reverse('showcase:actualbattle', kwargs={'battle_id': battle.id})
        redirect_url += '?auto_spin=true'
        print('the url is: ' + redirect_url)
        return redirect(redirect_url)

    messages.success(request, f"Robot '{selected_robot.name}' added successfully!")

    # If this is AJAX, return JSON; otherwise do a normal redirect
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'sound_url': sound_url,
            'robot_id': selected_robot.id,
            'robot_name': selected_robot.name,
            'robot_image_url': selected_robot.image.url if selected_robot.image else None,
            'is_full': is_now_full,
            'redirect_url': redirect_url,
        })
    return redirect('showcase:battle_detail', battle_id=battle.id)


def battle_detail_view(request, battle_id):
    battle = get_object_or_404(Battle, id=battle_id)

    slot_number = int(slugify(battle.slots).split('v')[-1]) if 'v' in battle.slots else int(battle.slots)

    return render(request,'battle_detail.html',{'game': game, 'battle': battle, 'slots': slot_number})


def update_profile_level(profile):
    if profile.rubies_spent is not None:
        highest_level = Level.objects.filter(
            experience__lte=profile.rubies_spent
        ).order_by('-level').first()
        if highest_level:
            print(f"Highest level found: {highest_level}")
            profile.level = highest_level
            profile.save()
        else:
            print(f"No level matches rubies_spent: {profile.rubies_spent}")

@receiver(post_save, sender=Ascension)
def reset_currency_spent_if_high_level(sender, instance, created, **kwargs):
    if created:
        profile = ProfileDetails.objects.filter(user=instance.user).first()
        if profile and profile.level.level >= 100:
            profile.rubies_spent = 0

            if hasattr(profile.rubies_spent, 'amount'):
                profile.rubies_spent.amount += int(profile.rubies_spent.amount / 10)

            print(f'User {profile.user} ascended at level {profile.level.level}')

            profile.level = Level.objects.order_by('id').first()
            profile.save()

class AscendView(BaseView):
    model = Ascension
    template_name = "ascend.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@login_required
def create_ascension(request):
    profile = ProfileDetails.objects.filter(user=request.user).first()
    if not profile:
        messages.error(request, "Profile not found.")
        return redirect('showcase:index')

    if request.method == "POST":

        ascension = Ascension(
            final_level=profile.level,
            reward=1,
            user=request.user,
            profile=profile,
        )
        ascension.save()
        messages.success(request, "Ascension created successfully!")
        return redirect('showcase:index')

    form = AscensionCreateForm()
    return render(request, 'ascend.html', {'form': form})


class LoricorfView(BaseView):
    model = Currency
    template_name = "loricorfs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['currency'] = Currency.objects.get(is_active=1, name="Loricorf")

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:
            # Fake an anonymous userprofile for consistency
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
            context['NewsProfiles'] = [userprofile]
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        currency = context.get('currency')
        context['weight_thresholds'] = currency.weight_thresholds

        return context



class EarningAchievement(BaseView):
    model = Achievements
    template_name = "achievements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def earningachievement(self, achievement_id):
        achievement = get_object_or_404(Achievements, id=achievement_id)
        user_profile = get_object_or_404(ProfileDetails, user=self.request.user)

        if not achievement.earned:

            achievement.earned = True
            achievement.user = self.request.user
            achievement.save()

            user_profile.add_currency(achievement.value)

            if not user_profile.currency:
                first_currency = Currency.objects.first()
                if first_currency:
                    user_profile.currency = first_currency

            user_profile.save()

            return JsonResponse({"status": "success", "message": "Achievement earned successfully!"})
        else:
            return JsonResponse({"status": "failure", "message": "Achievement has already been earned."})

def earningachievement(self, achievement_id):
    achievement = get_object_or_404(Achievements, id=achievement_id)

    if not achievement.earned:
        achievement.earned = True
        achievement.user = self.request.user
        achievement.save()
        return JsonResponse({"status": "success", "message": "Achievement earned successfully!"})
    else:
        return JsonResponse({"status": "failure", "message": "Achievement has already been earned."})

class ChatCreatePostView(CreateView):
    model = ChatBackgroundImage
    form_class = ChatBackgroundImagery
    template_name = "chatbackgroundimagechange.html"
    success_url = reverse_lazy("home")

class WhyBackgroundView(BaseView):
    model = WhyBackgroundImage
    template_name = "whydonate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class GameHubView(BaseView):
    model = GameHub
    template_name = "gamehub.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "gamehub.html", {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        user = self.request.user
        if user.is_authenticated:
            try:
                context['SentProfile'] = ProfileDetails.objects.get(user=self.request.user)
            except ObjectDoesNotExist:
                context['SentProfile'] = None
        else:
            context['SentProfile'] = None
        """if the user has no profile, allow it anyway"""
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1)
        context['form'] = EmailForm()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class GameRoomView(BaseView):
    model = GameHub
    template_name = "gameroom.html"
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        # fetch the GameHub so you can re‑use it in the template
        gameroom = get_object_or_404(GameHub, slug=kwargs['slug'])
        context['gameroom'] = gameroom

        try:
            instance = StoreViewType.objects.get(user=request.user, is_active=1)
        except StoreViewType.DoesNotExist:
            instance = None

        context['store_view_form'] = StoreViewTypeForm(instance=instance, request=request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "gameroom.html", {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        user = self.request.user
        if user.is_authenticated:
            try:
                context['SentProfile'] = ProfileDetails.objects.get(user=self.request.user)
            except ObjectDoesNotExist:
                context['SentProfile'] = None
        else:
            context['SentProfile'] = None
        current_user = self.request.user
        if isinstance(current_user, AnonymousUser):
            context['store_view'] = 'stream'
            context['streamfilter_string'] = 'stream filter set by anonymous user'
            print('store view does not exist, setting to stream for anonymous user')
        else:
            try:
                user_store_view_type = StoreViewType.objects.get(user=current_user, is_active=1)
                context['store_view'] = user_store_view_type.type
                context['store_view_type_str'] = str(user_store_view_type)
                context['streamfilter_string'] = f'stream filter set by {self.request.user.username}'
                print('store view exists, game')
                print(str(user_store_view_type))
            except StoreViewType.DoesNotExist:
                context['store_view'] = 'stream'
                context['store_view_type_str'] = 'stream'
                context['streamfilter_string'] = f'stream filter set by {self.request.user.username}'
                print('store view does not exist, setting to stream for signed-in user')

        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1).first()
        context['GameRoom'] = Game.objects.filter(is_active=1, daily=False).first()
        context['form'] = EmailForm()
        context['tophit'] = TopHits.objects.filter(is_active=True).order_by('-mfg_date')[:3]
        context['FeaturedGame'] = Game.objects.filter(is_active=1, filter='F')
        context['NewGame'] = Game.objects.filter(is_active=1, filter='N')
        context['PopularGame'] = Game.objects.filter(is_active=1, filter='P')
        if self.request.user.is_authenticated:

            try:
                instance = StoreViewType.objects.get(user=self.request.user, is_active=1)
            except StoreViewType.DoesNotExist:
                instance = None
            context['store_view_form'] = StoreViewTypeForm(instance=instance)
            user_favs = FavoriteChests.objects.filter(user=self.request.user, is_active=1)
            fav_dict = {fav.chest.id: fav for fav in user_favs}

            context["FavoriteGames"] = Game.objects.filter(id__in=user_favs.values_list("chest_id", flat=True))
        else:
            fav_dict = {}
            context["FavoriteGames"] = []
            context['store_view_form'] = StoreViewTypeForm()
        context['fav_dict'] = fav_dict

        newprofile = Game.objects.filter(is_active=1, daily=False)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@login_required
def toggle_favorite(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    fav = FavoriteChests.objects.filter(user=request.user, chest=game).first()

    if fav:
        fav.is_active = 0 if fav.is_active == 1 else 1
        fav.save()
    else:
        fav = FavoriteChests.objects.create(user=request.user, chest=game, is_active=1)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok', 'is_active': fav.is_active})
    else:
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', '/'))
        return redirect(next_url)


class OutcomeHistoryView(BaseView):
    model = Outcome
    template_name = "outcomehistory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        user_outcomes = Outcome.objects.filter(is_active=1, user=current_user)

        outcomes_data = []
        for outcome in user_outcomes:
            game_choice_instance = GameChoice.objects.filter(
                game=outcome.game,
                choice=outcome.choice
            ).first()

            if game_choice_instance:
                game_choice_data = {
                    'lower_nonce': game_choice_instance.lower_nonce,
                    'upper_nonce': game_choice_instance.upper_nonce,
                    'value': game_choice_instance.value,
                    'rarity': game_choice_instance.rarity,
                }
            else:
                game_choice_data = {
                    'lower_nonce': outcome.choice.lower_nonce,
                    'upper_nonce': outcome.choice.upper_nonce,
                    'value': outcome.choice.value,
                    'rarity': outcome.choice.rarity,
                }

            outcomes_data.append({
                'id': outcome.id,
                'user': str(outcome.user),
                'quick_spin': outcome.quick_spin,
                'slug': outcome.slug,
                'value': outcome.value,
                'file': outcome.file.url if outcome.file else None,
                'color': outcome.color,
                'game': str(outcome.game),
                'choice': str(outcome.choice),
                'nonce': outcome.nonce,
                'date_and_time': outcome.date_and_time.isoformat(),
                'game_choice': game_choice_data,
            })

        context['UserOutcomes'] = user_outcomes
        context['UserOutcomesJSON'] = json.dumps(outcomes_data, cls=DjangoJSONEncoder)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class UserRecentOutcomesView(LoginRequiredMixin, ListView):
    model = Outcome
    template_name = 'recent_outcomes.html'
    context_object_name = 'outcomes'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1).first()
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
        context['form'] = EmailForm()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        target = (
            get_object_or_404(User, pk=user_id)
            if user_id
            else self.request.user
        )
        return (
            Outcome.objects
            .filter(user=target, is_active=1)
            .order_by('-date_and_time')
        )

    def render_to_response(self, context, **response_kwargs):
        is_ajax = self.request.headers.get('x-requested-with') == 'XMLHttpRequest'
        if is_ajax:
            page = context['page_obj']
            outcomes = page.object_list

            data = [
                {
                    'slug': o.slug,
                    'nonce': int(o.nonce),
                    'value': o.value,
                    'ratio': o.ratio,
                    'date_and_time': o.date_and_time.strftime('%Y-%m-%d %H:%M:%S'),
                }
                for o in outcomes
            ]
            return JsonResponse({
                'outcomes': data,
                'has_next': page.has_next(),
                'page': page.number,
            })
        return super().render_to_response(context, **response_kwargs)


class ClubRoomView(BaseView):
    model = GameHub
    template_name = "clubroom.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "blog.html", {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1).first()
        context['form'] = EmailForm()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@shared_task
def update_locked_status():

    now = datetime.now()
    for game in Game.objects.filter(daily=True):

        if game.cooldown and game.cooldown <= now:

            users = ProfileDetails.objects.filter(level__gte=game.unlocking_level.level)

            if users.exists():
                game.locked = False
            else:
                game.locked = True

            tomorrow_5pm = datetime.combine(now.date() + timedelta(days=1), time(17, 0))
            game.cooldown = tomorrow_5pm
            game.save()

class AchievementsView(TemplateView):
    model = Achievements
    template_name = "achievements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        total_achievements = Achievements.objects.filter(is_active=1)

        earned_achievements = Achievements.objects.filter(
            is_active=1, user=user
        ).distinct()

        context['earned_count'] = earned_achievements.count()
        context['total_count'] = total_achievements.count()

        context['total_achievements'] = total_achievements
        context['earned_achievements'] = earned_achievements

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def CheckAchievements(self, user):
        return Achievements.objects.filter(user=user, earned=True, is_active=1)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['CheckedAchievements'] = self.CheckAchievements(request.user)
        return self.render_to_response(context)

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):

        response = super().form_valid(form)
        print("Password reset email sent (if user exists).")
        return response

class BlogBackgroundView(ListView):
    model = BlogBackgroundImage
    template_name = "blog.html"

    queryset = Blog.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BlogCreatePostView(CreateView):
    model = BlogBackgroundImage
    form_class = BlogBackgroundImagery
    template_name = "blogbackgroundimagechange.html"
    success_url = reverse_lazy("blog")

class PostBackgroundView(FormMixin, LoginRequiredMixin, ListView):
    model = UpdateProfile
    template_name = "post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:showcase')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "post_edit.html", {'form': form})

class ShufflerBackgroundView(BaseView):
    model = Shuffler
    template_name = "pack_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()
        context['Shuffle'] = Shuffler.objects.filter(is_active=1).order_by("category")

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PostCreatePostView(CreateView):
    model = PostBackgroundImage
    form_class = PostBackgroundImagery
    template_name = "postbackgroundimagechange.html"
    success_url = reverse_lazy("post_edit")

class BilletBackgroundView(BaseView):
    model = BilletBackgroundImage
    template_name = "billets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['BilletBackgroundImage'] = BilletBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BilletCreatePostView(CreateView):
    model = BilletBackgroundImage
    form_class = BilletBackgroundImagery
    template_name = "billetbackgroundimagechange.html"
    success_url = reverse_lazy("billets")

class RuleBackgroundView(BaseView):
    model = RuleBackgroundImage
    template_name = "rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Rules'] = RuleBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class RuleCreatePostView(CreateView):
    model = RuleBackgroundImage
    form_class = RuleBackgroundImagery
    template_name = "rulebackgroundimagechange.html"
    success_url = reverse_lazy("rules")

class PolicyBackgroundView(BaseView):
    template_name = "policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ServersView(BaseView):
    model = RuleBackgroundImage
    template_name = "servers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class AboutCreatePostView(CreateView):
    model = AboutBackgroundImage
    form_class = AboutBackgroundImagery
    template_name = "aboutbackgroundimagechange.html"
    success_url = reverse_lazy("about")

class FaqBackgroundView(BaseView):
    model = FaqBackgroundImage
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['FaqBackgroundImage'] = FaqBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class FaqCreatePostView(CreateView):
    model = FaqBackgroundImage
    form_class = FaqBackgroundImagery
    template_name = "faqbackgroundimagechange.html"
    success_url = reverse_lazy("faq")

class StaffBackgroundView(BaseView):
    model = BackgroundImage
    template_name = "staff.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class StaffCreatePostView(CreateView):
    model = StaffBackgroundImage
    form_class = StaffBackgroundImagery
    template_name = "staffbackgroundimagechange.html"
    success_url = reverse_lazy("staff")

class StaffApplyBackgroundView(FormMixin, ListView):
    model = StaffApplyBackgroundImage
    template_name = "staffapplications.html"
    form_class = StaffJoin

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['StaffApplyBackgroundImage'] = StaffApplyBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = StaffJoin(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:staffdone')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "staffapplications.html", {'form': form})
        else:
            form = StaffJoin()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "staffapplications.html", {'form': form})

class InformationBackgroundView(BaseView):
    InformationBackgroundImage
    template_name = "information.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class InformationCreatePostView(CreateView):
    model = InformationBackgroundImage
    form_class = InformationBackgroundImagery
    template_name = "Informationbackgroundimagechange.html"
    success_url = reverse_lazy("Information")

class TagBackgroundView(BaseView):
    model = TagBackgroundImage
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class TagCreatePostView(CreateView):
    model = TagBackgroundImage
    form_class = TagBackgroundImagery
    template_name = "tagbackgroundimagechange.html"
    success_url = reverse_lazy("tag")

class UserBackgroundView(BaseView):
    model = UserBackgroundImage
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['UserBackgroundImage'] = UserBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class UserCreatePostView(CreateView):
    model = UserBackgroundImage
    form_class = UserBackgroundImagery
    template_name = "userbackgroundimagechange.html"
    success_url = reverse_lazy("users")

class StaffRanksBackgroundView(BaseView):
    model = StaffRanksBackgroundImage
    template_name = "staffranks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['StaffRanksBackgroundImage'] = StaffRanksBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class StaffRanksCreatePostView(CreateView):
    model = StaffRanksBackgroundImage
    form_class = StaffRanksBackgroundImagery
    template_name = "staffranksbackgroundimagechange.html"
    success_url = reverse_lazy("staffranks")

class MegaBackgroundView(BaseView):
    model = MegaBackgroundImage
    template_name = "megacoins.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MegaCoinsBackgroundImage'] = MegaBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class MegaCreatePostView(CreateView):
    model = MegaBackgroundImage
    form_class = MegaBackgroundImagery
    template_name = "megacoinsbackgroundimagechange.html"
    success_url = reverse_lazy("megacoins")


class EventBackgroundView(BaseView):
    model = EventBackgroundImage
    template_name = "events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['EventBackgroundImage'] = EventBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
        context['Events'] = Event.objects.all()

        newprofile = Event.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class EventCreatePostView(CreateView):
    model = EventBackgroundImage
    form_class = EventBackgroundImagery
    template_name = "eventbackgroundimagechange.html"
    success_url = reverse_lazy("event")

class NewsBackgroundView(BaseView):
    model = NewsBackgroundImage
    template_name = "newsfeed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NewsBackgroundImage'] = NewsBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['News'] = NewsFeed.objects.all()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'),
                                                  is_active=1).first()

        newprofile = NewsFeed.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class SingleNewsView(DetailView):
    model = NewsFeed
    paginate_by = 10
    template_name = "singlenews.html"

    def get_object(self):
        slug = self.kwargs.get("slug")
        if slug:
            return get_object_or_404(NewsFeed, slug=slug)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NewsBackgroundImage'] = NewsBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['News'] = NewsFeed.objects.all()
        context['Money'] = Currency.objects.filter(is_active=1)

        newprofile = NewsFeed.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class NewsCreatePostView(CreateView):
    model = NewsBackgroundImage
    form_class = NewsBackgroundImagery
    template_name = "newsbackgroundimagechange.html"
    success_url = reverse_lazy("newsfeed")

class DonorView(BaseView):
    model = DonorBackgroundImage
    template_name = "donors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)

        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            user = request.user
            print(user)
        else:

            user = None

        return super().dispatch(request, *args, user=user, **kwargs)

class ContributorBackgroundView(BaseView):
    model = ContributorBackgroundImage
    template_name = "contributors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ContentBackgroundView(BaseView):
    model = ContentBackgroundImage
    template_name = "morecontent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ContentBackgroundImage'] = ContentBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PartnerApplicationView(FormMixin, LoginRequiredMixin, ListView):
    model = PartnerApplication
    template_name = "partnerapplication.html"
    form_class = Server_Partner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        form = Server_Partner(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:partners')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "partnerapplication.html", {'form': form})

class PartnerBackgroundView(BaseView):
    model = PartnerBackgroundImage
    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Partner'] = PartnerApplication.objects.all()

        newprofile = Partner.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ConvertBackgroundView(BaseView):
    model = ConvertBackgroundImage
    template_name = "convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ReasonsBackgroundView(BaseView):
    model = ReasonsBackgroundImage
    template_name = "reasons-to-convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PerksBackgroundView(BaseView):
    model = PerksBackgroundImage
    template_name = "perks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class MonstrosityView(ListView):
    model = Monstrosity
    template_name = "mymonstrosity.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_monstrosity'] = Monstrosity.objects.filter(user=self.request.user, is_active=1).first()
        context['Monster'] = Monstrosity.objects.filter(is_active=1)
        context['MonsterSprite'] = MonstrositySprite.objects.filter(is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class AddMonstrosityView(FormMixin, LoginRequiredMixin, ListView):
    model = Monstrosity
    form_class = AddMonstrosityForm
    template_name = "addamonstrosity.html"

    def dispatch(self, request, *args, **kwargs):

        if Monstrosity.objects.filter(user=request.user).exists():
            messages.error(request, "You already have a Monstrosity and cannot create another.")
            return redirect('showcase:mymonstrosity')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_monstrosity'] = Monstrosity.objects.filter(user=self.request.user, is_active=1).first()
        context['Monster'] = Monstrosity.objects.filter(is_active=1)
        context['MonsterSprite'] = MonstrositySprite.objects.filter(is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):

        form = AddMonstrosityForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Monstrosity added.')
            return redirect('showcase:mymonstrosity')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "addamonstrosity.html", {'form': form})

from .forms import FeedMonstrosityForm

@login_required
def feedmonstrosity(request, monstrosity_id):
    monstrosity = get_object_or_404(Monstrosity, id=monstrosity_id)

    if monstrosity.user != request.user:
        messages.error(request, "You do not have permission to feed this Monstrosity.")
        return redirect('mymonstrosity')

    if request.method == 'POST':
        form = FeedMonstrosityForm(request.POST)
        if form.is_valid():

            if monstrosity.currency_amount >= monstrosity.feed_amount:

                monstrosity.currency_amount -= monstrosity.feed_amount
                monstrosity.experience += monstrosity.feed_amount
                monstrosity.save()

                messages.success(request, f"You have successfully fed {monstrosity.monstrositys_name}.")
                return redirect('showcase:mymonstrosity')
            else:
                messages.error(request, "This Monstrosity does not have enough currency to be fed.")
    else:
        form = FeedMonstrosityForm()

    return render(request, 'feed_monstrosity.html', {'form': form, 'monstrosity': monstrosity})

from django.http import HttpRequest, JsonResponse
from django.views.generic import TemplateView

class RoomView(TemplateView):
    model = Room
    template_name = 'room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        room_name = self.kwargs['room']
        roomed = get_object_or_404(Room, name=room_name)
        context['room'] = roomed

        rooms_with_logo_same_name = Room.objects.filter(name=room_name).exclude(logo='')
        context['rooms_with_logo_same_name'] = rooms_with_logo_same_name

        if self.request.user.is_authenticated and getattr(self.request.user, 'current_room', None) == room_name:

            UserNotification.objects.filter(
                user=self.request.user,
                notification__content_type=ContentType.objects.get_for_model(Room),
                notification__object_id=roomed.id,
            ).update(is_read=True)

        username = self.request.GET.get('username')
        room_details = Room.objects.get(name=roomed)
        profile_details = ProfileDetails.objects.filter(user__username=username).first()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['username'] = username
        context['room_details'] = room_details
        context['profile_details'] = profile_details

        messages = Message.objects.all().order_by('-date')

        context['Messaging'] = messages

        for messages in context['Messaging']:
            profile = ProfileDetails.objects.filter(user=messages.signed_in_user).first()
            if profile:
                messages.user_profile_picture_url = profile.avatar.url
                messages.user_profile_url = messages.get_profile_url()

        current_user = self.request.user
        newprofile = UserProfile2.objects.filter(is_active=1, user=current_user)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        onlineprofile = Friend.objects.filter(is_active=1, user=current_user).order_by('-last_messaged')
        current_highlighted_profile = Friend.objects.filter(is_active=1, user=current_user)

        context['OnlineProfiles'] = onlineprofile
        context['CurrentProfiles'] = current_highlighted_profile

        for onlineprofile in context['OnlineProfiles']:
            friend = onlineprofile.friend
            activeprofile = ProfileDetails.objects.filter(user=friend).first()
            if activeprofile:
                onlineprofile.author_profile_picture_url = profile.avatar.url
                onlineprofile.author_profile_url = onlineprofile.get_profile_url()
                onlineprofile.friend_profile_picture_url = profile.avatar.url
                onlineprofile.friend_profile_picture_url = onlineprofile.get_profile_url()
                onlineprofile.friend_name = onlineprofile.friend.username
                print('activeprofile exists')

        blog_posts = Blog.objects.filter(status=1).order_by('-created_on')

        context['BlogPosts'] = blog_posts

        for onlineprofile in context['CurrentProfiles']:
            friend = onlineprofile.friend
            activeprofile = ProfileDetails.objects.filter(user=friend).first()
            if activeprofile:
                onlineprofile.author_profile_picture_url = profile.avatar.url
                onlineprofile.friend_profile_picture_url = profile.avatar.url
                onlineprofile.author_profile_url = onlineprofile.get_profile_url()
                onlineprofile.friend_name = onlineprofile.friend.username
                print('currentfriendprofile exists')

        friends = Friend.objects.filter(user=self.request.user).order_by('last_messaged')

        friends_data = []

        for friend in friends:

            profile = ProfileDetails.objects.filter(user=friend.friend).first()
            friend_pk = self.request.GET.get('friend_pk')

            if profile:

                friends_data.append({
                    'username': friend.friend.username,
                    'profile_picture_url': profile.avatar.url,
                    'profile_url': reverse('showcase:profile', args=[str(profile.pk)]),
                    'currently_active': friend.currently_active,
                    'user_profile_url': friend.get_profile_url2()
                })
            if friend_pk and int(friend_pk) == friend.pk:
                print('setting currently active')
                friend.currently_active = True
                friend.save()
                return redirect('showcase:room', room=room)

        context['friends_data'] = friends_data

        search_term = self.request.GET.get('search', '')
        if search_term:
            context = self.search_friends(context)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def search_friends(self, context):
        search_term = self.request.GET.get('search', '')
        if search_term:
            item_list = Friend.objects.filter(
                Q(friend__username__icontains=search_term)
            ).prefetch_related('friend')

            search_results_data = []
            current_user = self.request.user

            for friend in item_list:

                profile = ProfileDetails.objects.filter(user=friend.friend).first()

                if profile:
                    search_results_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': profile.avatar.url if profile else None,

                        'profile_url': reverse('showcase:profile', args=[str(profile.pk)]),
                    })
                    print('the friend does have a profile')
                else:

                    search_results_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': None,
                        'profile_url': reverse('showcase:profile', args=[str(friend.friend.pk)]),
                    })
                    print('no profile on the friend')

            context['search_results'] = search_results_data
        else:
            context['search_results'] = []

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def room(request, room):
    username = request.GET.get('username')

    profile_details = ProfileDetails.objects.filter(user__username=username).first()
    Logo = LogoBase.objects.filter(page='room.html', is_active=1)
    Header = NavBarHeader.objects.filter(is_active=1).order_by("row")
    DropDown = NavBar.objects.filter(is_active=1).order_by('position')

    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'signed_in_user': signed_in_user,
        'room_details': room_details,
        'profile_details': profile_details,
        'Logo': Logo,
        'Header': Header,
        'Dropdown': DropDown,
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    request.session['room_name'] = room
    request.session['username'] = username

    if Room.objects.filter(name=room).exists():
        return redirect('/home/' + room + '/?username=' + username)
    else:

        new_room = Room.objects.create(name=room)
        signed_in_user = request.user
        print('the room owner is ' + str(signed_in_user))
        new_room.signed_in_user = signed_in_user if signed_in_user.is_authenticated else None

        if hasattr(new_room, 'file_field') and new_room.file_field:
            new_room.file_field = os.path.basename(new_room.file_field.name)

        new_room.save()

        return redirect('showcase:create_room')

@csrf_exempt
def send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')
        page_name = request.POST.get('page_name')
        uploaded_file = request.FILES.get('file')

        if page_name == 'index.html':
            room_id = 'General'

        logger.debug(f"message: {message}, username: {username}, room_id: {room_id}, page_name: {page_name}")
        print(f"message: {message}, username: {username}, room_id: {room_id}, page_name: {page_name}")
        print('This is a personable-sent message')

        try:
            room = Room.objects.get(name=room_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Room does not exist.'})

        if not message:
            return JsonResponse({'status': 'error', 'message': 'Message is required.'})

        try:
            if request.user.is_authenticated:
                new_message = Message.objects.create(
                    value=message,
                    user=username,
                    room=room.name,
                    signed_in_user=request.user,
                    file=uploaded_file
                )
            else:
                new_message = Message.objects.create(
                    value=message,
                    user=username,
                    room=room.name,
                    file=uploaded_file
                )
            new_message.save()

            file_url = new_message.file.url if new_message.file and hasattr(new_message.file, 'url') else None

            response_data = {
                'status': 'success',
                'message': 'Message sent successfully',
                'message_data': {
                    'value': new_message.value,
                    'user': new_message.user,
                    'room': new_message.room,
                    'file_url': file_url,
                }
            }

            return JsonResponse(response_data)
        except Exception as e:
            print(f"Error saving message: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def mark_notifications_as_read(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            room_id = data.get("room_id")
            if not room_id:
                return JsonResponse({"status": "error", "message": "Room ID not provided."}, status=400)

            room_content_type = ContentType.objects.get_for_model(Room)

            user_notifications = UserNotification.objects.filter(
                user=request.user,
                notification__content_type=room_content_type,
                notification__object_id=room_id,
                is_read=False
            )

            print(f"Room ContentType: {room_content_type}")
            print(f"Room ID: {room_id}")
            if not user_notifications.exists():
                print(f"No UserNotifications found for user={request.user}, room_id={room_id}.")
            else:
                for notification in user_notifications:
                    print(f"Found UserNotification: {notification}")

            notifications_updated = user_notifications.update(is_read=True)
            print(f"Notifications updated: {notifications_updated}")

            return JsonResponse(
                {"status": "success", "message": f"{notifications_updated} notifications marked as read."})
        except Exception as e:
            print(f"Error in mark_notifications_as_read: {e}")
            return JsonResponse({"status": "error", "message": "An error occurred."}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse
from django.views import View
from django.core import serializers

"""
def get_profile_url(message):
   return f"http://127.0.0.1:8000/profile/{message.signed_in_user_id}/"
"""
from django.http import JsonResponse

class NewRoomSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "create_room.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_name = self.request.session.get('room_name')
        username = self.request.session.get('username')

        room = Room.objects.filter(name=room_name).first()
        form = RoomSettings(instance=room)

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['form'] = form
        context['room'] = room

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        room_name = self.request.session.get('room_name')
        username = self.request.session.get('username')
        room = Room.objects.filter(name=room_name).first()
        form = RoomSettings(request.POST, request.FILES, instance=room)

        if form.is_valid():
            form.save()
            return redirect(f'{reverse("showcase:room", kwargs={"room": room_name})}?username={username}')

        return render(request, self.template_name, {'form': form})

def serialize_default_avatar(avatar):
    if avatar:
        return {
            "default_avatar_name": avatar.default_avatar_name,
            "default_avatar_url": avatar.default_avatar.url if avatar.default_avatar else None,
            "is_active": avatar.is_active,
        }
    return None

def serialize_profile(profile_details):
    if profile_details:
        return {
            "avatar_url": profile_details.avatar.url if profile_details.avatar else None,
            "profile_url": profile_details.get_absolute_url(),
        }
    return None

def getMessages(request, room):
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        return JsonResponse({'messages': []})

    messages = Message.objects.filter(room=room_details)
    messages_data = []

    for message in messages:
        profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()
        default_avatar = DefaultAvatar.objects.first()

        avatar_url = (
            profile_details.avatar.url if profile_details and profile_details.avatar else
            serialize_default_avatar(default_avatar)['default_avatar_url']
        )
        user_profile_url = (
            profile_details.get_absolute_url() if profile_details else
            f'/home/{room}/?username={request.user.username}'
        )

        message_data = {
            'user_profile_url': user_profile_url,
            'avatar_url': avatar_url,
            'user': message.user,
            'value': message.value,
            'date': message.date.strftime("%Y-%m-%d %H:%M:%S"),
            'message_number': message.message_number,
            'file': message.file.url if message.file else None,
        }
        messages_data.append(message_data)

    return JsonResponse({'messages': messages_data})

def supportroom(request):
    username = request.user.username
    room_details = SupportChat.objects.get(name=username)
    profile_details = ProfileDetails.objects.filter(
        user__username=username).first()
    return render(request, 'supportroom.html', {
        'username': username,
        'room': room_details,
        'room_details': room_details,
        'profile_details': profile_details,
    })

def index(request):
    generalmessages = Message.objects.filter(room='GeneralChatMessages').order_by('-date')
    messages = SupportMessage.objects.filter(room=request.user.username).order_by('-timestamp')
    return render(request, 'index.html', {'messages': messages})

def supportchat(request):
    return render(request, 'supportchat.html')

def privateroom(request, room):
    username = request.user.username
    room_details = Room.objects.get(name=room)
    return render(request, 'privateroom.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def supportcheckview(request):
    help = request.POST['help']

    username = request.user.username

    if SupportChat.objects.filter(name=username).exists():
        new_message = SupportMessage.objects.create(value=help,
                                                    user=username,
                                                    room=username)
        new_message.save()

        return redirect('/supportchat/room/' + username)
    else:
        new_room = SupportChat.objects.create(name=username)
        new_room.save()

        new_message = SupportMessage.objects.create(value=help,
                                                    user=username,
                                                    room=username)
        new_message.save()

        return redirect('/supportchat/room/' + username)
        print('support message sent')

def supportsend(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room = request.POST.get('username')

        print(f"message: {message}, username: {username}, room_name: {username}")
        print('the support chat is where it is from')

        if request.user.is_authenticated:

            new_message = SupportMessage.objects.create(
                value=message,
                user=username,
                room=username,

                signed_in_user=request.user
            )

            new_message.save()
        else:

            new_message = SupportMessage.objects.create(
                value=message,
                user=username,
                room=username,
            )
            new_message.save()

        return HttpResponse('Message sent successfully')

    return HttpResponse('Invalid request method. Please use POST to send a message.')

import django
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import UpdateProfile, EmailField
from .models import Idea
from .models import VoteQuery
from .models import Choice
from .models import StaffApplication
from .models import Contact
from .models import BusinessMailingContact
from .models import PartnerApplication
from .models import PunishmentAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import City, VoteQuery, UpdateProfile, Idea, PartnerApplication
from .models import Support
from .models import FaviconBase
from .models import BackgroundImage
from .models import EBackgroundImage
from .models import ShowcaseBackgroundImage
from .models import ChatBackgroundImage
from .models import SupportChatBackgroundImage
from .models import BilletBackgroundImage
from .models import PatreonBackgroundImage
from .models import BusinessMessageBackgroundImage
from .models import Patreon
from .models import BlogBackgroundImage
from .models import PostBackgroundImage
from .models import PosteBackgroundImage
from .models import VoteBackgroundImage
from .models import RuleBackgroundImage
from .models import AboutBackgroundImage
from .models import FaqBackgroundImage
from .models import StaffBackgroundImage
from .models import InformationBackgroundImage
from .models import TagBackgroundImage
from .models import UserBackgroundImage
from .models import StaffRanksBackgroundImage
from .models import StaffApplyBackgroundImage
from .models import MegaBackgroundImage
from .models import EventBackgroundImage
from .models import NewsBackgroundImage
from .models import DonorBackgroundImage
from .models import ContributorBackgroundImage
from .models import ContentBackgroundImage
from .models import PartnerBackgroundImage
from .models import ShareBackgroundImage
from .models import WhyBackgroundImage
from .models import ProductBackgroundImage
from .models import SettingsModel
from .models import ImageCarousel
from .models import PostLikes
from .models import ConvertBackgroundImage
from .models import ReasonsBackgroundImage
from .models import SettingsBackgroundImage
from .models import PunishAppsBackgroundImage
from .models import BanAppealBackgroundImage
from .models import SupportBackgroundImage
from .models import OrderBackgroundImage
from .models import CheckoutBackgroundImage
from .models import SignupBackgroundImage
from .models import PerksBackgroundImage
from .models import ChangePasswordBackgroundImage
from .models import IssueBackgroundImage
from .models import BackgroundImageBase
from .models import TextBase
from .models import LogoBase
from .models import MemberHomeBackgroundImage
from .models import NavBar
from .models import NavBarHeader
from .models import DonateIcon
from .models import Donate
from .models import Titled
from .models import Membership
from .models import AdvertisementBase
from .models import ImageBase
from .models import SocialMedia
from .models import AdminRoles
from .models import AdminTasks
from .models import AdminPages

from .forms import VoteQueryForm, EmailForm
from .forms import PostForm
from .forms import Postit
from .forms import StaffJoin
from .forms import Server_Partner
from .forms import SignUpForm
from .forms import News_Feed
from .forms import PunishAppeale
from .forms import ReportIssues
from .forms import BanAppeale
from .forms import Staffprofile
from .forms import Eventform
from .forms import SupportForm
from .forms import SettingsForm
from .forms import BackgroundImagery
from .forms import EBackgroundImagery
from .forms import ShowcaseBackgroundImagery
from .forms import ChatBackgroundImagery
from .forms import BilletBackgroundImagery
from .forms import BlogBackgroundImagery
from .forms import PostBackgroundImagery
from .forms import RuleBackgroundImagery
from .forms import AboutBackgroundImagery
from .forms import FaqBackgroundImagery
from .forms import StaffBackgroundImagery
from .forms import InformationBackgroundImagery
from .forms import TagBackgroundImagery
from .forms import UserBackgroundImagery
from .forms import StaffRanksBackgroundImagery
from .forms import MegaBackgroundImagery
from .forms import EventBackgroundImagery
from .forms import NewsBackgroundImagery
from .forms import PaypalPaymentForm
from .forms import BaseCopyrightTextField
from .forms import ContactForme
from .forms import SignUpForm

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.db.models import Q
from django.views import generic
from django.views.generic import TemplateView, ListView

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Blog
from .models import Comment
from .models import UserProfile2
from django.views.generic.edit import FormMixin

import pdb
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .forms import ContactForm
from .forms import BusinessContactForm
from .forms import BusinessMailingForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404

from .models import Room, Message
from .models import SupportChat, SupportMessage
from django.http import JsonResponse
import os

from django.contrib.auth.decorators import login_required

from guest_user.mixins import RegularUserRequiredMixin

from guest_user.decorators import allow_guest_user

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .forms import CheckoutForm

class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        print('the login context is ' + context)
        return context

class SignupView(FormMixin, ListView):
    model = SignupBackgroundImage
    template_name = "cv-form.html"
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup'] = SignupBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        print('signup')
        if request.method == 'POST':
            print('post')
            form = SignUpForm(request.POST)
            if form.is_valid():
                print('is_valid')
                user = form.save()
                user.refresh_from_db()
                user.save()
                raw_password = form.cleaned_data.get('password')

                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                subject = "Welcome to IntelleX!"
                message = 'Hello {user.username}, thank you for becoming a member of the IntelleX Community!'
                email_from = settings.EMAIL_HOST_USER
                recipent_list = [user.email, ]
                send_mail(subject, message, email_from, recipent_list)

                return redirect('showcase:showcase')
                messages.info(request, "You have signed up successfully! Welcome!")
        else:
            form = SignUpForm()
        return render(request, 'cv-form.html', {'form': form})

class TotalView(ListView):
    model = BackgroundImageBase

    def _context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['TextFielde'] = TextBase.objects.filter(is_active=1).order_by("section")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class LogoView(ListView):
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter('page')
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

from .models import Advertising

class AdvertisementView(ListView):
    model = AdvertisementBase

    def display_advertisement(request, advertisement_id):
        advertising = Advertising.objects.get(id=advertising_id)
        context = {'advertising': advertising}
        return render(request, 'index.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Advertisement'] = AdvertisementBase.objects.filter(page=self.template_name, is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

"""    def handle_uploaded_image(i):

       imagefile  = StringIO.StringIO(i.read())
       imageImage = Image

       (width, height) = imageImage.size
       (width, height) = scale_dimensions(width, height, longest_side=240)

       resizedImage = imageImage.resize((width, height))

       imagefile = StringIO.StringIO()
       resizedImage.save(imagefile,'JPEG')"""

def set_image_position(image_id, xposition, yposition):

    image = ImageBase.objects.get(id=image_id)
    print("Current coordinates: x={image.x}, y={image.y}")

    image.x = xposition
    image.y = yposition

    image.save()

class ImageView(ListView):
    model = ImageBase

    def post(self, request, *args, **kwargs):

        image_id = request.POST.get('image_id')
        xposition = request.POST.get('xposition')
        yposition = request.POST.get('yposition')

        set_image_position(image_id, xposition, yposition)

        return HttpResponse('Image position updated.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BaseView(ListView):
    template_name = "base.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        current_user = self.request.user
        if current_user.is_authenticated:
            context['preferenceform'] = MyPreferencesForm(user=current_user)

        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class EBaseView(ListView):
    template_name = "ebase.html"
    model = NavBar

    def get_context_data(self, **kwargs):

        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logos'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BlogBaseView(ListView):
    template_name = "blogbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


@login_required
def ajax_update_amount(request):
    profile      = request.user.profiledetails
    rd_benefit   = profile.tier.benefits \
                         .filter(benefit='RD', is_active=1) \
                         .first()
    rd_multiplier = rd_benefit.multiplier if rd_benefit else 1

    return JsonResponse({
        'rd_multiplier': rd_multiplier,
    })


class NavView(ListView):
    template_name = "navtrove.html"
    model = LogoBase

    def post(self, request, *args, **kwargs):
        form = MyPreferencesForm(request.POST, user=request.user)
        if form.is_valid():
            preference = form.save(commit=False)
            preference.user = request.user
            preference.save()
            return JsonResponse({
                'status': 'success',
                'preference_value': preference.spintype
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'),
                                                  is_active=1)

        user = self.request.user
        if user.is_authenticated:
            preference_instance = MyPreferences.objects.filter(user=user).first()
            if preference_instance:
                context['preferenceform'] = MyPreferencesForm(instance=preference_instance, user=user)
                context['preference_instance'] = preference_instance
                context['is_signed_in'] = user.is_authenticated
                context['has_preference'] = preference_instance is not None
                context['preference_value'] = preference_instance.spintype if preference_instance else None
            else:
                context['preferenceform'] = MyPreferencesForm(user=user)
                context['preference_instance'] = None
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['form'] = MyPreferencesForm(user=self.request.user)

        print("navtrove here")
        for logo in context['Logo']:
            print("the logo is " + logo.title)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

                    clickables = Clickable.objects.filter(is_active=1)

                    user_clickables = UserClickable.objects.filter(user=user, clickable__in=clickables)

                    context['Clickables'] = user_clickables

        if self.request.user.is_authenticated:
            profile = (
                ProfileDetails.objects
                .filter(user=self.request.user, is_active=1)
                .select_related('tier')
                .first()
            )
        else:
            profile = None
        context['profiledetails'] = profile
        context['user_tier_code']  = (
            profile.tier.tier if profile and profile.tier else ''
        )
        return context

import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F

from .models import UserClickable, ProfileDetails

@login_required
@require_POST
def update_currency(request):
    data       = json.loads(request.body)
    name       = data.get("clickable_name")
    base_val   = data.get("actual_value", 0)
    multiplier = data.get("exponential_multiplier", 1)

    try:
        with transaction.atomic():
            # 1) Lock the UserClickable row
            uc = UserClickable.objects.select_for_update().get(
                user=request.user,
                clickable__name=name,
                is_active=1
            )

            # 2) Compute how much currency to add
            try:
                increment = float(base_val) * float(multiplier)
            except (TypeError, ValueError):
                increment = uc.actual_value * uc.exponential_level_multiplier

            # 3) Increment the click count in Python
            uc.count = uc.count + 1
            uc.save()

            # 4) Lock and update the user's currency
            profile = ProfileDetails.objects.select_for_update().get(user=request.user)
            profile.currency_amount = profile.currency_amount + increment
            profile.save()

    except UserClickable.DoesNotExist:
        return JsonResponse({"success": False, "error": "Invalid clickable"}, status=400)

    # 5) Return both new totals
    return JsonResponse({
        "success":    True,
        "new_amount": profile.currency_amount,
        "new_count":  uc.count
    })



def detail_post_view(request, id=None):
    eachpost = get_object_or_404(Post, id=id)

    context = {'eachpost': eachpost}

    return render(request, 'showcase:likes.html', context)

@login_required
def postpreference(request, post_name, like_or_dislike):
    if request.method == "POST":
        eachpost = get_object_or_404(Blog, slug=post_name)

        if request.user in eachpost.likes.iterator():
            eachpost.likes.remove(request.user)
        if request.user in eachpost.dislikes.iterator():
            eachpost.dislikes.remove(request.user)

        if int(like_or_dislike) == 1:
            eachpost.likes.add(request.user)
        else:
            eachpost.dislikes.add(request.user)

        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'likes.html', context)

    else:
        eachpost = get_object_or_404(Blog, slug=post_name)
        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'showcase:likes.html', context)

from django.contrib.admin.views.decorators import staff_member_required
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(staff_member_required, name='dispatch')
class AdminRolesView(BaseView):
    template_name = "administrativeroles.html"
    model = AdminRoles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Roles'] = AdminRoles.objects.filter(is_active=1)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTasksView(BaseView):
    template_name = "administrativetasks.html"
    model = AdminTasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Tasks'] = AdminTasks.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminPagesView(BaseView):
    template_name = "administrativepages.html"
    model = AdminPages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Pages'] = AdminPages.objects.filter(is_active=1)
        AdminPage = AdminPages.objects.filter(is_active=1)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@method_decorator(staff_member_required, name='dispatch')
class AdministrationView(ListView):
    template_name = "administration.html"
    model = AdminPages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Pages'] = AdminPages.objects.filter(is_active=1)
        context['Tasks'] = AdminTasks.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class DonateBaseView(ListView):
    template_name = "donatebase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ShippingBackgroundView(FormMixin, LoginRequiredMixin, ListView):
    model = UserProfile2
    template_name = "shippingform.html"
    form_class = ShippingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ShippingForm(user=self.request.user)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        form = ShippingForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Shipping fields updated successfully.')
            return redirect('showcase:shippingprofile')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "shippingform.html", {'form': form})

class ShippingProfileView(ListView):
    model = UserProfile2
    template_name = "shippingprofile.html"

    def get_queryset(self):
        return ShowcaseBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")

        current_user = self.request.user
        newprofile = UserProfile2.objects.filter(is_active=1, user=current_user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PrintShippingLabelView(LoginRequiredMixin, ListView):
    model = TradeShippingLabel
    template_name = "printandship.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Label'] = TradeShippingLabel.objects.filter(is_active=1, user=self.request.user)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class MembershipView(LoginRequiredMixin, ListView):
    model = Membership
    template_name = "membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Label'] = TradeShippingLabel.objects.filter(is_active=1, user=self.request.user)
        context['tier'] = Membership.objects.filter(is_active=1)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class MemberBaseView(ListView):
    template_name = "memberbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class usersview(ListView):
    paginate_by = 10
    template_name = 'users.html'

    def get_queryset(self):
        return Idea.objects.all()

from django.db.models import Count, F

class PostList(BaseView):
    model = BlogBackgroundImage

    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        print(124)
        context = super().get_context_data(**kwargs)
        paginate_by = int(self.request.GET.get('paginate_by', settings.DEFAULT_PAGINATE_BY))

        blog_query = Blog.objects.filter(is_active=1)
        paginator = Paginator(blog_query, paginate_by)
        blog_tips = Blog.objects.filter(is_active=1)
        page_number = self.request.GET.get('page')
        paginated_blog = paginator.get_page(page_number)

        PopularBlogOrder = Blog.objects.annotate(like_dislike_diff=Count(F('likes')) - Count(F('dislikes'))).order_by(
            '-like_dislike_diff', '-created_on')

        PopularBlogOrder = PopularBlogOrder.order_by('-like_dislike_diff')

        context = {'PopularBlogOrder': PopularBlogOrder}

        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['TextFielde'] = TextBase.objects.filter(is_active=1)
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1).order_by("image_position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1).order_by('image_position')

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['BlogFilter'] = BlogFilter.objects.filter(is_active=1).order_by('clicks')
        context['BlogHeader'] = BlogHeader.objects.filter(is_active=1).order_by('category')
        context['blog_count'] = BlogHeader.objects.filter(is_active=1).order_by('category').count()
        context['Email'] = EmailField.objects.filter(is_active=1)
        context['form'] = EmailForm()

        context['blogpagination'] = paginated_blog

        comments = Comment.objects.filter(active=True, is_active=1).order_by('-created_on')

        context['Comments'] = comments

        for comments in context['Comments']:
            commentator = comments.commentator
            profile = ProfileDetails.objects.filter(user=commentator).first()
            if profile:
                comments.author_profile_picture_url = profile.avatar.url
                comments.author_profile_url = comments.get_profile_url()

                print('imgsrcimg')

        blog_posts = Blog.objects.filter(status=1).order_by('-created_on')

        context['BlogPosts'] = blog_posts

        for blog_post in context['BlogPosts']:
            author = blog_post.author
            profile = ProfileDetails.objects.filter(user=author).first()
            if profile:
                blog_post.author_profile_picture_url = profile.avatar.url
                blog_post.author_profile_url = blog_post.get_profile_url()

                print('imgsrcimg')

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "blog.html", {'form': form})

    def get_blog_count():
        return Blog.objects.all().count()

    def get_queryset(self):
        return Blog.objects.filter(status=1).order_by('-created_on')

from django.shortcuts import render, redirect, get_object_or_404
from .models import VoteQuery, VoteOption, Ballot
from .forms import VoteQueryForm, VoteOptionFormSet

def vote(request, poll_id):
    poll = get_object_or_404(VoteQuery, pk=poll_id, is_active=True)

    if request.method == 'POST':
        option_id = request.POST.get('option')
        selected_option = get_object_or_404(VoteOption, pk=option_id)

        if not Ballot.objects.filter(user=request.user, vote_query=poll).exists():
            Ballot.objects.create(
                user=request.user,
                vote_query=poll,
                selected_option=selected_option
            )
            return redirect('showcase:poll_results', poll_id=poll.id)

    return render(request, 'ballot.html', {'poll': poll})

def poll_results(request, poll_id):
    poll = get_object_or_404(VoteQuery, pk=poll_id)
    return render(request, 'results.html', {'poll': poll})

class votingview(ListView):
    model = VoteBackgroundImage
    paginate_by = 10
    template_name = 'voting.html'

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return render(request, "emaildone.html", {'form': form})
        else:
            messages.error(request, "Form submission invalid")
            return render(request, "voting.html", {'form': form})

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)

        context['polls'] = VoteQuery.objects.filter(is_active=True)
        return render(request, "voting.html", {'form': form, **context})

    def get_queryset(self):
        return VoteBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['VoteQuery'] = VoteQuery.objects.all()

        profiles = VoteQuery.objects.filter(is_active=1)
        context['Profiles'] = profiles

        for poll in context['Profiles']:
            user = poll.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                poll.newprofile_profile_picture_url = profile.avatar.url
                poll.newprofile_profile_url = poll.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        context['NewsProfiles'] = userprofile if userprofile else None

        if context['NewsProfiles'] is None:
            dummy_profile = type('DummyProfile', (), {})()
            dummy_profile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            dummy_profile.newprofile_profile_url = None
            context['NewsProfiles'] = dummy_profile
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class CreateItemView(FormMixin, LoginRequiredMixin, ListView):
    model = Item
    paginate_by = 10
    template_name = 'create_product.html'
    form_class = ItemForm

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super(CreateItemView, self).get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Item'] = Item.objects.filter(is_active=1)

        newprofile = Item.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get(self, request, *args, **kwargs):
        form = ItemForm()
        context = self.get_context_data()
        context['form'] = form
        return render(request, 'create_product.html', context)

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:ehome')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            form = ItemForm()
        return render(request, 'create_product.html', {'form': form})

    def profileview(request):
        instance = Item.objects.get(pk=1)
        fields = []
        for field in instance._meta.get_fields():
            fields.append({
                'name': field.name,
                'value': getattr(instance, field.name),
            })
        return render(request, 'some_template.html', {'fields': fields})

class TradeItemCreateView(ListView):
    model = TradeItem
    template_name = 'tradingcentral.html'
    success_url = '/tradingcentral/'

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
       
        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['TradeItems'] = TradeItem.objects.filter(is_active=1)
        context['TradeOffers'] = TradeOffer.objects.filter(is_active=1)
        context['Friends'] = Friend.objects.filter(user=self.request.user, is_active=1)
        tradeoffering = RespondingTradeOffer.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")

        trade_offers = TradeOffer.objects.filter(is_active=1)

        slug = self.kwargs.get('slug')

        if slug:

            trade_objects = TradeOffer.objects.filter(slug=slug)

            context['TradeOffered'] = trade_objects

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class TradeBackgroundView(FormMixin, LoginRequiredMixin, ListView):
    model = TradeItem
    template_name = "tradeitems.html"
    form_class = TradeItemForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['TradeItem'] = TradeItem.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        form = TradeItemForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:tradingcentral')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            form = TradeItemForm()
        return render(request, 'tradeitems.html', {'form': form})

class TradeOfferCreateView(CreateView):
    model = TradeOffer
    form_class = TradeProposalForm
    template_name = 'createtradeoffer.html'
    success_url = '/tradingcentral/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        form = TradeProposalForm(self.request.POST or None, user=self.request.user)
        context['form'] = form
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['TradeOffer'] = TradeOffer.objects.filter(is_active=1)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def contact_trader(self, request, trade_item_id):
    trade_item = get_object_or_404(TradeItem, id=trade_item_id)
    current_user = request.user

    room = trade_item.create_room(current_user)

    return redirect('showcase:room', room=room.name, username=current_user.username)


class ResponseTradeOfferCreateView(CreateView):
    model = RespondingTradeOffer
    form_class = RespondingTradeOfferForm
    template_name = 'responsetradeitems.html'
    success_url = '/directedtradeoffers/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form_instance(self):
        form = self.form_class(self.request.POST or None, user=self.request.user)
        form.fields['offered_trade_items'].queryset = TradeItem.objects.filter(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form_instance()
            if form.is_valid():
                trade_request = form.save(commit=False)
                trade_request.user = request.user

                try:
                    trade_request.save()
                    trade_request.user2 = trade_request.wanted_trade_items.user
                    trade_request.save()
                    messages.success(request, "Trade offer submitted successfully.")
                    return redirect('showcase:directedtradeoffers')

                except IntegrityError as e:
                    if 'UNIQUE constraint failed: showcase_respondingtradeoffer.slug' in str(e):
                        messages.warning(request, "You have already submitted a trade offer for this item.")
                        return redirect('showcase:directedtradeoffers')

        context = {'form': self.get_form_instance()}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form_instance()
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['TradeOffer'] = TradeOffer.objects.filter(is_active=1)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@login_required
def contact_trader(request):
    trade_item_id = request.pk
    trade_item = get_object_or_404(TradeItem, id=trade_item_id)
    current_user = request.user

    room = trade_item.create_room(current_user)

    return redirect('showcase:room', room=room.name, username=current_user.username)

@method_decorator(login_required, name='dispatch')
class FriendRequestsView(View):
    def get(self, request, *args, **kwargs):

        pending_requests = FriendRequest.objects.filter(receiver=request.user, status=FriendRequest.PENDING)
        outgoing_requests = FriendRequest.objects.filter(sender=request.user, status=FriendRequest.PENDING)

        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        profiles = []
        for newprofile in FriendRequest.objects.filter(Q(sender=request.user) | Q(receiver=request.user)):
            user = newprofile.sender if newprofile.sender != request.user else newprofile.receiver
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url(request.user)
                profiles.append(newprofile)

        context['Profiles'] = profiles

        if is_ajax(request):
            context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
            return render(request, 'my_friend_request.html', context)

        context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
        return render(request, 'my_friend_requests.html', context)

from django.contrib import messages

@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    print('friend request acceptance')
    if request.user != friend_request.receiver:
        raise PermissionDenied
    friend_request.status = FriendRequest.ACCEPTED
    friend_request.save()
    messages.success(request, 'You have accepted the friend request.')
    return redirect('showcase:my_friend_requests')

@login_required
def decline_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if request.user != friend_request.receiver:
        raise PermissionDenied
    friend_request.status = FriendRequest.DECLINED
    friend_request.save()
    messages.success(request, 'You have declined the friend request.')
    return redirect('showcase:my_friend_requests')

class FriendlyView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        friends = user.get_friends()
        print(friends)
        context = {'friends': friends, 'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
                   'DropDown': NavBar.objects.filter(is_active=1).order_by('position')}
        current_user = request.user

        newprofile = Friend.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return render(request, 'my_friends.html', context)

@method_decorator(login_required, name='dispatch')
class SendFriendRequestView(View):
    def post(self, request):
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            friend_request = form.save(commit=False)
            friend_request.sender = request.user

            if not FriendRequest.objects.filter(sender=friend_request.sender,
                                                receiver=friend_request.receiver).exists():
                friend_request.save()
                return HttpResponseRedirect('/my_friend_requests')
            else:
                messages.error(request,
                               "You already sent a friend request to that user or you are already friends with them!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:

            messages.error(request, "Please send a friend request to the trader to continue.")
            return render(request, 'send_friend_request.html', {'form': form})

    def get(self, request):
        form = FriendRequestForm()
        context = {}
        context['form'] = form
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        return render(request, 'send_friend_request.html', context)

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def contact_trader(request, trade_offer_id):
    trade_offer = TradeOffer.objects.get(id=trade_offer_id)
    current_user = request.user

    if not FriendRequest.objects.filter(
            Q(sender=trade_offer.user, receiver=current_user, status=FriendRequest.ACCEPTED) |
            Q(sender=current_user, receiver=trade_offer.user, status=FriendRequest.ACCEPTED)
    ).exists():

        FriendRequest.objects.create(sender=current_user, receiver=trade_offer.user, status=FriendRequest.PENDING)
    else:

        room = Room.objects.filter(signed_in_user__in=[current_user, trade_offer.user], public=False).first()
        if not room:

            room = Room.objects.create(name=f'Private room: {current_user.username} and {trade_offer.user.username}',
                                       signed_in_user=current_user, public=False)

        return redirect(room.get_absolute_url())

class partnerview(ListView):
    paginate_by = 10
    template_name = 'partners.html'

    def get_queryset(self):
        return PartnerApplication.objects.all()

class newsfeedview(ListView):
    paginate_by = 10
    template_name = 'newsfeed.html'

    def get_queryset(self):
        return NewsFeed.objects.all()

class Issueview(ListView):
    paginate_by = 10
    template_name = 'issues.html'

    def get_queryset(self):
        return ReportIssue.objects.all()

class staffview(ListView):
    paginate_by = 10
    template_name = 'staff.html'

    def get_queryset(self):
        return StaffProfile.objects.all()

class eventview(ListView):
    paginate_by = 10
    template_name = 'events.html'

    def get_queryset(self):
        return Event.objects.all()

"""class SupportRoomView(TemplateView):
    model = SupportMessage
    template_name = 'supportroom.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.kwargs['room']
        username = self.request.GET.get('username')
        room_details = Room.objects.get(name=room)
        profile_details = ProfileDetails.objects.filter(user__username=username).first()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
    
        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        context['username'] = username
        context['room'] = room
        context['room_details'] = room_details
        context['profile_details'] = profile_details

        messages = Message.objects.all().order_by('-date')

        context['Messaging'] = messages

        for messages in context['Messaging']:
            profile = ProfileDetails.objects.filter(user=messages.signed_in_user).first()
            if profile:
                messages.user_profile_picture_url = profile.avatar.url
                messages.user_profile_url = messages.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context"""

class SupportRoomView(TemplateView):
    model = SupportMessage
    template_name = 'supportroom.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signed_in_user = self.kwargs['signed_in_user']

        context['username'] = signed_in_user

        profile_details = ProfileDetails.objects.filter(user__username=signed_in_user).first()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['room'] = signed_in_user
        context['profile_details'] = profile_details

        messages = SupportMessage.objects.all().order_by('-date')

        context['Messanger'] = messages

        messages_data = []

        for messages in context['Messanger']:
            profile = ProfileDetails.objects.filter(user=messages.signed_in_user).first()

            message_data = {
                'user_profile_picture_url': profile.avatar.url if profile else '',
                'user_profile_url': messages.get_profile_url(),
                'user': messages.signed_in_user,
                'value': messages.value,
                'date': messages.date,
            }

            messages_data.append(message_data)

        context['Messanger'] = messages_data

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def supportroom(request, signed_in_user):
    return render(request, 'supportroom.html', {
        'username': username,
        'supportroom': supportroom,
        'signed_in_user': signed_in_user,
        'room_details': room_details,
        'profile_details': profile_details,
        'Logo': Logo,
        'Header': Header,
        'Dropdown': DropDown,
    })

class SupportCombinedView(SupportRoomView, ListView):
    paginate_by = 10
    template_name = 'supportroom.html'

    def get_queryset(self):
        return SupportMessage.objects.all()

class supportview(ListView):
    paginate_by = 10
    template_name = 'supportissues.html'

    def get_queryset(self):
        return Support.objects.all()

class SupportLineView(TemplateView):
    model = SupportLine
    template_name = 'supportline.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.kwargs['room']
        username = self.request.GET.get('username')
        room_details = SupportInterface.objects.get(name=room)
        profile_details = ProfileDetails.objects.filter(user__username=username).first()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['username'] = username
        context['room'] = room
        context['room_details'] = room_details
        context['profile_details'] = profile_details

        messages = SupportLine.objects.all().order_by('-date')

        context['Messaging'] = messages

        for messages in context['Messaging']:
            profile = ProfileDetails.objects.filter(user=messages.signed_in_user).first()
            if profile:
                messages.user_profile_picture_url = profile.avatar.url
                messages.user_profile_url = messages.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def supportline(request, room):
    username = request.user.username
    room_details = SupportInterface.objects.get(name=username)
    profile_details = ProfileDetails.objects.filter(
        user__username=username).first()
    return render(request, 'supportline.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'profile_details': profile_details,
    })

def supportlinecheckview(request):
    room = request.POST['room_name']

    if SupportInterface.objects.filter(name=room).exists():

        return redirect('/supportinterface/room/' + room)
    else:
        new_room = SupportInterface.objects.create(name=room)
        signed_in_user = request.user
        print('the room owner is ' + str(signed_in_user))
        new_room.save()

        return redirect('/supportinterface/room/' + room)

from django.shortcuts import get_object_or_404

def supportlinesend(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')

        print(f"message: {message}, username: {username}, room_id: {room_id}")

        if request.user.is_authenticated and request.user.is_staff:

            user = request.user

        new_message = SupportLine.objects.create(
            value=message,
            user=user,
            room=room_id,
            signed_in_user=request.user if request.user.is_authenticated else None
        )

        return HttpResponse('Message sent successfully')

    return HttpResponse('Invalid request or authorization.')

def supportlinegetMessages(request, room, **kwargs):
    room_details = SupportInterface.objects.get(name=room)
    messages = SupportLine.objects.filter(room=room)

    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to access this chat room")

    chat_room = get_object_or_404(SupportInterface, name=room)

    if request.user.is_staff:

        messages = SupportLine.objects.filter(room=chat_room)
        messages_data = []

        for message in messages:
            profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()
            if profile_details:
                user_profile_url = message.get_profile_url()
                avatar_url = profile_details.avatar.url
            else:
                user_profile_url = f'/supportline/{message.signed_in_user}'
                avatar_url = DefaultAvatar.objects.first()

            messages_data.append({
                'user_profile_url': user_profile_url,
                'avatar_url': avatar_url,
                'user': message.signed_in_user.username,
                'value': message.value,
                'date': message.date.strftime("%Y-%m-%d %H:%M:%S"),
                'message_number': message.message_number,
            })

        return JsonResponse({'messages': messages_data})
    else:
        return HttpResponseForbidden("You do not have permission to access this chat room")

class MemberHomeBackgroundView(ListView):
    model = MemberHomeBackgroundImage
    template_name = "memberhome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['MemberHomeBackgroundImage'] = MemberHomeBackgroundImage.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BusinessMessageBackgroundView(ListView):
    model = BusinessMessageBackgroundImage
    template_name = "businessemail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['BusinessMessageBackgroundImage'] = BusinessMessageBackgroundImage.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class PatreonBackgroundView(ListView):
    model = Patreon
    template_name = "patreon.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

"""class BlogComment(generic.DetailView):
    model = Blog
    paginate_by = 10
    template_name = 'blog_comment.html'

    def post(self, request, slug, *args, **kwargs):
        most_recent = Blog.objects.order_by('-created_on')[:3]

        post = get_object_or_404(Blog, slug=slug)
        category_count = post.likes

        form = CommentForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.instance.user = request.user
                form.instance.post = post
                form.save()
                return redirect(reverse("blog_comment", kwargs={
                    'id': post.pk
                }))
        context = {
            'form': form,
            'post': post,
            'most_recent': most_recent,
            'category_count': category_count,
            'form': form
        }
        return render(request, 'blog_comment.html', context)"""

from django.views.generic import ListView, CreateView

class FaviconBaseView(ListView):
    model = FaviconBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicons'] = FaviconBase.objects.filter('faviconpage')
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class BackgroundBaseView(ListView):
    model = BackgroundImageBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BackgroundImages'] = BackgroundImageBase.objects.filter('page').order_by('position')
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class TextBaseView(ListView):
    model = TextBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(is_active=1).order_by("section")
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        return render(context)

class ImageCarouselView(BaseView):
    model = ImageCarousel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Carousel'] = ImageCarousel.objects.filter(is_active=1).order_by('position')
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def index(request):
    general_messages = Message.objects.filter(room="General").order_by('-date')
    context = {'GeneralMessanger': general_messages}
    return render(request, 'index.html', context)

from django.http import HttpResponse
from .models import Message

from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.decorators.csrf import csrf_exempt
from .models import Message, Room, ProfileDetails
import logging

def getGeneralMessages(request):
    messages = GeneralMessage.objects.all().order_by('date')[30:]
    messages_data = []

    default_avatar = DefaultAvatar.objects.first()
    default_avatar_data = serialize_default_avatar(default_avatar)

    for message in messages:
        profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()

        avatar_url = (
            profile_details.avatar.url if profile_details and profile_details.avatar else
            default_avatar_data['default_avatar_url'] if default_avatar_data else None
        )
        user_profile_url = (
            profile_details.get_absolute_url() if profile_details else
            'index.html'
        )

        message_data = {
            'user_profile_url': user_profile_url,
            'avatar_url': avatar_url,
            'user': str(message.user),
            'value': message.value,
            'date': message.date.strftime("%Y-%m-%d %H:%M:%S"),
            'message_number': message.message_number,
            'file': message.file.url if message.file else None,
        }
        messages_data.append(message_data)

    return JsonResponse({'messages': messages_data})

@csrf_exempt
def generalsend(request):
    if request.method == 'POST':
        generalmessage = request.POST.get('message')
        username = request.POST.get('username')
        uploaded_file = request.FILES.get('file')

        print(f"message: {generalmessage}, username: {username}")
        print('This is a community-sent message')

        if not generalmessage:
            return JsonResponse({'status': 'error', 'generalmessage': 'Message is required.'})

        try:

            if request.user.is_authenticated:
                new_message = GeneralMessage.objects.create(
                    value=generalmessage,
                    user=username,
                    signed_in_user=request.user,
                    file=uploaded_file
                )
            else:
                new_message = GeneralMessage.objects.create(
                    value=generalmessage,
                    user=username,
                    file=uploaded_file
                )
            new_message.save()

            file_url = None
            if new_message.file:
                file_url = new_message.file.url if hasattr(new_message.file, 'url') else None

            response_data = {
                'status': 'success',
                'generalmessage': 'Message sent successfully',
                'message_data': {
                    'value': new_message.value,
                    'user': new_message.user,
                    'file_url': file_url,
                }
            }
            return JsonResponse(response_data)
        except Exception as e:
            print(f"Error saving message: {e}")
            return JsonResponse({'status': 'error', 'generalmessage': 'An error occurred while saving the message.'})

    return JsonResponse({'status': 'error', 'generalmessage': 'Invalid request method.'})

from django.core.mail import send_mail
from django.conf import settings
from email.mime.image import MIMEImage


def get_games_context(request):
    filter_type = request.GET.get('filter')

    if filter_type in ['F', 'N', 'P']:
        games = Game.objects.filter(is_active=1, filter=filter_type)
    else:
        games = Game.objects.filter(is_active=1)
    game_length = games.count()

    if request.user.is_authenticated:
        user_favs = FavoriteChests.objects.filter(user=request.user, is_active=1)
        fav_dict = {fav.chest.id: fav for fav in user_favs}
    else:
        fav_dict = {}

    context = {
        'Games': games,
        'fav_dict': fav_dict,
        'game_length': game_length,
    }
    return context


def filter_games(request):
    context = get_games_context(request)
    return render(request, 'partial_game.html', context)


@login_required
def filter_games_count(request):
    context = get_games_context(request)
    return render(request, 'partial_game_count.html', context)


class BackgroundView(FormMixin, BaseView):
    model = BackgroundImage
    form_class = EmailForm
    template_name = "index.html"
    section = TextBase.section

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()

            subject = "Subscription Confirmation"
            recipient_email = form.cleaned_data.get('email')
            sender_email = settings.DEFAULT_FROM_EMAIL

            html_content = render_to_string('email_template.html', {'user': request.user})
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                subject,
                text_content,
                sender_email,
                [recipient_email],
            )
            email.attach_alternative(html_content, "text/html")

            image_path = os.path.join(settings.BASE_DIR, 'static/css/images/poketrove_logo.png')
            with open(image_path, 'rb') as img:
                image = MIMEImage(img.read())
                image.add_header('Content-ID', '<subscription_image>')
                email.attach(image)

            try:
                email.send()
                messages.success(request, 'Form submitted successfully. A confirmation email has been sent.')
            except Exception as e:
                messages.error(request, f"Form submitted successfully, but email could not be sent: {e}")

            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            return render(request, "index.html", {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signed_in_user = self.request.user
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['messages'] = SupportMessage.objects.filter(room=self.request.user.username).order_by('-date')
        context['friendmessages'] = Message.objects.filter(room=self.request.user.username).order_by('-date')
        context['Carousel'] = ImageCarousel.objects.filter(is_active=1, carouselpage=self.template_name).order_by("carouselposition")
        events = Event.objects.filter(is_active=1, page=self.template_name)
        for e in events:
            # combine date + time
            dt = datetime.combine(e.date, e.time)
            # make it timezone-aware
            dt = timezone.make_aware(dt, timezone.get_default_timezone())

            # milliseconds since epoch!
            e.start_timestamp = int(dt.timestamp() * 1000)

            # length must be a timedelta (DurationField)
            e.duration_ms = int(e.length.total_seconds() * 1000)
        context['Events'] = events

        spinpreference = None
        user = self.request.user
        if user.is_authenticated:
            preference_instance = MyPreferences.objects.filter(user=user).first()
            if preference_instance:
                context['preferenceform'] = MyPreferencesForm(instance=preference_instance, user=user)
                context['preference_instance'] = preference_instance
                context['is_signed_in'] = user.is_authenticated
                context['has_preference'] = preference_instance is not None
                context['preference_value'] = preference_instance.spintype if preference_instance else None
            else:
                context['preferenceform'] = MyPreferencesForm(user=user)
                context['preference_instance'] = None
            try:
                spinpreference = SpinPreference.objects.get(user=user)
            except SpinPreference.DoesNotExist:
                spinpreference = SpinPreference(user=user, quick_spin=False)
                spinpreference.save()

            context['quick_spin'] = spinpreference.quick_spin
        else:
            context['quick_spin'] = False

        context['spinpreference'] = spinpreference

        active_games = Game.objects.filter(is_active=1, filter='F')

        if active_games.exists():
            game = random.choice(list(active_games))
        else:
            game = None

        if game:
            slug = game.slug
            context['slug'] = game.slug
            context['game'] = game
        else:
            context['slug'] = ''
            context['game'] = None

        user = self.request.user
        if user.is_authenticated:
            try:
                context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
            except UserProfile.DoesNotExist:
                context['SentProfile'] = None
        else:
            context['SentProfile'] = None

        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['wager_form'] = WagerForm()

        choices = Choice.objects.filter(game=game)
        spinner_choice_renders = SpinnerChoiceRenders.objects.filter(game=game)
        context['spinner_choice_renders'] = spinner_choice_renders

        user = self.request.user
        if user.is_authenticated:
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                effective_cost = game.get_effective_cost()
                spin_multiplier = 1
                total_cost = effective_cost * spin_multiplier
                context['user_cash'] = profile.currency_amount
                context['total_cost'] = total_cost
            else:
                context['user_cash'] = None
                context['total_cost'] = None
        else:
            context['user_cash'] = None
            context['total_cost'] = None

        button_type = self.request.GET.get('button_type') or self.request.POST.get('button_type')

        if game:
            button_type = self.request.GET.get('button_type') or self.request.POST.get('button_type')
            if button_type == "start2":
                cost = 0
            else:
                cost = game.discount_cost if game.discount_cost else game.cost
        else:
            cost = 0

        context.update({
            'cost_threshold_80': cost * 0.8,
            'cost_threshold_100': cost,
            'cost_threshold_200': cost * 2,
            'cost_threshold_500': cost * 5,
            'cost_threshold_10000': cost * 100,
        })

        newprofile = UpdateProfile.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        user_profile = None
        slug = game.slug if game else None
        if game:
            if game.user:
                user_profile, created = UserProfile.objects.get_or_create(user=game.user)

                context['SentProfile'] = user_profile
                user_cash = user_profile.currency_amount

                context = {
                    'user_cash': user_cash,
                }

        context['Money'] = Currency.objects.filter(is_active=1).first()

        spinpreference = None

        if user.is_authenticated:
            try:
                spinpreference = SpinPreference.objects.get(user=user)
            except SpinPreference.DoesNotExist:
                spinpreference = SpinPreference(user=user, quick_spin=False)
                spinpreference.save()

            context['quick_spin'] = spinpreference.quick_spin
        else:
            context['quick_spin'] = False

        context['spinpreference'] = spinpreference

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if spinpreference:
            spinform = SpinPreferenceForm(instance=spinpreference)
        else:
            spinform = SpinPreferenceForm()
        context['spin_preference_form'] = spinform

        if user.is_authenticated:
            if spinpreference.quick_spin:
                random_amount = random.randint(500, 1000)
            else:
                random_amount = random.randint(150, 300)
        else:
            random_amount = random.randint(150, 300)

        context['random_amount'] = random_amount
        context['range_random_amount'] = range(random_amount)
        print(str('the random amount is ') + str(random_amount))

        random_amount = random.randint(150, 300)
        random_nonces = [random.randint(0, 1000000) for _ in range(random_amount)]
        context['random_nonces'] = random_nonces

        game_id = self.kwargs.get('slug')

        game = get_object_or_404(Game, slug=slug)

        context['game'] = game

        inline_choices = game.choice_fk_set.all()
        m2m_choices = game.choices.all()
        combined_choices = {choice.pk: choice for choice in list(inline_choices) + list(m2m_choices)}

        through_qs = GameChoice.objects.filter(game=game).select_related('choice')
        through_data = {}
        for gc in through_qs:
            choice = gc.choice
            through_data[choice.pk] = {
                'choice': choice,
                'lower_nonce': gc.lower_nonce if gc.lower_nonce is not None else choice.lower_nonce,
                'upper_nonce': gc.upper_nonce if gc.upper_nonce is not None else choice.upper_nonce,
                'value': gc.value if gc.value is not None else choice.value,
                'rarity': gc.rarity if gc.rarity is not None else choice.rarity,
                'file_url': choice.file.url if choice.file else '',
                'category': choice.category if choice.category else '',
                'currency': {
                    'symbol': choice.currency.name if choice.currency else '💎',
                    'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                }
            }

        all_choices = []
        for pk, choice in combined_choices.items():
            nonce_info = through_data.get(pk, {
                'choice': choice,
                'lower_nonce': choice.lower_nonce,
                'upper_nonce': choice.upper_nonce,
                'value': choice.value,
                'rarity': choice.rarity,
                'file_url': choice.file.url if choice.file else '',
                'category': choice.category if choice.category else '',
                'currency': {
                    'symbol': choice.currency.name if choice.currency else '💎',
                    'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                }
            })

            all_choices.append({
                'choice': choice,
                'choice_text': choice.choice_text,
                'lower_nonce': nonce_info['lower_nonce'],
                'upper_nonce': nonce_info['upper_nonce'],
                'value': nonce_info['value'],
                'rarity': nonce_info['rarity'],
                'file_url': nonce_info['file_url'],
                'category': nonce_info['category'],
                'currency': nonce_info['currency'],
                'image_width': getattr(choice, 'image_width', None),
                'image_length': getattr(choice, 'image_length', None),
                'get_color_display': getattr(choice, 'get_color_display', lambda: ''),
                'get_tier_display': getattr(choice, 'get_tier_display', lambda: ''),
            })

        context['choices'] = all_choices

        choices_with_nonce = []
        for nonce in random_nonces:
            for choice_data in all_choices:
                lower = choice_data['lower_nonce']
                upper = choice_data['upper_nonce']
                if lower is not None and upper is not None and lower <= nonce <= upper:
                    choices_with_nonce.append({
                        'choice': choice_data['choice'],
                        'nonce': nonce,
                        'lower_nonce': lower,
                        'upper_nonce': upper,
                        'rarity': choice_data['rarity'],
                        'file_url': choice_data['file_url'],
                        'currency': choice_data['currency']
                    })
                    break

        context['choices_with_nonce'] = choices_with_nonce

        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        print(context['Background'])

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        context['Advertisement'] = AdvertisementBase.objects.filter(page=self.template_name, is_active=1).order_by(
            "advertisement_position")
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1).order_by("image_position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['FeaturedGame'] = Game.objects.filter(is_active=1, filter='F')
        context['NewGame'] = Game.objects.filter(is_active=1, filter='N')
        context['PopularGame'] = Game.objects.filter(is_active=1, filter='P')
        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
        context['Email'] = EmailField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['About'] = Event.objects.filter(page=self.template_name, is_active=1)
        context['Feedback'] = Feedback.objects.filter(showcase=1, is_active=1)
        context['Events'] = Event.objects.filter(page=self.template_name, is_active=1)
        users = User.objects.all()

        for user in users:
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                user.newprofile_profile_picture_url = profile.avatar.url
                user.newprofile_profile_url = profile.get_profile_url()
            else:
                user.newprofile_profile_picture_url = None
                user.newprofile_profile_url = "#"
        context['Users'] = users

        context['username'] = signed_in_user
        context['room'] = signed_in_user
        context['show_chat'] = True
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['tophit'] = TopHits.objects.filter(is_active=True).order_by('-mfg_date')[:8]
        print(FaviconBase.objects.all())
        print(213324)

        product = Item.objects.filter(is_active=1)

        context['Products'] = product
        total_items = product.count()
        for product in context['Products']:
            image = product.image
            item = Item.objects.filter(slug=product.slug).first()
            if product:
                product.title = item.title
                product.price = item.price
                product.discount_price = item.discount_price
                product.image_url = item.image.url
                product.label = item.label
                product.hyperlink = item.get_profile_url()
                product.description = item.description

        currencyobject = CurrencyMarket.objects.filter(is_active=1)

        context['CurrencyItem'] = currencyobject

        for currencyobject in context['CurrencyItem']:
            image = currencyobject.file
            item = CurrencyMarket.objects.filter(slug=currencyobject.slug).first()
            if currencyobject:
                currencyobject.title = item.name
                currencyobject.price = item.price
                currencyobject.discount_price = item.discount_price
                currencyobject.image_url = item.file.url
                currencyobject.label = item.label
                currencyobject.hyperlink = item.get_profile_url()
                currencyobject.description = item.flavor_text

        events = Event.objects.filter(is_active=1)
        context['NewEvents'] = events

        for events in context['NewEvents']:
            image = events.image
            eventful = Event.objects.filter(date_and_time=events.date_and_time).first()
            if events:
                events.name = eventful.name
                events.image_url = eventful.image.url
                events.hyperlink = eventful.get_profile_url()
                events.description = eventful.description

        newprofile = NewsFeed.objects.filter(is_active=1)

        context['News'] = newprofile

        for newprofile in context['News']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        feed = Feedback.objects.filter(is_active=1).order_by('-timestamp')

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        feed = Feedback.objects.filter(is_active=1).order_by('-timestamp')

        context['FeedBacking'] = feed

        for feed in context['FeedBacking']:
            user = feed.username
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                feed.user_profile_picture_url = profile.avatar.url
                feed.user_profile_url = feed.get_profile_url2()
                feed.feedback_profile_url = feed.get_profile_url()
                print(user)

        messages = SupportMessage.objects.all().order_by('-date')
        context['Messanger'] = messages
        messages_data = []

        for message in context['Messanger']:
            profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()
            message_data = {
                'user_profile_picture_url': profile_details.avatar.url if profile_details else '',
                'user_profile_url': message.get_profile_url(),
                'user': message.signed_in_user,
                'value': message.value,
                'date': message.date,
            }
            messages_data.append(message_data)

        context['Messanger'] = messages_data

        general_messages = Message.objects.filter(room="General").order_by('-date')[:3][::-1]
        general_messages_data = []

        for general_message in general_messages:
            profile_details = ProfileDetails.objects.filter(user=general_message.signed_in_user).first()
            general_message_data = {
                'user_profile_picture_url': profile_details.avatar.url if profile_details else '',
                'user_profile_url': general_message.get_profile_url(),
                'user': general_message.signed_in_user,
                'value': general_message.value,
                'date': general_message.date,
            }
            general_messages_data.append(general_message_data)

        context['GeneralMessanger'] = general_messages_data

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if self.request.user.is_authenticated:
            profile = (
                ProfileDetails.objects
                .filter(user=self.request.user, is_active=1)
                .select_related('tier')
                .first()
            )
        else:
            profile = None
        context['profiledetails'] = profile
        context['user_tier_code']  = (
            profile.tier.tier if profile and profile.tier else ''
        )
        return context

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmailField

def unsubscribe(request):
    if request.user.is_authenticated:

        try:
            email_entry = EmailField.objects.get(user=request.user)
            if request.method == "POST":
                email_entry.delete()
                messages.success(request, "Your email has been unsubscribed successfully.")
                return redirect('home')
            return render(request, 'unsubscribe.html', {'email': email_entry.email})
        except EmailField.DoesNotExist:

            messages.info(request, "You do not have an associated email and are not currently subscribed.")
            return redirect('home')
    else:

        if request.method == "POST":
            email = request.POST.get('email')
            try:
                email_entry = EmailField.objects.get(email=email)
                email_entry.delete()
                messages.success(request, "The email has been unsubscribed successfully.")
                return redirect('showcase:home')
            except EmailField.DoesNotExist:
                messages.error(request, "The email you entered is not subscribed.")
                return redirect('showcase:unsubscribe')
        return render(request, 'unsubscribe.html')

"""
@login_required
def get_general_messages(request, room_name):
    general_messages = Message.objects.filter(room=room_name).order_by('date')

    messages_data = []
    for message in general_messages:
        profile = ProfileDetails.objects.filter(user=message.signed_in_user).first()
        message_data = {
            'user_profile_picture_url': profile.avatar.url if profile else '',
            'user_profile_url': message.get_profile_url(),
            'user': message.signed_in_user.username,
            'value': message.value,
            'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
        }
        messages_data.append(message_data)

    return JsonResponse({'messages': messages_data})"""

def indexsupportroom(request, signed_in_user):
    return render(request, 'index.html', {
        'username': username,
        'supportroom': supportroom,
        'signed_in_user': signed_in_user,
        'room_details': room_details,
        'profile_details': profile_details,
        'Logo': Logo,
        'Header': Header,
        'Dropdown': DropDown,
    })

def dynamic_css(request):
    background_objects = BackgroundImageBase.objects.filter(page='index').order_by("position")

    context = {
        'background_objects': background_objects,
    }

    return render(request, 'dynamic_css.css', context, content_type='text/css')

class CreatePostView(CreateView):
    model = BackgroundImage
    form_class = BackgroundImagery
    template_name = "backgroundimagechange.html"
    success_url = reverse_lazy("index")

class TermsAndConditionsView(BaseView):
    model = BackgroundImage
    form_class = EmailForm
    template_name = "termsandconditions.html"
    section = TextBase.section

class PolicyView(BaseView):
    model = BackgroundImage
    form_class = EmailForm
    template_name = "policy.html"
    section = TextBase.section

import urllib.request as url_request

def get_items_by_category(category):
    print(f"Filtering items by category: {category}")

    if category == 'all':
        items = Item.objects.all()
    elif category.lower() in ['gold', 'platinum', 'emerald', 'diamond']:
        items = Item.objects.filter(category=category[0].upper())
    else:
        items = Item.objects.none()

    return items


class EBackgroundView(BaseView, FormView):
    model = EBackgroundImage
    template_name = "ehome.html"
    form_class = EmailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = self.request.user
        total_items = Item.objects.filter(is_active=1).count()

        paginate_by = int(self.request.GET.get('paginate_by', settings.DEFAULT_PAGINATE_BY))

        items_query = Item.objects.filter(is_active=1).order_by('price')
        paginator = Paginator(items_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_items = paginator.get_page(page_number)
        if self.request.user.is_authenticated:
            active_order = (Order.objects.filter(user=self.request.user, ordered=False).prefetch_related('items').first())
            context['order'] = active_order

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Image'] = ImageBase.objects.filter(is_active=1, page=self.template_name)
        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(page=self.template_name,
                                                                                    is_active=1)
        context['Items'] = Item.objects.filter(is_active=1)
        context['Email'] = EmailField.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            try:
                instance = StoreViewType.objects.get(user=self.request.user, is_active=1)
            except StoreViewType.DoesNotExist:
                instance = None
            context['store_view_form'] = StoreViewTypeForm(instance=instance)
        else:
            context['store_view_form'] = StoreViewTypeForm()
        context['form'] = EmailForm()

        current_user = self.request.user
        if isinstance(current_user, AnonymousUser):
            context['store_view'] = 'stream'
            context['streamfilter_string'] = 'stream filter set by anonymous user'
            print('store view does not exist, setting to stream for anonymous user')
        else:
            try:
                user_store_view_type = StoreViewType.objects.get(user=current_user, is_active=1)
                context['store_view'] = user_store_view_type.type
                context['store_view_type_str'] = str(user_store_view_type)
                context['streamfilter_string'] = f'stream filter set by {self.request.user.username}'
                print('store view exists, ehome')
                print(str(user_store_view_type))
            except StoreViewType.DoesNotExist:
                context['store_view'] = 'stream'
                context['store_view_type_str'] = 'stream'
                context['streamfilter_string'] = f'stream filter set by {self.request.user.username}'
                print('store view does not exist, setting to stream for signed-in user')

        context['item_filters'] = ItemFilter.objects.filter(is_active=1)
        item_filters = ItemFilter.objects.filter(is_active=1)
        for item_filter in item_filters:
            print(str(item_filter))
        print(context)
        print('The item filters are:')
        items_query = Item.objects.filter(is_active=1)
        paginator = Paginator(items_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_items = paginator.get_page(page_number)

        context['items'] = paginated_items

        category = self.request.GET.get('category', 'all')
        categoryitems = self.get_items_by_category(category)
        context['categorizeditems'] = categoryitems
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)

        items = Item.objects.filter(is_active=1, price__isnull=False)
        total_price = sum(item.price for item in items)
        tax_price = total_price * Decimal('0.08')
        final_price = total_price + tax_price

        context['total_price'] = total_price  # match template name
        context['tax_price'] = tax_price
        context['final_price'] = final_price
        print(f"Total: {total_price}, Tax: {tax_price}, Final: {final_price}")

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def season_list(request):
        context = {
            'Season': Season.objects.filter(active=True),
        }
        return render(request, 'seasons.html', context)



    def get_items_by_category(self, category):
        if category == 'all':
            items = Item.objects.all()
        elif category == 'gold':
            items = Item.objects.filter(category='G')
        elif category == 'platinum':
            items = Item.objects.filter(category='P')
        elif category == 'emerald':
            items = Item.objects.filter(category='E')
        elif category == 'diamond':
            items = Item.objects.filter(category='D')
        else:
            items = Item.objects.all()
        return items

    def post(self, request, *args, **kwargs):
        if 'store_view_submit' in request.POST:
            if request.user.is_authenticated:
                try:
                    instance = StoreViewType.objects.get(user=request.user, is_active=1)
                except StoreViewType.DoesNotExist:
                    instance = None
                store_view_form = StoreViewTypeForm(request.POST, instance=instance)
                if store_view_form.is_valid():
                    store_view_form.instance.user = request.user
                    store_view_form.save()
                    messages.success(request, 'View type updated successfully.')
                    return redirect('ehome')
                else:
                    messages.error(request, 'Error updating view type.')
            else:
                messages.error(request, 'You must be logged in to update your view type.')

            context = self.get_context_data()
            context['store_view_form'] = store_view_form
            return render(request, self.template_name, context)

        form = EmailForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'EmailForm submitted successfully.')
            try:
                email = EmailField.objects.get(user=request.user)
                profile = ProfileDetails.objects.get(user=request.user)
                profile.email = email.email
                profile.save()
            except ProfileDetails.DoesNotExist:
                messages.error(request, 'Profile details not found.')
            except EmailField.DoesNotExist:
                print("EmailField does not exist.")
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
            try:
                email = EmailField.objects.get(user=request.user)
                user = request.user
                user.email = email.email
                user.save()
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
        else:
            messages.error(request, "EmailForm submission invalid")
            print("There was an error in registering the email")

        return render(request, self.template_name, self.get_context_data(form=form))


class StoreView(BaseView, FormView, ListView):
    model = StoreViewType
    template_name = "storeviewtypesnippet.html"
    form_class = StoreViewTypeForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        eform = StoreViewTypeForm(request=request)
        return render(request, 'storeviewtypesnippet.html', {'eform': eform, **context})

    def get_context_data(self, **kwargs):
        context = {}
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Image'] = ImageBase.objects.filter(is_active=1, page=self.template_name)
        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(page=self.template_name,
                                                                                    is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        eform = StoreViewTypeForm(request.POST, request=request)

        if eform.is_valid():
            post = eform.save(commit=False)
            post.save()
            return redirect('showcase:ehome')
        else:
            print('the errors with the ehomeviewtype form are ' + str(eform.errors))
        return render(request, 'storeviewtypesnippet.html', {'eform': eform})


class InventoreView(BaseView, FormView, ListView):
    model = StoreViewType
    template_name = "inventoryviewtypesnippet.html"
    form_class = StoreViewTypeForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        try:
            instance = StoreViewType.objects.get(user=request.user, is_active=1)
        except StoreViewType.DoesNotExist:
            instance = None

        store_view_form = StoreViewTypeForm(instance=instance, request=request)
        context['store_view_form'] = store_view_form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        eform = StoreViewTypeForm(request.POST, request=request)

        if eform.is_valid():
            post = eform.save(commit=False)
            post.save()
            return redirect('showcase:inventory')
        else:
            print('the errors with the inventoryviewtype form are ' + str(eform.errors))
        return render(request, 'inventoryviewtypesnippet.html', {'eform': eform})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Background': BackgroundImageBase.objects.filter(page=self.template_name).order_by("position"),
            'TextFielde': TextBase.objects.filter(page=self.template_name).order_by("section"),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Favicon': FaviconBase.objects.filter(is_active=1),
            'Image': ImageBase.objects.filter(is_active=1, page=self.template_name),
            'Social': SocialMedia.objects.filter(page=self.template_name, is_active=1),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
        })

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class ProfileTypeView(BaseView, FormView, ListView):
    model = StoreViewType
    template_name = "profileviewtypesnippet.html"
    form_class = ProfileViewTypeForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        try:
            instance = StoreViewType.objects.get(user=request.user, is_active=1)
        except StoreViewType.DoesNotExist:
            instance = None

        store_view_form = ProfileViewTypeForm(instance=instance, request=request)
        context['store_view_form'] = store_view_form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        eform = StoreViewTypeForm(request.POST, request=request)
        slug = request.POST.get('slug')
        try:
            profile = ProfileDetails.objects.get(pk=pk)
            if eform.is_valid():
                post = eform.save(commit=False)
                post.save()
                return redirect('showcase:profile', pk=profile.pk)
            else:
                print('the errors with the profileviewtypesnippet form are ' + str(eform.errors))

        except ProfileDetails.DoesNotExist:
            raise Http404("Game Room does not exist")
        return render(request, 'profileviewtypesnippet.html', {'eform': eform})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Background': BackgroundImageBase.objects.filter(page=self.template_name).order_by("position"),
            'TextFielde': TextBase.objects.filter(page=self.template_name).order_by("section"),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Favicon': FaviconBase.objects.filter(is_active=1),
            'Image': ImageBase.objects.filter(is_active=1, page=self.template_name),
            'Social': SocialMedia.objects.filter(page=self.template_name, is_active=1),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
        })

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class GameRoomTypeView(BaseView, FormView, ListView):
    model = StoreViewType
    template_name = "gameroomviewtypesnippet.html"
    form_class = StoreViewTypeForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        try:
            instance = StoreViewType.objects.get(user=request.user, is_active=1)
        except StoreViewType.DoesNotExist:
            instance = None

        store_view_form = ProfileViewTypeForm(instance=instance, request=request)
        context['store_view_form'] = store_view_form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        eform = StoreViewTypeForm(request.POST, request=request)
        slug = request.POST.get('slug')
        try:
            gameroom = GameHub.objects.get(slug=slug)
            if eform.is_valid():
                post = eform.save(commit=False)
                post.save()
                return redirect('showcase:gameroom', slug=gameroom.slug)
            else:
                print('the errors with the gameviewtypesnippet form are ' + str(eform.errors))

        except GameHub.DoesNotExist:
            raise Http404("Game Room does not exist")
        return render(request, 'gameroomviewtypesnippet.html', {'eform': eform})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Background': BackgroundImageBase.objects.filter(page=self.template_name).order_by("position"),
            'TextFielde': TextBase.objects.filter(page=self.template_name).order_by("section"),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Favicon': FaviconBase.objects.filter(is_active=1),
            'Image': ImageBase.objects.filter(is_active=1, page=self.template_name),
            'Social': SocialMedia.objects.filter(page=self.template_name, is_active=1),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
        })

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class CurrencyTypeView(BaseView, FormView, ListView):
    model = StoreViewType
    template_name = "currencyviewtypesnippet.html"
    form_class = StoreViewTypeForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        try:
            instance = StoreViewType.objects.get(user=request.user, is_active=1)
        except StoreViewType.DoesNotExist:
            instance = None

        context['store_view_form'] = StoreViewTypeForm(instance=instance, request=request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = StoreViewTypeForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('showcase:currencymarket')

        # on error, rebuild the full context and swap in the bound form
        context = self.get_context_data()
        context['store_view_form'] = form
        return render(request, self.template_name, context)

    def save(self, commit=True):
        user = self.request.user if self.request.user.is_authenticated else None
        storeviewtype = super().save(commit=False)
        if user and isinstance(user, User):
            storeviewtype.user = user
        else:
            storeviewtype.user = None
        if commit:
            storeviewtype.save()
        return storeviewtype

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Background': BackgroundImageBase.objects.filter(page=self.template_name).order_by("position"),
            'TextFielde': TextBase.objects.filter(page=self.template_name).order_by("section"),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Favicon': FaviconBase.objects.filter(is_active=1),
            'Image': ImageBase.objects.filter(is_active=1, page=self.template_name),
            'Social': SocialMedia.objects.filter(page=self.template_name, is_active=1),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
        })

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()
        context['store_view_form'] = StoreViewTypeForm()

        current_user = self.request.user
        if current_user.is_authenticated:
            try:
                store_view_instance = StoreViewType.objects.get(user=current_user, is_active=1)
                context['store_view'] = store_view_instance.type
                context['store_view_type_str'] = str(store_view_instance)
                context['streamfilter_string'] = f'stream filter set by {current_user.username}'
            except StoreViewType.DoesNotExist:
                store_view_instance = None
                context['store_view'] = 'stream'
                context['store_view_type_str'] = 'stream'
                context['streamfilter_string'] = f'stream filter set by {current_user.username}'
        else:
            store_view_instance = None
            context['store_view'] = 'stream'
            context['streamfilter_string'] = 'stream filter set by anonymous user'

        store_view_form = StoreViewTypeForm(instance=store_view_instance, request=self.request)
        context['store_view_form'] = store_view_form

        return context


class ECreatePostView(CreateView):
    model = EBackgroundImage
    form_class = EBackgroundImagery
    template_name = "ebackgroundimagechange.html"
    success_url = reverse_lazy("ehome")


class ShowcaseBackgroundView(BaseView):
    model = ShowcaseBackgroundImage
    template_name = "showcase.html"
    queryset = ShowcaseBackgroundImage.objects.all()

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})

        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "showcase.html", {'form': form})
            return redirect('showcase:showcase')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        return render(request, "showcase.html", {'form': form, **context})

    def get_queryset(self):
        return ShowcaseBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ShowcaseCreatePostView(CreateView):
    model = ShowcaseBackgroundImage
    form_class = ShowcaseBackgroundImagery
    template_name = "showcasebackgroundimagechange.html"
    success_url = reverse_lazy("showcase")

def forbidden_access(request):
    return render(request, 'forbiddenaccess.html')

class SupportLineBackgroundView(BaseView):
    model = SupportInterface
    template_name = "supportinterface.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ChatCreatePostView(CreateView):
    model = ChatBackgroundImage
    form_class = ChatBackgroundImagery
    template_name = "chatbackgroundimagechange.html"
    success_url = reverse_lazy("home")

class WhyBackgroundView(BaseView):
    model = WhyBackgroundImage
    template_name = "whydonate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class MemeHostView(BaseView):
    model = Meme
    template_name = "meme_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()

        newprofile = Meme.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class MemeView(FormMixin, ListView):
    model = Meme
    template_name = "create_meme.html"
    form_class = MemeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Profile'] = UpdateProfile.objects.all()
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = MemeForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:meme_list')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "create_meme.html", {'form': form})
        else:
            form = MemeForm()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "create_meme.html", {'form': form})

class BlogBackgroundView(ListView):
    model = BlogBackgroundImage
    template_name = "blog.html"

    queryset = Blog.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class BlogCreatePostView(CreateView):
    model = BlogBackgroundImage
    form_class = BlogBackgroundImagery
    template_name = "blogbackgroundimagechange.html"
    success_url = reverse_lazy("blog")

class PostBackgroundView(FormMixin, LoginRequiredMixin, ListView):
    model = UpdateProfile
    template_name = "post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:showcase')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "post_edit.html", {'form': form})

class PostCreatePostView(CreateView):
    model = PostBackgroundImage
    form_class = PostBackgroundImagery
    template_name = "postbackgroundimagechange.html"
    success_url = reverse_lazy("post_edit")

class BilletBackgroundView(BaseView):
    model = BilletBackgroundImage
    template_name = "billets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BilletBackgroundImage'] = BilletBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class BilletCreatePostView(CreateView):
    model = BilletBackgroundImage
    form_class = BilletBackgroundImagery
    template_name = "billetbackgroundimagechange.html"
    success_url = reverse_lazy("billets")


class RuleCreatePostView(CreateView):
    model = RuleBackgroundImage
    form_class = RuleBackgroundImagery
    template_name = "rulebackgroundimagechange.html"
    success_url = reverse_lazy("rules")


class AboutBackgroundView(BaseView):
    model = AboutBackgroundImage
    template_name = "about.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})

        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "about.html", {'form': form})
            return redirect('showcase:newsfeed')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        return render(request, "about.html", {'form': form, **context})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Image'] = ImageBase.objects.filter(is_active=1, page=self.template_name)
        context['Staff'] = StaffProfile.objects.filter(is_active=1).prefetch_related('socialmedia_set')

        newprofile = ProfileDetails.objects.filter(user__is_staff=True, is_active=1)
        context['Profiles'] = newprofile

        for profile in context['Profiles']:
            user = profile.user

            profile.newprofile_profile_picture_url = profile.avatar.url if profile.avatar else None
            profile.newprofile_profile_url = profile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class AboutCreatePostView(CreateView):
    model = AboutBackgroundImage
    form_class = AboutBackgroundImagery
    template_name = "aboutbackgroundimagechange.html"
    success_url = reverse_lazy("about")

class FaqBackgroundView(BaseView):
    model = FaqBackgroundImage
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['FaqBackgroundImage'] = FaqBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Faq'] = FrequentlyAskedQuestions.objects.all().order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class FaqCreatePostView(CreateView):
    model = FaqBackgroundImage
    form_class = FaqBackgroundImagery
    template_name = "faqbackgroundimagechange.html"
    success_url = reverse_lazy("faq")

class StaffBackgroundView(BaseView):
    model = BackgroundImage
    template_name = "staff.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class StaffCreatePostView(CreateView):
    model = StaffBackgroundImage
    form_class = StaffBackgroundImagery
    template_name = "staffbackgroundimagechange.html"
    success_url = reverse_lazy("staff")

class InformationBackgroundView(BaseView):
    InformationBackgroundImage
    template_name = "information.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class InformationCreatePostView(CreateView):
    model = InformationBackgroundImage
    form_class = InformationBackgroundImagery
    template_name = "Informationbackgroundimagechange.html"
    success_url = reverse_lazy("Information")

class TagBackgroundView(BaseView):
    model = TagBackgroundImage
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class TagCreatePostView(CreateView):
    model = TagBackgroundImage
    form_class = TagBackgroundImagery
    template_name = "tagbackgroundimagechange.html"
    success_url = reverse_lazy("tag")

class UserBackgroundView(BaseView):
    model = UserBackgroundImage
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['UserBackgroundImage'] = UserBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class UserCreatePostView(CreateView):
    model = UserBackgroundImage
    form_class = UserBackgroundImagery
    template_name = "userbackgroundimagechange.html"
    success_url = reverse_lazy("users")

class StaffRanksBackgroundView(BaseView):
    model = StaffRanksBackgroundImage
    template_name = "staffranks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['StaffRanksBackgroundImage'] = StaffRanksBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class StaffRanksCreatePostView(CreateView):
    model = StaffRanksBackgroundImage
    form_class = StaffRanksBackgroundImagery
    template_name = "staffranksbackgroundimagechange.html"
    success_url = reverse_lazy("staffranks")

class MegaBackgroundView(BaseView):
    model = MegaBackgroundImage
    template_name = "megacoins.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MegaCoinsBackgroundImage'] = MegaBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class MegaCreatePostView(CreateView):
    model = MegaBackgroundImage
    form_class = MegaBackgroundImagery
    template_name = "megacoinsbackgroundimagechange.html"
    success_url = reverse_lazy("megacoins")

class NewsBackgroundView(ListView):
    model = NewsBackgroundImage
    form_class = EmailForm
    template_name = "newsfeed.html"
    queryset = NewsBackgroundImage.objects.all()

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})

        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "newsfeed.html", {'form': form})
            return redirect('showcase:newsfeed')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        return render(request, "newsfeed.html", {'form': form, **context})

    def get_queryset(self):
        return NewsBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NewsBackgroundImage'] = NewsBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['News'] = NewsFeed.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1)
        context['Email'] = EmailField.objects.filter(is_active=1)

        newprofile = NewsFeed.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class NewsCreatePostView(CreateView):
    model = NewsBackgroundImage
    form_class = NewsBackgroundImagery
    template_name = "newsbackgroundimagechange.html"
    success_url = reverse_lazy("newsfeed")

class UploadACardView(FormMixin, LoginRequiredMixin, ListView):
    model = UploadACard
    template_name = "makeacard.html"
    form_class = UploadCardsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        form = UploadCardsForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:index')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "makeacard.html", {'form': form})

class DonorView(BaseView):
    model = DonorBackgroundImage
    template_name = "donors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)

        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            user = request.user
            print(user)
        else:

            user = None

        return super().dispatch(request, *args, user=user, **kwargs)

class ContributorBackgroundView(BaseView):
    model = ContributorBackgroundImage
    template_name = "contributors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ContentBackgroundView(BaseView):
    model = ContentBackgroundImage
    template_name = "morecontent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ContentBackgroundImage'] = ContentBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PartnerBackgroundView(BaseView):
    model = PartnerBackgroundImage
    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Partner'] = PartnerApplication.objects.all()

        newprofile = PartnerApplication.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ShareBackgroundView(BaseView):
    model = ShareBackgroundImage
    template_name = "share.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})

        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "share.html", {'form': form})
            return redirect('showcase:share')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        return render(request, "share.html", {'form': form, **context})

    def get_queryset(self):
        return ShareBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Ideas'] = Idea.objects.all()

        newprofile = Idea.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ConvertBackgroundView(BaseView):
    model = ConvertBackgroundImage
    template_name = "convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ReasonsBackgroundView(BaseView):
    model = ReasonsBackgroundImage
    template_name = "reasons-to-convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PerksBackgroundView(BaseView):
    model = PerksBackgroundImage
    template_name = "perks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.shortcuts import render

def home(request):
    events = [
        {
            'title': '春节晚会 Spring Festival Gala',
            'date': '2025-02-09',
            'location': 'Celestial Hall'
        },
        {
            'title': '中秋节 Mid-Autumn Festival',
            'date': '2025-09-13',
            'location': 'Moon Garden'
        },
        {
            'title': '文化展览 Cultural Exhibition',
            'date': '2025-03-15',
            'location': 'Ethereal Gallery'
        }
    ]
    return render(request, 'home.html', {'events': events})

from django.http import HttpRequest, JsonResponse
from django.views.generic import TemplateView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse
from django.views import View
from django.core import serializers

"""
def get_profile_url(message):
   return f"http://127.0.0.1:8000/profile/{message.signed_in_user_id}/"
"""
from django.http import JsonResponse

from django.shortcuts import get_object_or_404

def supportgetMessages(request, signed_in_user, **kwargs):

    if not request.user.is_authenticated:
        return JsonResponse({'messages': []})

    chat_room, created = SupportChat.objects.get_or_create(signed_in_user__username=signed_in_user, defaults={
        'signed_in_user': request.user,
    })

    if request.user != chat_room.signed_in_user and not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to access this chat room")

    messages = SupportMessage.objects.filter(room=chat_room)
    messages_data = []

    default_avatar = DefaultAvatar.objects.first()

    for message in messages:
        profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()

        avatar_url = (
            profile_details.avatar.url if profile_details and profile_details.avatar else
            serialize_default_avatar(default_avatar)['default_avatar_url']
        )
        user_profile_url = (
            profile_details.get_absolute_url() if profile_details else ""
        )

        messages_data.append({
            'user_profile_url': user_profile_url,
            'avatar_url': avatar_url,
            'user': str(message.signed_in_user) if message.signed_in_user else 'Support Request',
            'value': message.value,
            'date': message.date.strftime("%Y-%m-%d %H:%M:%S"),
        })

    return JsonResponse({'messages': messages_data})

"""def supportgetMessages(request, **kwargs):
   messages = SupportMessage.objects.filter(room=request.user.username)
   return JsonResponse({"messages": list(messages.values())})
"""

"""@login_required
def poste(request):
  if (request.method == "POST"):
      form = Postit(request.POST)
      if (form.is_valid()):
          post = form.save(commit=False)
          post.save()
          return redirect('showcase:users')
  else:
      form = Postit()
      return render(request, 'share.html', {'form': form})
      messages.error(
          request, 'Form submission failed to register, please try again.')
      messages.error(request, form.errors)"""

"""class PostBackgroundView(FormMixin, ListView):
   model = UpdateProfile
   template_name = "post_edit.html"
   form_class = PostForm

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
       context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
       context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
           "position")

       context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
       return context
"""

class PostView(FormMixin, ListView):
    model = PostBackgroundImage
    template_name = "ideas.html"
    form_class = Postit
    queryset = PostBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ShareBackgroundImage'] = ShareBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Idea'] = Idea.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = Postit(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:share')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "ideas.html", {'form': form})
        else:
            form = Postit()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "ideas.html", {'form': form})

"""@login_required
def post_new(request):
  if (request.method == "POST"):
      form = PostForm(request.POST)
      if (form.is_valid()):
          post = form.save(commit=False)
          post.save()
          return redirect('showcase:showcase')
          messages.success(request, 'Form submitted successfully.')
      else:
          messages.error(request, "Form submission invalid")
          return render(request, "post_edit.html", {'form': form})
  else:
      form = PostForm()
      return render(request, "post_edit.html", {'form': form})
      messages.error(
          request, 'Form submission failed to register, please try again.')
      messages.error(request, form.errors)"""

class Title(ListView):
    model = Titled

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        return render(context)

class DonateIconView(ListView):
    model = DonateIcon
    template_name = "donatebase.html"

class SupportBackgroundView(FormMixin, ListView):
    model = Support
    template_name = "support.html"
    form_class = SupportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SupportBackgroundImage'] = SupportBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Support'] = Support.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = SupportForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                print('works')
                messages.success(request, 'Form submitted successfully.')
                return HttpResponse('Support ticket generated')
                return redirect('showcase:showcase')
            else:
                messages.error(request, "Form submission invalid")
                return render(request, "support.html", {'form': form})
                return HttpResponse('Form submission invalid.')
        else:
            form = SupportForm()
            return render(request, "support.html", {'form': form})
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return HttpResponse('Form submission failed to register, please try again.')

class PostingView(FormMixin, ListView):
    model = UpdateProfile
    template_name = "post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Profile'] = UpdateProfile.objects.all()
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:showcase')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "post_edit.html", {'form': form})
        else:
            form = PostForm()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "post_edit.html", {'form': form})

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import PollQuestion

from django.shortcuts import render
from django.views import View
from .models import PollQuestion

class PollQuestionsView(View):
    template_name = "pollquestions.html"

    def get_context_data(self, **kwargs):
        context = {
            'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'PostBackgroundImage': PostBackgroundImage.objects.all(),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Logo': LogoBase.objects.filter(
                Q(page='navtrove.html') | Q(page=self.template_name),
                is_active=1
            ),
        }
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get(self, request, *args, **kwargs):

        latest_question_list = PollQuestion.objects.order_by('-pub_date')[:5]

        context = {
            'latest_question_list': latest_question_list,
            'object_list': latest_question_list
        }

        context.update(self.get_context_data())

        return render(request, self.template_name, context)

def polldetail(request, question_id):
    try:
        question = PollQuestion.objects.get(pk=question_id)
    except PollQuestion.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polldetail.html', {'question': question})

class PollDetailView(TemplateView):
    template_name = 'polldetail.html'

    def get_context_data(self, **kwargs):
        question_id = self.kwargs.get('question_id')
        question = get_object_or_404(PollQuestion, pk=question_id)

        context = {
            'question': question,
            'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'PostBackgroundImage': PostBackgroundImage.objects.all(),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Logo': LogoBase.objects.filter(
                Q(page='navtrove.html') | Q(page=self.template_name),
                is_active=1
            ),
        }
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PollResultsView(View):
    template_name = 'pollresults.html'

    def get(self, request, question_id):
        context = self.get_context_data(question_id)
        return render(request, self.template_name, context)

    def get_context_data(self, question_id):
        question = get_object_or_404(PollQuestion, pk=question_id)
        context = {
            'question': question,
            'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'PostBackgroundImage': PostBackgroundImage.objects.all(),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Logo': LogoBase.objects.filter(
                Q(page='navtrove.html') | Q(page=self.template_name),
                is_active=1
            ),
        }
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PollingView(View):
    model = Choice
    template_name = "pollvote.html"

    def post(self, request, *args, **kwargs):
        question_id = self.kwargs.get('question_id')
        question = get_object_or_404(PollQuestion, pk=question_id)

        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            error_message = "You did not select a choice."
            context = {
                'question': question,
                'error_message': error_message,
                'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
                    "position"),
                'PostBackgroundImage': PostBackgroundImage.objects.all(),
                'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
                'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
                'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
                'DropDown': NavBar.objects.filter(is_active=1).order_by('position')
            }
            return render(request, self.template_name, context)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('showcase:pollresults', args=(question.id,)))

class InventoryView(FormMixin, ListView):
    model = PrizePool
    template_name = "pokespinner.html"
    form_class = VoteQueryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['PrizePool'] = PrizePool.objects.all()
        context['Shuffle'] = Shuffler.objects.filter(is_active=1).order_by("category")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.db import transaction
from django.urls import reverse

@login_required
def inventory_view(request):
    inventory = Inventory.objects.get(user=request.user)
    number_of_cards = inventory.inventoryobject_set.filter(is_active=1).count()
    return render(request, 'inventory.html', {'number_of_cards': number_of_cards})

@method_decorator(login_required, name='dispatch')
def sse_total_value(request):
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    def event_stream():
        last_total = None
        while True:
            try:
                event = inventory_sse_queue.get(timeout=30)
            except queue.Empty:
                yield ":\n\n"
                continue

            if event == "changed":
                stock_objects = InventoryObject.objects.filter(is_active=1, user=request.user)
                total_value = stock_objects.aggregate(total=Sum('price'))['total'] or 0

                if total_value != last_total:
                    last_total = total_value
                    yield f"data: {total_value}\n\n"

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


class PlayerInventoryView(LoginRequiredMixin, FormMixin, ListView):
    model = InventoryObject
    template_name = "inventory.html"
    form_class = AddTradeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['store_view_form'] = StoreViewTypeForm()

        current_user = self.request.user
        if current_user.is_authenticated:
            try:
                store_view_instance = StoreViewType.objects.get(user=current_user, is_active=1)
                context['store_view'] = store_view_instance.type
                context['store_view_type_str'] = str(store_view_instance)
                context['streamfilter_string'] = f'stream filter set by {current_user.username}'
            except StoreViewType.DoesNotExist:
                store_view_instance = None
                context['store_view'] = 'stream'
                context['store_view_type_str'] = 'stream'
                context['streamfilter_string'] = f'stream filter set by {current_user.username}'
        else:
            store_view_instance = None
            context['store_view'] = 'stream'
            context['streamfilter_string'] = 'stream filter set by anonymous user'

        store_view_form = StoreViewTypeForm(instance=store_view_instance, request=self.request)
        context['store_view_form'] = store_view_form

        context['Stockpile'] = Inventory.objects.filter(is_active=1, user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        try:
            context['SentProfile'] = ProfileDetails.objects.get(user=self.request.user) #specifically used to get ruby amount
        except UserProfile.DoesNotExist:
            context['SentProfile'] = None

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['NewsProfiles'] = newprofile

        for newprofile in context['NewsProfiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:
            # Create a new object with the necessary attributes
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        context['Money'] = Currency.objects.filter(is_active=1)
        context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=self.request.user)
        context['TradeItems'] = TradeItem.objects.filter(is_active=1, user=self.request.user)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:
            # Create a new object with the necessary attributes
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        pk = kwargs.get('pk')

        try:
            inventory_object = InventoryObject.objects.get(pk=pk, user=request.user)
        except InventoryObject.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Inventory object not found'}, status=404)

        if action == 'sell':
            response = self.sell_inventory_object(request, pk)
        elif action == 'withdraw':
            response = self.withdraw_inventory_object(request, pk)
        elif action == 'move':
            print("Move action triggered")  # Debugging line
            response = self.move_to_trade(request, pk)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid action'}, status=400)

        # Update inventory count after performing the action
        inventory_object.inventory.update_inventory_count()
        updated_count = inventory_object.inventory.number_of_cards

        return response

    def withdraw_inventory_object(self, request, pk):
        inventory_object = get_object_or_404(InventoryObject, pk=pk)

        if inventory_object.user != request.user:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX check
                return JsonResponse({'success': False}, status=403)
            return redirect('showcase:inventory')

        inventory_object.user = None
        inventory_object.inventory = None
        inventory_object.save()

        user = request.user
        with transaction.atomic():
            withdraw = Withdraw.objects.filter(
                user=user, is_active=1, shipping_state='S', number_of_cards__lt=25
            ).first()

            if withdraw:
                withdraw.cards.add(inventory_object)
            else:
                withdraw = Withdraw.objects.create(user=user, is_active=1, shipping_state='S')
                withdraw.save()  # Save the object to generate an ID
                withdraw.cards.add(inventory_object)  # Add the InventoryObject

            withdraw.number_of_cards = withdraw.cards.count()
            withdraw.save()  # Update the number of cards

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            stock_count = InventoryObject.objects.filter(is_active=1, user=request.user).count()
            stock_count2 = InventoryObject.objects.filter(is_active=1, user=request.user).count()
            return JsonResponse({
                'success': True,
                'stock_count': stock_count,
                'stock_count2': stock_count2
            })
        return redirect('showcase:inventory')


    def sell_inventory_object(self, request, pk):
        inventory_object = get_object_or_404(InventoryObject, pk=pk)

        if inventory_object.user != request.user:
            return JsonResponse({'success': False}, status=403)

        total_value = inventory_object.price
        sold_value = 0  # Since only one item is being sold

        inventory_object.user = None
        inventory_object.inventory = None

        with transaction.atomic():
            Transaction.objects.create(
                inventory_object=inventory_object,
                user=request.user,
                currency=inventory_object.currency,
                amount=inventory_object.price
            )
            inventory_object.save()

            user_profile = get_object_or_404(ProfileDetails, user=request.user)
            user_profile.currency_amount += inventory_object.price
            user_profile.save()

        stock_count = InventoryObject.objects.filter(is_active=1, user=request.user).count()
        stock_count2 = InventoryObject.objects.filter(is_active=1, user=request.user).count()
        return JsonResponse({
            'success': True,
            'stock_count': stock_count,
            'stock_count2': stock_count2,
            'currency_amount': user_profile.currency_amount,
            'sold_value': sold_value,
        })


    def move_to_trade(self, request, pk):
        # Fetch the InventoryObject instance by primary key
        inventory_object = get_object_or_404(InventoryObject, pk=pk)

        # Check if the user owns the inventory object
        if inventory_object.user != request.user:
            messages.error(request, 'You cannot trade items you do not own!')
            return redirect('showcase:inventory')

        user = request.user

        # Use a transaction to ensure atomicity
        with transaction.atomic():
            # Create a new TradeItem instance
            tradeitem = TradeItem.objects.create(
                user=user,
                title=inventory_object.choice_text or inventory_object.choice.text,  # Use choice_text if set
                inventoryobject=inventory_object,  # Save reference to the InventoryObject
                category=inventory_object.category,
                is_active=1,
                currency=inventory_object.currency,
                value=inventory_object.price,
                condition=inventory_object.condition,
                image=inventory_object.image,
                image_length=inventory_object.image_length,
                image_width=inventory_object.image_width,
                length_for_resize=inventory_object.length_for_resize,
                width_for_resize=inventory_object.width_for_resize,
                description=f"Automatically moved to trade by {user.username}"  # Example description
            )

            # Delete the inventory object after creating the trade item
            inventory_object.delete()

            # Redirect to the trade inventory page
            return redirect('showcase:tradeinventory')

@csrf_exempt
def withdraw_cost(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            withdraw_id = data.get("withdraw_id")
            if not withdraw_id:
                return JsonResponse({"success": False, "error": "Withdraw ID not provided."})

            withdraw = get_object_or_404(Withdraw, pk=withdraw_id)

            cost = withdraw.fees

            profile = ProfileDetails.objects.filter(user=request.user).first()
            if not profile:
                return JsonResponse({"success": False, "error": "User profile not found."})

            if profile.currency_amount < cost:
                return JsonResponse({"success": False, "error": "Insufficient currency."})

            profile.currency_amount -= cost
            profile.save()

            return JsonResponse({
                "success": True,
                "message": f"Withdraw charged {cost} {profile.currency.name}",
                "updated_currency_amount": profile.currency_amount,
                "currency_name": profile.currency.name
            })

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON."})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method."})


@method_decorator(login_required, name='dispatch')
class SellAllInventoryObjectsView(View):
    def post(self, request, *args, **kwargs):
        selected_ids_str = request.POST.get('selected_ids', '')
        if not selected_ids_str:
            return JsonResponse({'success': False, 'error': 'No inventory objects selected'}, status=400)

        try:
            selected_ids = [int(pk.strip()) for pk in selected_ids_str.split(',') if pk.strip()]
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid inventory IDs provided'}, status=400)

        inventory_objects = InventoryObject.objects.filter(pk__in=selected_ids, user=request.user)
        if not inventory_objects.exists():

            updated_inventory_html = render_to_string(
                "inventory_items.html",
                {"StockObject": InventoryObject.objects.filter(is_active=1, user=request.user)},
                request=request
            )
            return JsonResponse({
                'success': True,
                'stock_count': 0,
                'stock_count2': 0,
                'currency_amount': get_object_or_404(ProfileDetails, user=request.user).currency_amount,
                'inventory_html': updated_inventory_html
            })

        total_value = 0
        with transaction.atomic():
            for inventory_object in inventory_objects:
                total_value += inventory_object.price
                inventory_object.user = None
                inventory_object.inventory = None
                Transaction.objects.create(
                    inventory_object=inventory_object,
                    user=request.user,
                    currency=inventory_object.currency,
                    amount=inventory_object.price
                )
                inventory_object.save()

            user_profile = get_object_or_404(ProfileDetails, user=request.user)
            user_profile.currency_amount += total_value
            user_profile.save()

        stock_count = InventoryObject.objects.filter(is_active=1, user=request.user).count()
        stock_count2 = InventoryObject.objects.filter(is_active=1, user=request.user).count()
        updated_inventory_html = render_to_string(
            "inventory_items.html",
            {"StockObject": InventoryObject.objects.filter(is_active=1, user=request.user)},
            request=request
        )
        return JsonResponse({
            'success': True,
            'stock_count': stock_count,
            'stock_count2': stock_count2,
            'currency_amount': user_profile.currency_amount,
            'inventory_html': updated_inventory_html
        })

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from .models import InventoryObject, Transaction, ProfileDetails

@method_decorator(login_required, name='dispatch')
class SellEverythingInventoryObjectsView(View):
    def post(self, request, *args, **kwargs):
        try:
            inventory_objects = InventoryObject.objects.filter(is_active=True, user=request.user)
            if not inventory_objects.exists():
                return JsonResponse({'success': False, 'error': 'No inventory objects available to sell'}, status=400)

            total_value = sum(item.price for item in inventory_objects)

            user_profile = get_object_or_404(ProfileDetails, user=request.user)

            with transaction.atomic():
                for inventory_object in inventory_objects:
                    inventory_object.is_active = False
                    inventory_object.save()
                    Transaction.objects.create(
                        inventory_object=inventory_object,
                        user=request.user,
                        currency=inventory_object.currency,
                        amount=inventory_object.price
                    )
                user_profile.currency_amount += total_value
                user_profile.save()

            stock_objects = InventoryObject.objects.filter(is_active=True, user=request.user)
            stock_count = stock_objects.count()
            inventory_html = render_to_string(
                "inventory_items.html",
                {"StockObject": stock_objects},
                request=request
            )

            return JsonResponse({
                'success': True,
                'stock_count': stock_count,
                'currency_amount': user_profile.currency_amount,
                'total_value': total_value,
                'inventory_html': inventory_html,
            })
        except Http404:
            return JsonResponse({'success': False, 'error': 'User profile not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)


@csrf_exempt
def create_inventory_object(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            button_id = data.get('buttonId')

            inventory = None
            if button_id == "start":
                inventory = Inventory.objects.get(user=request.user)
            print("Received payload:", data)
        except Inventory.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'No inventory found for the user!'}, status=400)

        choice_id = data.get('choice_id')
        choice_value = data.get('choice_value')

        try:
            choice = Choice.objects.get(id=choice_id) if choice_id else None
        except Choice.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid choice!'}, status=400)

        try:
            with transaction.atomic():
                inventory_object = InventoryObject(
                    user=request.user if button_id == "start" else None,
                    inventory=inventory if button_id == "start" else None,
                    choice=choice,
                    choice_text=choice.choice_text if choice else "Default Choice",
                    category=data.get('category', 'default'),
                    currency=Currency.objects.first(),
                    price=data.get('price', 0),
                    condition=data.get('condition', 'M'),
                    quantity=data.get('quantity', 1),
                )
                inventory_object.save()
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

        response_data = {
            'status': 'success',
            'message': 'Inventory object created successfully!',
            'button_id': button_id,
            'inventory_object_id': inventory_object.id
        }
        return JsonResponse(response_data)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)


@csrf_exempt
def delete_inventory_object(request, object_id):
    if request.method == 'DELETE':
        try:
            inventory_object = InventoryObject.objects.get(id=object_id, user__isnull=True)
            inventory_object.delete()
            return JsonResponse({'success': True, 'message': 'Temporary inventory object deleted!'})
        except InventoryObject.DoesNotExist:
            return JsonResponse({'error': 'Inventory object not found!'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


class CreateChestView(FormView):
    template_name = "create_chest.html"
    form_class = InventoryGameForm

    def get_game_instance(self):
        """
        Returns a Game instance. If a game_id is provided in the URL kwargs,
        return the corresponding Game, otherwise return a new instance.
        """
        game_id = self.kwargs.get('game_id')
        if game_id:
            return get_object_or_404(Game, id=game_id)
        return Game()

    def form_valid(self, form):
        game_form = InventoryGameForm(self.request.POST, self.request.FILES, instance=self.get_game_instance())
        choice_formset = ChoiceFormSet(self.request.POST, self.request.FILES)

        if game_form.is_valid() and choice_formset.is_valid():
            game = game_form.save()
            print('saved game instance here')

            choices = choice_formset.save(commit=False)
            for choice in choices:
                choice.save()
            game.choices.set(choices)

            return redirect('showcase:game', pk=game.pk)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.get_game_instance()

        if self.request.method == 'POST':
            game_form = InventoryGameForm(self.request.POST, self.request.FILES, instance=game)
            choice_formset = ChoiceFormSet(self.request.POST, self.request.FILES)
        else:
            game_form = InventoryGameForm(instance=game)

            choices_queryset = Choice.objects.all()

            if game.pk:
                selected_choices = game.choices.all()
            else:
                selected_choices = []

            initial_data = [
                {'selected': choice in selected_choices}
                for choice in choices_queryset
            ]

            choice_formset = ChoiceFormSet(
                queryset=choices_queryset,
                initial=initial_data
            )

        context.update({
            'game_form': game_form,
            'choice_formset': choice_formset,
            'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'PostBackgroundImage': PostBackgroundImage.objects.all(),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'PrizePool': PrizePool.objects.all(),
            'Shuffle': Shuffler.objects.filter(is_active=1).order_by("category"),
        })

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:
            dummy_profile = type('Dummy', (), {})()
            dummy_profile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            dummy_profile.newprofile_profile_url = None
            context['NewsProfiles'] = dummy_profile
        else:
            for profile in context['NewsProfiles']:
                user = profile.user
                prof = ProfileDetails.objects.filter(user=user).first()
                if prof:
                    profile.newprofile_profile_picture_url = prof.avatar.url
                    profile.newprofile_profile_url = profile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        game = self.get_game_instance()
        game_form = InventoryGameForm(request.POST, request.FILES, instance=game)
        choice_formset = ChoiceFormSet(request.POST, request.FILES)

        if game_form.is_valid() and choice_formset.is_valid():
            saved_game = game_form.save()
            print('saved the game here')
            choices = choice_formset.save(commit=False)
            print('the choices are' + str(choices))
            for choice in choices:
                choice.game = game
                choice.save()
                print(choice)
            saved_game.choices.set(choices)
            return redirect('showcase:game', slug=saved_game.slug)
        else:
            print("game_form errors:", game_form.errors)
            print("choice_formset errors:", choice_formset.errors)
            return self.render_to_response(self.get_context_data(game_form=game_form,
                                                                 choice_formset=choice_formset))

from django.shortcuts import render
from .models import Card

def card_list(request):
    supertype = request.GET.get('supertype')
    type = request.GET.get('type')
    view = request.GET.get('view', 'compact')

    cards = Card.objects.all()
    if supertype:
        cards = cards.filter(supertype=supertype)
    if type:
        cards = cards.filter(types__contains=type)

    sort_by = request.GET.get('sort_by', 'name')
    sort_order = request.GET.get('sort_order', 'asc')
    if sort_order == 'desc':
        sort_by = f'-{sort_by}'

    cards = cards.order_by(sort_by)

    return render(request, 'card_list.html', {'cards': cards, 'view': view})

class DirectChestView(BaseView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['slug'] = slug

        game = get_object_or_404(Game, slug=slug)
        context['game'] = game

        user = self.request.user
        if user.is_authenticated:
            try:
                context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
            except UserProfile.DoesNotExist:
                context['SentProfile'] = None
        else:
            context['SentProfile'] = None

        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['wager_form'] = WagerForm()

        choices = Choice.objects.filter(game=game)
        spinner_choice_renders = SpinnerChoiceRenders.objects.filter(game=game)
        context['spinner_choice_renders'] = spinner_choice_renders

        user = self.request.user
        if user.is_authenticated:
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                effective_cost = game.get_effective_cost()
                spin_multiplier = 1
                total_cost = effective_cost * spin_multiplier
                context['user_cash'] = profile.currency_amount
                context['total_cost'] = total_cost
            else:
                context['user_cash'] = None
                context['total_cost'] = None
        else:
            context['user_cash'] = None
            context['total_cost'] = None

        button_type = self.request.GET.get('button_type') or self.request.POST.get('button_type')

        cost = game.discount_cost if game.discount_cost else game.cost

        context.update({
            'cost_threshold_80': cost * 0.8,
            'cost_threshold_100': cost,
            'cost_threshold_200': cost * 2,
            'cost_threshold_500': cost * 5,
            'cost_threshold_10000': cost * 100,
        })

        newprofile = UpdateProfile.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        user_profile = None
        if game.user:
            user_profile, created = UserProfile.objects.get_or_create(user=game.user)

        context['SentProfile'] = user_profile
        if game.user:
            user_cash = user_profile.currency_amount

            context = {
                'user_cash': user_cash,
            }

        context['Money'] = Currency.objects.filter(is_active=1).first()

        spinpreference = None

        if user.is_authenticated:
            try:
                spinpreference = SpinPreference.objects.get(user=user)
            except SpinPreference.DoesNotExist:
                spinpreference = SpinPreference(user=user, quick_spin=False)
                spinpreference.save()

            context['quick_spin'] = spinpreference.quick_spin
        else:
            context['quick_spin'] = False

        context['spinpreference'] = spinpreference

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if spinpreference:
            spinform = SpinPreferenceForm(instance=spinpreference)
        else:
            spinform = SpinPreferenceForm()
        context['spin_preference_form'] = spinform

        if user.is_authenticated:
            if spinpreference.quick_spin:
                random_amount = random.randint(500, 1000)
            else:
                random_amount = random.randint(150, 300)
        else:
            random_amount = random.randint(150, 300)

        context['random_amount'] = random_amount
        context['range_random_amount'] = range(random_amount)
        print(str('the random amount is ') + str(random_amount))

        random_amount = random.randint(150, 300)
        random_nonces = [random.randint(0, 1000000) for _ in range(random_amount)]
        context['random_nonces'] = random_nonces

        game_id = self.kwargs.get('slug')

        game = get_object_or_404(Game, slug=slug)

        context['game'] = game

        inline_choices = game.choice_fk_set.all()
        m2m_choices = game.choices.all()
        combined_choices = {choice.pk: choice for choice in list(inline_choices) + list(m2m_choices)}

        through_qs = GameChoice.objects.filter(game=game).select_related('choice')
        through_data = {}
        for gc in through_qs:
            choice = gc.choice
            through_data[choice.pk] = {
                'choice': choice,
                'lower_nonce': gc.lower_nonce if gc.lower_nonce is not None else choice.lower_nonce,
                'upper_nonce': gc.upper_nonce if gc.upper_nonce is not None else choice.upper_nonce,
                'value': gc.value if gc.value is not None else choice.value,
                'rarity': gc.rarity if gc.rarity is not None else choice.rarity,
                'file_url': choice.file.url if choice.file else '',
                'category': choice.category if choice.category else '',
                'currency': {
                    'symbol': choice.currency.name if choice.currency else '💎',
                    'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                }
            }

        all_choices = []
        for pk, choice in combined_choices.items():
            nonce_info = through_data.get(pk, {
                'choice': choice,
                'lower_nonce': choice.lower_nonce,
                'upper_nonce': choice.upper_nonce,
                'value': choice.value,
                'rarity': choice.rarity,
                'file_url': choice.file.url if choice.file else '',
                'category': choice.category if choice.category else '',
                'currency': {
                    'symbol': choice.currency.name if choice.currency else '💎',
                    'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                }
            })

            all_choices.append({
                'choice': choice,
                'choice_text': choice.choice_text,
                'lower_nonce': nonce_info['lower_nonce'],
                'upper_nonce': nonce_info['upper_nonce'],
                'value': nonce_info['value'],
                'rarity': nonce_info['rarity'],
                'file_url': nonce_info['file_url'],
                'category': nonce_info['category'],
                'currency': nonce_info['currency'],
                'image_width': getattr(choice, 'image_width', None),
                'image_length': getattr(choice, 'image_length', None),
                'get_color_display': getattr(choice, 'get_color_display', lambda: ''),
                'get_tier_display': getattr(choice, 'get_tier_display', lambda: ''),
            })

        context['choices'] = all_choices

        choices_with_nonce = []
        for nonce in random_nonces:
            for choice_data in all_choices:
                lower = choice_data['lower_nonce']
                upper = choice_data['upper_nonce']
                if lower is not None and upper is not None and lower <= nonce <= upper:
                    choices_with_nonce.append({
                        'choice': choice_data['choice'],
                        'nonce': nonce,
                        'lower_nonce': lower,
                        'upper_nonce': upper,
                        'rarity': choice_data['rarity'],
                        'file_url': choice_data['file_url'],
                        'currency': choice_data['currency']
                    })
                    break

        context['choices_with_nonce'] = choices_with_nonce

        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        print(context['Background'])

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def game_detail(request, slug):
        game = get_object_or_404(Game, slug=slug)
        choices = game.choices.all()
        return render(request, 'game_detail.html', {'game': game, 'choices': choices})

    def display_choices(request, game_id, slug):
        game = get_object_or_404(Game, id=game_id, slug=slug)
        choices = Choice.objects.filter(game=game)

        for choice in choices:
            if choice.lower_nonce is None or choice.upper_nonce is None:
                choice.lower_nonce = random.randint(0, 1000000)
                choice.upper_nonce = random.randint(0, 1000000)
                choice.save()

        return render(request, 'game.html', {'game': game, 'choices': choices})

    def take_spinner_slot(user, game, choice):
        SpinnerChoiceRenders.take_up_slot(user=user, game=game, choice=choice, value=100, ratio=2, type=game.type,
                                          image=choice.image.url, color=choice.color)

    def post(self, request, *args, **kwargs):
        if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            quick_spin = request.POST.get('quick_spin') == 'true'
            spinpreference, created = SpinPreference.objects.get_or_create(user=request.user)
            spinpreference.quick_spin = quick_spin
            spinpreference.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)

    def create_spinner_choice_render_automatically(request):
        nonce = random.randint(0, 1000000)
        choice = Choice.objects.filter(Q(lower_nonce__lte=nonce) & Q(upper_nonce__gte=nonce)).first()

        if choice:
            game = choice.game
            game_hub = GameHub.objects.first()

            spinner_choice_render = SpinnerChoiceRenders.objects.create(
                user=choice.user,
                value=choice.value,
                ratio=choice.rarity,
                type=game_hub,
                image=choice.file,
                color=choice.color,
                game=game,
                choice=choice,
                nonce=nonce,
                is_active=1,
            )
            return redirect('showcase:game', slug=choice.slug)
        else:
            return render(request, 'error.html', {'message': 'No choice found for the generated nonce'})

    def spinner_choice_render_list(request):
        spinner_choice_renders = SpinnerChoiceRenders.objects.filter(game=self.game)
        return render(request, 'game.html', {'spinner_choice_renders': spinner_choice_renders})

    @csrf_exempt
    def layoutspinner(request, slug):
        if request.method == 'POST':
            game_id = request.POST.get('game_id')
            user = request.user

            if not game_id:
                return JsonResponse({'status': 'error', 'message': 'Game ID is required.'})

            try:
                game = Game.objects.get(id=game_id, slug=slug)
                nonce = random.randint(1, 1000000)
                choices = Choice.objects.filter(lower_nonce__lte=nonce, upper_nonce__gte=nonce)

                if not choices.exists():
                    return JsonResponse({'status': 'error', 'message': 'No valid choice found for the given nonce.'})

                choice = choices.order_by('?').first()

                outcome = Outcome.objects.create(
                    user=user,
                    game=game,
                    choice=choice,
                    nonce=nonce,
                    value=random.randint(1, 1000000),
                    ratio=random.randint(1, 10),
                    type=game.type
                )
                return JsonResponse({'status': 'success', 'outcome': outcome.id, 'nonce': outcome.nonce})
            except Game.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Game not found.'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


class GameChestBackgroundView(BaseView):
    template_name = "game.html"
    print("Debug: Received POST data:")

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        pk = kwargs.get('pk')

        try:
            inventory_object = InventoryObject.objects.get(pk=pk, user=request.user)
        except InventoryObject.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Inventory object not found'}, status=404)

        if action == 'sell':
            print('point-blank sell action called')
            response = self.sell_inventory_object(request, pk)
            return response
        return JsonResponse({'error': 'Invalid action'}, status=400)

    @csrf_exempt
    def sell_game_inventory_object(request, pk):
        if request.method != "POST":
            return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

        inventory_object = get_object_or_404(InventoryObject, pk=pk)

        if inventory_object.user != request.user:
            return JsonResponse({'success': False, 'message': 'Unauthorized'}, status=403)

        try:

            data = json.loads(request.body)
            items = data.get("items", [])

            if not items:
                return JsonResponse({'success': False, 'message': 'No items provided'}, status=400)

            total_sale_value = sum(float(item["price"]) for item in items if "price" in item)

            django.db.close_old_connections()
            with transaction.atomic():
                for item in items:
                    item_pk = item.get("inventory_pk")
                    item_inventory = get_object_or_404(InventoryObject, pk=item_pk)

                    item_inventory.user = None
                    item_inventory.inventory = None
                    item_inventory.save()

                    Transaction.objects.create(
                        inventory_object=item_inventory,
                        user=request.user,
                        currency=item.get("currencySymbol", ""),
                        amount=float(item.get("price", 0))
                    )

                user_profile = get_object_or_404(ProfileDetails, user=request.user)
                user_profile.currency_amount += total_sale_value
                user_profile.save()

            stock_count = InventoryObject.objects.filter(is_active=1, user=request.user).count()
            stock_count2 = InventoryObject.objects.filter(is_active=1, user=request.user).count()

            return JsonResponse({
                'success': True,
                'stock_count': stock_count,
                'stock_count2': stock_count2,
                'currency_amount': user_profile.currency_amount,
                'message': f"Sold {len(items)} items for {total_sale_value} currency."
            })

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['slug'] = slug

        game = get_object_or_404(Game, slug=slug)
        context['game'] = game

        context['tophit'] = TopHits.objects.filter(game=game, is_active=True).order_by('-mfg_date')[:8]
        user = self.request.user
        if user.is_authenticated:
            preference_instance = MyPreferences.objects.filter(user=user).first()
            if preference_instance:
                context['preferenceform'] = MyPreferencesForm(instance=preference_instance, user=user)
                context['preference_instance'] = preference_instance
                context['is_signed_in'] = user.is_authenticated
                context['has_preference'] = preference_instance is not None
                context['preference_value'] = preference_instance.spintype if preference_instance else None
            else:
                context['preferenceform'] = MyPreferencesForm(user=user)
                context['preference_instance'] = None
            try:
                context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
            except UserProfile.DoesNotExist:
                context['SentProfile'] = None
        else:
            context['SentProfile'] = None
            context['preferenceform'] = MyPreferencesForm()

        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['wager_form'] = WagerForm()

        choices = Choice.objects.filter(game=game)
        spinner_choice_renders = SpinnerChoiceRenders.objects.filter(game=game)
        context['spinner_choice_renders'] = spinner_choice_renders

        user = self.request.user
        if user.is_authenticated:
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                effective_cost = game.get_effective_cost()
                spin_multiplier = 1
                total_cost = effective_cost * spin_multiplier
                context['user_cash'] = profile.currency_amount
                context['total_cost'] = total_cost
            else:
                context['user_cash'] = None
                context['total_cost'] = None
        else:
            context['user_cash'] = None
            context['total_cost'] = None

        button_type = self.request.GET.get('button_type') or self.request.POST.get('button_type')

        if button_type == "start2":
            cost = 0
        else:
            cost = game.discount_cost if game.discount_cost else game.cost

        context.update({
            'cost_threshold_80': cost * 0.8,
            'cost_threshold_100': cost,
            'cost_threshold_200': cost * 2,
            'cost_threshold_500': cost * 5,
            'cost_threshold_10000': cost * 100,
        })

        newprofile = UpdateProfile.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        user_profile = None
        if game.user:
            user_profile, created = UserProfile.objects.get_or_create(user=game.user)

        context['SentProfile'] = user_profile
        if game.user:
            user_cash = user_profile.currency_amount

            context = {
                'user_cash': user_cash,
            }

        context['Money'] = Currency.objects.filter(is_active=1).first()

        spinpreference = None

        if user.is_authenticated:
            try:
                spinpreference = SpinPreference.objects.get(user=user)
            except SpinPreference.DoesNotExist:
                spinpreference = SpinPreference(user=user, quick_spin=False)
                spinpreference.save()

            context['quick_spin'] = spinpreference.quick_spin
        else:
            context['quick_spin'] = False

        context['spinpreference'] = spinpreference

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if spinpreference:
            spinform = SpinPreferenceForm(instance=spinpreference)
        else:
            spinform = SpinPreferenceForm()
        context['spin_preference_form'] = spinform

        if user.is_authenticated:
            if spinpreference.quick_spin:
                random_amount = random.randint(500, 1000)
            else:
                random_amount = random.randint(150, 300)
        else:
            random_amount = random.randint(150, 300)

        context['random_amount'] = random_amount
        context['range_random_amount'] = range(random_amount)
        print(str('the random amount is ') + str(random_amount))

        random_amount = random.randint(150, 300)
        random_nonces = [random.randint(0, 1000000) for _ in range(random_amount)]
        context['random_nonces'] = random_nonces

        game_id = self.kwargs.get('slug')

        game = get_object_or_404(Game, slug=slug)

        context['game'] = game

        inline_choices = game.choice_fk_set.all()
        m2m_choices = game.choices.all()
        combined_choices = {choice.pk: choice for choice in list(inline_choices) + list(m2m_choices)}

        through_qs = GameChoice.objects.filter(game=game).select_related('choice')
        through_data = {}
        for gc in through_qs:
            choice = gc.choice
            through_data[choice.pk] = {
                'choice': choice,
                'lower_nonce': gc.lower_nonce if gc.lower_nonce is not None else choice.lower_nonce,
                'upper_nonce': gc.upper_nonce if gc.upper_nonce is not None else choice.upper_nonce,
                'value': gc.value if gc.value is not None else choice.value,
                'rarity': gc.rarity if gc.rarity is not None else choice.rarity,
                'file_url': choice.file.url if choice.file else '',
                'category': choice.category if choice.category else '',
                'currency': {
                    'symbol': choice.currency.name if choice.currency else '💎',
                    'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                }
            }

        all_choices = []
        for pk, choice in combined_choices.items():
            nonce_info = through_data.get(pk, {
                'choice': choice,
                'lower_nonce': choice.lower_nonce,
                'upper_nonce': choice.upper_nonce,
                'value': choice.value,
                'rarity': choice.rarity,
                'file_url': choice.file.url if choice.file else '',
                'category': choice.category if choice.category else '',
                'currency': {
                    'symbol': choice.currency.name if choice.currency else '💎',
                    'file_url': choice.currency.file.url if choice.currency and choice.currency.file else None
                }
            })

            all_choices.append({
                'choice': choice,
                'choice_text': choice.choice_text,
                'lower_nonce': nonce_info['lower_nonce'],
                'upper_nonce': nonce_info['upper_nonce'],
                'value': nonce_info['value'],
                'rarity': nonce_info['rarity'],
                'file_url': nonce_info['file_url'],
                'category': nonce_info['category'],
                'currency': nonce_info['currency'],
                'image_width': getattr(choice, 'image_width', None),
                'image_length': getattr(choice, 'image_length', None),
                'get_color_display': getattr(choice, 'get_color_display', lambda: ''),
                'get_tier_display': getattr(choice, 'get_tier_display', lambda: ''),
            })

        context['choices'] = all_choices

        choices_with_nonce = []
        for nonce in random_nonces:
            for choice_data in all_choices:
                lower = choice_data['lower_nonce']
                upper = choice_data['upper_nonce']
                if lower is not None and upper is not None and lower <= nonce <= upper:
                    choices_with_nonce.append({
                        'choice': choice_data['choice'],
                        'nonce': nonce,
                        'lower_nonce': lower,
                        'upper_nonce': upper,
                        'rarity': choice_data['rarity'],
                        'file_url': choice_data['file_url'],
                        'currency': choice_data['currency']
                    })
                    break

        context['choices_with_nonce'] = choices_with_nonce

        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        print(context['Background'])

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        action = self.request.POST.get('action')
        pk = self.request.POST.get('pk')

        if action == 'sell':
            print('direct sell called in the GameChestBackgroundView')
            return self.sell_game_inventory_object(request)

    def game_detail(request, slug):
        game = get_object_or_404(Game, slug=slug)
        choices = game.choices.all()
        return render(request, 'game_detail.html', {'game': game, 'choices': choices})

    def display_choices(request, game_id, slug):
        game = get_object_or_404(Game, id=game_id, slug=slug)
        choices = Choice.objects.filter(game=game)

        for choice in choices:
            if choice.lower_nonce is None or choice.upper_nonce is None:
                choice.lower_nonce = random.randint(0, 1000000)
                choice.upper_nonce = random.randint(0, 1000000)
                choice.save()

        return render(request, 'game.html', {'game': game, 'choices': choices})

    def take_spinner_slot(user, game, choice):
        SpinnerChoiceRenders.take_up_slot(user=user, game=game, choice=choice, value=100, ratio=2, type=game.type,
                                          image=choice.image.url, color=choice.color)

    def save_spin_preference(request):
        if request.method == "POST" and request.is_ajax():
            quick_spin = request.POST.get('quick_spin') == 'true'
            spinpreference, created = SpinPreference.objects.get_or_create(user=request.user)
            spinpreference.quick_spin = quick_spin
            spinpreference.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)

    def wager(self, request, *args, **kwargs):
        form = WagerForm(request.POST, user_profile=request.user.user_profile)
        if form.is_valid():
            wager = form.save(commit=False)
            wager.user_profile = request.user.user_profile
            wager.save()
            return redirect('showcase:blackjack')
        else:
            return self.get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            quick_spin = request.POST.get('quick_spin') == 'true'
            spinpreference, created = SpinPreference.objects.get_or_create(user=request.user)
            spinpreference.quick_spin = quick_spin
            spinpreference.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)

    def create_spinner_choice_render_automatically(request):
        nonce = random.randint(0, 1000000)
        choice = Choice.objects.filter(Q(lower_nonce__lte=nonce) & Q(upper_nonce__gte=nonce)).first()

        if choice:
            game = choice.game
            game_hub = GameHub.objects.first()

            spinner_choice_render = SpinnerChoiceRenders.objects.create(
                user=choice.user,
                value=choice.value,
                ratio=choice.rarity,
                type=game_hub,
                image=choice.file,
                color=choice.color,
                game=game,
                choice=choice,
                nonce=nonce,
                is_active=1,
            )
            return redirect('showcase:game', slug=choice.slug)
        else:
            return render(request, 'error.html', {'message': 'No choice found for the generated nonce'})

class CreateInventoryChestView(FormView):
    template_name = "inventory_create_chest.html"
    form_class = PlayerInventoryGameForm
    success_url = reverse_lazy('showcase:game')

    def form_valid(self, form):
        game = form.save(commit=False)
        game.user = self.request.user
        game.save()

        game.items.set(form.cleaned_data['items'])

        for prize_id, field_name in form.quantity_fields.items():
            quantity = self.request.POST.get(field_name)
            if quantity:
                prize = PrizePool.objects.get(id=prize_id)
                print(f"Prize: {prize.prize_name}, Quantity: {quantity}")

        return super().form_valid(form)

def move_to_trading(self, **kwargs):
    valid_fields = {
        'title': kwargs.get('title'),
        'fees': kwargs.get('fees'),
        'category': kwargs.get('category'),
        'specialty': kwargs.get('specialty'),
        'condition': kwargs.get('condition'),
        'label': kwargs.get('label'),
        'slug': kwargs.get('slug'),
        'value': kwargs.get('value'),
        'description': kwargs.get('description'),
        'image': kwargs.get('image'),
        'image_length': kwargs.get('image_length'),
        'image_width': kwargs.get('image_width'),
        'length_for_resize': kwargs.get('length_for_resize'),
        'width_for_resize': kwargs.get('width_for_resize'),
    }

    valid_fields = {k: v for k, v in valid_fields.items() if v is not None}

    trade_item = TradeItem.objects.create(**valid_fields)

    return trade_item

@method_decorator(login_required)
def move_to_trade(self, request, pk):
    inventory_item = get_object_or_404(InventoryObject, pk=pk, user=request.user)

    if request.method == 'POST':
        form = MoveToTradeForm(request.POST, request.FILES)
        if form.is_valid():
            trade_item = inventory_item.move_to_trading(
                title=form.cleaned_data['title'],
                fees=form.cleaned_data['fees'],
                category=form.cleaned_data['category'],
                specialty=form.cleaned_data['specialty'],
                condition=form.cleaned_data['condition'],
                label=form.cleaned_data['label'],
                slug=form.cleaned_data['slug'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                image_length=form.cleaned_data['image_length'],
                image_width=form.cleaned_data['image_width'],
                length_for_resize=form.cleaned_data['length_for_resize'],
                width_for_resize=form.cleaned_data['width_for_resize']
            )
            return redirect('showcase:tradeitem_detail', trade_item.id)
    else:
        form = MoveToTradeForm()

    return render(request, 'inventory.html', {'form': form, 'inventory_item': inventory_item})

from django.forms import inlineformset_factory, DecimalField
from django.shortcuts import render, redirect
from .models import Game, Choice
from django.shortcuts import render, redirect
from .models import Game, Choice
from .forms import ChoiceFormSet

class SecretRoomView(LoginRequiredMixin, FormMixin, ListView):
    model = SecretRoom
    template_name = "secretrooms.html"
    form_class = VoteQueryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Stockpile'] = Inventory.objects.filter(is_active=1, user=self.request.user)
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1)
        context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=self.request.user)
        context['TradeItems'] = TradeItem.objects.filter(is_active=1, user=self.request.user)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@login_required
def delete_trade_item(request, item_id):
    trade_item = get_object_or_404(TradeItem, id=item_id)
    if trade_item.user == request.user:
        trade_item.delete()
        messages.success(request, 'Trade item deleted successfully.')
        return redirect('showcase:tradeinventory')
    else:
        messages.error(request, 'You do not have permission to delete this item.')
        return redirect('showcase:tradeinventory')

class TradeInventoryView(LoginRequiredMixin, FormMixin, ListView):
    model = TradeItem
    template_name = "tradeinventory.html"
    form_class = MoveToTradeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Stockpile'] = Inventory.objects.filter(is_active=1, user=self.request.user)
        context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=self.request.user)
        context['SentProfile'] = ProfileDetails.objects.get(user=self.request.user)
        context['TradeItems'] = TradeItem.objects.filter(is_active=1, user=self.request.user)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        action = self.request.POST.get('action')
        pk = self.request.POST.get('pk')

        if action == 'remove':
            return self.remove_trade_object(request, pk)
            print('trade item removed from trading inventory!')
        elif action == 'inventory_remove':
            return self.existing_inventory_remove_trade_object(request, pk)
            print('inventory trade item moved from trading inventory to inventory!')

        return HttpResponse(status=400)

    def remove_trade_object(self, request, pk):
        trade_item = get_object_or_404(TradeItem, pk=pk)

        if trade_item.user != request.user:
            messages.error(request, 'You cannot remove tradable items you do not own!')
            return redirect('showcase:tradeinventory')

        inventory_object = InventoryObject.objects.create(
            user=trade_item.user,
            choice_text=trade_item.title,
            category=trade_item.category,
            is_active=1,
            currency=trade_item.currency,
            price=trade_item.value,
            condition=trade_item.condition,
            image=trade_item.image,
            image_length=trade_item.image_length,
            image_width=trade_item.image_width,
            length_for_resize=trade_item.length_for_resize,
            width_for_resize=trade_item.width_for_resize,
        )

        inventory_object.save()
        trade_item.delete()
        messages.success(request, f"Successfully removed {trade_item.title}!")
        return redirect('showcase:inventory')

    def existing_inventory_remove_trade_object(self, request, pk):
        trade_item = get_object_or_404(TradeItem, pk=pk)

        if trade_item.user != request.user:
            messages.error(request, 'You cannot remove tradable items you do not own!')
            return redirect('showcase:tradeinventory')

        trade_item.user = None
        trade_item.inventory = None
        trade_item.save()

        user = request.user

        with transaction.atomic():

            inventory_object = InventoryObject.objects.filter(user=user, is_active=1).first()
            if not inventory_object:
                inventory_object = InventoryObject.objects.create(
                    user=user,
                    choice_text=trade_item.title,
                    category=trade_item.category,
                    is_active=1,
                    currency=trade_item.currency,
                    price=trade_item.value,
                    condition=trade_item.condition,
                    image=trade_item.image,
                    image_length=trade_item.image_length,
                    image_width=trade_item.image_width,
                    length_for_resize=trade_item.length_for_resize,
                    width_for_resize=trade_item.width_for_resize,
                )

            inventory_object.save()

            trade_item.delete()

        messages.success(request, f"Successfully removed {trade_item.title}!")
        return redirect('showcase:inventory')

from .models import LotteryTickets, Lottery
from .forms import TicketRequestForm

class LotteryBackgroundView(BaseView):
    model = Lottery
    template_name = "lotteries.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Lotto'] = Lottery.objects.filter(is_active=1)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


class DailyLotteryView(FormMixin, ListView):
    model = Lottery
    template_name = "dailylotto.html"
    form_class = TicketRequestForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Profile'] = UpdateProfile.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        context["lottery_prize"] = Lottery.objects.get(name="Daily Lotto").prize

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = TicketRequestForm(request.POST, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            lottery, created = Lottery.objects.get_or_create(
                name__in=['Daily Lotto', 'Daily Lottery'],
                defaults={'name': 'Daily Lotto', 'flavor_text': 'Your daily chance to win!'}
            )
            lottery.save()
            post.lottery = lottery
            post.user = request.user
            post.save()
            return redirect('showcase:dailylottoclaimed')
        else:
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            messages.error(request, 'You need to log in to claim your daily ticket!')
            return render(request, 'registration/login.html', {'form': form})


class DailyLotteryClaimedView(ListView):
    model = Lottery
    template_name = "dailylottoclaimed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Profile'] = UpdateProfile.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


@require_POST
@login_required
def claim_ruby(request):
    try:
        payload     = json.loads(request.body)
        drop_amount = int(payload.get("dropAmount", 0))
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({"error": "Invalid payload"}, status=400)

    profile = ProfileDetails.objects.select_related('tier') \
                .get(user=request.user)

    rd_benefit = (
        profile.tier
               .benefits
               .filter(benefit='RD', is_active=1)
               .first()
    )
    multiplier = rd_benefit.multiplier if rd_benefit else 1

    applied_amount = drop_amount * multiplier
    profile.currency_amount += applied_amount
    profile.save(update_fields=["currency_amount"])

    return JsonResponse({
        "newAmount":    profile.currency_amount,
        "rd_multiplier": multiplier,
        "added":         applied_amount,
    })


def login_view(request):
    next_url = request.GET.get('next', '/')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', next_url)
            parsed_url = urlparse(next_url)
            if not parsed_url.netloc and is_valid_path(next_url):
                print('next path accessed')
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form, 'next': next_url})


class Lottereal(BaseView):
    model = Lottery
    template_name = "lotteries.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['VoteQuery'] = VoteQuery.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PosteView(FormMixin, ListView):
    model = VoteBackgroundImage
    template_name = "vote.html"
    form_class = VoteQueryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.get_form(self.get_form_class())
        if 'formset' not in context:
            context['formset'] = VoteOptionFormSet()

        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['VoteQuery'] = VoteQuery.objects.all()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        context['NewsProfiles'] = userprofile if userprofile else None

        if context['NewsProfiles'] is None:
            dummy_profile = type('DummyProfile', (), {})()
            dummy_profile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            dummy_profile.newprofile_profile_url = None
            context['NewsProfiles'] = dummy_profile
        else:
            for profile in context['NewsProfiles']:
                user = profile.user
                user_profile = ProfileDetails.objects.filter(user=user).first()
                if user_profile:
                    profile.newprofile_profile_picture_url = user_profile.avatar.url
                    profile.newprofile_profile_url = profile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = VoteQueryForm(request.POST)
        formset = VoteOptionFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            poll = form.save(commit=False)
            poll.user = request.user
            poll.save()

            formset.instance = poll
            formset.save()
            return redirect('showcase:voting')
        else:

            return self.render_to_response(self.get_context_data(form=form, formset=formset))

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

@method_decorator(login_required, name='dispatch')
class TradeOffersView(View):
    def get(self, request, *args, **kwargs):

        pending_requests = TradeOffer.objects.select_related('trade_items').filter(user2=request.user,
                                                                                   status=TradeOffer.PENDING)
        outgoing_requests = TradeOffer.objects.filter(user=request.user, status=TradeOffer.PENDING)

        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        current_user = self.request.user

        newprofile = TradeOffer.objects.filter(user=request.user, is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if is_ajax(request):
            context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
            return render(request, 'pendingtrades.html', context)

        context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
        return render(request, 'pendingtrades.html', context)

from django.http import JsonResponse

@method_decorator(login_required, name='dispatch')
class DirectedTradeOfferView(View):

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, request, *args, **kwargs):

        pending_requests = TradeOffer.objects.filter(user2=request.user, trade_status=TradeOffer.PENDING)
        outgoing_requests = TradeOffer.objects.filter(user=request.user, trade_status=TradeOffer.PENDING)

        response_pending_requests = RespondingTradeOffer.objects.filter(user2=request.user,
                                                                        trade_status=RespondingTradeOffer.PENDING)
        response_outgoing_requests = RespondingTradeOffer.objects.filter(user=request.user,
                                                                         trade_status=RespondingTradeOffer.PENDING)

        context = {}
        context.update({
            'pending_requests': pending_requests,
            'outgoing_requests': outgoing_requests,
            'response_pending_requests': response_pending_requests,
            'response_outgoing_requests': response_outgoing_requests
        })
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['request'] = request
        current_user = request.user

        newprofile = TradeOffer.objects.filter(user=current_user.id, is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        responsetradeoffers = RespondingTradeOffer.objects.filter(user=self.request.user, is_active=1)
        context['ResponseTrade'] = responsetradeoffers
        for responsetradeoffer in context['ResponseTrade']:
            user = responsetradeoffer.user
            if user:
                responsetradeoffer.responsetradeoffer_trade_url = responsetradeoffer.get_profile_url2()

        if self.is_ajax(request):
            context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
            return render(request, 'directedtradeoffers.html', context)

        context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
        return render(request, 'directedtradeoffers.html', context)

@login_required
def accept_trade(request, request_id):
    trade_offer = get_object_or_404(TradeOffer, id=request_id)
    print('trade offer acceptance')
    if request.user != trade_offer.user2 or not trade_offer.user2:
        raise PermissionDenied
    trade_offer.trade_status = TradeOffer.ACCEPTED
    trade_offer.save()
    messages.success(request, 'You have accepted the trade offer.')
    return redirect('showcase:mytrades')

@login_required
def decline_trade(request, request_id):
    trade_offer = get_object_or_404(TradeOffer, id=request_id)
    if request.user != trade_offer.user2 or not trade_offer.user2:
        raise PermissionDenied
    trade_offer.trade_status = TradeOffer.DECLINED
    trade_offer.save()
    messages.success(request, 'You have declined the trade offer.')
    return redirect('showcase:mytrades')

@login_required
def accept_response_trade(request, request_id):
    trade_offer = get_object_or_404(RespondingTradeOffer, id=request_id)

    if request.user != trade_offer.user2 or not trade_offer.user2:
        raise PermissionDenied

    RespondingTradeOffer.objects.filter(id=request_id).update(trade_status=RespondingTradeOffer.ACCEPTED)

    wanted_trade_offer = trade_offer.wanted_trade_items
    if wanted_trade_offer and not Trade.objects.filter(trade_offers__in=[wanted_trade_offer]).exists():
        trade = Trade.objects.create()
        trade.trade_offers.add(wanted_trade_offer)
        trade.users.add(trade_offer.user, trade_offer.user2)

    messages.success(request, 'You have accepted the trade offer.')
    return redirect('showcase:mytrades')

@login_required
def decline_response_trade(request, request_id):
    trade_offer = get_object_or_404(RespondingTradeOffer, id=request_id)
    if request.user != trade_offer.user2 or not trade_offer.user2:
        raise PermissionDenied
    trade_offer.trade_status = RespondingTradeOffer.DECLINED
    trade_offer.save()
    messages.success(request, 'You have declined the trade offer.')
    return redirect('showcase:mytrades')

class TradeHistory(ListView):
    model = Trade
    template_name = "mytrades.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'You must be signed in to access this feature!')
            return redirect(reverse('showcase:account_login'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        current_user = self.request.user
        user_trades = Trade.objects.filter(users=current_user)
        context['user_trades'] = user_trades
        context['feedback'] = Feedback.objects.all()

        print(user)

        items = TradeItem.objects.filter(is_active=1)

        context['Iteme'] = items

        for items in context['Iteme']:

            image = items.image

            if user.is_authenticated:

                profile = ProfileDetails.objects.filter(user=user).first()

                if profile:

                    items.author_profile_picture_url = profile.avatar.url

            else:

                messages.warning(self.request, "You need to log in")
                return redirect("accounts/login")

        current_user = self.request.user
        user_trades = Trade.objects.filter(is_active=1, users=current_user)
        total_items = OrderItem.objects.filter(is_active=1).count()

        paginate_by = int(self.request.GET.get('paginate_by', settings.DEFAULT_PAGINATE_BY))

        items_query = Trade.objects.filter(is_active=1)
        paginator = Paginator(items_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_items = paginator.get_page(page_number)

        context['orders'] = paginated_items
        for order_item in context['orders']:

            user = self.request.user
            profile = ProfileDetails.objects.filter(user=user).first()

            order_item.author_profile_url = order_item.get_profile_url() if order_item.get_profile_url() else None
            order_item.hyperlink = order_item.get_profile_url()

            if profile:
                order_item.author_profile_picture_url = profile.avatar.url

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class SettingsView(RegularUserRequiredMixin, UserPassesTestMixin, FormView):
    """Only allow registered users to change their settings."""
    form_class = SettingsForm
    model = SettingsModel
    template_name = "myaccount.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            user_settings = SettingsModel.objects.get(user=self.request.user, is_active=1)
        except SettingsModel.DoesNotExist:
            user_settings = None

        context['settings'] = user_settings

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def test_func(self):
        return self.request.user.is_superuser

from django.contrib.messages.views import SuccessMessageMixin

class SettingsBackgroundView(SuccessMessageMixin, FormView):
    model = SettingsBackgroundImage
    form_class = SettingsForm
    template_name = "settings.html"
    success_url = reverse_lazy('showcase:myaccount')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'You must be signed in to access this feature!')
            return redirect(reverse('showcase:account_login'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        print(FaviconBase.objects.all())
        context['SettingsBackgroundView'] = self.model.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    from django.db import transaction

    @transaction.atomic
    def form_valid(self, form):
        user = self.request.user
        settings_model, _ = SettingsModel.objects.get_or_create(user=user)

        new_username = form.cleaned_data['username']
        if User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
            messages.error(self.request, 'Username already exists. Please choose a different username.')
            return self.form_invalid(form)

        user.username = new_username
        user.set_password(form.cleaned_data['password'])
        new_email = form.cleaned_data['email']
        user.email = new_email
        user.save()

        settings_model.email = form.cleaned_data['email']
        settings_model.coupons = form.cleaned_data['coupons']
        settings_model.news = form.cleaned_data['news']
        settings_model.save()

        return super().form_valid(form)

from django.shortcuts import render
from .models import AdministrationChangeLog


class AdministrationChangeLogView(ListView):
    model = AdministrationChangeLog
    template_name = "administrationchangelog.html"

    # By default, a ListView will provide a context variable named "object_list".
    # We’d rather call it "changelogs" in the template. This replaces the old
    # function that did:
    #     changelogs = ChangeLog.objects.all()
    #     return render(..., {'changelogs': changelogs})
    context_object_name = "changelogs"

    def get_context_data(self, **kwargs):
        # First, let the ListView build the baseline context (which already contains
        #   "changelogs" = ChangeLog.objects.all(), plus pagination stuff if you enabled it).
        context = super().get_context_data(**kwargs)

        # ─── Navbar/Header Stuff ─────────────────────────────────────────────────────
        # (unchanged from your original get_context_data)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
        # ─── User‐specific clickables & profile URLs ─────────────────────────────────
        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for uc in user_clickables:
                if uc.clickable.chance_per_second > 0:
                    # Precompute chance (your original logic)
                    uc.precomputed_chance = 1000 / uc.clickable.chance_per_second
                else:
                    uc.precomputed_chance = 0
            context["Clickables"] = user_clickables

            # Grab the ProfileDetails for this user (if any)
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        else:
            # If not authenticated, you may want to explicitly set these to empty
            context["Clickables"] = []
            context['Profile'] = []
            context['profile_pk'] = None
            context['profile_url'] = None

        # ─── Feedback / Footer / Background / NewsProfiles ───────────────────────────
        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")

        # “NewsProfiles” logic: if the user is authenticated, pass back their ProfileDetails;
        # otherwise, create a dummy object for avatar and url placeholders.
        if self.request.user.is_authenticated:
            userprofile_qs = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile_qs = ProfileDetails.objects.none()

        if userprofile_qs.exists():
            # If there _are_ active profiles, annotate each with picture_url and profile_url
            for up in userprofile_qs:
                up.newprofile_profile_picture_url = up.avatar.url if up.avatar else ""
                up.newprofile_profile_url = up.get_profile_url()  # assuming get_profile_url() exists on your model
            context['NewsProfiles'] = userprofile_qs
        else:
            # Create a dummy “object” with just two attributes so the template can still find them:
            dummy = type("DummyProfile", (), {})()
            dummy.newprofile_profile_picture_url = "static/css/images/a.jpg"
            dummy.newprofile_profile_url = None
            context['NewsProfiles'] = [dummy]

        return context


def get_changes(instance):
    if not instance.pk:
        return None
    old_instance = instance.__class__.objects.get(pk=instance.pk)
    changes = {}
    for field in instance._meta.fields:
        field_name = field.name
        old_value = getattr(old_instance, field_name)
        new_value = getattr(instance, field_name)
        if old_value != new_value:
            changes[field_name] = {
                'old': old_value,
                'new': new_value
            }
    return changes


class ChangeLogView(ListView):
    model = ChangeLog
    template_name = "changelog.html"

    # By default, a ListView will provide a context variable named "object_list".
    # We’d rather call it "changelogs" in the template. This replaces the old
    # function that did:
    #     changelogs = ChangeLog.objects.all()
    #     return render(..., {'changelogs': changelogs})
    context_object_name = "changelogs"

    def get_context_data(self, **kwargs):
        # First, let the ListView build the baseline context (which already contains
        #   "changelogs" = ChangeLog.objects.all(), plus pagination stuff if you enabled it).
        context = super().get_context_data(**kwargs)

        # ─── Navbar/Header Stuff ─────────────────────────────────────────────────────
        # (unchanged from your original get_context_data)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        # ─── User‐specific clickables & profile URLs ─────────────────────────────────
        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for uc in user_clickables:
                if uc.clickable.chance_per_second > 0:
                    # Precompute chance (your original logic)
                    uc.precomputed_chance = 1000 / uc.clickable.chance_per_second
                else:
                    uc.precomputed_chance = 0
            context["Clickables"] = user_clickables

            # Grab the ProfileDetails for this user (if any)
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        else:
            # If not authenticated, you may want to explicitly set these to empty
            context["Clickables"] = []
            context['Profile'] = []
            context['profile_pk'] = None
            context['profile_url'] = None

        # ─── Feedback / Footer / Background / NewsProfiles ───────────────────────────
        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
        # “NewsProfiles” logic: if the user is authenticated, pass back their ProfileDetails;
        # otherwise, create a dummy object for avatar and url placeholders.
        if self.request.user.is_authenticated:
            userprofile_qs = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile_qs = ProfileDetails.objects.none()

        if userprofile_qs.exists():
            # If there _are_ active profiles, annotate each with picture_url and profile_url
            for up in userprofile_qs:
                up.newprofile_profile_picture_url = up.avatar.url if up.avatar else ""
                up.newprofile_profile_url = up.get_profile_url()  # assuming get_profile_url() exists on your model
            context['NewsProfiles'] = userprofile_qs
        else:
            # Create a dummy “object” with just two attributes so the template can still find them:
            dummy = type("DummyProfile", (), {})()
            dummy.newprofile_profile_picture_url = "static/css/images/a.jpg"
            dummy.newprofile_profile_url = None
            context['NewsProfiles'] = [dummy]

        return context



class HomePageView(TemplateView):
    template_name = 'index.html'

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class EcommerceSearchResultsView(ListView):
    model = Item
    template_name = 'ecommercesearch_results.html'

    def get_queryset(self):
        print(1234)
        query = self.request.GET.get('q')
        item_list = Item.objects.filter(
            Q(title__icontains=query) | Q(slug__icontains=query))

        all_list = {
            "item_list": item_list,
        }
        print(234)
        print(all_list)

        return (all_list)

class BlogSearchResultsView(ListView):
    template_name = 'blogsearch_results.html'
    paginate_by = 10
    context_object_name = 'all_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        filter_by = self.request.GET.get('filter')

        search_lists = []

        if filter_by == 'blog':
            search_lists.append(Blog.objects.filter(
                Q(title__icontains=query) | Q(slug__icontains=query) | Q(type__icontains=query) | Q(
                    author__username__icontains=query)))
        elif filter_by == 'blogfilter':
            search_lists.append(BlogFilter.objects.filter(
                Q(blog_filter__icontains=query)))
        elif filter_by == 'blogheader':
            search_lists.append(BlogHeader.objects.filter(
                Q(category__icontains=query)))
        else:
            search_lists = [Blog.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query) |
                                                Q(type__icontains=query) | Q(author__username__icontains=query)),
                            BlogFilter.objects.filter(Q(blog_filter__icontains=query)),
                            BlogHeader.objects.filter(Q(category__icontains=query))]

        search_results = []
        for search_list in search_lists:
            for item in search_list:
                search_result = SearchResult(content_object=item)
                search_results.append(search_result)

        return search_results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        for result in context['all_list']:
            if isinstance(result.content_object, Blog):
                result.type = 'Blog'
                result.url = reverse_lazy('showcase:blog')
            elif isinstance(result.content_object, BlogFilter):
                result.type = 'BlogFilter'
                result.url = reverse_lazy('showcase:blog')
            elif isinstance(result.content_object, BlogHeader):
                result.type = 'Blog Header'
                result.url = reverse_lazy('showcase:blog')
            else:
                result.type = 'Unknown'
                result.url = ''

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class GameCategorySearchResultsView(ListView):
    model = GameHub
    template_name = 'gamehubsearchresults.html'

    def get_queryset(self):
        print(1234)
        query = self.request.GET.get('q')
        game_category_list = GameHub.objects.filter(
            Q(name__icontains=query) | Q(slug__icontains=query))

        all_list = {
            "game_category_list": game_category_list,
        }
        print(234)
        print(all_list)

        return (all_list)

class GameSearchResultsView(ListView):
    model = Game
    template_name = 'gamesearchresults.html'

    def get_queryset(self):
        print(1234)
        query = self.request.GET.get('q')
        game_list = Game.objects.filter(
            Q(name__icontains=query) | Q(slug__icontains=query))

        all_list = {
            "game_list": game_list,
        }
        print(234)
        print(all_list)

        return (all_list)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        newprofile = Game.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.views.generic import ListView
from django.db.models import Q
from showcase.models import City, VoteQuery, UpdateProfile, Idea, PartnerApplication, SearchResult

class SearchResultsView(ListView):
    template_name = 'search_results.html'
    paginate_by = 10
    context_object_name = 'all_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        filter_by = self.request.GET.get('filter')

        search_lists = []

        if filter_by == 'city':
            search_lists.append(City.objects.filter(Q(name__icontains=query) | Q(state__icontains=query)))
        elif filter_by == 'VoteQuery':
            search_lists.append(VoteQuery.objects.filter(
                Q(name__icontains=query) | Q(category__icontains=query) | Q(description__icontains=query)))
        elif filter_by == 'profile':
            search_lists.append(UpdateProfile.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(image__icontains=query)))
        elif filter_by == 'idea':
            search_lists.append(Idea.objects.filter(
                Q(name__icontains=query) | Q(category__icontains=query) | Q(description__icontains=query) | Q(
                    image__icontains=query)))
        elif filter_by == 'partner':
            search_lists.append(PartnerApplication.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(server_invite__icontains=query)))
        elif filter_by == 'news':
            search_lists.append(NewsFeed.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query)))
        else:

            search_lists = [City.objects.filter(Q(name__icontains=query) | Q(state__icontains=query)),
                            VoteQuery.objects.filter(Q(name__icontains=query) | Q(category__icontains=query) | Q(
                                description__icontains=query)),
                            UpdateProfile.objects.filter(
                                Q(name__icontains=query) | Q(description__icontains=query) | Q(image__icontains=query)),
                            Idea.objects.filter(Q(name__icontains=query) | Q(category__icontains=query) | Q(
                                description__icontains=query) | Q(image__icontains=query)),
                            PartnerApplication.objects.filter(
                                Q(name__icontains=query) | Q(description__icontains=query) | Q(
                                    server_invite__icontains=query)),
                            NewsFeed.objects.filter(
                                Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query))]

        search_results = []
        for search_list in search_lists:
            for item in search_list:
                search_result = SearchResult(content_object=item)
                search_results.append(search_result)

        return search_results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        for result in context['all_list']:
            if isinstance(result.content_object, City):
                result.type = 'City'
                result.url = ''
            elif isinstance(result.content_object, VoteQuery):
                result.type = 'VoteQuery'
                result.url = reverse_lazy('showcase:voting')
            elif isinstance(result.content_object, UpdateProfile):
                result.type = 'Profile'
                result.url = reverse_lazy('showcase:showcase')
            elif isinstance(result.content_object, Idea):
                result.type = 'Idea'
                result.url = reverse_lazy('showcase:share')
            elif isinstance(result.content_object, PartnerApplication):
                result.type = 'Partner'
                result.url = reverse_lazy('showcase:partners')
            elif isinstance(result.content_object, NewsFeed):
                result.type = 'News'
                result.url = reverse_lazy('showcase:newsfeed')
            else:
                result.type = 'Unknown'
                result.url = ''

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class PageSearchResultsView(ListView):
    model = NavBar
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        search_type = self.request.GET.get('search_type')
        search_lists = []

        if search_type == "text":
            nav_list = NavBar.objects.filter(
                Q(text__icontains=query))
        elif search_type == "url":
            if query.startswith(("http://", "https://")):

                url_path = urllib.parse.urlparse(query).path
                nav_list = NavBar.objects.filter(url__icontains=url_path)
            else:

                nav_list = None
        else:

            nav_list = None

        all_list = {
            "nav_list": nav_list,
        }
        return all_list

    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('search_query')
        search_type = request.POST.get('search_type')

        if search_type == "text":
            nav_list = NavBar.objects.filter(
                Q(text__icontains=search_query))
        elif search_type == "url":

            if query.startswith(("http://", "https://")):

                url_path = urllib.parse.urlparse(query).path
                nav_list = NavBar.objects.filter(url__icontains=url_path)
            else:

                nav_list = None
        else:

            nav_list = None

        if nav_list:
            redirect_url = nav_list.first().url
            return redirect(redirect_url)
        else:

            return render(request, 'search_results.html',
                          {'message': 'No matching results found.'})

    def get(self, request, *args, **kwargs):

        response = super().get(request, *args, **kwargs)
        context = response.context

        if context['nav_list']:

            redirect_url = context['nav_list'].first().url
            return redirect(redirect_url)
        else:

            return response

class CreateWithdrawView(LoginRequiredMixin, CreateView):
    model = Withdraw
    form_class = WithdrawForm
    template_name = "create_withdraw.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def my_cards(request):
        if request.user.is_authenticated:

            withdraws = Withdraw.objects.filter(user=request.user).prefetch_related('cards')
        else:
            withdraws = None

        context = {'withdraws': withdraws}
        return render(request, 'my_cards.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = WithdrawForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user

                selected_cards = request.POST.getlist('selected_cards')

                withdraw = form.save()

                withdraw.cards.set(selected_cards)

                withdraw.save()

                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:withdraws')
            else:
                messages.error(request, "Form submission invalid")
                return render(request, "create_withdraw.html", {'form': form})
        else:
            form = WithdrawForm()
            return render(request, "create_withdraw.html", {'form': form})


class WithdrawView(LoginRequiredMixin, ListView):
    model = Withdraw
    template_name = "withdraws.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        completed_withdraws = Withdraw.objects.filter(user=self.request.user, is_active=1, withdraw_state='C',
                                                      shipping_state='C')
        incomplete_withdraws = Withdraw.objects.filter(user=self.request.user, is_active=1, withdraw_state='C').exclude(
            shipping_state='C')

        context['CompletedWithdraws'] = completed_withdraws
        context['IncompleteWithdraws'] = incomplete_withdraws
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        for withdraw in context['CompletedWithdraws']:
            user = withdraw.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                withdraw.newprofile_profile_picture_url = profile.avatar.url
                withdraw.newprofile_profile_url = withdraw.get_profile_url()

        for withdraw in context['IncompleteWithdraws']:
            user = withdraw.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                withdraw.newprofile_profile_picture_url = profile.avatar.url
                withdraw.newprofile_profile_url = withdraw.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get_queryset(self):
        return Withdraw.objects.filter(user=self.request.user, is_active=1)

    def post(self, request, *args, **kwargs):
        withdraw_id = request.POST.get("withdraw_id")
        if withdraw_id:
            withdraw = get_object_or_404(Withdraw, id=withdraw_id, user=request.user)
            if withdraw.shipping_state != 'C':
                withdraw.mark_complete()
                messages.success(request, "Withdrawal marked complete successfully!")
        return redirect('showcase:withdraws')


class WithdrawDetailView(LoginRequiredMixin, DetailView):
    model = Withdraw
    template_name = "withdraw_detail.html"

    def get_object(self):
        slag = self.kwargs.get('slag')
        return get_object_or_404(Withdraw, slag=slag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        withdraw = self.get_object()

        profile = ProfileDetails.objects.filter(user=withdraw.user).first()
        if profile:
            context['profile_picture_url'] = profile.avatar.url
            context['profile_url'] = reverse_lazy('showcase:profile', args=[str(profile.pk)])

        context['card_images'] = withdraw.get_card_images()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class ProcessingWithdrawView(LoginRequiredMixin, ListView):
    model = Withdraw
    template_name = "processing_withdraws.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        completed_withdraws = Withdraw.objects.filter(user=self.request.user, is_active=1, withdraw_state='I',
                                                      shipping_state='Y')
        incomplete_withdraws = Withdraw.objects.filter(user=self.request.user, is_active=1, withdraw_state='I').exclude(
            shipping_state='Y')

        context['CompletedWithdraws'] = completed_withdraws
        context['IncompleteWithdraws'] = incomplete_withdraws
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        for withdraw in context['CompletedWithdraws']:
            user = withdraw.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                withdraw.newprofile_profile_picture_url = profile.avatar.url
                withdraw.newprofile_profile_url = withdraw.get_profile_url()

        for withdraw in context['IncompleteWithdraws']:
            user = withdraw.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                withdraw.newprofile_profile_picture_url = profile.avatar.url
                withdraw.newprofile_profile_url = withdraw.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get_queryset(self):
        return Withdraw.objects.filter(user=self.request.user, is_active=1)

    def post(self, request, *args, **kwargs):
        withdraw_id = request.POST.get("withdraw_id")
        if withdraw_id:
            withdraw = get_object_or_404(Withdraw, id=withdraw_id, user=request.user)
            if withdraw.shipping_state != 'C':
                withdraw.mark_complete()
                messages.success(request, "Withdrawal marked complete successfully!")
        return redirect('showcase:withdraws')

from django.contrib.auth.decorators import login_required
from .models import InviteCode
from .forms import InviteCodeForm
from secrets import token_urlsafe

def generate_unique_code(room_name):
    """Generates a unique alphanumeric code with the room name prefix"""
    while True:

        code_suffix = token_urlsafe(16)

        code = f"{room_name}_{code_suffix}" if room_name else code_suffix

        if not InviteCode.objects.filter(code=code).exists():
            return code

@login_required
def generate_invite_link(request):
    if request.method == 'POST':
        form = InviteCodeForm(request.POST)
        if form.is_valid():

            code = generate_unique_code()
            invite_code, created = InviteCode.objects.get_or_create(user=request.user, code=code)
            invite_link = f"https://your_app.com/join/{invite_code.code}"
            return render(request, 'invite_link.html', {'invite_link': invite_link})
    else:
        form = InviteCodeForm()
    return render(request, 'generate_invite.html', {'form': form})

from .models import ProfileDetails

class ProfileView(LoginRequiredMixin, UpdateView):
    model = ProfileDetails
    form_class = ProfileForm
    paginate_by = 10
    success_url = reverse_lazy('home')
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):

        pk = self.kwargs.get('pk')
        return get_object_or_404(ProfileDetails, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['current_user'] = user
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        games = Game.objects.filter(user=self.request.user)
        popular_chests = []
        favorites = []

        context['store_view_form'] = ProfileViewTypeForm()

        current_user = self.request.user
        if current_user.is_authenticated:
            try:
                store_view_instance = StoreViewType.objects.get(user=current_user, is_active=1)
                context['store_view'] = store_view_instance.type
                context['store_view_type_str'] = str(store_view_instance)
                context['streamfilter_string'] = f'stream filter set by {current_user.username}'
            except StoreViewType.DoesNotExist:
                store_view_instance = None
                context['store_view'] = 'stream'
                context['store_view_type_str'] = 'stream'
                context['streamfilter_string'] = f'stream filter set by {current_user.username}'
        else:
            store_view_instance = None
            context['store_view'] = 'stream'
            context['streamfilter_string'] = 'stream filter set by anonymous user'

        store_view_form = ProfileViewTypeForm(instance=store_view_instance, request=self.request)
        context['store_view_form'] = store_view_form

        for game in games:
            chest_stat = IndividualChestStatistics.objects.filter(user=self.request.user, chest=game).order_by(
                "-plays").first()
            if chest_stat:
                popular_chests.append(chest_stat)

            fav = FavoriteChests.objects.filter(user=self.request.user, chest=game).first()
            if fav:
                favorites.append(fav)

        popular_chests = sorted(popular_chests, key=lambda c: c.plays, reverse=True)[:5]

        context['popular_chested'] = popular_chests
        context['favorites'] = favorites

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        user = self.request.user
        total_achievements = Achievements.objects.filter(is_active=1)

        earned_achievements = Achievements.objects.filter(
            is_active=1, user=user
        ).distinct()

        context['earned_count'] = earned_achievements.count()
        context['total_count'] = total_achievements.count()

        context['total_achievements'] = total_achievements
        context['earned_achievements'] = earned_achievements
        context['SettingsModel'] = SettingsModel.objects.filter(is_active=1)
        profile = self.get_object()
        if profile:
            context['profile'] = profile
            context['remaining_rubies'] = profile.level.experience - profile.rubies_spent

        if self.request.user.is_authenticated:
            news_profiles = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            news_profiles = None

        if news_profiles:
            for news_profile in news_profiles:
                user = news_profile.user
                user_profile = ProfileDetails.objects.filter(user=user).first()
                if user_profile:
                    news_profile.newprofile_profile_picture_url = user_profile.avatar.url
                    news_profile.newprofile_profile_url = news_profile.get_profile_url()
        else:
            news_profiles = [type('Dummy', (), {
                "newprofile_profile_picture_url": 'static/css/images/a.jpg',
                "newprofile_profile_url": None,
            })]

        context['NewsProfiles'] = news_profiles

        if self.request.user.is_authenticated:
            player_profiles = ProfileDetails.objects.filter(is_active=1, user=profile.user)
        else:
            player_profiles = None

        if player_profiles:
            for player_profile in player_profiles:
                user = player_profile.user
                user_profile = ProfileDetails.objects.filter(user=user).first()
                if user_profile:
                    player_profile.newprofile_profile_picture_url = user_profile.avatar.url
                    player_profile.newprofile_profile_url = player_profile.get_profile_url()
                    if player_profile.level and player_profile.level.experience:
                        player_profile.progress_percent = (
                                player_profile.rubies_spent * 100
                        )
                    else:
                        player_profile.progress_percent = 0
        else:
            player_profiles = [type('Dummy', (), {
                "newprofile_profile_picture_url": 'static/css/images/a.jpg',
                "newprofile_profile_url": None,
                "progress_percent": 0,
                "rubies_spent": 0,
                "level": type('DummyLevel', (), {"experience": 0})(),
            })]

        context['PlayerProfiles'] = player_profiles

        return context

@login_required
def fetch_remaining_rubies(request, pk):
    profile = get_object_or_404(ProfileDetails, is_active=1, pk=pk)
    remaining = profile.level.experience - profile.rubies_spent
    return JsonResponse({'remaining_rubies': remaining})

@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(ProfileDetails, pk=pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('showcase:profile_detail', pk=pk)

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_edit.html', {'form': form, 'profile': profile})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('showcase:profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

class MyLevelView(LoginRequiredMixin, ListView):
    model = Level
    template_name = 'mylevel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        profile = ProfileDetails.objects.filter(user=user).first()
        mylevel = math.floor(1.02 ** profile.level.level)
        context['created_level'] = mylevel
        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['SettingsModel'] = SettingsModel.objects.filter(is_active=1)

        levels = Level.objects.filter(is_active=1).order_by("level")
        context['levels'] = [
            {
                "level": level,
                "background": level.get_background_style(),
                "given_level": level.level,
                "actual_level": level.actual_level,
            }
            for level in levels
        ]

        if user.is_authenticated:
            profile = ProfileDetails.objects.filter(user=user, is_active=1).first()
            if profile:
                context['Profile'] = profile
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
            else:
                context['Profile'] = None
        else:
            context['Profile'] = None

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class StaffJoine(ListView):
    paginate_by = 10
    template_name = 'staffapplication.html'

    def get_queryset(self, *args, **kwargs):
        return StaffApplication.objects.all()

class PunishAppsBackgroundView(FormMixin, ListView):
    model = PunishmentAppeal
    template_name = "punishapps.html"
    form_class = PunishAppeale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PunishAppsBackgroundImage'] = PunishAppsBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['PunishApps'] = PunishmentAppeal.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PunishAppeale(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:punishdone')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "punishapps.html", {'form': form})
        else:
            form = PunishAppeale()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "punishapps.html", {'form': form})

class BanAppealBackgroundView(FormMixin, ListView):
    model = BanAppeal
    template_name = "banappeals.html"
    form_class = BanAppeale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BanAppealBackgroundImage'] = BanAppealBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")

        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['BanAppeal'] = BanAppeal.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = BanAppeale(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:bandone')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "banappeals.html", {'form': form})
        else:
            form = BanAppeale()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "banappeals.html", {'form': form})

class CommerceExchangeView(CreateView):
    model = CommerceExchange
    template_name = "commerce.html"
    form_class = ExchangePrizesForm
    success_url = reverse_lazy('showcase:commerce')

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self):

        return self.form_class(user=self.request.user, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user = self.request.user

        trade_items = TradeItem.objects.filter(user=user)

        context['trade_items'] = trade_items
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['Prizes'] = ExchangePrize.objects.filter(
            is_active=1).order_by('value')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import TradeItem

class InventoryTradeView(CreateView):
    model = CommerceExchange
    template_name = "inventorytrade.html"
    form_class = InventoryTradeForm
    success_url = reverse_lazy('showcase:inventorytradeofferstatuses')

    def form_invalid(self, form):
        print("Form validation errors:", form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        trading_user = form.cleaned_data['trading_user']
        offered_items = form.cleaned_data['usercard']
        requested_items = form.cleaned_data['exchangeprizes']

        try:
            trade_offer = InventoryTradeOffer.objects.create(
                initiator=self.request.user,
                receiver=trading_user
            )
            trade_offer.offered_items.set(offered_items)
            trade_offer.requested_items.set(requested_items)
            trade_offer.save()
            print("Trade offer created:", trade_offer)
        except Exception as e:
            print("Error creating trade offer:", str(e))

        return response

    def get_form(self):
        return self.form_class(user=self.request.user, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        trade_items = TradeItem.objects.filter(user=user, is_active=1)
        other_trade_items = TradeItem.objects.exclude(user=user).filter(is_active=1)

        items_in_pending_offers = InventoryTradeOffer.objects.filter(
            (Q(initiator=user) | Q(receiver=user)) & Q(status='pending')
        ).values_list('offered_items', flat=True)

        context['disabled_items'] = set(items_in_pending_offers)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['other_trade_items'] = [
            {
                'id': item.id,
                'title': item.title,
                'value': item.value,
                'image_url': item.image.url if item.image and hasattr(item.image,
                                                                      'url') else '/path/to/placeholder/image.jpg',

                'condition': item.get_condition_display(),
            }
            for item in other_trade_items
        ]

        context.update({
            'form': self.get_form(),
            'trade_items': trade_items,
            'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Prizes': ExchangePrize.objects.filter(is_active=1).order_by('value'),
        })

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class UpdateTradeOfferStatusView(View):
    def post(self, request, *args, **kwargs):
        trade_offer_id = kwargs.get('pk')
        trade_offer = get_object_or_404(InventoryTradeOffer, id=trade_offer_id)

        if trade_offer.receiver != request.user:
            raise PermissionDenied("You are not authorized to update this trade offer.")

        new_status = request.POST.get('status')
        if new_status not in ['accepted', 'declined']:
            return JsonResponse({'error': 'Invalid status value.'}, status=400)

        trade_offer.status = new_status
        trade_offer.save()

        return JsonResponse({'message': 'Status updated successfully.', 'status': trade_offer.status})

def trade_items_api(request, user_id):

    trade_items = TradeItem.objects.filter(user_id=user_id, is_active=1)
    trade_items_data = [
        {
            'id': item.id,
            'title': item.title,
            'value': item.value,
            'image_url': item.image.url if item.image and hasattr(item.image,
                                                                  'url') else '/path/to/placeholder/image.jpg',

            'condition': item.get_condition_display(),
        }
        for item in trade_items
    ]
    return JsonResponse({'trade_items': trade_items_data})

class UserTradeOffersView(LoginRequiredMixin, View):
    def get(self, request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            user = request.user
            trade_offers = InventoryTradeOffer.objects.filter(
                models.Q(initiator=user) | models.Q(receiver=user)
            ).select_related('initiator', 'receiver').prefetch_related('offered_items', 'requested_items')

            categories = {
                "pending_initiator": trade_offers.filter(initiator=user, status='pending'),
                "pending_receiver": trade_offers.filter(receiver=user, status='pending'),
                "accepted_initiator": trade_offers.filter(initiator=user, status='accepted'),
                "accepted_receiver": trade_offers.filter(receiver=user, status='accepted'),
                "declined_initiator": trade_offers.filter(initiator=user, status='declined'),
                "declined_receiver": trade_offers.filter(receiver=user, status='declined'),
            }

            data = {
                category: [
                    {
                        "id": offer.id,
                        "initiator": str(offer.initiator),
                        "initiator_id": offer.initiator.id,
                        "receiver": str(offer.receiver),
                        "receiver_id": offer.receiver.id,
                        'offered_items': [
                            {'title': item.title, 'fees': float(item.value or 0)} for item in offer.offered_items.all()
                        ],
                        'requested_items': [
                            {'title': item.title, 'fees': float(item.value or 0)} for item in
                            offer.requested_items.all()
                        ],
                        "status": offer.status,
                        "created_at": offer.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    for offer in offers
                ]
                for category, offers in categories.items()
            }

            data['receiver_currency_amount'] = user.profiledetails.currency_amount
            return JsonResponse(data)

        context = {
            "user_id": request.user.id,
            "user_username": request.user.username,
            "currency_amount": request.user.profiledetails.currency_amount,
        }
        return render(request, "inventorytradeofferstatuses.html", context)

@login_required
def get_trade_items(request, user_id):
    if request.method == "GET":

        current_user = request.user
        trade_user = User.objects.filter(id=user_id).first()

        trade_items = TradeItem.objects.filter(user_id=user_id, is_active=True).values(
            'id', 'title', 'condition', 'value', 'currency__name', 'image'
        )

        my_trade_items = TradeItem.objects.filter(user_id=current_user.id, is_active=True).values(
            'id', 'title', 'condition', 'value', 'currency__name', 'image'
        )

        response = {
            'trade_user': trade_user.username if trade_user else "Unknown",
            'trade_items': list(trade_items),
            'my_trade_items': list(my_trade_items),
        }
        return JsonResponse(response)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def fetch_trade_items(request, user_id):
    if request.method == "GET":

        trade_items = TradeItem.objects.filter(user_id=user_id, is_active=True).values(
            'id', 'title', 'condition', 'value', 'currency__name'
        )
        return JsonResponse({'trade_items': list(trade_items)})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def create_trade_offer(request):
    if request.method == 'POST':
        form = InventoryTradeForm(request.POST, user=request.user)
        if form.is_valid():

            trade_offer = TradeOffer.objects.create(
                initiator=request.user,
                receiver=form.cleaned_data['trading_user'],
            )
            trade_offer.offered_items.set(form.cleaned_data['usercard'])
            trade_offer.requested_items.set(form.cleaned_data['exchangeprizes'])
            trade_offer.save()

            messages.success(request, "Trade offer sent successfully!")
            return redirect('trade_offer_sent')
    else:
        form = InventoryTradeForm(user=request.user)

    return render(request, 'trade_form.html', {'form': form})

def respond_to_trade_offer(request, trade_offer_id):
    trade_offer = get_object_or_404(TradeOffer, id=trade_offer_id, receiver=request.user)
    if request.method == 'POST':
        form = InventoryTradeOfferResponseForm(request.POST, instance=trade_offer)
        if form.is_valid():
            form.save()

            if trade_offer.status == 'accepted':
                messages.success(request, "You accepted the trade offer!")
            else:
                messages.info(request, "You declined the trade offer.")
            return redirect('trade_dashboard')
    else:
        form = InventoryTradeOfferResponseForm(instance=trade_offer)

    return render(request, 'trade_response_form.html', {'form': form, 'trade_offer': trade_offer})

def create_notification(user, message, related_object=None):
    content_type = None
    object_id = None

    if related_object:
        content_type = ContentType.objects.get_for_model(related_object)
        object_id = related_object.id

    Notification.objects.create(
        user=user,
        message=message,
        content_type=content_type,
        object_id=object_id
    )

def notify(request, pk):
    notification = get_object_or_404(InventoryTradeOffer, pk=pk)

    create_notification(
        user=InventoryTradeOffer.receiver,
        message=f"An update has been made to {InventoryTradeOffer.name}",
        related_object=notification
    )

def dashboard_view(request):
    notifications = request.user.notifications.filter(is_read=False)
    return render(request, 'dashboard.html', {'notifications': notifications})

class ExchangePrizesView(FormMixin, ListView):
    model = ExchangePrize
    template_name = "commerce.html"
    form_class = ExchangePrizesForm

    def get_form_kwargs(self):
        """Pass the user to the form."""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):

        form.instance.user = self.request.user

        exchange_prize = form.save(commit=False)

        selected_inventory_objects = form.cleaned_data.get('usercard')
        total_usercard_value = (
                selected_inventory_objects.aggregate(
                    total_price=Sum(F('price') * F('quantity'), output_field=DecimalField())
                )['total_price'] or 0
        )

        exchange_prize.total_usercard_value = total_usercard_value
        exchange_prize.save()
        form.save_m2m()

        messages.success(self.request, f"Form submitted successfully. Total Value: ${total_usercard_value:.2f}.")
        return redirect('showcase:commerce')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['BanAppealBackgroundImage'] = BanAppealBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['BanAppeal'] = BanAppeal.objects.all()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            messages.error(request, "Form submission invalid")
            return self.render_to_response(self.get_context_data(form=form))

class IssueBackgroundView(FormMixin, ListView):
    model = IssueBackgroundImage
    template_name = "issues.html"
    form_class = ReportIssues

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['IssueBackgroundImage'] = IssueBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Support'] = Support.objects.all()
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def usercheck(request):
        try:
            report_issue = ReportIssues.objects.get(user=request.user)
            if report_issue.name.lower() != "anonymous":
                user = request.user
            else:
                user = None
        except ReportIssues.DoesNotExist:
            user = None

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ReportIssues(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:issuedone')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "issues.html", {'form': form})
        else:
            form = ReportIssues()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "issues.html", {'form': form})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            print(from_email)
            try:
                send_mail(subject, message, 'intellexcompany1@gmail.com', ['intellexcompany1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('success')
    print('success')

    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

class ContacteView(FormView):
    template_name = 'showcase/email.html'
    form_class = ContactForme
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):

        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'showcase/email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(kwargs)
        context["Contact"] = "2123123123123"
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def businessemailcontactView(request):
    if request.method == 'GET':
        form = BusinessContactForm()
    else:
        form = BusinessContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            print(from_email)
            form.save()
            try:
                send_mail(subject, message, from_email, ['intellexcompany1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('businessemailsuccess')
    print('success')

    return render(request, "businessemail.html", {'form': form})

class BusinessMailingView(FormView):
    template_name = 'businessemail.html'
    form_class = BusinessMailingForm
    success_url = reverse_lazy('showcase:businessmailingsuccess')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def form_valid(self, form):

        form.send()
        form.save()
        return super().form_valid(form)

class BusinessSuccessMailingView(TemplateView):
    template_name = 'businessmailingsuccess.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Contact'] = Contact.objects.all()[len(Contact.objects.all()) - 1]
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        print(context["Contact"])
        context["BusinessMailingContact"] = "2123123123123"
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class contact(TemplateView):
    paginate_by = 10
    template_name = 'email.html'

class businessemailcontact(TemplateView):
    paginate_by = 10
    template_name = 'businessemail.html'

class PostDetailView(View):
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, slug):
        post = get_object_or_404(Blog, slug=slug)
        comments = post.comments.filter(active=True).order_by("-created_on")
        comment_form = CommentForm()
        header_data = NavBarHeader.objects.filter(is_active=1).order_by("row")
        dropdown_data = NavBar.objects.filter(is_active=1).order_by('position')

        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'Header': header_data,
            'DropDown': dropdown_data
        }

        return render(request, self.template_name, context)

    def post(self, request, slug):
        post = get_object_or_404(Blog, slug=slug)
        comments = post.comments.filter(active=True).order_by("-created_on")
        new_comment = None
        header_data = NavBarHeader.objects.filter(is_active=1).order_by("row")
        dropdown_data = NavBar.objects.filter(is_active=1).order_by('position')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = post
            new_comment.save()

        context = {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
            'Header': header_data,
            'DropDown': dropdown_data
        }

        return render(request, self.template_name, context)

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
@csrf_exempt
def subtract_currency(request):
    if request.method == 'POST':
        user = request.user
        cost = request.POST.get('cost')
        profile = ProfileDetails.objects.get(user=user)
        try:
            profile.subtract_currency(cost)
            return JsonResponse({'status': 'success'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Not enough currency'})


class CurrencyProductView(DetailView):
    model = CurrencyMarket
    paginate_by = 10
    template_name = "currencyproduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name
        ).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(
            Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1
        )

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] is None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        in_cart = False
        if self.request.user.is_authenticated:
            try:
                order = CurrencyFullOrder.objects.get(user=self.request.user, ordered=False)
                in_cart = order.items.filter(items=self.object).exists()
            except CurrencyFullOrder.DoesNotExist:
                in_cart = False
        context['in_cart'] = in_cart

        return context


class CurrencyMarketView(EBaseView, FormView, ListView):
    model = CurrencyMarket
    template_name = "currencymarket.html"
    form_class = CurrencyViewTypeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            active_order = (CurrencyFullOrder.objects.filter(user=user, ordered=False).prefetch_related('items').first())
            context['order'] = active_order
        else:
            context['order'] = None

        context['Favicon'] = FaviconBase.objects.filter(is_active=1)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        current_user = self.request.user
        if current_user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=self.request.user).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
            try:
                active = StoreViewType.objects.get(
                    user=self.request.user,
                    is_active=1
                )
            except StoreViewType.DoesNotExist:
                active = None

            # 2) set the “store_view” string (fallback to 'stream')
            context['store_view'] = active.type if active else 'stream'

            # 3) build the same form you had in CurrencyTypeView
            context['store_view_form'] = StoreViewTypeForm(
                instance=active,
                request=self.request
            )

        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

            favorited_items = FavoriteCurrency.objects.filter(user=self.request.user).values_list('currency_market_id', flat=True)
            context['favorited_ids'] = set(favorited_items)

            show_only_favorites = self.request.GET.get('favorites') == '1'
            if show_only_favorites:
                context['Currency'] = CurrencyMarket.objects.filter(id__in=favorited_items,
                                                                    is_active=1).order_by(
                    'price')
            else:
                context['Currency'] = CurrencyMarket.objects.filter(is_active=1).order_by('price')

        context['Currency'] = CurrencyMarket.objects.filter(is_active=1).order_by(
            'price')


        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context


@login_required
def toggle_favorite_currency(request, slug):
    item = get_object_or_404(CurrencyMarket, slug=slug)
    favorite, created = FavoriteCurrency.objects.get_or_create(user=request.user, currency_market=item)
    if not created:
        favorite.delete()
    return JsonResponse({'favorited': created})


class CurrencyCheckoutView(EBaseView):
    model = CheckoutBackgroundImage
    template_name = "currencycheckout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['endowment_form'] = EndowmentForm(request=self.request)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.warning(self.request, "Please log in to see your order history.")
            return redirect("accounts/login")
        try:
            order = CurrencyFullOrder.objects.get(user=self.request.user, ordered=False)
            form = CurrencyCheckoutForm()
            context = self.get_context_data()
            context['form'] = form
            context['couponform'] = CouponForm()
            context['order'] = order
            context['DISPLAY_COUPON_FORM'] = True
            return render(self.request, "currencycheckout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("showcase:currencycheckout")

    def post(self, *args, **kwargs):
        form = CurrencyCheckoutForm(self.request.POST or None)
        endowment_form = EndowmentForm(self.request.POST, request=self.request)
        if endowment_form.is_valid():
            endowment = endowment_form.save(commit=False)
            endowment.save()

        try:
            order = CurrencyFullOrder.objects.get(user=self.request.user, ordered=False)

            if form.is_valid():
                payment_option = form.cleaned_data.get('payment_option')
                if payment_option == 'S':
                    return redirect('showcase:currencypayment', payment_option='stripe')
                elif payment_option == 'P':
                    return redirect('showcase:currencypayment', payment_option='paypal')
                elif payment_option == 'C':
                    return redirect('showcase:currencypayment', payment_option='card')
                else:
                    messages.warning(self.request, "Invalid payment option selected")
                    return redirect('showcase:currencycheckout')

            if endowment_form.is_valid():
                endowment = endowment_form.save(commit=False)
                endowment.user = self.request.user
                endowment.order = order
                endowment.save()
                messages.success(self.request, "Endowment has been successfully recorded!")

        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("showcase:currencymarket")

        return redirect('showcase:currencycheckout')


class CurrencyPaymentView(EBaseView):
    template_name = "currencypayment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=True)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=True, page=self.template_name
        ).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def save_stripe_customer(user_profile, token, save):
        if save and user_profile.stripe_customer_id:
            customer = stripe.Customer.retrieve(user_profile.stripe_customer_id)
            customer.sources.create(source=token)
        elif save:
            customer = stripe.Customer.create(email=user_profile.user.email)
            customer.sources.create(source=token)
            user_profile.stripe_customer_id = customer['id']
            user_profile.one_click_purchasing = True
            user_profile.save()
        return user_profile

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("accounts/login")

        try:
            order = CurrencyOrder.objects.filter(user=self.request.user, ordered=False)
        except CurrencyOrder.DoesNotExist:
            messages.warning(self.request, "Please add a billing address.")
            return redirect("showcase:currencycheckout")

        context = self.get_context_data(**kwargs)
        context.update({
            'order': order,
            'DISPLAY_COUPON_FORM': False,
            'STRIPE_PUBLIC_KEY': getattr(settings, 'STRIPE_PUBLIC_KEY', None),
        })

        userprofile = get_object_or_404(UserProfile, user=self.request.user)
        if userprofile.one_click_purchasing:
            cards = stripe.Customer.list_sources(
                userprofile.stripe_customer_id,
                limit=3,
                object='card'
            )
            context['card'] = cards['data'][0] if cards['data'] else None

        if getattr(userprofile, 'paypal_enabled', False):
            context['PAYPAL_CLIENT_ID'] = getattr(settings, 'PAYPAL_CLIENT_ID', None)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            messages.warning(request, "Invalid JSON received")
            return redirect("/currencypayment/stripe")

        token = data.get("token")
        if not token:
            messages.warning(request, "Invalid data received")
            return redirect("/currencypayment/stripe")

        order_user = request.user
        orders = CurrencyOrder.objects.filter(user=order_user, ordered=False)
        if not orders.exists():
            messages.warning(request, "No active orders found.")
            return redirect("/currencycheckout/")

        ruby_profile = get_object_or_404(ProfileDetails, user=order_user)

        total_amount = sum(order.get_total_price() for order in orders)
        total_currency_amount = sum(order.items.amount for order in orders)

        try:
            charge = stripe.Charge.create(
                amount=int(total_amount * 100),
                currency="usd",
                source=token,
                description=f"Order(s) for user {order_user.id}",
            )
            ruby_profile.currency_amount += total_currency_amount
            ruby_profile.total_currency_spent_30 += total_amount
            ruby_profile.total_currency_spent += total_amount
            ruby_profile.save()
            new_spent = ruby_profile.total_currency_spent_30
            new_tier = (
                Tier.objects
                    .filter(lower_bound__lte=new_spent)
                    .filter(
                        Q(upper_bound__gte=new_spent) |
                        Q(upper_bound__isnull=True)
                    )
                    .order_by('-lower_bound')
                    .first()
            )
            if new_tier and ruby_profile.tier != new_tier:
                ruby_profile.tier = new_tier
                ruby_profile.save()
            full_order = CurrencyFullOrder.objects.create(
                user=order_user,
                ordered=True,
                ordered_date=timezone.now(),
                stripe_transaction_id=charge.id,
                is_active=1
            )
            full_order.items.set(orders)
            full_order.save()

            for order in orders:
                order.ordered = True
                order.ordered_date = timezone.now()
                order.save()
            return JsonResponse({"success": "Thanks for purchasing!"})
        except stripe.error.StripeError as e:
            return JsonResponse({"error": str(e)}, status=400)


class CurrencyPayPalExecuteView(View):
    def get(self, request, *args, **kwargs):
        payer_id = request.GET.get('PayerID')
        payment_id = request.GET.get('paymentId')

        try:
            order = CurrencyOrder.objects.get(paypal_payment_id=payment_id, ordered=False)
            paypal_payment = PayPalPayment.find(payment_id)

            if paypal_payment.execute({'payer_id': payer_id}):

                payment = Payment()
                payment.paypal_payment_id = payment_id
                payment.user = self.request.user
                payment.amount = order.get_total_price()
                payment.save()
                print('your payment has been saved')

                order_items = order.items.all()
                order_items.update(ordered=True)
                print('your payment has been updated')

                order.ordered = True
                order.payment = payment
                order.ref_code = create_ref_code()
                print('the value of order is ' + order.ref_code)
                order.save()

                messages.success(self.request, 'Your order was successful!')
                return redirect('showcase:currencymarket')

            messages.error(self.request, 'Failed to process PayPal payment')
            return redirect('/currencypayment')

        except CurrencyOrder.DoesNotExist:
            messages.error(self.request, 'Order not found')
            return redirect('/currencypayment')


class CurrencyPaypalFormView(FormView):
    template_name = 'paypalpayment.html'
    form_class = CurrencyPaypalPaymentForm

    def get_initial(self):
        return {
            'business': 'your-paypal-business-address@example.com',
            'amount': 20,
            'currency_code': 'EUR',
            'item_name': 'Example item',
            'invoice': 1234,
            'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
            'return_url': self.request.build_absolute_uri(reverse('paypal-return')),
            'cancel_return': self.request.build_absolute_uri(reverse('paypal-cancel')),
            'lc': 'EN',
            'no_shipping': '1',
        }


@allow_guest_user
def currency_add_to_cart(request, slug):
    item = get_object_or_404(CurrencyMarket, slug=slug)

    order_item_qs = CurrencyOrder.objects.filter(
        user=request.user,
        items=item,
        ordered=False
    )

    if order_item_qs.exists():
        order_item = order_item_qs.first()
        order_item.quantity += 1
        order_item.save()
        messages.info(request, f"Updated quantity of \"{item.name}\" in your cart.")
    else:
        order_item = CurrencyOrder.objects.create(
            user=request.user,
            items=item,
            ordered=False,
            quantity=1,
            slug=item.slug
        )
        messages.info(request, f"Added \"{item.name}\" to your cart.")

    order_qs = CurrencyFullOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()
    else:
        order = CurrencyFullOrder.objects.create(
            user=request.user,
            ordered=False,
            ordered_date=timezone.now()
        )

    if not order.items.filter(id=order_item.id).exists():
        order.items.add(order_item)

    return redirect("showcase:currencycheckout")

@login_required
def currency_remove_from_cart(request, slug):

    order_item = get_object_or_404(
        CurrencyOrder,
        items__slug=slug,
        user=request.user,
        ordered=False
    )

    order_qs = CurrencyFullOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()
        if order.items.filter(id=order_item.id).exists():
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, f"Removed \"{order_item.items.name}\" from your cart.")
        else:
            messages.info(request, "This item is no longer in your cart.")
        return redirect("showcase:currencycheckout")
    else:
        messages.info(request, "You do not have an active cart.")
        return redirect("showcase:currencymarket")


def currency_get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(
            request,
            "Sorry, this coupon seems to have either expired or does not exist. Do you want to try another one?"
        )
        return redirect("showcase:currencycheckout")

class CurrencyAddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(user=self.request.user,
                                          ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("showcase:currencycheckout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("showcase:currencycheckout")

class GiftCodeRedemptionView(LoginRequiredMixin, ListView, FormMixin):
    model = GiftCodeRedemption
    template_name = "giftcoderedemption.html"
    context_object_name = "redemptions"
    form_class = GiftCodeForm

    def get_queryset(self):
        return GiftCodeRedemption.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, user=request.user)
        if self.request.user.is_authenticated:
            if form.is_valid():
                code_str = form.cleaned_data['code']
                gift_code = GiftCode.objects.get(code=code_str)

                if gift_code.tracking_total_uses < gift_code.total_uses and gift_code.is_active == 1:
                    GiftCodeRedemption.objects.create(user=request.user, gift_code=gift_code)

                    profile = ProfileDetails.objects.filter(user=request.user).first()
                    if profile:
                        profile.currency_amount += gift_code.value
                        profile.save()

                    gift_code.tracking_total_uses += 1
                    gift_code.save()

                    messages.success(request, "Gift code redeemed successfully.")
                    return redirect('showcase:giftcodeclaimed')
                else:
                    messages.error(request, "This gift code has reached its maximum number of uses or is inactive.")
            else:
                messages.error(request, "Form submission invalid.")
        else:
            return redirect('accounts/login')

        return self.get(request, *args, **kwargs)

class GiftCodeClaimedView(ListView):
    model = Lottery
    template_name = "giftcodeclaimed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Profile'] = UpdateProfile.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def index(request):
    return redirect('showcase')

@login_required
def currency_reduce_quantity_item(request, slug):
    item = get_object_or_404(CurrencyOrder, slug=slug)
    order_qs = CurrencyOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = CurrencyOrder.objects.filter(item=item,
                                                      user=request.user,
                                                      ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("showcase:order-summary")
        else:
            messages.info(request, "This Item is not in your cart")
            return redirect("showcase:order-summary")
    else:

        messages.info(request, "You do not have an Order")
        return redirect("showcase:order-summary")

class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "ehome.html"

class Featured(ListView):
    model = Item
    paginate_by = 10
    template_name = "featuredproducts.html"

class ProductView(DetailView):
    model = Item
    paginate_by = 10
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        context['quick_items'] = item.images.all()
        context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def product_detail_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    quick_items = item.images.all()
    context = {
        'item': item,
        'quick_items': quick_items,
    }
    return render(request, 'product.html', context)

class OrderSummaryView(EBaseView):
    model = OrderBackgroundImage
    template_name = "order-summary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        user_profile_exists = UserProfile2.objects.filter(user=self.request.user, is_active=1).exists()
        context['user_profile_exists'] = user_profile_exists

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.warning(self.request, "Please log in to see your order history.")
            return redirect("accounts/login")
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = self.get_context_data()
            context['object'] = order
            return render(self.request, 'order-summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("showcase:ehome")

def check_and_deduct_currency(user, amount_required):
    try:
        profile = ProfileDetails.objects.get(user=user)
        if profile.currency_amount < amount_required:
            return False, profile.currency_amount
        profile.currency_amount -= amount_required
        profile.save()
        return True, profile.currency_amount
    except ProfileDetails.DoesNotExist:
        return False, 0

class CheckoutView(EBaseView):
    model = CheckoutBackgroundImage
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['address'] = Address.objects.filter(is_active=1, user=self.request.user).first()
        context.update(kwargs)

        user_profile_exists = UserProfile2.objects.filter(user=self.request.user, is_active=1).exists()
        context['user_profile_exists'] = user_profile_exists

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)

            if hasattr(order, "update_total_prices"):
                order.update_total_prices()

            try:
                currency_order = CurrencyOrder.objects.filter(user=self.request.user, ordered=False)
                if hasattr(currency_order, "update_total_prices"):
                    currency_order.update_total_prices()
            except CurrencyOrder.DoesNotExist:
                currency_order = None

            all_items_currency_based = self.are_all_items_currency_based(order)
            form = CheckoutForm(all_items_currency_based=all_items_currency_based)

            shipping_address_qs = Address.objects.filter(user=self.request.user, address_type='S', is_active=1)
            if shipping_address_qs.exists():
                shipping_address = shipping_address_qs.first()
                form.fields['shipping_address'].initial = shipping_address.street_address
                form.fields['shipping_address2'].initial = shipping_address.apartment_address
                form.fields['shipping_country'].initial = shipping_address.country
                form.fields['shipping_zip'].initial = shipping_address.zip

            billing_address_qs = Address.objects.filter(user=self.request.user, address_type='B', is_active=1)
            if billing_address_qs.exists():
                billing_address = billing_address_qs.first()
                form.fields['billing_address'].initial = billing_address.street_address
                form.fields['billing_address2'].initial = billing_address.apartment_address
                form.fields['billing_country'].initial = billing_address.country
                form.fields['billing_zip'].initial = billing_address.zip

            context = self.get_context_data(
                form=form,
                couponform=CouponForm(),
                order=order,
                currency_order=currency_order,
                DISPLAY_COUPON_FORM=True
            )

            return render(self.request, self.template_name, context)

        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("showcase:checkout")

    def post(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            all_items_currency_based = self.are_all_items_currency_based(order)
            form = CheckoutForm(request.POST or None, all_items_currency_based=all_items_currency_based)
            print(f'Form valid: {form.is_valid()}')
            if form.is_valid():
                if form.fields['payment_option'].widget.is_hidden:
                    print('hidden formats')

                    total_order_currency_amount = sum(
                        item.item.currency_price for item in OrderItem.objects.filter(order=order)
                    )

                    sufficient_funds, remaining_amount = check_and_deduct_currency(
                        request.user, total_order_currency_amount
                    )
                    if not sufficient_funds:
                        messages.warning(request, "You do not have enough currency to complete this order.")
                        context = self.get_context_data(form=form)
                        context['order'] = order
                        return redirect('showcase:currencymarket')

                    order.deduct_currency_amount()

                    order.ordered = True
                    order.ordered_date = timezone.now()
                    order.save()

                    return redirect('showcase:orderdone')

            else:
                print("Form errors:", form.errors)
                messages.warning(request, "Form is not valid. Please correct the errors below.")
                context = self.get_context_data(form=form)
                context['order'] = order
                return render(request, self.template_name, context)

            use_default_shipping = form.cleaned_data.get('use_default_shipping')
            order.deduct_currency_amount()
            if use_default_shipping:
                address_qs = Address.objects.filter(user=self.request.user, address_type='S', default=True)
                if address_qs.exists():
                    shipping_address = address_qs[0]
                    order.shipping_address = shipping_address
                    order.save()
                else:
                    messages.info(request, "No default shipping address available")
                    return redirect('showcase:checkout')
            else:
                shipping_address1 = form.cleaned_data.get('shipping_address')
                shipping_address2 = form.cleaned_data.get('shipping_address2')
                shipping_country = form.cleaned_data.get('shipping_country')
                shipping_zip = form.cleaned_data.get('shipping_zip')

                if self.is_valid_form([shipping_address1, shipping_country, shipping_zip]):
                    shipping_address = Address(
                        user=self.request.user,
                        street_address=shipping_address1,
                        apartment_address=shipping_address2,
                        country=shipping_country,
                        zip=shipping_zip,
                        address_type='S'
                    )
                    shipping_address.save()
                    order.shipping_address = shipping_address
                    order.save()

                    set_default_shipping = form.cleaned_data.get('set_default_shipping')
                    if set_default_shipping:
                        shipping_address.default = True
                        shipping_address.save()
                else:
                    address_qs = Address.objects.filter(user=self.request.user, address_type='S', default=True)
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:
                        messages.info(self.request, "kindly Please fill in the required shipping address fields")
                        return redirect('showcase:checkout')

            use_default_billing = form.cleaned_data.get('use_default_billing')
            same_billing_address = form.cleaned_data.get('same_billing_address')

            if same_billing_address:
                billing_address = shipping_address
                billing_address.pk = None
                billing_address.save()
                billing_address.address_type = 'B'
                billing_address.save()
                order.billing_address = billing_address
                order.save()
            elif use_default_billing:
                address_qs = Address.objects.filter(user=self.request.user, address_type='B', default=True)
                if address_qs.exists():
                    billing_address = address_qs[0]
                    order.billing_address = billing_address
                    order.save()
                else:
                    messages.info(self.request, "No default billing address available")
                    return redirect('showcase:checkout')
            else:
                billing_address1 = form.cleaned_data.get('billing_address')
                billing_address2 = form.cleaned_data.get('billing_address2')
                billing_country = form.cleaned_data.get('billing_country')
                billing_zip = form.cleaned_data.get('billing_zip')

                if self.is_valid_form([billing_address1, billing_country, billing_zip]):
                    billing_address = Address(
                        user=self.request.user,
                        street_address=billing_address1,
                        apartment_address=billing_address2,
                        country=billing_country,
                        zip=billing_zip,
                        address_type='B'
                    )
                    billing_address.save()
                    order.billing_address = billing_address
                    order.save()

                    set_default_billing = form.cleaned_data.get('set_default_billing')
                    if set_default_billing:
                        billing_address.default = True
                        billing_address.save()
                else:
                    address_qs = Address.objects.filter(user=self.request.user, address_type='S', default=True)
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:
                        messages.info(self.request, "Please fill in the required billing address fields")
                        return redirect('showcase:checkout')

            payment_option = form.cleaned_data.get('payment_option')
            return redirect('showcase:payment', payment_option=payment_option)

            print(form.errors)
            messages.warning(self.request, "Form is not valid. Please correct the errors below.")
            context = self.get_context_data(form=form, order=order)
            return render(self.request, self.template_name, context)

        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("showcase:order-summary")
        except Exception as e:
            messages.error(self.request, str(e))
            context = self.get_context_data(form=form)
            return render(self.request, self.template_name, context)

    def are_all_items_currency_based(self, order):
        return all(order_item.item.is_currency_based for order_item in OrderItem.objects.filter(order=order))

    def is_valid_form(self, values):
        valid = True
        for field in values:
            if field == '':
                valid = False
        return valid


class PaymentView(EBaseView):
    template_name = "payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.billing_address:
            context = self.get_context_data(**kwargs)
            context['order'] = order
            context['DISPLAY_COUPON_FORM'] = False
            context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
            userprofile = User.objects.get(username=self.request.user.username)

            if hasattr(userprofile, "one_click_purchasing") and userprofile.one_click_purchasing:

                cards = stripe.Customer.list_sources(
                    userprofile.stripe_customer_id,
                    limit=3,
                    object='card'
                )
                card_list = cards['data']
                if card_list:
                    context['card'] = card_list[0]

            if hasattr(userprofile, 'paypal_enabled') and userprofile.paypal_enabled:
                context['PAYPAL_CLIENT_ID'] = settings.PAYPAL_CLIENT_ID

            return render(self.request, "payment.html", context)
        else:
            messages.warning(self.request, "You have not added a billing address.")
            return redirect("showcase:checkout")

    def post(self, *args, **kwargs):
        order_user = self.request.user
        orders = Order.objects.filter(user=order_user, ordered=False)

        if not orders.exists():
            messages.warning(self.request, "No active orders found.")
            return redirect("/checkout/")

        if self.request.content_type == 'application/json':
            try:
                data = json.loads(self.request.body.decode('utf-8'))
            except json.JSONDecodeError:
                messages.warning(self.request, "Invalid JSON received")
                return redirect("/payment/stripe")
            token = data.get('token')
            payment_method = data.get('payment_method')
        else:
            token = self.request.POST.get('token')
            payment_method = self.request.POST.get('payment_method')

        ruby_profile = get_object_or_404(ProfileDetails, user=order_user)

        total_amount = sum(order.get_total_price() for order in orders)
        total_currency_amount = sum(
            item.orderprice * item.quantity for order in orders for item in order.items.all()
        )

        if token:
            try:
                # Assuming single charge for all orders
                charge = stripe.Charge.create(
                    amount=int(total_amount * 100),
                    currency="usd",
                    source=token,
                    description=f"User {order_user.id} purchase",
                )
                ruby_profile.total_currency_amount += total_amount
                ruby_profile.save()
                return JsonResponse({"success": "Thanks for purchasing!"})
            except stripe.error.StripeError as e:
                return JsonResponse({"error": str(e)}, status=400)

        messages.warning(self.request, "Invalid data received")
        return redirect("/payment/stripe")


class PayPalExecuteView(View):
    def get(self, request, *args, **kwargs):
        payer_id = request.GET.get('PayerID')
        payment_id = request.GET.get('paymentId')

        try:
            order = Order.objects.get(paypal_payment_id=payment_id, ordered=False)
            paypal_payment = PayPalPayment.find(payment_id)

            if paypal_payment.execute({'payer_id': payer_id}):
                payment = Payment()
                payment.paypal_payment_id = payment_id
                payment.user = self.request.user
                payment.amount = order.get_total_price()
                payment.save()

                order_items = order.items.all()
                order_items.update(ordered=True)

                order.ordered = True
                order.payment = payment
                order.ref_code = create_ref_code()
                order.save()

                messages.success(self.request, 'Your order was successful!')
                return redirect('showcase:ehome')

            messages.error(self.request, 'Failed to process PayPal payment')
            return redirect('/payment')

        except Order.DoesNotExist:
            messages.error(self.request, 'Order not found')
            return redirect('/payment')


class PaypalFormView(FormView):
    template_name = 'paypalpayment.html'
    form_class = PaypalPaymentForm

    def get_initial(self):
        return {
            'business': 'your-paypal-business-address@example.com',
            'amount': 20,
            'currency_code': 'EUR',
            'item_name': 'Example item',
            'invoice': 1234,
            'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
            'return_url': self.request.build_absolute_uri(reverse('paypal-return')),
            'cancel_return': self.request.build_absolute_uri(reverse('paypal-cancel')),
            'lc': 'EN',
            'no_shipping': '1',
        }

class OrderDoneView(ListView):
    model = CheckoutBackgroundImage
    template_name = "orderdone.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        try:
            order = Order.objects.filter(user=self.request.user, ordered=True).order_by('-ordered_date').first()
            context['order'] = order
        except Order.DoesNotExist:
            context['order'] = None

        context.update(kwargs)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

@allow_guest_user
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        order_item = OrderItem.objects.filter(
            item=item, user=request.user, ordered=False
        ).first()

        if order_item:

            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"\"{order_item.item.title}\" was added to your cart.")
        else:

            order_item = OrderItem(item=item, user=request.user, ordered=False, quantity=1)
            order_item.save()
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")

        address = Address.objects.filter(user=request.user, is_active=1).first()
        if address:
            order.shipping_address = address
            order.billing_address = address
            order.save()

        return redirect("showcase:order-summary")

    else:

        order = Order.objects.create(
            user=request.user,
            ordered=False,
            ordered_date=timezone.now()
        )
        print("Order created")

        address = Address.objects.filter(user=request.user, is_active=1).first()
        if address:
            order.shipping_address = address
            order.billing_address = address
            order.save()
            print('Added an address to the created order')

        order_item = OrderItem(item=item, user=request.user, ordered=False, quantity=1)
        order_item.save()
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("showcase:order-summary")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,
                                                  user=request.user,
                                                  ordered=False)[0]
            order_item.delete()
            messages.info(
                request, "Item \"" + order_item.item.title +
                         "\" was removed from your cart")
            return redirect("showcase:order-summary")
        else:
            messages.info(request, "This item is no longer in your cart")
            return redirect("showcase:product", slug=slug)
    else:

        messages.info(request, "You do not seem to have an order currently")
        return redirect("showcase:product", slug=slug)

def index(request):
    return redirect('showcase')

@login_required
def reduce_quantity_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,
                                                  user=request.user,
                                                  ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("showcase:order-summary")
        else:
            messages.info(request, "This Item is not in your cart")
            return redirect("showcase:order-summary")
    else:

        messages.info(request, "You do not have an Order")
        return redirect("showcase:order-summary")


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits,
                                  k=20))

from django.db.models import Count, Avg

def products(request):
    context = {'items': Item.objects.all()}
    return render(request, "products.html", context)

def reviewproducts(request, pid):
    product = Item.objects.get(pid=pid)

    products = ProductReview.objects.filter(product=product).order_by("-date")

    reviews = ProductReview.objects.filter(Item=Item)

    average_rating = ProductReview.objects.filter(Item=Item).aggregate(rating=Avg('rating'))

    p_image = Item.image.all()

    context = {
        "p": products,
        "p_image": p_image,
        "average_rating": average_rating,
        "review": review,
        "products": products,
    }

    return render(request, "showcase:index.html", context)

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

class ItemDetailView(DetailView):
    model = Item
    paginate_by = 10
    template_name = "product.html"

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,
                                                  user=request.user,
                                                  ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("showcase:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("showcase:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("showcase:product", slug=slug)

def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(
            request,
            "Sorry, this coupon seems to have either expired or does not exist. Do you want to try another one?"
        )
        return redirect("showcase:checkout")

class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(user=self.request.user,
                                          ordered=False)
                order.coupon = get_coupon(self.request, code)

                if order.coupon:
                    order.save()
                    messages.success(self.request, "Successfully added coupon")
                    return redirect("showcase:checkout")
                else:
                    messages.info(self.request, "Coupon did not work, maybe it expired?")
                    return redirect("showcase:checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("showcase:checkout")

class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {'form': form}
        return render(self.request, "request_refund.html", context)

    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST)
        if form.is_valid():
            ref_code = form.cleaned_data.get('ref_code')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')

            try:
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.email = email
                refund.save()

                messages.info(self.request, "Your request was received.")
                return redirect("showcase:request-refund")

            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist.")
                return redirect("showcase:request-refund")

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'showcase/profile.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'showcase:edit_profile.html'
    success_url = reverse_lazy('login')

class SuccessView(TemplateView):
    template_name = 'success.html'

class CancelView(TemplateView):
    template_name = 'cancel.html'

def product_view(request, slug):
    item = get_object_or_404(Item, slug=slug)
    context = {
        'item': item,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'product.html', context)

@csrf_exempt
@require_POST
def create_checkout_session(request, slug):
    item = get_object_or_404(Item, slug=slug)

    if item.is_currency_based:
        return JsonResponse({'error': 'This item requires in-game currency and cannot be purchased here.'}, status=400)

    price = item.discount_price if item.discount_price else item.price
    if price is None:
        return JsonResponse({'error': 'Price not set for this item'}, status=400)

    currency = item.currency.code.lower() if item.currency else 'usd'
    print('the currency is ' + currency)

    if currency not in ['usd', 'eur']:
        return JsonResponse({'error': 'Currency not supported'}, status=400)

    amount = int(price * 100)

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': currency,
                    'product_data': {'name': item.title},
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('showcase:success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('showcase:cancel')),
        )
        print('one-click checkout session created')
        return JsonResponse({'session_id': checkout_session.id})
    except stripe.error.StripeError as e:
        print('there were errors with the submition of the one-click checkout ')
        print('the errors are ' + str(e))
        return JsonResponse({'errors here': str(e)}, status=400)

@csrf_exempt
@require_POST
def create_currency_checkout_session(request, slug):
    item = get_object_or_404(CurrencyMarket, slug=slug)

    if item.is_currency_based:
        return JsonResponse({'error': 'This item requires in-game currency and cannot be purchased here.'}, status=400)

    price = item.discount_price if item.discount_price else item.price
    if price is None:
        return JsonResponse({'error': 'Price not set for this currency item'}, status=400)

    currency = item.currency.code.lower() if item.currency else 'usd'
    print('the currency is ' + currency)

    if currency not in ['usd', 'eur']:
        return JsonResponse({'error': 'Currency not supported'}, status=400)

    amount = int(price * 100)

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': currency,
                    'product_data': {'name': item.title},
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('showcase:success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('showcase:cancel')),
        )
        print('one-click checkout session created')
        return JsonResponse({'session_id': checkout_session.id})
    except stripe.error.StripeError as e:
        print('there were errors with the submition of the one-click checkout ')
        print('the errors are ' + str(e))
        return JsonResponse({'errors here': str(e)}, status=400)
# payments/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import get_paypal_access_token
from django.conf import settings
import requests

@csrf_exempt
def create_order(request):
    access_token = get_paypal_access_token()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    data = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": "10.00"
            }
        }]
    }

    response = requests.post(
        f"{settings.PAYPAL_API_BASE}/v2/checkout/orders",
        headers=headers,
        json=data
    )

    return JsonResponse(response.json())


@csrf_exempt
def capture_order(request):
    import json
    access_token = get_paypal_access_token()
    body = json.loads(request.body)
    order_id = body.get('orderID')

    response = requests.post(
        f"{settings.PAYPAL_API_BASE}/v2/checkout/orders/{order_id}/capture",
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
    )

    return JsonResponse(response.json())


@csrf_exempt
def create_subscription(request):
    import json
    access_token = get_paypal_access_token()
    body = json.loads(request.body)
    plan_id = body.get('plan_id')  # send from JS

    response = requests.post(
        f"{settings.PAYPAL_API_BASE}/v1/billing/subscriptions",
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        },
        json={
            "plan_id": plan_id,
            "application_context": {
                "brand_name": "My Django App",
                "return_url": "http://localhost:8000/payment/success/",
                "cancel_url": "http://localhost:8000/payment/cancel/"
            }
        }
    )

    return JsonResponse(response.json())


from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

from .forms import (EditProfileForm)

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def profile(request, user):
    args = {'user': user}
    return render(request, 'profile.html', args)

def edit_profile(request, pk):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('showcase:profile', pk=pk)

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

class ProfileEditView(FormView):
    template_name = 'profile_edit.html'
    form_class = ProfileDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return redirect('showcase:profile', pk=profile.pk)

    def post(self, request, pk=None):
        profile = ProfileDetails.objects.filter(user=request.user).first()
        if profile:
            form = self.form_class(request.POST, request.FILES, instance=profile)
        else:
            form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('showcase:profile', pk=profile.pk)
        return render(request, self.template_name, {'form': form})

class SignupView(FormMixin, ListView):
    model = SignupBackgroundImage
    template_name = "cv-form.html"
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup'] = SignupBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        print('signup')
        if request.method == 'POST':
            print('post')
            form = SignUpForm(request.POST)
            if form.is_valid():
                print('is_valid')
                user = form.save()
                user.refresh_from_db()
                user.save()
                raw_password = form.cleaned_data.get('password')

                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                subject = "Welcome to PokeTrove!"
                message = f"Hello {user.username}, thank you for becoming a member of the PokeTrove Community!"
                email_from = settings.EMAIL_HOST_USER
                recipent_list = [user.email, ]
                send_mail(subject, message, email_from, recipent_list)

                return redirect('showcase:showcase')
                messages.info(request, "You have signed up successfully! Welcome!")
        else:
            form = SignUpForm()
        return render(request, 'cv-form.html', {'form': form})

class ChangePasswordView(BaseView):
    model = ChangePasswordBackgroundImage
    template_name = "/accounts/change-password.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'),
                                                  is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/login')

        else:
            return redirect('showcase:accounts/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'registration/change-password.html', args)

from .forms import (
    RegistrationForm, )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showcase/index.html')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'registration/regform.html', args)

@allow_guest_user
def my_view(request):
    assert request.user.is_authenticated
    return render(request, "showcase.html")

from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:

        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:

        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session["customer_details"]["email"]
        product_id = session["metadata"]["product_id"]

        product = Product.objects.get(id=product_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
            recipient_list=[customer_email],
            from_email="IntelleXCompany.com"
        )

    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        customer_email = stripe_customer['email']
        product_id = intent["metadata"]["product_id"]

        product = Product.objects.get(id=product_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
            recipient_list=[customer_email],
            from_email="matt@test.com"
        )

    return HttpResponse(status=200)

class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            product_id = self.kwargs["pk"]
            product = Product.objects.get(id=product_id)
            intent = stripe.PaymentIntent.create(
                amount=product.price,
                currency='usd',
                customer=customer['id'],
                metadata={
                    "product_id": product.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})

class DonateView(ListView):
    model = DonorBackgroundImage
    template_name = "donate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'),
                                                  is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['donation'] = Donate.objects.filter(is_active=1)
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY

        texts = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        context['TextBySection'] = {text.section: text for text in texts}

        donors = Donate.objects.filter(is_active=1)
        context['Donator'] = donors
        for donor in context['Donator']:
            profile = ProfileDetails.objects.filter(user=donor.user).first()
            if profile:
                donor.donor_profile_picture_url = profile.avatar.url
                donor.donor_profile_url = donor.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])
        nickname = request.POST.get('nickname')
        anonymous = request.POST.get('anonymous') == 'on'

        donation = Donate.objects.create(
            amount=amount,
            donor=request.user,
            nickname=nickname,
            anonymous=anonymous,
            is_active=1,
        )
        customer = stripe.Customer.create(email=request.POST['email'],
                                          name=request.POST['nickname'],
                                          source=request.POST['stripeToken']

                                          )

        charge = stripe.Charge.create(customer=customer,
                                      amount=amount * 100,
                                      currency='usd',
                                      description="Donation")

    return redirect(reverse('showcase:patreoned', args=[amount]))

class PatreonedView(ListView):
    model = DonorBackgroundImage
    template_name = "patreoned.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'),
                                                  is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def successMsg(request, args):
        amount = args
        return render(request, 'patreoned.html', {'amount': amount})

class DonateHistoryView(ListView):
    model = DonorBackgroundImage
    template_name = "mydonationhistory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'),
                                                  is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['donations'] = Donate.objects.filter(donor=self.request.user, is_active=1)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

class DonationsView(ListView):
    model = DonorBackgroundImage
    template_name = "donors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'),
                                                  is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)

        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)

        donation = Donate.objects.filter(is_active=1).order_by('-timestamp')

        context['donations'] = donation

        for donation in context['donations']:
            profile = ProfileDetails.objects.filter(user=donation.donor).first()
            if profile:
                donation.donor_profile_picture_url = profile.avatar.url
                donation.donor_profile_url = donation.get_profile_url()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.http import JsonResponse
from .models import UserProfile

def get_user_currency(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        currency_amount = profile.currency_amount
        currency_symbol = profile.currency.symbol
        return JsonResponse({"currency_amount": currency_amount, "currency_symbol": currency_symbol})
    else:
        return JsonResponse({"error": "User not authenticated"}, status=403)

@allow_guest_user
def hello_guest(request):
    """
  This view will always have an authenticated user, but some may be guests.
  The default username generator will create a UUID4.

  Example response: "Hello, b5daf1dd-1a2f-4d18-a74c-f13bf2f086f7!
  """
    return HttpResponse("Hello, {request.user.username}!")

from guest_user.decorators import guest_user_required

from django.template.response import TemplateResponse

@guest_user_required
def why_convert(request):
    """Show reasons why to convert, only for guest users."""
    return TemplateResponse("reasons-to-convert.html")

from django.dispatch import receiver

class ContactViewe(CreateView):
    template_name = 'contact.html'
    form_class = ContactForme
    success_url = reverse_lazy('showcase:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Contact'] = Contact.objects.order_by('-id').first()
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        print(context["Contact"])

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def form_valid(self, form):

        form.send()
        return super().form_valid(form)

class ContactSuccessView(BaseView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Contact'] = Contact.objects.all()[len(Contact.objects.all()) - 1]
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        print(context["Contact"])

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from twilio.rest import Client
from .forms import SellerApplicationForm

from django_otp.plugins.otp_totp.models import TOTPDevice
from .forms import SellerApplicationForm

import pyotp
import qrcode
from django.shortcuts import render
from io import BytesIO
from django.http import FileResponse

import base64
from django.core.mail import send_mail
import pyotp

class SellerApplicationView(FormMixin, LoginRequiredMixin, ListView):
    model = SellerApplication
    template_name = "sellerapplication.html"
    form_class = SellerApplicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.warning(self.request, "Please log in to apply.")
            return redirect("accounts/login")
        return super().get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = SellerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            application = form.save()

            device = TOTPDevice.objects.create(user=application.user)
            device.save()

            secret_key = base64.b32encode(device.bin_key).decode()

            totp = pyotp.TOTP(secret_key)
            otp = totp.now()

            user = form.save()
            subject = "Your One-Time Password"
            message = f'Your OTP is: {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipent_list = [application.email, ]
            send_mail(subject, message, email_from, recipent_list)

            request.session['device_id'] = device.id

            return redirect('showcase:verify_otp')
        else:
            form = SellerApplicationForm()

        return render(request, 'submit_application.html', {'form': form})

import base64
from django.http import HttpResponse
from PIL import Image
import io

def submit_seller_application(request):
    if request.method == 'POST':
        form = SellerApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()

            device = TOTPDevice.objects.create(user=application.user)
            device.save()

            secret_key = device.bin_key

            otp_provision_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(name=request.user.email,
                                                                             issuer_name='YourApp')

            qr_img = qrcode.make(otp_provision_uri)

            byte_arr = io.BytesIO()
            qr_img.save(byte_arr, format='PNG')
            byte_arr.seek(0)

            base64_image = base64.b64encode(byte_arr.getvalue()).decode('utf-8')

            request.session['device_id'] = device.id

            return render(request, 'submit_application.html',
                          {'form': form, 'qr_code_data_url': f'data:image/png;base64,{base64_image}'})
    else:
        form = SellerApplicationForm()

    return render(request, 'submit_application.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        user_entered_otp = request.POST.get('otp')
        resend_request = request.POST.get('resend_otp')

        if resend_request:
            try:

                device_id = request.session.get('device_id')
                device = TOTPDevice.objects.get(id=device_id)

                secret_key = base64.b32encode(device.bin_key).decode()
                totp = pyotp.TOTP(secret_key)
                new_otp = totp.now()

                user = request.user
                subject = "Your One-Time Password (Resent)"
                message = f'Your new OTP is: {new_otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail(subject, message, email_from, recipient_list)

                request.session['otp_timestamp'] = datetime.now().isoformat()

                messages.success(request, 'A new OTP has been sent to your registered email.')
            except TOTPDevice.DoesNotExist:
                messages.error(request, 'Device not found. Please try again.')
            except Exception as e:
                messages.error(request, f'An error occurred while resending OTP: {e}')

            return render(request, 'verify_otp.html')

        try:
            device_id = request.session.get('device_id')
            device = TOTPDevice.objects.get(id=device_id)

            secret_key = base64.b32encode(device.bin_key).decode()

            totp = pyotp.TOTP(secret_key)

            if totp.verify(int(user_entered_otp)):
                try:
                    application = SellerApplication.objects.get(user=request.user)
                    application.email_verified = True
                    application.save()

                    user = request.user
                    user.email_verified = True
                    user.save()

                    messages.success(request, 'OTP verified successfully.')
                    return render(request, 'sellerapplicationfinish.html')
                except SellerApplication.DoesNotExist:
                    messages.error(request, 'Seller application not found.')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
        except TOTPDevice.DoesNotExist:
            messages.error(request, 'Device not found. Please try again.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

    return render(request, 'verify_otp.html')

class BusinessEmailViewe(CreateView):
    template_name = 'businessemail.html'
    form_class = BusinessContactForm
    success_url = reverse_lazy('showcase:businessmailingsuccess')

    def form_valid(self, form):

        form.send()
        return super().form_valid(form)

class BusinessEmailSuccessView(BaseView):
    template_name = 'businessmailingsuccess.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['BusinessMailingContact'] = BusinessMailingContact.objects.all()[
            len(BusinessMailingContact.objects.all()) - 1]
        print(context["BusinessMailingContact"])

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import FeedbackForm
import json

from .fusioncharts import FusionCharts
from showcase.models import Feedback
from django.core.mail import send_mail

data = [
    ['Year', 'Sales', 'Expenses'],
    [2004, 1000, 400],
    [2005, 1170, 460],
    [2006, 660, 1120],
    [2007, 1030, 540]
]


def detail(request, slug):
    try:
        item = Item.objects.get(slug=slug)
    except Item.DoesNotExist:
        raise Http404("Product does not exist")
    company_list = Item.objects.all()
    context = {
        "company_list": company_list,
        "Item": Item,

    }
    return render(request, 'review_detail.html', context)

def review(request, slug):
    if request.POST:
        form = FeedbackForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = FeedbackForm()

    try:
        company = Item.objects.get(Item, slug=slug)
    except Item.DoesNotExist:
        raise Http404("Product does not exist")
    context = {
        "Item": Item,
        "form": form,

    }
    return render(request, 'reviews.html', context)

def index(request):
    username = request.user.username
    is_employee = request.user.groups.filter(name='Employees').exists()
    is_manager = request.user.groups.filter(name='Managers').exists()

    if is_employee:
        company_list = Item.objects.filter(employee=request.user)
        context = {
            "companies": company_list,
            "is_employee": is_employee,
            "is_manager": is_manager
        }

        return render(request, 'employee_index.html', context)
    elif request.user.is_staff:

        dataSource = {}

        dataSource['chart'] = {
            "caption": "Graph for Companies versus their respective reviews",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "xaxisname": "Companies",
            "yaxisname": "Reviews",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor": "#999999",
            "showValues": "0",
            "divlineColor": "#999999",
            "divLineIsDashed": "1",
            "showAlternateHGridColor": "0",
            "exportEnabled": "1"
        }

        reviewsDataSource = {}

        reviewsDataSource['chart'] = {
            "caption": "Number of reviews added",
            "subcaption": "Last Year",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "xaxisname": "Months",
            "yaxisname": "Reviews",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor": "#999999",
            "showValues": "0",
            "divlineColor": "#999999",
            "divLineIsDashed": "1",
            "showAlternateHGridColor": "0",
            "exportEnabled": "1"
        }

        reviewsDataSource['data'] = []

        for i in range(1, 13):
            data = {}
            currentMonth = datetime.date(2008, i, 1).strftime('%B')
            data['label'] = currentMonth
            count = 0
            for key in Feedback.objects.all():
                if currentMonth == key.timestamp.strftime("%B"):
                    count = count + 1
            data['value'] = count
            reviewsDataSource['data'].append(data)

        dataSource['data'] = []

        for key in Company.objects.all():
            data = {}
            data['label'] = key.name
            data['value'] = Feedback.objects.filter(Company=key).count()
            dataSource['data'].append(data)

        column2D = FusionCharts("column2D", "ex1", "600", "400", "chart-1", "json", dataSource)

        column3D = FusionCharts("column2D", "ex2", "600", "400", "chart-2", "json", reviewsDataSource)

        company_list = Company.objects.all()
        review_list = Feedback.objects.all()
        employees = User.objects.filter(groups__name='Employees')
        managers = User.objects.filter(groups__name='Managers')

        context = {
            "companies": company_list,
            "employees": employees,
            "managers": managers,
            "chart": column2D.render(),
            "chart2": column3D.render(),
            "reviews": review_list,
            "latestReviews": Feedback.objects.order_by('-timestamp')[:5]
        }

        return render(request, 'admin_index.html', context)
    elif is_manager:
        employees = User.objects.filter(groups__name='Employees')
        companies = Company.objects.all()

        context = {
            "employees": employees,
            "companies": companies
        }

        return render(request, 'manager_index.html', context)
    else:
        companies = Company.objects.all()

        context = {
            "companies": companies,
        }

        return render(request, 'customer_index.html', context)

def thanks(request):
    return render(request, 'thank-you.html')

"""@login_required(login_url='/accounts/login/')
def create_company(request):
   if request.POST:
       form = CompanyForm(request.POST)

       if form.is_valid():
           instance = form.save(commit=False)
           instance.save()
           return HttpResponseRedirect('/thanks')
   else:
       form = CompanyForm()
   return render(request,'create_company.html',{'form':form })"""

from django.template.loader import render_to_string

def sendEmployeeEmailOnAddReview(Company, form):
    subject, from_email, to = "Tech Greatness.com : A customer has added a review", "IntelleXCompany1@gmail.com", \
        Company.employee.email

    context = {
        "employee": Company.employee.get_full_name(),
        "Company": Company,
        "form": form,
        "first_name": form.cleaned_data['first_name'],
        "last_name": form.cleaned_data['last_name'],
        "comment": form.cleaned_data['comment'],
    }

    msg_plain = render_to_string('add_review_email_template.txt', context)
    msg_html = render_to_string('add_review_email_template.html', context)

    send_mail(subject, msg_plain, from_email, [to], fail_silently=False, html_message=msg_html)

from .models import Item

@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Order, Feedback
from .forms import FeedbackForm

@login_required
def create_feedback(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.order = order
            feedback.save()
            return redirect('my_orders')
    else:
        form = FeedbackForm()
    return render(request, 'create_feedback.html', {'form': form})

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Feedback

class FeedbackView(BaseView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'review_detail.html'
    context_object_name = 'feedback'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['SettingsModel'] = SettingsModel.objects.filter(is_active=1)
        context['Items'] = Item.objects.filter(is_active=1)
        context['Image'] = ImageBase.objects.filter(is_active=1, page=self.template_name)

        slug = self.kwargs.get('slug')

        if slug:

            feedback_objects = Feedback.objects.filter(slug=slug)

            context['Feed'] = feedback_objects

        for feedback_objects in context['Feed']:
            user = feedback_objects.username
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                feedback_objects.newprofile_profile_picture_url = profile.avatar.url
                feedback_objects.newprofile_profile_url = feedback_objects.get_profile_url2()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

"""@method_decorator(login_required, name='dispatch')
class FeedbackView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    paginate_by = 10
    template_name = 'review_detail.html'
    context_object_name = 'feedback'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['SettingsModel'] = SettingsModel.objects.filter(is_active=1)
        context['Items'] = Item.objects.filter(is_active=1)

        slug = self.kwargs.get('slug')

        if slug:

            feedback_objects = Feedback.objects.filter(slug=slug)

            context['feedback_objects'] = feedback_objects

        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['success_url'] = reverse('feedbackfinish')

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

"""

"""
class FeedbackView(LoginRequiredMixin, FormView):
    model = FeedbackBackgroundImage
    template_name = "review_detail.html"
    form_class = FeedbackForm
    success_url = '/feedbackfinish'

    def get_context_data(self, **kwargs):
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
            context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

            if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
                        
        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)

            context['Feed'] = Feedback.objects.filter(is_active=1).order_by("slug")
            context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
            context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
            context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")

            product = Item.objects.filter(is_active=1)

            context['Products'] = product

            for product in context['Products']:
                image = product.image
                item = Item.objects.filter(slug=product.slug).first()
                if product:
                    product.title = item.title
                    product.price = item.price
                    product.discount_price = item.discount_price
                    product.image_url = item.image.url
                    product.hyperlink = item.get_profile_url()

            return context

    def form_valid(self, form):

        feedback = form.save(commit=False)
        feedback.username = self.request.user.username  
        feedback.save()
        messages.success(self.request, 'Your feedback has been submitted successfully.')
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        cleaned_data = self.form.cleaned_data

        feedback = Feedback()
        feedback.item = cleaned_data['item']
        feedback.order = cleaned_data['order']
        feedback.username = cleaned_data['username']
        feedback.comment = cleaned_data['comment']
        feedback.feedbackpage = cleaned_data['feedbackpage']
        feedback.slug = cleaned_data['slug']
        feedback.star_rating = cleaned_data['star_rating']
        feedback.showcase = cleaned_data['showcase']
        feedback.image = cleaned_data['image']
        feedback.image_length = cleaned_data['image_length']
        feedback.feedbackpage = cleaned_data['feedbackpage']
        feedback.image_width = cleaned_data['image_width']
        feedback.timestamp = cleaned_data['timestamp']
        feedback.is_active = cleaned_data['is_active']

        feedback.save()

        messages.success(request, 'Your feedback has been submitted successfully.')
        return redirect('showcase:feedbackfinish')"""

class ReviewView(BaseView):
    model = ShowcaseBackgroundImage
    template_name = "reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")

        product = Item.objects.filter(is_active=1)

        context['Products'] = product

        for product in context['Products']:
            image = product.image
            item = Item.objects.filter(slug=product.slug).first()
            if product:
                product.title = item.title
                product.price = item.price
                product.discount_price = item.discount_price
                product.image_url = item.image.url
                product.hyperlink = item.get_profile_url()

        feeder = Feedback.objects.filter(is_active=1).order_by('-timestamp')

        context['FeedBacking'] = feeder

        for feeder in context['FeedBacking']:
            user = feeder.username
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                feeder.user_profile_picture_url = profile.avatar.url
                feeder.user_profile_url = feeder.get_profile_url()

                print('imgsrcimg')

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

"""
   def form_valid(self, form):

       feedback = form.save(commit=False)
       feedback.username = self.request.user.username  
       feedback.save()
       form = FeedbackForm(request=request)
       messages.success(self.request, 'Your feedback has been submitted successfully.')
       return super().form_valid(form)

   def get_queryset(self):
       queryset = super().get_queryset()
       if self.request.user.is_authenticated:

           queryset = queryset.filter(order__user=self.request.user)
       else:

           queryset = Feedback.objects.none()
       return queryset

   def test_func(self):
       feedback = self.get_object()
       order = feedback.OrderItem
       return self.request.user == OrderItem.user

   def post(self, request, *args, **kwargs):

       feedback = self.get_object()
       order = feedback.OrderItem
       if self.request.user == OrderItem.user:

           messages.success(request, 'Your feedback has been submitted successfully.')
           return redirect('showcase:feedbackfinish')
       else:
           messages.error(request, 'You are not allowed to submit feedback for this order.')
           return redirect('showcase:ehome')

   @login_required
   def get_current_user(self, request, feedback):
       if request.method == 'POST':

           username = request.user.username
           post = form.save(commit=False)
           post.save()

           return redirect('showcase:feedbackfinish')

   def getobject(self, request, item):
       item = Item.objects.get(pk=item)

       return render(request, 'review_detail.html', {'item': item})

   def create_review(request, orderitem_id):
       try:
           Item = Item.objects.get(slug=slug)
       except Item.DoesNotExist:
           raise Http404("Product does not exist")
       if request.POST:
           form = FeedbackForm(request.POST)
           url = '/'
           data = json.dumps(url)

           if form.is_valid():
               instance = form.save(commit=False)
               instance.Item = item
               instance.save()
               sendEmployeeEmailOnAddReview(Item, form)
               return HttpResponse(data, content_type='application/json')
       else:
           form = FeedbackForm()
       context = {
           "Item": Item,
           "form": form,

       }
       return render(request, 'create_review.html', context)
"""

@login_required
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)

            new_comment.blog = post

            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request, template_name, {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        })

@login_required
def postpreference(request, post_name, like_or_dislike):
    if request.method == "POST":
        eachpost = get_object_or_404(Blog, slug=post_name)

        if int(like_or_dislike) == 1:

            if request.user in eachpost.likes.iterator():
                eachpost.likes.remove(request.user)
            else:

                eachpost.likes.add(request.user)

                if request.user in eachpost.dislikes.iterator():
                    eachpost.dislikes.remove(request.user)
        else:

            if request.user in eachpost.dislikes.iterator():
                eachpost.dislikes.remove(request.user)
            else:

                eachpost.dislikes.add(request.user)

                if request.user in eachpost.likes.iterator():
                    eachpost.likes.remove(request.user)

        eachpost.save()

        return JsonResponse({'likes': eachpost.likes.count(), 'dislikes': eachpost.dislikes.count()})

    else:
        eachpost = get_object_or_404(Blog, slug=post_name)
        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'showcase:likes.html', context)

from django.shortcuts import get_object_or_404, redirect, render
from .forms import FeedbackForm
from .models import Item, OrderItem, Feedback

from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import FeedbackForm
from .models import Item, OrderItem, Feedback

"""
class SubmitFeedbackView(DetailView):
   template_name = "review_detail.html"
   form_class = FeedbackForm
   success_url = '/feedbackfinish'
   paginate_by = 10

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
       context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

       context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=self.request.user).order_by(
            "created_at")
       context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)
 
        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
context['preferenceform'] = MyPreferencesForm(user=self.request.user)

       context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
       context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
       context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
       context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
       return context

   def get_form_kwargs(self):
       kwargs = super().get_form_kwargs()
       kwargs['request'] = self.request
       return kwargs

   def get(self, request, orderitem_id):
       order_item = get_object_or_404(OrderItem, id=orderitem_id, user=request.user)
       form = FeedbackForm(request=request, initial={'order_item': order_item})
       return render(request, 'create_review.html', {'form': form})

   def form_valid(self, form):
       orderitem_id = self.kwargs['orderitem_id']
       order_item = get_object_or_404(OrderItem, id=orderitem_id, user=self.request.user)

       feedback = form.save(commit=False)
       feedback.username = self.request.user.username
       feedback.order = order_item
       feedback.slug = order_item.slug
       feedback.item = order_item.item
       feedback.save()

       messages.success(self.request, 'Your feedback has been submitted successfully.')
       return redirect(self.success_url)

   def form_invalid(self, form):
       messages.error(self.request, 'Invalid form data.')
       return render(self.request, 'create_review.html', {'form': form})"""

from django.shortcuts import get_object_or_404

"""
def submit_feedback(request, item_id):
   item = get_object_or_404(Item, id=item_id)
   user = request.user
   order_items = OrderItem.objects.filter(user=user, item=item).first()  

   if request.method == 'POST':
       form = FeedbackForm(request.POST, request=request)
       if form.is_valid():
           feedback = form.save(commit=False)
           feedback.username = user.username
           feedback.slug = order_item.slug  
           feedback.item = item
           feedback.order = order_item.first()  
           feedback.save()
           messages.success(request, 'Your feedback has been submitted successfully.')
           return redirect('showcase:feedbackfinish')
       else:
           messages.error(request, "Invalid form data.")
   else:
       form = FeedbackForm(request=request)

   context = {
       'form': form,
       'order_items': order_items,
   }

   return render(request, 'create_review.html', context)"""

"""
def submit_feedback(request, item_id):
   item = get_object_or_404(Item, id=item_id)
   user = request.user
   order_item = get_object_or_404(OrderItem, user=user, item=item)

   if request.method == 'POST':
       form = FeedbackForm(request.POST, request=request)
       if form.is_valid():
           feedback = form.save(commit=False)
           feedback.username = user
           feedback.slug = order_item.slug
           feedback.item = item
           feedback.order = order_item
           feedback.save()
           messages.success(request, 'Your feedback has been submitted successfully.')
           return redirect('showcase:feedbackfinish')
       else:
           messages.error(request, "Invalid form data.")
   else:
       form = FeedbackForm(request=request)

   return render(request, 'create_review.html', {'form': form})
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem, Feedback
from .forms import FeedbackForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Feedback, Item, OrderItem
from .forms import FeedbackForm

from django.shortcuts import render, redirect
from .forms import FeedbackForm

from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import OrderItem, Feedback

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormMixin
from .models import Feedback, OrderItem
from .forms import FeedbackForm
from .models import (
    LogoBase,
    BaseCopyrightTextField,
    Titled,
    FaviconBase,
    NavBarHeader,
    NavBar,
    BackgroundImageBase,
)

class CreateReviewView(LoginRequiredMixin, FormView):
    template_name = "create_review.html"
    form_class = FeedbackForm

    def get(self, request, *args, **kwargs):
        item_slug = request.GET.get('item_slug')
        orderitem_id = request.GET.get('orderitem_id')

        try:
            orderitem = OrderItem.objects.get(id=orderitem_id)
        except OrderItem.DoesNotExist:
            return HttpResponse('Sorry, this order does not exist.')

        if orderitem.item:
            initial = {
                'item': orderitem.item,
                'slug': orderitem.slug,
                'order': orderitem,
            }
        else:
            initial = {'slug': orderitem.slug}

        form = FeedbackForm(initial=initial, request=request)

        context = self.get_context_data(form=form)

        return render(request, 'create_review.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")

        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Profile'] = UpdateProfile.objects.all()
        context['Logo'] = LogoBase.objects.all()
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    def post(self, request, *args, **kwargs):
        item_slug = request.GET.get('item_slug')
        orderitem_id = request.GET.get('orderitem_id')

        try:
            orderitem = OrderItem.objects.get(id=orderitem_id)
        except OrderItem.DoesNotExist:
            return redirect('showcase:ehome')

        try:
            existing_feedback = Feedback.objects.get(order=orderitem)
        except Feedback.DoesNotExist:
            existing_feedback = None

        form = FeedbackForm(request.POST, request.FILES, request=request, instance=existing_feedback)

        if form.is_valid():
            feedback = form.save(commit=False)

            feedback.item = orderitem.item

            feedback.username = request.user if request.user.is_authenticated else None
            feedback.order = orderitem
            feedback.slug = orderitem.slug

            if request.user.is_authenticated:
                feedback.username = request.user
            else:
                feedback.username = None

            feedback.item = orderitem.item
            feedback.order = orderitem

            feedback.save()

            if existing_feedback and existing_feedback != feedback:
                existing_feedback.delete()
                slug = str(existing_feedback.slug)
            else:
                slug = str(feedback.slug)

            url = reverse('showcase:review_detail', args=[slug])
            return redirect(url)

        else:
            context = self.get_context_data(form=form)
            return render(request, 'create_review.html', context)

        return render(request, 'create_review.html', {'form': form})

from .forms import FeedForm

class FeedView(FormMixin, ListView):
    model = Feedback
    template_name = "create_review.html"
    form_class = FeedForm

    def get_context_data(self, **kwargs):
        print("get_context_data is being called")
        context = {
            'Logo': LogoBase.objects.filter(page=self.template_name, is_active=1).order_by("section"),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Favicons': FaviconBase.objects.filter(is_active=1),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Background': BackgroundImageBase.objects.filter(is_active=1)
        }
        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = FeedForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            url = reverse('showcase:review_detail', args=[slug])
            return redirect(url)
        else:
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            messages.error(request, "Form submission invalid")
            return render(request, "create_review.html", {'form': form})

@login_required(login_url='/accounts/login/')
def submit_feedback(request):
    user = request.user

    if request.method == 'POST':
        form = FeedbackForm(request=request, item=item, orderitem=orderitem)
        if form.is_valid():
            star_rating = form.cleaned_data['star_rating']
            comment = form.cleaned_data['comment']

            feedback, created = Feedback.objects.update_or_create(
                username=request.user,

                defaults={'star_rating': star_rating, 'comment': comment}
            )

            return redirect('showcase:feedbackfinish')

    else:

        form = FeedbackForm(request=request)

    return render(request, 'create_review.html', {'form': form})

def edit_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback, request=request)
        if form.is_valid():
            form.save()
            return redirect('showcase:create_review')
    else:
        form = FeedbackForm(instance=feedback, request=request)

    return render(request, 'create_review.html', {'form': form})

@login_required(login_url='/accounts/login/')
def submit_feedback(request):
    user = request.user

    if request.method == 'POST':
        form = FeedbackForm(request.POST, request=request)
        if form.is_valid():
            star_rating = form.cleaned_data['star_rating']
            comment = form.cleaned_data['comment']

            feedback, created = Feedback.objects.update_or_create(
                username=request.user,

                defaults={'star_rating': star_rating, 'comment': comment}
            )

            return redirect('showcase:feedbackfinish')

    else:

        form = FeedbackForm(request=request)

    return render(request, 'create_review.html', {'form': form})

def edit_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback, request=request)
        if form.is_valid():
            form.save()
            return redirect('showcase:create_review')
    else:
        form = FeedbackForm(instance=feedback, request=request)

    return render(request, 'create_review.html', {'form': form})

@login_required
def my_order_items(request):
    user = request.user
    order_items = OrderItem.objects.filter(user=user)
    context = {'order_items': order_items}
    return render(request, 'order_history.html', context)

class OrderHistory(ListView):
    model = Order
    template_name = "order_history.html"
    context_object_name = 'order'

    def get_context_data(self, **kwargs):

        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        if self.request.user.is_authenticated:
            context['StockObject'] = InventoryObject.objects.filter(
                is_active=1, user=self.request.user
            ).order_by("created_at")
            context['preferenceform'] = MyPreferencesForm(user=self.request.user)
        context['Logo'] = LogoBase.objects.filter(Q(page=self.template_name) | Q(page='navtrove.html'), is_active=1)

        user = self.request.user
        if user.is_authenticated:
            user_clickables = UserClickable.objects.filter(user=user)
            for user_clickable in user_clickables:
                if user_clickable.clickable.chance_per_second > 0:
                    user_clickable.precomputed_chance = 1000 / user_clickable.clickable.chance_per_second
                    print('chance exists' + str(user_clickable.precomputed_chance))
                else:
                    user_clickable.precomputed_chance = 0

            context["Clickables"] = user_clickables
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['items'] = Item.objects.all()
        context['feedback'] = Feedback.objects.all()

        print(user)

        items = Item.objects.filter(is_active=1)

        context['Iteme'] = items

        for items in context['Iteme']:

            image = items.image

            if user.is_authenticated:

                profile = ProfileDetails.objects.filter(user=user).first()

                if profile:

                    items.author_profile_picture_url = profile.avatar.url

                    items.author_profile_url = items.get_profile_url()
            else:

                messages.warning(self.request, "You need to log in")
                return redirect("accounts/login")

        order = OrderItem.objects.filter(is_active=1, user=user)
        context['orders'] = order
        total_items = OrderItem.objects.filter(is_active=1).count()

        paginate_by = int(self.request.GET.get('paginate_by', settings.DEFAULT_PAGINATE_BY))

        items_query = OrderItem.objects.filter(is_active=1)
        paginator = Paginator(items_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_items = paginator.get_page(page_number)

        context['orders'] = paginated_items
        for order_item in context['orders']:

            image = order_item.image
            user = self.request.user
            profile = ProfileDetails.objects.filter(user=user).first()

            if order_item.image:
                order_item.image_url = order_item.image.url

            order_item.author_profile_url = order_item.get_profile_url() if order_item.get_profile_url() else None
            order_item.hyperlink = order_item.get_profile_url()

            if profile:
                order_item.author_profile_picture_url = profile.avatar.url
                order_item.profile_url = order_item.get_profile_url2()

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['NewsProfiles'] = userprofile
        else:
            context['NewsProfiles'] = None

        if context['NewsProfiles'] == None:

            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['NewsProfiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        return context

from django.forms import formset_factory
from .models import Questionaire
from .forms import QuestionCountForm, QuestionForm

def get_num_questions(request, question_id):
    if request.method == 'POST':
        form = QuestionCountForm(request.POST)
        if form.is_valid():
            num_questions = form.cleaned_data['num_questions']

            return HttpResponseRedirect(reverse('showcase:create_questions', args=[num_questions]))
    else:
        form = QuestionCountForm()
    return render(request, 'get_num_questions.html', {'form': form})

from django.forms import formset_factory, modelformset_factory

@login_required
def create_questioned(request, num_questions):
    QuestionFormSet = formset_factory(QuestionForm, extra=num_questions)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, prefix='question')
        if formset.is_valid():
            user = request.user
            for form in formset:
                text = form.cleaned_data['text']
                Questionaire.objects.create(user=user, text=text)
            return HttpResponseRedirect(reverse('showcase:index'))
    else:
        formset = QuestionFormSet(prefix='question')

    return render(request, 'create_questions.html', {'formset': formset})

@login_required
def create_questions(request, num_questions):
    if request.method == 'POST':
        FormSet = modelformset_factory(
            Questionaire,
            fields=('text', 'form_type', 'answer_choices'),
            extra=num_questions,
        )
        formset = FormSet(request.POST, prefix='question')

        if formset.is_valid():
            user = request.user
            instances = formset.save(commit=False)

            for form, instance in zip(formset, instances):
                if instance.form_type == 'option1':
                    answer_choices = form.cleaned_data.get('answer_choices', '').split(',')
                    instance.answer_choices = answer_choices
                instance.user = user
                instance.save()

            return HttpResponseRedirect(reverse('showcase:index'))
    else:
        FormSet = modelformset_factory(
            Questionaire,
            fields=('text', 'form_type', 'answer_choices'),
            extra=num_questions,
        )
        formset = FormSet(queryset=Questionaire.objects.none(), prefix='question')

    return render(request, 'create_questions.html', {'formset': formset})

def add_question(request):
    QuestionAnswerFormSet = formset_factory(AnswerForm, extra=2, can_delete=True)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        formset = QuestionAnswerFormSet(request.POST, prefix='answer')

        if question_form.is_valid() and formset.is_valid():

            return redirect('showcase:index')
    else:
        question_form = QuestionForm()
        formset = QuestionAnswerFormSet(prefix='answer')

    return render(request, 'add_question.html', {'question_form': question_form, 'formset': formset})

"""
def create_questionaire(request, num_questions):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():

            questionaire = form.save(commit=False)
            answer_choices = request.POST.getlist('answer_choices')
            questionaire.answer_choices = answer_choices
            questionaire.save()
            return redirect('showcase:index')
    else:
        form = QuestionForm()
    return render(request, 'create_questions.html', {'form': form})
"""


def submit_answer(request, question_id):
    questionaire = get_object_or_404(Questionaire, pk=question_id)
    questions = questionaire.question_set.all()

    if request.method == 'POST':
        form = AnswerForm(request.POST, questions=questions)

        if form.is_valid():
            for question in questions:
                answer_text = form.cleaned_data[f'answer_{question.id}']
                correct_answer = getattr(questionaire, f'correct_answer_{question.form_type}')
                is_correct = answer_text == correct_answer

            return HttpResponseRedirect(reverse('showcase:index'))
    else:
        form = AnswerForm(questions=questions)

    return render(request, 'showcase/answer_questions.html', {'form': form})


def sociallogin(request):
    return render(request, 'registration/sociallogin.html')