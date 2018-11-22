from django.shortcuts import render, redirect
from . import forms
from menu.models import Menu
from user.models import User
from orderfood.models import Orderfood
from random import randint, random


def order(request, pk):
    login_id = request.session['logid']
    model_object = Orderfood.objects.filter(user_id=login_id)
    #for _ in range(10):
        #billno = randint(0, 10)



    # model_object = User.objects.get(id=login_id)

    model_object2 = Menu.objects.filter(id=pk)
    model_object1 = Menu.objects.get(id=pk)
    price = model_object1.menuprice
    name = model_object1.menuname

    if request.method == 'POST':

        form = forms.orderfood_forms(request.POST, request.FILES)
        if form.is_valid():
            orderObj = form.cleaned_data
            date = orderObj['orderfooddate']
            quantity = orderObj['orderfoodquantity']
            orderfoodbillno = orderObj['orderfoodbillno']
            total = int(price) * int(quantity)
            request.session['orderfoodbillno'] = orderfoodbillno
            #request.session['orderfooddate'] = orderfooddate
            #orderfooddate=request.session['orderfooddate']




            a = Orderfood(orderfooddate=date, orderfoodquantity=quantity, orderitemname=name,
                          orderfoodtotalamount=total, orderfoodbillno=orderfoodbillno, menu_id=pk,
                          user_id=login_id)
            a.save()

            return redirect('food:food_forms')
    else:
        form = forms.orderfood_forms

    return render(request, "orderfood/Orderfood.html", {'form': form, 'data1': model_object, 'data': model_object2})

    # return render(request, "orderfood/Orderfood.html", {'data': model_object1})
