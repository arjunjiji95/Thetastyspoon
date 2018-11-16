from django.shortcuts import render, redirect
from . import forms
from django.core.mail import EmailMessage


def manager(request):
    if request.method == 'POST':
        form = forms.manager_forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            obj = form.cleaned_data
            mail = obj['branchmanageremail']
            uname = obj['branchmanagerusername']
            pwd = obj['branchmanagerpassword']
            email = EmailMessage('Branch Manager Registration',
                                 'Registration Successfull username:  ' + uname + '     password:' + pwd + '',
                                 to=[mail])

            email.send()

            return redirect('branchmanager:manager_forms')
    else:
        form = forms.manager_forms

    return render(request, "mgregistration/mgregistration.html", {'form': form})
