from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('sair/', views.logout_user, name='user-logout'),
    path('produto/<int:pk>', views.produto_item, name='produto'),
    path('registrar-produto', views.add_produto, name='add-produto'),
    path('atualizar-produto/<int:pk>', views.update_produto, name='atualizar-produto'),
    path('deletar-produto/<int:pk>', views.delete_produto, name='deletar-produto'),
]