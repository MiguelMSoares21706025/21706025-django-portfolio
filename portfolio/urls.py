from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name='home'),
    path('courses', views.courses_page_view, name='courses'),
    path('playground', views.playground_page_view, name='playground'),
    path('sitemap', views.sitemap_page_view, name='sitemap'),
    path('blog', views.blog_page_view, name='blog'),
    path('webDev', views.webDev_page_view, name='webDev'),
    path('about', views.about_page_view, name='about'),

]



