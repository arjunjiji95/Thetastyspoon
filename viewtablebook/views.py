from django.shortcuts import render, redirect
from tablebook.models import Tablebook
from branchmanager.models import Branchmanager


def tablebook(request):
    login_id = request.session['logid']
    model_object = Branchmanager.objects.get(id=login_id)

    model_object1 = Tablebook.objects.all()
    #model_object = Tablebook.objects.filter(branch_id=branchmanager_id)
    #model_object1=Feedback.objects.filter(branch_id=model_object.branch_id)

    return render(request, "viewtablebook/viewtablebook.html", {'data': model_object1, 'data1':model_object})