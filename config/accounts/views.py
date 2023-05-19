from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
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


class Contact(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("/")
    template_name = 'auth/contact.html'

    def post(self, request):
        form = ContactForm(request.POST)
        if request.user.is_authenticated:
            form.name=request.user.username
            form.email=request.user.email
        if form.is_valid():
            f = form.save(commit=False)  
            print(f)          
            f.slug = slugify(f.name)
            form.save()
            return redirect('/')
        return render(request, 'auth/contact.html', {'form': form})
