import django
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import ShowcasePost
from .models import Post
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
from .models import City, Poste, ShowcasePost, Post, Partner
from .models import Support
from .models import Patreon
from .models import Item
from .models import FaviconBase
from .models import BackgroundImage
from .models import EBackgroundImage
from .models import ShowcaseBackgroundImage
from .models import ChatBackgroundImage
from .models import SupportChatBackgroundImage
from .models import BilletBackgroundImage
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
from .models import SettingsModel
from .models import ImageCarousel
from .models import PatreonBackgroundImage
from .models import ConvertBackgroundImage
from .models import SettingsBackgroundImage
from .models import BackgroundImageBase
from .models import TextBase
from .models import LogoBase
from .models import RuleTextField9
from .models import RuleTextField10
from .models import RuleTextField11
from .models import RuleTextField12
from .models import AboutTextField
from .models import AboutTextField2
from .models import AboutTextField3
from .models import AboutTextField4
from .models import AboutTextField5
from .models import AboutTextField6
from .models import AboutTextField7
from .models import AboutTextField8
from .models import BilletTextField
from .models import BilletTextField2
from .models import BilletTextField3
from .models import BilletTextField4
from .models import BilletTextField5
from .models import BilletTextField6
from .models import BilletTextField7
from .models import BilletTextField8
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
from .models import ContentTextField
from .models import ContentTextField2
from .models import ContentTextField3
from .models import ContentTextField4
from .models import ContentTextField5
from .models import ContentTextField6
from .models import ContentTextField7
from .models import ContentTextField8
from .models import BaseCopyrightTextField
from .models import NavBar
from .models import NavBarHeader
from .models import DonateIcon
from .models import Titled
# from .models import Background2aImage
from .forms import MyForm
from .forms import PosteForm
from .forms import PostForm
from .forms import Postit
from .forms import StaffJoin
from .forms import Server_Partner
from .forms import SignUpForm
from .forms import News_Feed
from .forms import PunishAppeal
from .forms import ReportIssues
from .forms import BanAppeal
from .forms import Staffprofile
from .forms import Eventform
from .forms import ProfileDetail
from .forms import Support
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
from .forms import TextFielde
from .forms import TextFielde2
from .forms import TextFielde3
from .forms import TextFielde4
from .forms import TextFielde5
from .forms import TextFielde6
from .forms import TextFielde7
from .forms import TextFielde8
from .forms import BilletTextFielde
from .forms import BilletTextFielde2
from .forms import BilletTextFielde3
from .forms import BilletTextFielde4
from .forms import BilletTextFielde5
from .forms import BilletTextFielde6
from .forms import BilletTextFielde7
from .forms import BilletTextFielde8
from .forms import AboutTextFielde
from .forms import AboutTextFielde2
from .forms import AboutTextFielde3
from .forms import AboutTextFielde4
from .forms import AboutTextFielde5
from .forms import AboutTextFielde6
from .forms import AboutTextFielde7
from .forms import AboutTextFielde8
from .forms import BaseCopyrightTextField
from .forms import ContactForme
# from .forms import OrderItems
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
from .models import UserProfile2
from django.views.generic.edit import FormMixin

import pdb
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

from .forms import CommentForm
from django.shortcuts import get_object_or_404

from .models import Room, Message
from .models import SupportChat, SupportMessage
from django.http import JsonResponse
import os

from django.contrib.auth.decorators import login_required

from guest_user.mixins import RegularUserRequiredMixin

from django.views.generic.edit import FormView


def my_form(request):
    print('signup')
    if request.method == 'POST':
        print('post')
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('is_valid')
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password')

            # login user after signing up
            user = form.save()
            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')
            subject = "Welcome to IntelleX!"
            message = 'Hello {user.username}, thank you for becoming a member of the IntelleX Community!'
            email_from = settings.EMAIL_HOST_USER
            recipent_list = [user.email, ]
            send_mail(subject, message, email_from, recipent_list)

            # redirect user to home page
            return redirect('showcase:showcase')
            messages.info(request, "You have signed up successfully! Welcome!")
    else:
        form = SignUpForm()
    return render(request, 'cv-form.html', {'form': form})


class LogoView(ListView):
    model = LogoBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter(
            'page')
        return context


class BaseView(ListView):
    template_name = "base.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name,
            is_active=1)
        return context


class EBaseView(ListView):
    template_name = "ebase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name,
            is_active=1)
        return context


class BlogBaseView(ListView):
    template_name = "blogbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name,
            is_active=1)
        return context


class DonateBaseView(ListView):
    model = "donatebase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name,
            is_active=1)
        return context


class MemberBaseView(ListView):
    template_name = "memberbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name,
            is_active=1)
        return context


