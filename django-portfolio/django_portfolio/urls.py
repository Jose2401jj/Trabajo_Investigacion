"""
URL configuration for django_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import CustomLoginView, register
from django.contrib.auth import views as auth_views
from portfolio import views
from portfolio.views import experiencia_view, educacion_view


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('home/', views.home, name='home_view'), 
    path('blog/', include('blog.urls')),
    path('experiencia/', experiencia_view, name='experiencia'),
    path('educacion/', views.educacion_view, name='educacion'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
