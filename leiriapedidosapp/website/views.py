from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Produto

# Create your views here.
def home(request):
    produtos = Produto.objects.all()

    #Checa se o usuário está loggado
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Autenticar
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Você foi loggado com sucesso!!")
            return redirect('homepage')
        else:
            messages.success(request, "Não foi possível concluir o processo de Login. Tente novamente.")
            return redirect('homepage')
    else:
        return render(request, 'homepage.html', {'produtos':produtos})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout feito com sucesso! Até logo :D")
    return redirect('homepage')

def produto_item(request, pk):
    if request.user.is_authenticated:
        registro_produto = Produto.objects.get(id=pk)
        return render(request, 'produto.html', {'registro_produto':registro_produto})
    else:
        messages.success(request, "Não foi possível acessar o produto. Faça login novamente!!")
        return redirect('homepage')