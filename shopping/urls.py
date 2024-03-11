"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from plants import views as plantsviews
from equipments import views as equipviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', plantsviews.home, name='home'),
    path('insideplants/', plantsviews.showinsideplants, name='insideplants'),
    path('details/<int:id>/',plantsviews.details, name='details'),
    path('auth_login/', plantsviews.auth_login, name='auth_login'),
    path('auth_register/',plantsviews.auth_register,name='auth_register'),
    path('auth_login/', plantsviews.auth_login, name='auth_login'),
    path('auth_logout/',plantsviews.auth_logout,name='auth_logout'),
    path('checkout/', plantsviews.checkout, name='checkout'),
    path('add_to_cart/<int:id>/',plantsviews.add_to_cart, name='add_to_cart'),

    path('showequipments/', equipviews.showequipments, name='showequipments'),
    path('equiepmentdetails/<int:id>/', equipviews.edetails, name='edetails'),
    path('echeckout/', equipviews.checkout, name='echeckout'),
    path('add_to_ecart/<int:id>/',equipviews.add_to_cart, name='add_to_ecart')
]
