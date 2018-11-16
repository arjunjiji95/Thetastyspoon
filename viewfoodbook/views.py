from django.shortcuts import render, redirect
from orderfood.models import Orderfood


def foodbook(request):
    login_id = request.session['logid']

    model_object = Orderfood.objects.all()
    #model_object1=Feedback.objects.filter(branch_id=model_object.branch_id)

    return render(request, "viewfoodbook/viewfoodbook.html", {'data': model_object})