# from django.shortcuts import render, redirect, get_object_or_404
# from . import forms
# from user.models import User
# from branchmanager.models import Branchmanager
#
#
#
#
# def login(request):
#     if request.method == 'POST':
#         form = forms.login_forms(request.POST)
#         if form.is_valid():
#             userObj = form.cleaned_data
#             username = userObj['username']
#             password = userObj['password']