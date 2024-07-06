from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import *

router = routers.DefaultRouter()
router.register('login', Usuario_view_login, basename='login')
router.register('registro', Usuario_view_registro, basename='registro')
router.register('inicio', Usuario_view_login, basename='inicio')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    # path('registro', Usuario_view_registro.as_view({'get': 'list'}), name='registro'),
    path('token', TokenProvider.as_view(), name = 'token'),
]





# urlpatterns = [
#     path('', views.redirect_view),
#     path('registro/', views.registro, name='registro'),
#     path('login/', views.login_view, name='login'),
#     path('inicio/', views.inicio, name='inicio'),
# ]
