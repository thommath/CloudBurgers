from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/dashboard/login/')
def index(request):
    return render(request, 'dashboard/index.html', {})





# Create your views here.
def login(request):
    try:
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            #Success!
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard:index'))
        else:
            #Wrong Password
            error_message = "Username and password did not match"
            return render(request, 'user/login.html', {'error_message': error_message})
    except KeyError as e:
        pass

    #No username set


    return render(request, 'user/login.html', render_list)

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
