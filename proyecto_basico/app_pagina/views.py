from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def inicio(request):
    return render(request, 'inicio.html')

def pagina1(request):
    return render(request, 'pagina1.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pagina1')  # Nombre de la URL para la página1
        else:
            return render(request, 'inicio.html', {'error': 'Credenciales inválidas.'})
    return render(request, 'inicio.html')
