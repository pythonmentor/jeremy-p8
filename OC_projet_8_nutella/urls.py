"""OC_projet_8_nutella URL Configuration

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
from django.urls import path, include
from django.contrib import admin

from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('legales_notices/', views.legales_notices, name='legales_notices'),
    path('users/', include('users.urls')), 
    path('products/', include('products.urls')),
    path('favorites/', include('favorites.urls')),
]
