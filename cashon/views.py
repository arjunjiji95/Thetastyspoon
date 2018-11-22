from django.db.models import Sum, Count
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from orderfood.models import Orderfood


def cashon(request):
    login_id = request.session['logid']
    model_object = Orderfood.objects.filter(user_id=login_id)
    #d = Orderfood.objects.filter(user_id=login_id, orderfoodstatus=0).last()
    grandtotal = Orderfood.objects.filter(user_id=login_id).aggregate(grand=Sum('orderfoodtotalamount'))
    quant = Orderfood.objects.filter(user_id=login_id).aggregate(quan=Count('orderfoodquantity'))

    return render(request, "cashon/cashon.html",
                  {'data': model_object, 'q': quant, 'g': grandtotal})
