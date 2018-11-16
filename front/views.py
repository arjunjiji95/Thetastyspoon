from django.shortcuts import render, redirect



def front(request):

    return render(request, "front/front.html")