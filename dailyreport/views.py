from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Dailyreport
from orderfood.models import Orderfood
from tablebook.models import Tablebook


def dailyreport(request):
    login_id = request.session['logid']
    model_object = Dailyreport.objects.all()
    # model_object1 = Orderfood.objects.filter(user_id=login_id)
    # model_object2 = Tablebook.objects.filter(branch_id=model_object.branch_id)
    # #d = Orderfood.objects.filter(user_id=login_id, orderfoodstatus=0).last()
    # grandtotal = Orderfood.objects.filter(user_id=login_id).aggregate(grand=Sum('orderfoodtotalamount'))
    # quant = Orderfood.objects.filter(user_id=login_id).aggregate(quan=Count('orderfoodquantity'))
    if request.method == 'POST':
        form = forms.dailyreport_forms(request.POST, request.FILES)
        if form.is_valid():
            reportObj = form.cleaned_data
            reportdate = reportObj['reportdate']
            a = Dailyreport(reportdate=reportdate)
            request.session['reportdate']=reportdate
            a.save()

            return redirect('dailyreport:dailyreport_forms')
    else:
        form = forms.dailyreport_forms

    return render(request, "dailyreport/dailyreport.html",
                  {'form': form, 'data': model_object})
