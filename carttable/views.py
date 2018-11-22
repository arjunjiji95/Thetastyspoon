from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from tablebook.models import Tablebook


def carttable(request):
    login_id = request.session['logid']
    # orderfoodbillno = request.session['orderfoodbillno']
    #model_object1 = Address.objects.filter(user_id=login_id)


    # orderfoodbillno = request.session['orderfoodbillno']
    # pkphobj = Orderfood.objects.get(orderfoodbillno=orderfoodbillno)
    # fk = pkphobj.id
    # model_object1 = Address.objects.filter(billno=fk)
    model_object = Tablebook.objects.filter(user_id=login_id)
    #d = Orderfood.objects.filter(user_id=login_id,orderfoodstatus=0).last()
    grandtotal = Tablebook.objects.filter(user_id=login_id).aggregate(grand=Sum('tablerate'))
    quant = Tablebook.objects.filter(user_id=login_id).aggregate(quan=Count('tableno'))


    # total = model_object.orderfoodtotalamount
    # billno = model_object.orderfoodbillno
    #form=forms.address_forms

    # if request.method == 'POST':
    #
    #     form = forms.address_forms(request.POST, request.FILES)
    #     if form.is_valid():
    #         addressObj = form.cleaned_data
    #         address = addressObj['address']
    #         phone = addressObj['phone']
    #
    #         a = Address(address=address, phone=phone, billno=d, total=grandtotal.grand,user_id=login_id)
    #         a.save()
    #
    #         return redirect('address:address_forms')
    # else:
    #     form = forms.address_forms

    # return render(request, "mycart/mycart.html", {'form': form, 'data': model_object, 'data1': model_object1})


    return render(request, "carttable/carttable.html", {'data': model_object, 'q':quant, 'g': grandtotal})

def delete_tab(request, pk):
    post = get_object_or_404(Tablebook, pk=pk)
    post.delete()
    return redirect('carttable:carttable_forms')
#