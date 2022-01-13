from django.contrib.auth import authenticate, login
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def profile_1(request):
    return render(request, 'profile_1.html')


def profile_2(request):
    return render(request, 'profile_2.html')


def contactUs(request):
    return render(request, 'contactUs.html')


def membershipplans(request):
    return render(request, 'membershipplans.html')


def forgot_password(request):
    return render(request, 'forgot-password-password.html')


def success_story(request):
    return render(request, 'success-story.html')


def search(request):
    return render(request, 'search.html')


def feedback(request):
    return render(request, 'feedback.html')


def image_upload(request):
    return render(request, 'image_upload.html')


def edit(request):
    return render(request, 'edit.html')


# register
def index(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            profile = form.cleaned_data.get('profile')
            gender = form.cleaned_data.get('gender')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            mobile = form.cleaned_data.get('mobile')
            email = form.cleaned_data.get('email')

            # mail system

            htmly = get_template('email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()

    # Welcome Email

    # subject = 'welcome to mail'
    # message = f'Hi {username.username}, thank you for registering in matrimony.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [user.email, ]
    # send_mail(subject, message, email_from, recipient_list)

    return render(request, 'index.html',
                  {'form': form})


# @login_required()
# def profile(request):
#     return render(request, 'users/profile.html')


def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})
