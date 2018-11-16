from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Branch


def branch(request):
    model_object = Branch.objects.all()

    if request.method == 'POST':

        form = forms.branch_forms(request.POST, request.FILES)
        if form.is_valid():
            branchObj = form.cleaned_data
            branchname = branchObj['branchname']
            branchplace = branchObj['branchplace']
            branchcity = branchObj['branchcity']
            branchdistrict = branchObj['branchdistrict']
            branchpin = branchObj['branchpin']
            branchcontact = branchObj['branchcontact']
            branchemail = branchObj['branchemail']

            a = Branch(branchname=branchname, branchplace=branchplace, branchcity=branchcity,
                       branchdistrict=branchdistrict, branchpin=branchpin, branchcontact=branchcontact,
                       branchemail=branchemail)
            a.save()

            return redirect('branch:branch_forms')
    else:
        form = forms.branch_forms

    return render(request, "branch/Branch.html", {'form': form, 'data': model_object})


def edit_branch(request, pk):
    model_object = Branch.objects.all()

    template = 'branch/Branch.html'
    post = get_object_or_404(Branch, pk=pk)
    # model_objects = Feedback.objects.all()
    if request.method == 'POST':
        form = forms.branch_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('branch:branch_forms')
    else:
        form = forms.branch_forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,

        }
    return render(request, template, context)


def delete_branch(request, pk):
    post = get_object_or_404(Branch, pk=pk)
    post.delete()
    return redirect('branch:branch_forms')
