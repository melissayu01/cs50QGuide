"""cs50_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from . import views

urlpatterns = [
    # url(r'^$', views.populate_home_page),
    url(r'^club/([0-9]+)$', views.populate_long_club),
    url(r'^reviewed/', views.populate_review_submitted),
    url(r'^register/$', views.get_new_user),
    url(r'^thanks/$', views.populate_user_created),
    url(r'^login/$', views.populate_login),
    url(r'^logout/$', views.populate_logout),
    url(r'^static/(.*)', views.return_static_file),
    url(r'^$', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
