"""
URL configuration for myproject project.

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # # Serve the AASA file from the .well-known directory
    # re_path(r'^\.well-known/apple-app-site-association$', serve, {
    #     'document_root': settings.STATIC_ROOT,
    #     'path': 'apple-app-site-association'
    # }),

    # Serve the AASA file
    path('.well-known/apple-app-site-association', TemplateView.as_view(template_name='apple-app-site-association', content_type='application/json')),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

