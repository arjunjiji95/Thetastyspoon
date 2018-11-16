from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from orderfood.models import Orderfood
from address.models import Address

def address(request):
    login_id = request.session['logid']
    # orderfoodbillno = request.session['orderfoodbillno']
    #model_object1 = Address.objects.filter(user_id=login_id)


    # orderfoodbillno = request.session['orderfoodbillno']
    # pkphobj = Orderfood.objects.get(orderfoodbillno=orderfoodbillno)
    # fk = pkphobj.id
    # model_object1 = Address.objects.filter(billno=fk)
    model_object = Orderfood.objects.filter(user_id=login_id)
    d = Orderfood.objects.filter(user_id=login_id,orderfoodstatus=0).last()
    grandtotal = Orderfood.objects.filter(user_id=login_id).aggregate(grand=Sum('orderfoodtotalamount'))
    quant = Orderfood.objects.filter(user_id=login_id).aggregate(quan=Count('orderfoodquantity'))


    # total = model_object.orderfoodtotalamount
    # billno = model_object.orderfoodbillno
    form=forms.address_forms

    # if request.method == 'POST':
    #
    #     form = forms.address_forms(request.POST, request.FILES)
    #     if form.is_valid():
    #         addressObj = form.cleaned_data
    #         address = addressObj['address']
    #         phone = addressObj['phone']
    #
    #         a = Address(address=address, phone=phone, orderfoodbillno=d, total=grandtotal)
    #         a.save()
    #
    #         return redirect('address:address_forms')
    # else:
    #     form = forms.address_forms

    # return render(request, "mycart/mycart.html", {'form': form, 'data': model_object, 'data1': model_object1})


    return render(request, "mycart/mycart.html", {'form': form, 'data': model_object, 'q':quant, 'g': grandtotal, 'e':d})

def delete_food(request, pk):
    post = get_object_or_404(Orderfood, pk=pk)
    post.delete()
    return redirect('address:address_forms')
#