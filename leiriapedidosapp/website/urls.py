from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('user-logout/', views.logout_user, name='user-logout'),
    path('produto/<int:pk>', views.produto_item, name='produto')
]