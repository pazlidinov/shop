from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import ContactForm, RegisterForm
from .models import Contact


# Create your views here.
def my_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            print("OK")
            return redirect('/')
        else:
            # No backend authenticated the credentials
            print("error")
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")


def logged_out(request):
    logout(request)
    return redirect("/accounts/login/")


def my_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('ok1')
            return redirect('accounts:login')  
    
    form = RegisterForm()
    data = {
        'form': form
    }
        # return render(request, 'auth/register.html', context=data)
    return render(request, 'auth/register.html', context=data)


class Contact(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'auth/contact.html'
    success_url = reverse_lazy("/")

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            print('ook1')
            f = form.save(commit=False)
            f.name = request.user

            f.save()
            print('ok')
            return redirect('/')
        return render(request, 'auth/contact.html', {'form': form})
