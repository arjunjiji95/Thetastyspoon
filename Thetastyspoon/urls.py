"""Thetastyspoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib import admin
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import path, include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('front.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^complaint/', include('complaint.urls')),
    url(r'^orderfood/', include('orderfood.urls')),
    url(r'^manager/', include('managerlogin.urls')),
    url(r'^agency/', include('agency.urls')),
    url(r'^table/', include('tabledetails.urls')),
    url(r'^employee/', include('employee.urls')),
    #url(r'^viewfeedback/', include('feedback.urls')),
    url(r'^adminlogin/', include('adminlogin.urls')),
    url(r'^managerreg/', include('branchmanager.urls')),
    url(r'^purchase/', include('purchasehead.urls')),
    url(r'^purchasedetails/', include('purchasedetails.urls')),
    url(r'^viewfeedback/', include('viewfeedback.urls')),
    url(r'^viewcomplaint/', include('viewcomplaint.urls')),
    url(r'^menu/', include('menu.urls')),
    url(r'^foodtype/', include('foodtype.urls')),
    url(r'^branch/', include('branch.urls')),
    url(r'^viewbranch/', include('viewbranch.urls')),
    url(r'^booknow/', include('booknow.urls')),
    url(r'^tablebook/', include('tablebook.urls')),
    url(r'^viewfood/', include('food.urls')),
    url(r'^vegetarian/', include('vegetarian.urls')),
    url(r'^address/', include('address.urls')),
    url(r'^nonveg/', include('nonveg.urls')),
    url(r'^snacks/', include('snacks.urls')),
    url(r'^drinks/', include('drinks.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^dailyreport/', include('dailyreport.urls')),
    url(r'^viewreport/', include('viewreport.urls')),
    url(r'^viewfoodbook/', include('viewfoodbook.urls')),
    url(r'^viewtablebook/', include('viewtablebook.urls')),
    url(r'^card/', include('card.urls')),
    url(r'^net/', include('net.urls')),
    url(r'^cash/', include('cash.urls')),
    url(r'^adbranch/', include('adbranch.urls')),
    url(r'^adfeed/', include('adfeed.urls')),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^repbranch/', include('repbranch.urls')),
    url(r'^carttable/', include('carttable.urls')),
    url(r'^dreport/', include('dreport.urls')),
    url(r'^cashon/', include('cashon.urls')),
    url(r'^pay/', include('pay.urls')),
    url(r'^nett/', include('nett.urls')),
    url(r'^creditt/', include('creditt.urls')),
    url(r'^casht/', include('casht.urls')),
    url(r'^cashtab/', include('cashtab.urls')),








]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()