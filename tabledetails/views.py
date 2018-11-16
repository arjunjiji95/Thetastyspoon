from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Table


def tabledetails(request):
    login_id = request.session['logid']
    model_object = Table.objects.filter(branchmanager_id=login_id)
    if request.method == 'POST':
        form = forms.table_forms(request.POST, request.FILES)
        if form.is_valid():
            tableObj = form.cleaned_data
            no = tableObj['tableno']
            seat = tableObj['seatno']
            rate = tableObj['tablerate']
            status = tableObj['tablestatus']

            a = Table(tableno=no, seatno=seat, tablerate=rate, tablestatus=status,
                      branchmanager_id=login_id)
            a.save()

            return redirect('tabledetails:table_forms')
    else:
        form = forms.table_forms

    return render(request, "table/Table.html", {'form': form, 'data': model_object})


def edit_tabledetails(request, pk):
    login_id = request.session['logid']
    model_objects = Table.objects.filter(branchmanager_id=login_id)
    template = 'table/Table.html'
    post = get_object_or_404(Table, pk=pk)
    if request.method == 'POST':
        form = forms.table_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('tabledetails:table_forms')
    else:
        form = forms.table_forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_objects,
        }
    return render(request, template, context)


def delete_tabledetails(request, pk):
    post = get_object_or_404(Table, pk=pk)
    post.delete()
    return redirect('tabledetails:table_forms')
