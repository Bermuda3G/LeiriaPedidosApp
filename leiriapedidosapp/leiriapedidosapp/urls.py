# filepath: c:\Users\victo\Desktop\leiriapedidosapp\leiriapedidosapp\leiriapedidosapp\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('homepage.urls')),
]