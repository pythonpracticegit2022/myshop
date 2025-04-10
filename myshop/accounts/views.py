from django.shortcuts import render, reverse
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib import messages

from .models import Profile
from .forms import SignUpForm, LoginForm

# class UserListView(ListView):
#
#     model = User
    # queryset = User.objects.all()
    # template_name = ""
    # context_object_name = # obj_list


# class UserDetail(DetailView):
#
#     model = User


class DashboardView(View):

    template_name = 'accounts/dashboard.html'

    @method_decorator(login_required)
    def get(self, request):
        if True:
            messages.success(request, "Welcome to the dashboard")
        messages.error(request, "Error", extra_tags="alert alert-success")
        return render(self.request, self.template_name, {})


class SignUpView(View):

    form_class = SignUpForm
    template_name = 'registration/registration_done.html'
    initial_template = 'registration/register.html'

    def get(self, request):
        user_form = self.form_class()
        return render(request, self.initial_template, {'user_form': user_form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # set the chosen password
            password = form.cleaned_data.get('password1')
            new_user.set_password(password)
            # save the user object
            new_user.save()         # we define the post_save signal to create profile
            messages.success(request, "user registerd")
            # create the user profile
            # Profile.objects.create(user=new_user)     # Profile is created when after use is created by using signal
            return render(request, 'registration/registration_done.html', context={'new_user': new_user, "name": ""})
        else:
            messages.error(request, "Form has error, please check")
            return render(request, self.initial_template, {'user_form': form})
        
        
        
class LoginView(View):

    form_class = LoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('accounts:dashboard'))
                else:
                    return HttpResponse('Disabled accounts')
            else:
                return HttpResponse('Invalid Login')
        else:
            form = LoginForm()
            return render(request, self.template_name, {'form': form})


class LogoutView(View):
    """
    Logs out user from session
    """

    template_name = 'registration/logout.html'

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return render(self.request, self.template_name)
