from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    #path('login/', views.login_user, name='user login'),
    #path('logout/', views.logout_user, name='user logout'),
]