class usersview(ListView):
    paginate_by = 10
    template_name = 'users.html'

    def get_queryset(self):
        return Post.objects.all()


class votingview(ListView):
    paginate_by = 10
    template_name = 'voting.html'

    def get_queryset(self):
        return Poste.objects.all()


class partnerview(ListView):
    paginate_by = 10
    template_name = 'partners.html'

    def get_queryset(self):
        return Partner.objects.all()


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


class PostList(ListView):
    model = BlogBackgroundImage
    # backgroundqueryset = BackgroundImageBase.objects.filter('page').order_by('position')
    # queryset = Blog.objects.filter(status=1).order_by('-created_on')
    # normally can only filter once per view
    paginate_by = 10
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        print(124)
        context = super().get_context_data(**kwargs)
        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.all
        return context

    def get_queryset(self):
        return Blog.objects.filter(status=1).order_by('-created_on')

    # def get(self, request, *args, **kwargs):
    # return super().get(request, *args, **kwargs)


class PostDetail(generic.DetailView):
    model = Blog
    paginate_by = 10
    template_name = 'post_detail.html'


# class BackgroundView(ListView):
#  paginate_by = 10
#  template_name = 'index.html'

#  def get_queryset(self):
#    return BackgroundImage.objects.all()

from django.views.generic import ListView, CreateView


# class TextFieldView(ListView):
#    model = TextField
#    template_name = "index.html"


class FaviconBaseView(ListView):
    model = FaviconBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicons'] = FaviconBase.objects.filter('faviconpage')
        return context


class BackgroundBaseView(ListView):
    model = BackgroundImageBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BackgroundImages'] = BackgroundImageBase.objects.filter(
            'page').order_by('position')
        return context

    # def backgrounds(request, showcase, index, blog):
    #    page = get_object_or_404(BackgroundImageBase,
    #                             showcase=showcase,
    #                             index=index,
    #                             blog=blog)

    # context = {
    #    'page': page,
    # }

    # if index == 'index':
    #    template = 'index.html'
    #    print(index)
    # elif index == 'showcase':
    #    template = 'showcase.html'
    #    print(index)
    # else render the one you're already rendering
    # else:
    #    template = 'blog.html'
    #    print(index)

    # return render(request, template, context)


class TextBaseView(ListView):
    model = TextBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(
            is_active=1).order_by("section")
        # texts = TextBase.objects.all()

        # if texts.exists():
        #    return JsonResponse({})
        # else:
        #    return context

        # def backgrounds(request, showcase, index, blog):
        #    page = get_object_or_404(BackgroundImageBase,
        #                             showcase=showcase,
        #                             index=index,
        #                             blog=blog)

        # context = {
        #    'page': page,
        # }

        # if index == 'index':
        #    template = 'index.html'
        #    print(index)
        # elif index == 'showcase':
        #    template = 'showcase.html'
        #    print(index)
        # else render the one you're already rendering
        # else:
        #    template = 'blog.html'
        #    print(index)

        return render(context)


class ImageCarouselView(BaseView):
    model = ImageCarousel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Carousel'] = ImageCarousel.objects.filter(is_active=1).order_by('position')
        return context


class BackgroundView(BaseView):
    model = BackgroundImage
    template_name = "index.html"
    section = TextBase.section

    print(section)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Carousel'] = ImageCarousel.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Favicons'] = FaviconBase.objects.all()
        print(FaviconBase.objects.all())
        print(213324)
        return context


class CreatePostView(CreateView):
    model = BackgroundImage
    form_class = BackgroundImagery
    template_name = "backgroundimagechange.html"
    success_url = reverse_lazy("index")


class EBackgroundView(BaseView):
    model = EBackgroundImage
    template_name = "ehome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        return context


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
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        return context


class ShowcaseCreatePostView(CreateView):
    model = ShowcaseBackgroundImage
    form_class = ShowcaseBackgroundImagery
    template_name = "showcasebackgroundimagechange.html"
    success_url = reverse_lazy("showcase")


class ChatBackgroundView(BaseView):
    model = ChatBackgroundImage
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        return context


class SupportChatBackgroundView(BaseView):
    model = SupportChatBackgroundImage
    template_name = "supportchat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
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
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        return context


class BlogBackgroundView(ListView):
    model = BlogBackgroundImage
    template_name = "blog.html"

    queryset = Blog.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        return context


class BlogCreatePostView(CreateView):
    model = BlogBackgroundImage
    form_class = BlogBackgroundImagery
    template_name = "blogbackgroundimagechange.html"
    success_url = reverse_lazy("blog")


