from django.shortcuts import render
from branch.models import Branch
from user.models import User
from branchmanager.models import Branchmanager
from feedback.models import Feedback
from complaint.models import Complaint


def adfeed(request, pk):
    login_id = request.session['logid']
    request.session['branch_id'] = pk
    model_object = Branch.objects.filter(id=pk)
    #model_object3 = Branchmanager.objects.get(id=login_id)
    model_object1 = Feedback.objects.filter(branch_id=pk)
    model_object2 = Complaint.objects.filter(branch_id=pk)

    return render(request, "adfeed/adfeed.html",
                  {'data': model_object, 'data1': model_object1, 'data2': model_object2})
