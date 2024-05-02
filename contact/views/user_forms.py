from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Formulario enviado com sucesso')
            return redirect('contact:index')

    context = {
        'form': form
    }
    return render(request, 'contact/register.html', context)

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('contact:index')
        messages.error(request, 'Mermão login errado invalido')

    context = {
        'form': form
    }

    return render(request, 'contact/login.html', context)

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')