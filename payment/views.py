from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404

from orderfood.models import Orderfood
from address.models import Address
from django.contrib import messages


def payment(request):
    login_id = request.session['logid']

    model_object = Orderfood.objects.filter(user_id=login_id)
    d = Orderfood.objects.filter(user_id=login_id, orderfoodstatus=0).last()
    grandtotal = Orderfood.objects.filter(user_id=login_id).aggregate(grand=Sum('orderfoodtotalamount'))
    quant = Orderfood.objects.filter(user_id=login_id).aggregate(quan=Count('orderfoodquantity'))

    1
    # form=forms.payment_forms

    return render(request, "python/purchase/PaymentMethod.html",
                  {'data': model_object, 'q': quant, 'g': grandtotal, 'e': d})


def card(request):
    if request.method == 'POST':

        a = request.POST.get['method']
        return redirect('payment:card')
    else:
        return redirect('payment:payment')

    return render(request, "python/purchase/PaymentMethod.html", {'a': a})

# def card(request):
#     if request.method == 'POST':
#
#       a=request.GET['method']
#       messages.info(request, a)
#       if a==1:
#        return render(request, "python/purchase/CardPyment.html")
#       elif a==2:
#        return render(request, "python/purchase/NetBanking.html")
#       else:
#        return render(request, "python/purchase/FinalPage.html")
