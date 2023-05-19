from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import ContactForm, CustomUserCreationForm
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            u.save()
            return redirect("/")
    else:
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'auth/register.html', context)


class ContactForm(CreateView):
    model = Contact
    # fields = ["name", "email", 'subject', 'message']
    form_class=ContactForm
    success_url = reverse_lazy("/")
    template_name='auth/contact.html'


    # def get(self, request):
    #     context = {'form': ContactForm()}
    #     return render(request, 'auth/contact.html', context)

    # def post(self, request):
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, '/')
    #     return render(request, '/', {'form': form})
