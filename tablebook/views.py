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
    model_object1 = Table.objects.filter(id=pk)
    # no = model_object1.seatno
    # rate = model_object1.tablerate
    # grandtotal = viewbranch.objects.filter(user_id=login_id).aggregate(grand=Sum('tablerate'))
    if request.method == 'POST':
        form = forms.tablebook_forms(request.POST, request.FILES)
        if form.is_valid():
            bookObj = form.cleaned_data
            bookingdate = bookObj['bookingdate']
            bookingtime = bookObj['bookingtime']
            bookingrate = bookObj['bookingrate']
            bookingstatus = bookObj['bookingstatus']
            branch_id = request.session['branch_id']
            # bookingdate=request.session['bookingdate']
            # request.session['table_id'] = pk
            # model_object4 = Branchmanager.objects.get(table_id=pk)

            a = Tablebook(bookingdate=bookingdate, bookingtime=bookingtime, bookingrate=bookingrate,
                          bookingstatus=bookingstatus, branch_id=branch_id, table_id=pk,
                          user_id=login_id)
            a.save()
            # messages.info(request,'Table booked successfully!')

            return redirect('booknow:booknow_forms')
    else:
        form = forms.tablebook_forms

    return render(request, "booktable/Booktable.html", {'form': form, 'data': model_object1, 'data1': model_object})
