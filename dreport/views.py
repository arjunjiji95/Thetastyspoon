from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Dreport


def dreport(request):
    login_id = request.session['logid']
    model_object = Dreport.objects.filter(branchmanager_id=login_id)
    if request.method == 'POST':
        form = forms.dreport_forms(request.POST, request.FILES)
        if form.is_valid():
            drObj = form.cleaned_data
            date = drObj['reportdate']
            tcount = drObj['tablecount']
            tamt = drObj['tableamt']
            fcunt = drObj['foodcount']
            famt = drObj['foodamt']
            pc = drObj['pcount']
            pa = drObj['pamt']

            a = Dreport(reportdate=date, tablecount=tcount, tableamt=tamt, foodcount=fcunt, foodamt=famt, pcount=pc,
                        pamt=pa,
                        branchmanager_id=login_id)
            a.save()

            return redirect('dreport:dreport_forms')
    else:
        form = forms.dreport_forms

    return render(request, "report/report.html", {'form': form, 'data': model_object})
