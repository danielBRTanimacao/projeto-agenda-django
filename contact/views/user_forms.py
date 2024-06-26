from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contact.forms import RegisterForm, RegisterUpdateForm

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

@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        context = {
            'form': form
        }
        return render(request, 'contact/user_update.html', context)
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'contact/user_update.html', context)
    
    form.save()
    return redirect('contact:user_update')

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')