"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.dashboard, name='dashboard')
Class-based views
    1. Add an import:  from other_app.views import dashboard
    2. Add a URL to urlpatterns:  path('', dashboard.as_view(), name='dashboard')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.customer.urls')),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('pending-customers/',views.export_pending_customers_csv, name='export_pending_customers'),
    path('',include('apps.events.urls')),
    path('',include('apps.cameramen.urls')),
    
]
