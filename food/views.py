from django.shortcuts import render, redirect
from foodtype.models import Foodtype
from menu.models import Menu


def viewfood(request):
    #login_id = request.session['logid']
    model_object = Foodtype.objects.all()
    #model_object1 = Menu.objects.filter(menu_id=pk)


    return render(request, "viewfood/Viewfood.html")