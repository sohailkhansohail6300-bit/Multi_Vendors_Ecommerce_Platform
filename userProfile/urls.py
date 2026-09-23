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

from django.urls import path,include
from . import views
app_name = 'userProfile'
urlpatterns = [
    
    path('profile/', views.user_profile, name='user_profile'),
    path('inventory/', views.seller_inventory, name='seller_inventory'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/update/<int:id>/', views.update_product, name='update_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('orders/', views.order_list, name='order_list'),
    path('logout/', views.logout, name='logout'),
    
]

