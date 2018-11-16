from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Complaint


def comp(request):
    login_id = request.session['logid']
    model_object = Complaint.objects.filter(user_id=login_id)
    if request.method == 'POST':

        form = forms.complaint_forms(request.POST, request.FILES)
        if form.is_valid():
            compObj = form.cleaned_data
            content = compObj['complaintcontent']
            complaintdate = compObj['complaintdate']
            branch_id = compObj['branch_id']
            a = Complaint(complaintcontent=content, complaintdate=complaintdate, branch_id=branch_id, user_id=login_id)
            a.save()

            return redirect('complaint:complaint_forms')
    else:
        form = forms.complaint_forms

    return render(request, "complaint/Complaint.html", {'form': form, 'data': model_object})


def edit_complaint(request, pk):
    login_id = request.session['logid']
    model_objects = Complaint.objects.filter(user_id=login_id)
    template = 'complaint/Complaint.html'
    post = get_object_or_404(Complaint, pk=pk)
   # model_objects = Feedback.objects.all()
    if request.method == 'POST':
        form = forms.complaint_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('complaint:complaint_forms')
    else:
            form = forms.complaint_forms(instance=post)
            context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_complaint(request, pk):
    post = get_object_or_404(Complaint, pk=pk)
    post.delete()
    return redirect('complaint:complaint_forms')
