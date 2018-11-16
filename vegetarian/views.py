from django.shortcuts import render, redirect
from foodtype.models import Foodtype
from menu.models import Menu

def vegetarian(request):
    #login_id = request.session['logid']

    model_object = Foodtype.objects.get(foodname="Vegetarian")
    idd=model_object.id
    model_object2= Menu.objects.all().filter(foodtype_id=idd)

    return render(request, "vegetarian/Vegetarian.html", {'data': model_object2})