"""
URL configuration for foodmain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('items/<int:pk>/',views.items,name='items'),
    path('description/<int:pk>/',views.description,name='description'),
    path('view_menu/',views.view_menu,name='view_menu'),
    

    path('update-quantity/<int:item_id>/<str:action>/', views.update_quantity, name='update_quantity'),
    path('order-summary/', views.order_summary, name='order_summary'),

    path('clear_cart/', views.clear_cart, name='clear_cart'),


    path('checkout/', views.checkout, name='checkout'),


    path('',views.login,name='login'),

    # path('paynow/', views.paynow, name='paynow'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