class PatreonBackgroundView(ListView):
    model = Patreon
    template_name = "patreon.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PatreonBackgroundImage'] = PatreonBackgroundImage.objects.all()
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        # context['Patreon'] = Patreon.objects.all()
        return context


@login_required
# @RegularUserRequiredMixin
class PostBackgroundView(FormMixin, ListView):
    model = ShowcasePost
    template_name = "post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['ShowcasePost'] = ShowcasePost.objects.all()
        return context

    @login_required
    def post_new(self, request, *args, **kwargs):
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
                request,
                'Form submission failed to register, please try again.')
            messages.error(request, form.errors)


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
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        return context


class BilletCreatePostView(CreateView):
    model = BilletBackgroundImage
    form_class = BilletBackgroundImagery
    template_name = "billetbackgroundimagechange.html"
    success_url = reverse_lazy("billets")


from .models import RuleTextField
from .models import RuleTextField2
from .models import RuleTextField3
from .models import RuleTextField4
from .models import RuleTextField5
from .models import RuleTextField6
from .models import RuleTextField7
from .models import RuleTextField8


class RuleBackgroundView(BaseView):
    model = RuleBackgroundImage
    template_name = "rules.html"


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['RuleBackgroundImage'] = RuleBackgroundImage.objects.all()
    context['TextFielde'] = TextBase.objects.filter(
        page=self.template_name).order_by("section")
    context['Titles'] = Titled.objects.filter(
        is_active=1, page=self.template_name).order_by("position")
    context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
    context['Background'] = BackgroundImageBase.objects.filter(
        page=self.template_name).order_by("position")
    return context


class RuleCreatePostView(CreateView):
    model = RuleBackgroundImage
    form_class = RuleBackgroundImagery
    template_name = "rulebackgroundimagechange.html"
    success_url = reverse_lazy("rules")


class AboutBackgroundView(BaseView):
    model = AboutBackgroundImage
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        return context


class FaqCreatePostView(CreateView):
    model = FaqBackgroundImage
    form_class = FaqBackgroundImagery
    template_name = "faqbackgroundimagechange.html"
    success_url = reverse_lazy("faq")


class StaffBackgroundView(BaseView):
    model = StaffBackgroundImage
    template_name = "staff.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        print(124)
        context = super().get_context_data(**kwargs)
        context[
            'StaffApplyBackgroundImage'] = StaffApplyBackgroundImage.objects.all(
        )
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        return context

    @login_required
    def staffjoin1(self, request, *args, **kwargs):
        print('staffapply')
        if request.method == 'POST':
            print('post')
            form = StaffJoin(request.POST)
            if (form.is_valid()):
                post = form.save(commit=False)
                post.save()
                # redirect user to staffdone
                return redirect('staffdone')
        else:
            form = StaffJoin()
        return render(request, 'staffapplications.html', {'form': form})


class InformationBackgroundView(BaseView):
    model = InformationBackgroundImage
    template_name = "information.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['UserBackgroundImage'] = UserBackgroundImage.objects.all()
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        context[
            'StaffRanksBackgroundImage'] = StaffRanksBackgroundImage.objects.all(
        )
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['EventBackgroundImage'] = EventBackgroundImage.objects.all()
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
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
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        # context['BaseHomeTexted'] = BaseHomeText.objects.all()
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        return context


class ContributorBackgroundView(BaseView):
    model = ContributorBackgroundImage
    template_name = "contributors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        return context


class ContentBackgroundView(BaseView):
    model = ContentBackgroundImage
    template_name = "morecontent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ContentBackgroundImage'] = ContentBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class PartnerBackgroundView(BaseView):
    model = PartnerBackgroundImage
    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PartnerBackgroundImage'] = PartnerBackgroundImage.objects.all(
        )
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        return context


class ShareBackgroundView(BaseView):
    model = ShareBackgroundImage
    template_name = "share.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ShareBackgroundImage'] = ShareBackgroundImage.objects.all()
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        return context


class ConvertBackgroundView(BaseView):
    model = ConvertBackgroundImage
    template_name = "convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ConvertBackgroundImage'] = ConvertBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(
            page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        return context


#  def get_queryset(self):
#    return BackgroundImage.objects.all()

#  def get_context_data(request):
#    images = os.listdir("static/css/images") #Can use glob as well
#    context = {'images': images}
#    return render(request,'/home/runner/PokeTrove-Attempt-Backedmore/templates',context)

# class Background2aView(ListView):
#  model = Background2aImage
#  paginate_by = 10
#  template_name = 'index.html'
#  extra_context = {'Background2aImage.url': Background2aImage.objects.all()[0].get_absolute_url()}

#  def get_queryset(self):
#    return Background2aImage.objects.all()


