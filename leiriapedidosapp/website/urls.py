from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('sair/', views.logout_user, name='user-logout'),
    path('produtos-todos', views.all_produtos, name='produtos-todos'),
    path('produto/<int:pk>', views.produto_item, name='produto'),
    path('registrar-produto', views.add_produto, name='add-produto'),
    path('atualizar-produto/<int:pk>', views.update_produto, name='atualizar-produto'),
    path('deletar-produto/<int:pk>', views.delete_produto, name='deletar-produto'),

    path('registrar-pedido', views.add_pedido_1, name='add-pedido'),
    path('registrar-itens-pedido', views.add_item_pedido, name='add-item-pedido'),
    path('registrar-observacoes-pedido', views.add_pedido_obs, name='add-obs')
]