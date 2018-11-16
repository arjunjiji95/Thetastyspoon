from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Purchasedetails
from purchasehead.models import Purchasehead



def purchasedetails(request):

    purchaseinvoice = request.session['purchaseinvoice']
    pkphobj=Purchasehead.objects.get(purchaseinvoice=purchaseinvoice)
    fk=pkphobj.id
    model_object = Purchasedetails.objects.filter(purchaseinvoice=fk)
    grandtotal = Purchasedetails.objects.filter(purchaseinvoice=fk).aggregate(grand=Sum('itemunittotal'))
    quant = Purchasedetails.objects.filter(purchaseinvoice=fk).aggregate(quan=Count('itemname'))


    if request.method == 'POST':
        form = forms.purchasedetails_forms(request.POST, request.FILES)
        if form.is_valid():
            purObj = form.cleaned_data
            itemname = purObj['itemname']
            itemquantity = purObj['itemquantity']
            itembasicrate = purObj['itembasicrate']
            total=int(itembasicrate)*int(itemquantity)



            a = Purchasedetails(itemname=itemname, itemquantity=itemquantity, itembasicrate=itembasicrate,
                                 itemunittotal=total, purchaseinvoice=fk)
            a.save()


            return redirect('purchasedetails:purchasedetails_forms')
    else:
        form = forms.purchasedetails_forms

    return render(request, "Purchase/Purchase.html", {'form': form, 'data': model_object, 'invs':purchaseinvoice, 'g':grandtotal, 'q':quant})
