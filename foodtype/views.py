from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Foodtype


def foodtype(request):
    model_object = Foodtype.objects.all()

    if request.method == 'POST':

        form = forms.foodtype_forms(request.POST, request.FILES)
        if form.is_valid():
            foodObj = form.cleaned_data
            foodname = foodObj['foodname']


            a = Foodtype(foodname=foodname)
            a.save()

            return redirect('foodtype:foodtype_forms')
    else:
        form = forms.foodtype_forms

    return render(request, "foodtype/foodtype.html", {'form': form, 'data': model_object})

def edit_foodtype(request, pk):
    model_object = Foodtype.objects.all()

    template = 'foodtype/foodtype.html'
    post = get_object_or_404(Foodtype, pk=pk)
   # model_objects = Feedback.objects.all()
    if request.method == 'POST':
        form = forms.foodtype_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('foodtype:foodtype_forms')
    else:
            form = forms.foodtype_forms(instance=post)
            context = {
                'form': form,
                'post': post,
                'data': model_object,

            }
    return render(request, template, context)


def delete_foodtype(request, pk):
    post = get_object_or_404(Foodtype, pk=pk)
    post.delete()
    return redirect('foodtype:foodtype_forms')

