from django.shortcuts import render, redirect
from . import forms
from .models import User


def user(request):

    if request.method == 'POST':
        form = forms.user_forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            msg = "Inserted Successfully"
            return redirect('user:user_forms')
    else:
        form = forms.user_forms
        msg = "Insertion not successfull"

    return render(request, "registration/Registration.html", {'form': form, 'msg': msg})


