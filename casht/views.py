from django.db.models import Sum, Count
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from tablebook.models import Tablebook


def casht(request):
    login_id = request.session['logid']

    model_object = Tablebook.objects.filter(user_id=login_id)
    # d = Orderfood.objects.filter(user_id=login_id, orderfoodstatus=0).last()
    grandtotal = Tablebook.objects.filter(user_id=login_id).aggregate(grand=Sum('tablerate'))
    quant = Tablebook.objects.filter(user_id=login_id).aggregate(quan=Count('tableno'))

    1
    # form=forms.payment_forms

    return render(request, "casht/casht.html",
                  {'data': model_object, 'q': quant, 'g': grandtotal})
