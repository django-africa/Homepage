"""djangoafrica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from django.conf.urls import url
from homepage.views import HomeView 
from blog.views import ckeditor_form_view, PostDetailView



urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('blog/', ckeditor_form_view, name='ckeditor-form'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/<int:pk>/<slug:slug>/', PostDetailView.as_view(), 
    name='detail'),
    path('xxxxhas2/', admin.site.urls),
    path('forum/', include('django_simple_forum.urls')),
] + static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
