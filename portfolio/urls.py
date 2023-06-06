from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about me', views.about_me_page_view, name='about me')
]



