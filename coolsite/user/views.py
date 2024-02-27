from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm


# Create your views here.
def loginUser(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponse("Вы успешно авторизовались")
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})
def registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponse("Вы успешно зарегистрировались")
    else:
        form = RegisterUserForm()
    return render(request, 'users/registration.html', {'form': form})


def logoutUser(request):
    logout(request)
    return HttpResponse("Вы успешно авторизовались!")

def homepage(request):
    return render(request, 'users/homepage.html')