def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/home/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/home/' + room + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message,
                                         user=username,
                                         room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
    print('returned')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


def supportroom(request):
    username = request.user.username
    room_details = SupportChat.objects.get(name=username)
    return render(request, 'supportroom.html', {
        'username': username,
        'room': username,
        'room_details': room_details
    })


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
        return redirect('/supportchat/room')
    else:
        new_room = SupportChat.objects.create(name=username)
        new_room.save()

        new_message = SupportMessage.objects.create(value=help,
                                                    user=username,
                                                    room=username)
        new_message.save()
        return redirect('/supportchat/room')
        print('message sent')


def supportsend(request):
    print(23455)
    message = request.POST['message']
    username = request.user.username
    room_id = request.user.username

    new_message = SupportMessage.objects.create(value=message,
                                                user=username,
                                                room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def supportgetMessages(request, **kwargs):
    messages = SupportMessage.objects.filter(room=request.user.username)
    return JsonResponse({"messages": list(messages.values())})


# class post(ListView):
#  template_name = 'users.html'


class PostingView(FormMixin, ListView):
    model = PostBackgroundImage
    template_name = "post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['Post'] = Post.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('showcase:showcase')
            messages.success(request, 'Form submitted successfully.')
        else:
            messages.error(request, "Form submission invalid")
            return render(request, "post_edit.html", {'form': form})



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


class PostView(FormMixin, ListView):
    model = PostBackgroundImage
    template_name = "share.html"
    form_class = Postit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ShareBackgroundImage'] = ShareBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['Post'] = Post.objects.all()
        return context

    @login_required
    def poste(self, request, *args, **kwargs):
        if (request.method == "POST"):
            form = Postit(request.POST)
            if (form.is_valid()):
                post = form.save(commit=False)
                post.save()
                return redirect('showcase:users')
            return super().get(request, *args, **kwargs)
        else:
            form = Postit()
            return render(request, 'share.html', {'form': form})
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return super().get(request, *args, **kwargs)


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


class PosteView(FormMixin, ListView):
    model = VoteBackgroundImage
    template_name = "vote.html"
    form_class = PosteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['VoteBackgroundImage'] = VoteBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context[
            'BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.all()
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        # context['Poste'] = Poste.objects.all()
        return context

    @login_required
    def post(self, request, *args, **kwargs):
        if (request.method == "POST"):
            form = PosteForm(request.POST)
            if (form.is_valid()):
                post = form.save(commit=False)
                post.save()
                return redirect('showcase:voting')
        else:
            form = PosteForm()
            return render(request, 'vote.html', {'form': form})
            messages.error(
                request,
                'Form submission failed to register, please try again.')
            messages.error(request, form.errors)


@login_required
class SettingsView(RegularUserRequiredMixin, FormView):
    """Only allow registered users to change their settings."""
    form_class = SettingsForm
    model = SettingsModel
    template_name = "myaccount.html"
    context = {
        'username': User.username,
        'password': User.password,
        'coupons': SettingsModel.coupons,
        'news': SettingsModel.news,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Showcase.objects.filter(
            page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        return context
        return HttpResponse(template.render(context, request))


class SettingsBackgroundView(FormMixin, ListView):
    model = SettingsBackgroundImage
    form_class = SettingsForm
    template_name = "changesettings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(
            page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Favicons'] = FaviconBase.objects.all()
        print(FaviconBase.objects.all())
        # context['SettingsView'] = SettingsView.objects.all()
        return context

    # @RegularUserRequiredMixin
    @login_required
    def settingschange(self, request, *args, **kwargs):
        if (request.method == "POST"):
            form = SettingsForm(request.POST)
            if (form.is_valid()):
                post = form.save(commit=False)
                post.save()
                return redirect('showcase:showcase')
                messages.success(request, 'Form submitted successfully.')
            else:
                messages.error(request, "Form submission invalid")
                return render(request, "changesettings.html", {'form': form})
        else:
            form = SettingsForm()
            return render(request, "changesettings.html", {'form': form})
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)


def support(request):
    if (request.method == "POST"):
        form = Support(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.save()
            print('works')
            return redirect('showcase:supportissues')
    else:
        form = Support()
        return render(request, 'support.html', {'form': form})
        messages.error(
            request, 'Form submission failed to register, please try again.')
        print('submitted issue')
        messages.error(request, form.errors)


class HomePageView(TemplateView):
    template_name = 'index.html'


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class SearchResultsView(ListView):
    model = City, Poste, ShowcasePost, Post, Partner, UserProfile2
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        city_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query))

        vote_list = Poste.objects.filter(
            Q(name__icontains=query) | Q(catagory__icontains=query)
            | Q(description__icontains=query) | Q(image__icontains=query))

        profile_list = ShowcasePost.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
            | Q(image__icontains=query))

        idea_list = Post.objects.filter(
            Q(name__icontains=query) | Q(catagory__icontains=query)
            | Q(description__icontains=query) | Q(image__icontains=query))

        partner_list = Partner.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
            | Q(server_invite__icontains=query))

        all_list = {
            "city_list": city_list,
            "vote_list": vote_list,
            "idea_list": idea_list,
            "profile_list": profile_list,
            "partner_list": partner_list,
        }

        return (all_list)


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


