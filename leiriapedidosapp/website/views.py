from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def home(request):
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
        return render(request, 'homepage.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logout feito com sucesso! Até logo :D")
    return redirect('homepage')

def all_produtos(request):
    if request.user.is_authenticated:
        produtos = Produto.objects.all()
        return render(request, 'produtos_todos.html', {'produtos':produtos})
    else:
        messages.success(request, "Não foi possível visualizar os produtos. Faça login novamente!!")
        return redirect('homepage')

def produto_item(request, pk):
    if request.user.is_authenticated:
        registro_produto = Produto.objects.get(id=pk)
        return render(request, 'produto.html', {'registro_produto':registro_produto})
    else:
        messages.success(request, "Não foi possível acessar o produto. Faça login novamente!!")
        return redirect('homepage')
    
def add_produto(request):
    submitted = False
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registrar-produto?submitted=True')
    else:
        form = ProdutoForm
        if 'submitted' in request.GET:
            submitted=True
    
    return render(request, 'add_produto.html', {'form':form, 'submitted':submitted})
    
def update_produto(request, pk):
    registro_produto = Produto.objects.get(id=pk)
    form = ProdutoForm(request.POST or None, instance=registro_produto)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    
    return render(request, 'update_produto.html', {'registro_produto':registro_produto, 'form':form})

def delete_produto(request, pk):
    registro_produto = Produto.objects.get(id=pk)
    registro_produto.delete()
    return redirect('homepage')
