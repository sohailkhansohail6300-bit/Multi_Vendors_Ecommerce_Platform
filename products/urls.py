"""
URL configuration for confi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('products/',views.all_products, name='all_products'),
    path('product_detail/<int:id>/',views.product_detail, name='product_detail'),
    path('product_order/<int:id>/',views.product_order, name='product_order'),
    path('category_product/<int:id>/',views.category_product, name='category_product'),
    path('nave_link/<int:id>/',views.nave_link, name='nave_link'),
    path('order/',views.order, name='order'),
     
]
