from django.shortcuts import render


def card(request):
    return render(request, "python/purchase/CardPayment.html" )
