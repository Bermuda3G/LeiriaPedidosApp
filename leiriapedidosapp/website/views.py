from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Produto, Pedido
from .forms import ProdutoForm, PedidoForm_1, ItemPedidoForm, PedidoForm_2

def home(request):
    #Debug
    print(request.session.get('pedido_id'))
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
    return redirect(request, 'homepage')

def add_pedido_1(request):
    submitted = False
    if request.method == "POST":
        form = PedidoForm_1(request.POST)
        if form.is_valid():
            pedido = form.save()
            request.session['pedido_id'] = pedido.id 
            request.session['valor_total'] = 0
            return redirect('add-item-pedido')
           
    else:
        form = PedidoForm_1
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_pedido_1.html', {'form':form, 'submitted':submitted}) #PARA O FINAL DO REGISTRO DE PEDIDO

def add_item_pedido(request):
    pk = request.session.get('pedido_id')
    pedido = Pedido.objects.get(id=pk)
    if request.method == "POST":
        form = ItemPedidoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.pedido_id = pk
            #Calcula valor
            valor_total = request.session.get('valor_total')
            valor_total += float(item.produto.preco) * item.quantidade
            request.session['valor_total'] = valor_total
            #Fim do cálculo
            item.save()
            if 'add_more' in request.POST:
                return redirect('add-item-pedido')
            elif 'next_step' in request.POST:
                return redirect('add-obs')
        
    else:
        form = ItemPedidoForm
    
    return render(request, 'add_item_pedido.html', {'form':form, 'pedido':pedido})

def add_pedido_obs(request):
    pk = request.session.get('pedido_id')
    pedido = Pedido.objects.get(id=pk)
    if request.method == "POST":
        form = PedidoForm_2(request.POST, instance=pedido)
        if form.is_valid():
            pedido.valor = request.session.get('valor_total')
            pedido.data_entrega = form.cleaned_data['data_entrega']
            pedido.observacoes = form.cleaned_data['observacoes']
            form.save()
            return HttpResponseRedirect('/registrar-pedido?submitted=True')
        
    else:
        form = PedidoForm_2
    return render(request, 'add_obs_pedido.html', {'form': form, 'pedido':pedido})