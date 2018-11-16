import datetime
from time import strftime

from django.shortcuts import render, redirect
from . import forms
from .models import Purchasehead


def purchase(request):
    login_id = request.session['logid']
    model_object = Purchasehead.objects.filter(branchmanager_id=login_id)

    if request.method == 'POST':

        form = forms.purchasehead_forms(request.POST, request.FILES)
        if form.is_valid():
            purchaseObj = form.cleaned_data
            purchaseinvoice = purchaseObj['purchaseinvoice']
            purchasedate = purchaseObj['purchasedate']
            # purchasedate=strftime('purchasedate')

            agency_id = purchaseObj['agency_id']
            request.session['purchaseinvoice'] = purchaseinvoice
            # request.session['purchasedate'] = purchasedate


            a = Purchasehead(purchaseinvoice=purchaseinvoice, purchasedate=purchasedate,
                             agency_id=agency_id,
                             branchmanager_id=login_id)
            a.save()

            return redirect('purchasehead:purchasehead_forms')
    else:
        form = forms.purchasehead_forms

    return render(request, "purchasedetails/Purchasedetails.html", {'form': form, 'data': model_object})
