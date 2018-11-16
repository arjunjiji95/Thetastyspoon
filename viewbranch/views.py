from django.shortcuts import render
from branch.models import Branch
from tabledetails.models import Table
from branchmanager.models import Branchmanager

def branchview(request, pk):
    login_id = request.session['logid']
    request.session['branch_id'] = pk

    model_object1=Branch.objects.filter(id=pk)
    model_object3=Branchmanager.objects.get(branch_id=pk)
    model_object2=Table.objects.filter(branchmanager_id=model_object3.id)

    return render(request, "viewbranch/Viewbranch.html", {'data': model_object1, 'data1': model_object2})