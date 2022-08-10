"""backendchallenge4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from revenue.urls import *
from revenue.urls import revenue_router
from expenditure.urls import expenditure_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('revenue/', include(revenue_router.urls)),
    path('revenue/', include('revenue.urls')),
    path('expenditure/', include(expenditure_router.urls)),
    path('expenditure/',include('expenditure.urls')),
]
