from django.shortcuts import render, redirect
from branch.models import Branch



def repbranch(request):
    login_id = request.session['logid']

    #model_object = User.objects.get(id=login_id)
    model_object1=Branch.objects.all()

    return render(request, "repbranch/repbranch.html", {'data': model_object1})