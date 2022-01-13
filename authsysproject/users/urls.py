from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
    path('index/', views.index, name='index'),
    path('profile/', auth_view.LogoutView.as_view(template_name='profile.html'), name="profile"),
    path('profile_1/', auth_view.LogoutView.as_view(template_name='profile_1.html'), name="profile_1"),
    path('profile_2/', auth_view.LogoutView.as_view(template_name='profile_2.html'), name="profile_2"),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('contactUs/', auth_view.LogoutView.as_view(template_name='contactUs.html'), name="contactUs"),
    path('membershipplans/', auth_view.LogoutView.as_view(template_name='membershipplans.html'), name="membershipplans"),
    path('forgot-password-password/', auth_view.LogoutView.as_view(template_name='forgot-password-password.html'), name="forgot-password-password"),
    path('success-story/', auth_view.LogoutView.as_view(template_name='success-story.html'), name="success-story"),
    path('search/', auth_view.LogoutView.as_view(template_name='search.html'), name='search'),
    path('feedback/', auth_view.LogoutView.as_view(template_name='feedback.html'), name='feedback'),
    path('image_upload/', auth_view.LogoutView.as_view(template_name='image_upload.html'), name='image_upload'),
    path('edit/', auth_view.LogoutView.as_view(template_name='edit.html'), name='edit'),
    # path('login/', auth_view.LoginView.as_view(), name="login"),
]
