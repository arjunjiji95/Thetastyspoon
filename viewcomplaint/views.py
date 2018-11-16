from django.shortcuts import render, redirect
from complaint.models import Complaint
from branchmanager.models import Branchmanager

def compp(request):
    login_id = request.session['logid']

    model_object = Branchmanager.objects.get(id=login_id)
    model_object1=Complaint.objects.filter(branch_id=model_object.branch_id)

    return render(request, "viewcomplaint/Viewcomplaint.html", {'data': model_object1})