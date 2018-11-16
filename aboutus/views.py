from django.shortcuts import render


def aboutus(request):
    return render(request, "aboutus/about.html" )
