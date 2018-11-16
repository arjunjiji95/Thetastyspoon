from django.shortcuts import render, redirect
from . import forms
from user.models import User
from branchmanager.models import Branchmanager


def userhome(request):
    return render(request, 'Homepage/Homepage.html', {'logid': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.login_forms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if User.objects.filter(userusername=username).exists() and User.objects.filter(userpassword=password).exists():
                obj = User.objects.get(userusername=username)

                request.session['logid'] = obj.id
                return redirect('login:userhome')
            elif Branchmanager.objects.filter(branchmanagerusername=username).exists() and Branchmanager.objects.filter(branchmanagerpassword=password).exists():
                obj = Branchmanager.objects.get(branchmanagerusername=username)

                request.session['logid'] = obj.id
                return redirect('managerlogin:managerhome')


            else:
                return render(request, 'Login/Login.html', {'form': form})
    else:
        form = forms.login_forms()
    return render(request, 'Login/Login.html', {'form': form})


# def logout(request):
#     if request.method == 'POST':
#         request.session.clear()


