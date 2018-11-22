from django.shortcuts import render, redirect

from dreport.models import Dreport
from branch.models import Branch
from branchmanager.models import Branchmanager




def viewreport(request, pk):
    login_id = request.session['logid']
    request.session['branch_id'] = pk

    model_object1 = Branch.objects.filter(id=pk)
    model_object3 = Branchmanager.objects.get(branch_id=pk)
    model_object2 = Dreport.objects.filter(branchmanager_id=model_object3.id)
    # cursor = connection.cursor()
    # cursor.execute("update tabledetails_tabledetails set status='Booked' where id='%s'" % (pk,))

    return render(request, "viewreport/viewreport.html", {'data': model_object1, 'data1': model_object2})
