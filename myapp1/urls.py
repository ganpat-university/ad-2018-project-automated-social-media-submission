from django.urls import path
from .views import home, landing, login, UserCreateView, signup_view, main, UserCreateView_fb,UserCreateView_linked_in


urlpatterns = [
    path('', home),
    path('landing.html', landing, name='landing.html'),
    path('login.html', UserCreateView.as_view(), name='login.html'),
    path('signup.html', signup_view, name='signup.html'),
    path('main.html', main, name='main.html'),
    path('fb_signup.html', UserCreateView_fb.as_view(), name='fb_signup.html'),
    path('linkedin_signup.html', UserCreateView_linked_in, name='linkedin_signup.html')
]
