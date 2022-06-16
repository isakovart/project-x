from json import loads
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Swimmer,Award,Fact
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from .forms import SearchForm, UserRegisterForm, UserLoginForm, UserCreationForm
from django.contrib import messages
from django.db.models import Q

def HomePageRender(request):
    Swimmers = Swimmer.objects.all()
    paginator = Paginator(Swimmers, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render( request, 'main/HomePage.html', {'page_obj': page_obj} )

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1']==form.cleaned_data['password2']:
                user = form.save()
                login(request, user)
                messages.success(request, 'Вы успешно зарегистрировались')
                return redirect('Login')
            else:
                messages.error(request, 'Ошибка регистрации')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/Register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли')
            return redirect('Home')
        else:
            messages.error(request, 'Ошибка входа')
    else:
        form = UserLoginForm()
    return render(request, 'main/Login.html',  {'form':form})

def Logout(request):
    logout(request)
    return redirect('Login')

def Search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            
            
            qr = form.cleaned_data['search'].split()
            res = list()
            if qr != []:
                for i in qr:
                    
                    a = Swimmer.objects.filter(Q(Name__icontains= i))
                    res.append(*a)
            return render( request, 'main/searchresult.html', {'swimmers':res} )
    else:
        form = SearchForm()
        return render(request, 'main/Search.html', {'form': form})

def SwimmerPage(request, id):
    Swimmers = Swimmer.objects.get(pk=id)
    return render(request, 'main/Swimmer.html', {'swimmer': Swimmers})

def renderadd(request):
    return render(request, 'main/AddSwimmer.html')

def createswimmer(request):
    my_json = request.body.decode('utf8')
    
    my_json = loads(my_json)
    print(type(my_json))
    sw = Swimmer.objects.create(Name = my_json['Name'], Age = int(my_json['Age']), Weight = int(my_json['Weight']))
    Awards = my_json['Awards']
    Facts = my_json['Facts']
    
    for award in Awards:
        aw = Award.objects.create(Name = award[0], Date = award[1])
        sw.Awards.add(aw)
    
    for fact in Facts:
        fc = Fact.objects.create(Name = fact[0], Content = fact[1])
        sw.Facts.add(fc)

    return HttpResponse()