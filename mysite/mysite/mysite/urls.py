"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#mysite urls.py
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qna/', include('qna.urls')),
    path('about/', blog_views.about_me, name='about'),
    path('profile/', blog_views.my_profile, name='profile'),
    path('contact/', blog_views.get_contact, name='contact'),
    path('blog/', include('blog.urls')),  
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
]

