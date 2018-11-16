from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Menu


def menu(request):
    model_object = Menu.objects.all()

    if request.method == 'POST':
        form = forms.menu_forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('menu:menu_forms')
    else:
        form = forms.menu_forms

    return render(request, "menu/Menu.html", {'form': form, 'data': model_object})

def edit_menu(request, pk):
    model_object = Menu.objects.all()

    template = 'menu/Menu.html'
    post = get_object_or_404(Menu, pk=pk)
   # model_objects = Feedback.objects.all()
    if request.method == 'POST':
        form = forms.menu_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('menu:menu_forms')
    else:
            form = forms.menu_forms(instance=post)
            context = {
                'form': form,
                'post': post,
                'data': model_object,

            }
    return render(request, template, context)


def delete_menu(request, pk):
    post = get_object_or_404(Menu, pk=pk)
    post.delete()
    return redirect('menu:menu_forms')

