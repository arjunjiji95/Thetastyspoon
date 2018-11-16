from django.shortcuts import render, redirect
from dailyreport.models import Dailyreport
from orderfood.models import Orderfood



def viewreport(request, pk):
    #login_id = request.session['logid']
    reportdate = request.session['reportdate']
    #model_object = Viewreport.objects.filter(id=pk)
    model_object = Dailyreport.objects.filter(id=pk)
    model_object1 = Orderfood.objects.filter(orderfooddate=reportdate)
    #model_object1 = Menu.objects.filter(menu_id=pk)


    return render(request, "viewreport/viewreport.html", {'data': model_object, 'data1':model_object1})