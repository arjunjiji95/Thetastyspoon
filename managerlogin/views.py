from django.shortcuts import render, redirect
from . import forms
from branchmanager.models import Branchmanager


def managerhome(request):
    return render(request, 'managerhomepage/Managerhomepage.html', {'logid': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.manager_forms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if Branchmanager.objects.filter(branchmanagerusername=username).exists() and Branchmanager.objects.filter(branchmanagerpassword=password).exists():
                obj = Branchmanager.objects.get(branchmanagerusername=username)

                request.session['logid'] = obj.id
                return redirect('managerlogin:managerhome')

            else:
                return render(request, 'managerlogin/Managerlogin.html', {'form': form})
    else:
        form = forms.manager_forms()
    return render(request, 'managerlogin/Managerlogin.html', {'form': form})