from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Diner, UserWorksAtDiner, Table
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/dashboard/login/')
def index(request):
    return render(request, 'dashboard/index.html', {})


@login_required(login_url='/dashboard/login/')
def map(request):

    tables = Table.objects.filter()

    return render(request, 'dashboard/map.html')


# Create your views here.
def login_view(request):
    try:
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            #Success!
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard:index'))
        else:
            #Wrong Password
            error_message = "Username and password did not match"
            return render(request, 'dashboard/login.html', {'error_message': error_message})
    except KeyError as e:
        pass

    #No username set

    return render(request, 'dashboard/login.html', {})

def setup(request):
    try:
        if len(User.objects.filter(username='Admin')) != 0:
            error_message = "Username already in use"
            return render(request, 'splash/index.html', {'error_message': error_message})


        user = User(username='Admin',
                    first_name='admin',
                    last_name='admin',
                    email='admin')
        user.set_password('admin')
        user.save()
        login(request, user)

        diner = Diner(address='Langkaia 1',
                      tlf='0985678908')
        diner.save()

        uwad = UserWorksAtDiner(user=user, diner=diner)
        uwad.save()

        t1 = Table(pos="0 0", diner=diner)
        t1.save()
        t2 = Table(pos="0 1", diner=diner)
        t2.save()
        t3 = Table(pos="0 2", diner=diner)
        t3.save()
        t4 = Table(pos="2 2", diner=diner)
        t4.save()

        return HttpResponseRedirect(reverse('dashboard:index'))

    except(KeyError):
        return render(request, 'splash/index.html', {})


def register(request):
    try:
        if(request.POST['password'] != request.POST['password_repeat']):
            error_message = "Passwords does not match"
            return render(request, 'user/register.html', {'error_message': error_message})

        if len(User.objects.filter(username=request.POST['email'])) != 0:
            error_message = "Username already in use"
            return render(request, 'user/register.html', {'error_message': error_message})


        user = User(username=request.POST['email'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'])
        user.set_password(request.POST['password'])
        user.save()

        return HttpResponseRedirect(reverse('dashboard:index'))

    except(KeyError):
        return render(request, 'user/register.html', {})
