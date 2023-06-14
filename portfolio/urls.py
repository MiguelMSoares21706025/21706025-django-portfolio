
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name='home'),
    path('courses', views.courses_page_view, name='courses'),
    path('playground', views.playground_page_view, name='playground'),
    path('sitemap', views.sitemap_page_view, name='sitemap'),
    path('der', views.der_page_view, name='der'),
    path('blog/', views.blog_page_view, name='blog'),
    path('webDev', views.webDev_page_view, name='webDev'),
    path('article/<int:article_id>/', views.article_page_view, name='article'),
    path('add_author', views.add_author_page_view, name='add_author'),
    path('add_article', views.add_article_page_view, name='add_article'),
    path('edit_article/<int:article_id>/', views.edit_article_page_view, name='edit_article'),
    path('remove_article/<int:article_id>/', views.remove_article, name='remove_article'),
    path('add_curricularUnit', views.add_curricularUnit_page_view, name='add_curricularUnit'),
    path('edit_curricularUnit/<int:curricularUnit_id>', views.edit_curricularUnit_page_view, name='edit_curricularUnit'),
    path('remove_curricularUnit/<int:curricularUnit_id>', views.remove_curricularUnit, name='remove_curricularUnit'),
    path('add_project', views.add_project_page_view, name='add_project'),
    path('edit_project/<int:project_id>/', views.edit_project_page_view, name='edit_project'),
    path('remove_project/<int:project_id>/', views.remove_project, name='remove_project'),
    path('login/', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
]



