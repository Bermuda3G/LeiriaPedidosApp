from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
        print(f'essa é a minha request: {request}')
        return render(request, 'homepage.html', {})

def logout_user(request):
    print(f'essa é')
    logout(request)
    messages.success(request, "Logout feito com sucesso! Até logo :D")
    return redirect('homepage')