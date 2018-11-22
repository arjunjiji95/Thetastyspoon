from django.db import connection
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Tablebook
from tabledetails.models import Table
from branchmanager.models import Branchmanager
from django.contrib import messages



def tablebook(request, pk):
    login_id = request.session['logid']
    model_object = Tablebook.objects.filter(user_id=login_id)
    model_object3 = Table.objects.filter(id=pk)
    model_object1 = Table.objects.get(id=pk)
    table = model_object1.tableno
    no = model_object1.seatno
    rate = model_object1.tablerate

    # grandtotal = viewbranch.objects.filter(user_id=login_id).aggregate(grand=Sum('tablerate'))
    if request.method == 'POST':
        form = forms.tablebook_forms(request.POST, request.FILES)
        if form.is_valid():
            bookObj = form.cleaned_data
            bookingdate = bookObj['bookingdate']
            bookingtime = bookObj['bookingtime']
            # bookingrate = bookObj['bookingrate']
            # bookingstatus = bookObj['bookingstatus']
            branch_id = request.session['branch_id']
            # bookingdate=request.session['bookingdate']
            # request.session['table_id'] = pk
            # model_object4 = Branchmanager.objects.get(table_id=pk)

            a = Tablebook(bookingdate=bookingdate, bookingtime=bookingtime, tablerate=rate, tableno=table, seatno=no, branch_id=branch_id,
                          table_id=pk,
                          user_id=login_id)
            a.save()

            cursor1 = connection.cursor()
            cursor1.execute("update tabledetails_table set tablestatus='Booked' where id='%s'" % (pk,))

            return redirect('booknow:booknow_forms')
            messages.info(request, 'Table added to cart!')
    else:
        form = forms.tablebook_forms

    return render(request, "booktable/Booktable.html", {'form': form, 'data': model_object3, 'data1': model_object})