# class ProductSearchResultsView(ListView):
#    model = Item
#    template_name = 'search_results.html'

#    def get_queryset(self):
#        query = self.request.GET.get('q')
#        item_list = Item.objects.filter(
#            Q(name__icontains=query) | Q(state__icontains=query)
#        )

#        all_list = {
#           "item_list": item_list,
#       }

#        return (all_list)


# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    paginate_by = 10
    success_url = reverse_lazy('home')
    template_name = 'templates/profile.html'


class StaffJoine(ListView):
    paginate_by = 10
    template_name = 'staffapplication.html'

    def get_queryset(self, *args, **kwargs):
        return StaffApplication.objects.all()


@login_required
def unpunish(request):
    if (request.method == "POST"):
        form = PunishAppeal(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.save()
            return redirect('showcase:punishdone')
    else:
        form = PunishAppeal()
        return render(request, 'punishapps.html', {'form': form})
        messages.error(
            request, 'Form submission failed to register, please try again.')
        messages.error(request, form.errors)


@login_required
def unban(request):
    if (request.method == "POST"):
        form = BanAppeal(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.save()
            return redirect('showcase:bandone')
    else:
        form = BanAppeal()
        return render(request, 'banappeals.html', {'form': form})
        messages.error(
            request, 'Form submission failed to register, please try again.')
        messages.error(request, form.errors)


@login_required
def issue(request):
    if (request.method == "POST"):
        form = ReportIssues(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.save()
            return redirect('issuedone')
    else:
        form = ReportIssues()
        return render(request, 'issues.html', {'form': form})
        messages.error(
            request, 'Form submission failed to register, please try again.')
        messages.error(request, form.errors)


# sendemail/views.py


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['intellexcompany1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('success')
    print('success')
    # pdb.set_trace()
    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


class contact(TemplateView):
    paginate_by = 10
    template_name = 'email.html'


@login_required
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog = post
            # Save the comment to the database
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


# users/views.py

# ...

# @login_required
# def profile(request, username):
#    user = get_object_or_404(User, username=username)
#    profile = get_object_or_404(Profile, user=user)
#    return render(request, 'like.html', {'profile': profile, 'user': user})

# ...

# @login_required
# def edit_profile(request):
# if request.method == "POST":
# form = EditProfileForm(request.POST, request.FILES)
# if form.is_valid():
# about_me = form.cleaned_data["about_me"]
# username = form.cleaned_data["username"]
# image = form.cleaned_data["image"]

# user = User.objects.get(id=request.user.id)
# profile = Profile.objects.get(user=user)
# user.username = username
# user.save()
# profile.about_me = about_me
# if image:
# profile.image = image
# profile.save()
# return redirect('like', username=user.username)
# else:
# form = EditProfileForm()
# return render(request, 'edit_profile.html', {'form': form})

# @login_required
# def backgroundimages(request):
#  if(request.method == "POST"):
#    form = BackgroundImagery(request.POST)
#    if(form.is_valid()):
#      post = form.save(commit=False)
#      post.save()
#      return redirect('showcase:index')
#  else:
#      form = PosteForm()
#      return render(request, 'index.html', {'form':form})
#      messages.error(request, 'Image submission failed to register, please try again.')
#      messages.error(request, form.errors)

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from datetime import datetime
from django.utils import timezone
from .forms import CheckoutForm
from .models import (Item, OrderItem, Order, Address, Payment, Coupon, Refund,
                     UserProfile)

import stripe

stripe.api_key = "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"

stripe.Source.create(type='ach_credit_transfer',
                     currency='usd',
                     owner={'email': 'Ultramaster123456@gmail.com'})


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


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'object': order}
            return render(self.request, 'order-summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("showcase:ehome")


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'couponform': CouponForm(),
                'order': order,
                'DISPLAY_COUPON_FORM': True
            }

            shipping_address_qs = Address.objects.filter(
                user=self.request.user, address_type='S', default=True)
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(user=self.request.user,
                                                        address_type='B',
                                                        default=True)
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("showcase:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        # print(self.request.GET)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():

                use_default_shipping = form.cleaned_data.get(
                    'use_default_shipping')
                if use_default_shipping:
                    print("Using the defualt shipping address")
                    address_qs = Address.objects.filter(user=self.request.user,
                                                        address_type='S',
                                                        default=True)
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:

                        print("User is entering a new shipping address")
                        shipping_address1 = form.cleaned_data.get(
                            'shipping_address')
                        shipping_address2 = form.cleaned_data.get(
                            'shipping_address2')
                        shipping_country = form.cleaned_data.get(
                            'shipping_country')
                        shipping_zip = form.cleaned_data.get('shipping_zip')

                        messages.info(self.request,
                                      "No default shipping address available")
                        return redirect('showcase:checkout')
                else:
                    # change to allow for saved information without posting
                    print("shipping_address1")
                    shipping_address1 = form.cleaned_data.get(
                        'shipping_address')
                    shipping_address2 = form.cleaned_data.get(
                        'shipping_address2')
                    shipping_country = form.cleaned_data.get(
                        'shipping_country')
                    shipping_zip = form.cleaned_data.get('shipping_zip')

                    if is_valid_form(
                            [shipping_address1, shipping_country, shipping_zip]):
                        shipping_address = Address(
                            user=self.request.user,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            address_type='S')
                        shipping_address.save()

                        order.shipping_address = shipping_address
                        order.save()

                        set_default_shipping = form.cleaned_data.get(
                            'set_default_shipping')
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()

                    else:
                        shipping_address = Address(
                            user=self.request.user,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            address_type='S')
                        shipping_address.save()

                        order.shipping_address = shipping_address
                        order.save()

                        messages.info(
                            self.request,
                            "Please fill in the required shipping address fields"
                        )
                        # save = form.data.get('save')
                        # order.save()
                        return redirect('showcase:checkout')

                use_default_billing = form.cleaned_data.get(
                    'use_default_billing')
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address')

                if same_billing_address:
                    billing_address = shipping_address
                    billing_address.pk = None
                    billing_address.save()
                    billing_address.address_type = 'B'
                    billing_address.save()
                    order.billing_address = billing_address
                    order.save()

                elif use_default_billing:
                    print("Using the defualt billing address")
                    address_qs = Address.objects.filter(user=self.request.user,
                                                        address_type='B',
                                                        default=True)
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        order.billing_address = billing_address
                        order.save()
                    else:
                        messages.info(self.request,
                                      "No default billing address available")
                        return redirect('showcase:checkout')
                else:
                    print("User is entering a new billing address")
                    billing_address1 = form.cleaned_data.get('billing_address')
                    billing_address2 = form.cleaned_data.get(
                        'billing_address2')
                    billing_country = form.cleaned_data.get('billing_country')
                    billing_zip = form.cleaned_data.get('billing_zip')

                    if is_valid_form(
                            [billing_address1, billing_country, billing_zip]):
                        billing_address = Address(
                            user=self.request.user,
                            street_address=billing_address1,
                            apartment_address=billing_address2,
                            country=billing_country,
                            zip=billing_zip,
                            address_type='B')
                        billing_address.save()

                        order.billing_address = billing_address
                        order.save()

                        set_default_billing = form.cleaned_data.get(
                            'set_default_billing')
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()

                    else:
                        messages.info(
                            self.request,
                            "Please fill in the required billing address fields"
                        )
                        return redirect('showcase:checkout')

                payment_option = form.cleaned_data.get('payment_option')

                if payment_option == 'S':
                    return redirect('showcase:payment',
                                    payment_option='stripe')
                elif payment_option == 'P':
                    return redirect('showcase:payment',
                                    payment_option='paypal')
                else:
                    messages.warning(self.request,
                                     "Invalid payment option selected")
                    return redirect('showcase:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("showcase:order-summary")


class PaymentView(View):
    def get(self, *args, **kwargs):
        # request (self) does not seem to be getting user
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.billing_address:
            context = {
                'order': order,
                'DISPLAY_COUPON_FORM': False,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            }
            userprofile = User.objects.get(username=self.request.user.username)
            if hasattr(userprofile, "one_click_purchasing"):
                # userprofile is probably not linked to database
                if userprofile.one_click_purchasing:
                    # fetch the users list
                    cards = stripe.Customer.list_sources(
                        userprofile.stripe_customer_id,
                        limit=3,
                        object='card'
                    )
                    card_list = cards['data']
                    if len(card_list) > 0:
                        # update the context with the default card
                        context.update({
                            'card': card_list[0]
                        })
            else:
                userprofile.one_click_purchasing = False
                return render(self.request, "payment.html", context)
        else:
            messages.warning(
                self.request, "You have not added a billing address.")
            return redirect("showcase:checkout")

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = PaymentForm(self.request.POST)
        userprofile = User.objects.get(username=self.request.user.username)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("expiry"))

            token = stripe.Token.create(
                card={
                    "number": form.cleaned_data.get("number"),
                    "exp_month": form.cleaned_data.get("exp_month"),
                    "exp_year": form.cleaned_data.get("exp_year"),
                    "cvc": form.cleaned_data.get("cvc"),
                },
            )
            save = form.cleaned_data.get('save')
            use_default = form.cleaned_data.get('use_default')

            if save:
                if userprofile.stripe_customer_id != '' and userprofile.stripe_customer_id is not None:
                    customer = stripe.Customer.retrieve(
                        userprofile.stripe_customer_id)
                    customer.sources.create(source=token)

                else:
                    customer = stripe.Customer.create(
                        email=self.request.user.email,
                    )
                    customer.sources.create(source=token)
                    userprofile.stripe_customer_id = customer['id']
                    userprofile.one_click_purchasing = True
                    userprofile.save()

            amount = int(order.get_total_price() * 100)

            try:

                if use_default or save:
                    # charge the customer because we cannot charge the token more than once
                    charge = stripe.Charge.create(
                        amount=amount,  # cents
                        currency="usd",
                        customer=userprofile.stripe_customer_id
                    )
                    print('the payment went through')
                else:
                    # charge once off on the token
                    charge = stripe.Charge.create(
                        amount=amount,  # cents
                        currency="usd",
                        source=token
                    )
                    print('the payment went through')

                # create the payment
                payment = Payment()
                payment.stripe_charge_id = charge['id']
                payment.user = self.request.user
                payment.amount = order.get_total_price()
                payment.save()

                # assign the payment to the order

                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()

                order.ordered = True
                order.payment = payment
                order.ref_code = create_ref_code()
                order.save()

                messages.success(self.request, "Your order was successful!")
                return redirect("showcase:ehome")

            except stripe.error.CardError as e:
                body = e.json_body
                err = body.get('error', {})
                messages.warning(self.request, f"{err.get('message')}")
                return redirect("showcase:ehome")

            except stripe.error.RateLimitError as e:
                # Too many requests made to the API too quickly
                messages.warning(self.request, "Rate limit error")
                return redirect("showcase:ehome")

            except stripe.error.InvalidRequestError as e:
                # Invalid parameters were supplied to Stripe's API
                print(e)
                print(12345)
                # print ('stripeToken', stripeToken)
                messages.warning(self.request, "Invalid parameters")
                return redirect("/ehome")

            except stripe.error.AuthenticationError as e:
                # Authentication with Stripe's API failed
                # (maybe you changed API keys recently)
                messages.warning(self.request, "Not authenticated")
                return redirect("/")

            except stripe.error.APIConnectionError as e:
                # Network communication with Stripe failed
                messages.warning(self.request, "Network error")
                return redirect("/ehome")

            except stripe.error.StripeError as e:
                # Display a very generic error to the user, and maybe send
                # yourself an email
                messages.warning(
                    self.request, "Something went wrong. You were not charged. Please try again.")
                return redirect("/ehome")

            except Exception as e:
                # send an email to ourselves
                messages.warning(
                    self.request, "A serious error occurred. We have been notifed.")
                return redirect("/ehome")

        messages.warning(self.request, "Invalid data received")
        return redirect("/payment/stripe")


from guest_user.decorators import allow_guest_user


@allow_guest_user
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
        # id=10,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(
                request,
                "\"" + order_item.item.title + "\" was added to your cart.")
            return redirect("showcase:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("showcase:order-summary")
    else:
        order_qs = Order.objects.create(user=request.user,
                                        ordered=False,
                                        ordered_date=timezone.now())
        print("Order created")
        # check if the order item is in the order
        if order_qs.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(
                request,
                "\"" + order_item.item.title + "\" was added to your cart.")
            return redirect("showcase:order-summary")
        else:
            order_qs.items.add(order_item)
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
        # add message doesnt have order
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
        # add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("showcase:order-summary")


import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CouponForm, RefundForm, PaymentForm


# from .models import Address, Coupon, Refund, UserProfile

# stripe.api_key = settings.STRIPE_SECRET_KEY


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits,
                                  k=20))


def products(request):
    context = {'items': Item.objects.all()}
    return render(request, "products.html", context)


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
        # check if the order item is in the order
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
                order.save()
                messages.success(self.request, "Successfully added coupon")
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
            # edit the order
            try:
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                # store the refund
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


# @login_required
# def ProfileDetaile(request):
#  user = get_object_or_404(User, username=username)
#  profile = get_object_or_404(Profile, user=user)
#  aboutme = get_object_or_404(Aboutme, user=user)
#  return render(request, 'profile.html', {'profile': profile, 'user': user})

from django.contrib.auth.forms import UserChangeForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'showcase/profile.html'
    sucess_url = reverse_lazy('login')


class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'showcase:edit_profile.html'
    sucess_url = reverse_lazy('login')


# from .models import PublicProfile
# from .forms import PublicForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

# def edit_user(request, pk):
# querying the User object with pk from url
# user = User.objects.get(pk=pk)

# prepopulate UserProfileForm with retrieved user values from above.
# user_form = PublicForm(instance=user)

# The sorcery begins from here, see explanation below
# ProfileInlineFormset = inlineformset_factory(User, PublicProfile, fields=('website', 'bio', 'phone', 'city', 'country', 'organization'))
# formset = ProfileInlineFormset(instance=user)

# if request.user.is_authenticated() and request.user.id == user.id:
# if request.method == "POST":
# user_form = PublicForm(request.POST, request.FILES, instance=user)
# formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

# if user_form.is_valid():
# created_user = user_form.save(commit=False)
# formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

# if formset.is_valid():
# created_user.save()
# formset.save()
# return HttpResponseRedirect('/accounts/profile/')

# return render(request, "account/account_update.html", {
# "noodle": pk,
# "noodle_form": user_form,
# "formset": formset,
# })
# else:
# raise PermissionDenied

# from .forms import NewUserForm, UserForm, ProfileForm

# def userpage(request):
# if request.method == "POST":
# user_form = UserForm(request.POST, instance=request.user)
# profile_form = ProfileForm(request.POST, instance=request.user.profile)
# if user_form.is_valid():
# user_form.save()
# messages.success(request,('Your profile was successfully updated!'))
# elif profile_form.is_valid():
#    profile_form.save()
#    messages.success(request,('Your wishlist was successfully updated!'))
# else:
#    messages.error(request,('Unable to complete request'))
# return redirect ("showcase:userpage")
# user_form = UserForm(instance=request.user)
# profile_form = ProfileForm(instance=request.user.profile)
# return render(request = request, template_name ="showcase/user.html", context = {"user":request.user,
#	"user_form": user_form, "profile_form": profile_form })

# @def products(request):
#	if request.method == "POST":
#		product_id = request.POST.get("product_pk")
#		product = Product.objects.get(id = product_id)
#		request.user.profiletwo.products.add(product)
#		messages.success(request,(f'{product} added to wishlist.'))
#		return redirect ('showcase:products')
#	products = Product.objects.all()
#	paginator = Paginator(products, 18)
#	page_number = request.GET.get('page')
#	page_obj = paginator.get_page(page_number)
#	return render(request = request, template_name="showcase/products.html", context = { "page_obj":page_obj})

# from .models import ExtendUser
# Create your views here.

# def phome(request):
#    data = request.user
#    return render(request,'showcase/profile.html',{'data':data})

from .forms import (EditProfileForm)

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# from django.contrib.auth.decorators import login_required

# def index1(request):
# return HttpResponse('Welcome to my Registration System')
#    numbers = [1,2,3,4,5]
#    name = 'apoorva'

#    args ={'myname':name, 'mynums':numbers}
#    return render(request,'showcase/index.html',args)


def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid:
            form.save()
            return redirect('showcase:profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('registration/profile')

        else:
            return redirect('accounts/change-password')

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

stripe.api_key = "sk_test_51JSB5LH4sbqF1dn75jWAc2wiQvhKq0HfNkQXthKPYmycweqQQkmyTSYgY0vzxQadtgDd2j1RqXYglHspHQXb22kG0086JLfOxS"


def donate(request):
    return render(request, 'donate.html')


def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(email=request.POST['email'],
                                          name=request.POST['nickname'],
                                          source=request.POST['stripeToken']
                                          # stripetoken not defined
                                          )

        charge = stripe.Charge.create(customer=customer,
                                      amount=amount * 100,
                                      currency='usd',
                                      description="Donation")

    return redirect(reverse('showcase:patreoned', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'patreoned.html', {'amount': amount})


@allow_guest_user
def hello_guest(request):
    """
    This view will always have an authenticated user, but some may be guests.
    The default username generator will create a UUID4.

    Example response: "Hello, b5daf1dd-1a2f-4d18-a74c-f13bf2f086f7!"
    """
    return HttpResponse("Hello, {request.user.username}!")


from guest_user.decorators import guest_user_required

from django.template.response import TemplateResponse


@guest_user_required
def why_convert(request):
    """Show reasons why to convert, only for guest users."""
    return TemplateResponse("reasons_to_convert.html")


from django.dispatch import receiver


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'showcase/success.html'