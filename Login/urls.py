"""
URL configuration for TourExpress13 project.

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
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('salir/', views.salir, name="salir"),
    path('registrarEmprendimiento/', views.registrarEmprendimiento, name='registrarEmprendimiento'),

    path('cliente/catalogo', views.productos_cliente, name="productos_cliente"),
    path('cliente/info', views.info_graffitour, name="info_graffitour"),
    

    path('productos/', views.productos, name='productos'),
    path('productos/crear_producto', views.crear_producto, name='crear_producto'),
    path('productos/<int:producto_id>', views.producto_detalle, name='producto_detalle'),
    path('productos/<int:producto_id>/eliminar', views.eliminar_producto, name='eliminar_producto'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
