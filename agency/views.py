from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Agency


def agency(request):
    login_id = request.session['logid']
    model_object = Agency.objects.filter(branchmanager_id=login_id)
    if request.method == 'POST':
        form = forms.agency_forms(request.POST, request.FILES)
        if form.is_valid():
            agencyObj = form.cleaned_data
            name = agencyObj['agencyname']
            place = agencyObj['agencyplace']
            city = agencyObj['agencycity']
            district = agencyObj['agencydistrict']
            pin = agencyObj['agencypin']
            contact = agencyObj['agencycontact']
            email = agencyObj['agencyemail']

            a = Agency(agencyname=name, agencyplace=place, agencycity=city, agencydistrict=district, agencypin=pin, agencycontact=contact, agencyemail=email, branchmanager_id=login_id)
            a.save()

            return redirect('agency:agency_forms')
    else:
        form = forms.agency_forms

    return render(request, "Agency/Agency.html", {'form': form, 'data': model_object})


def edit_agency(request, pk):
    login_id = request.session['logid']
    model_objects = Agency.objects.filter(branchmanager_id=login_id)
    template = 'Agency/Agency.html'
    post = get_object_or_404(Agency, pk=pk)
   # model_objects = Feedback.objects.all()
    if request.method == 'POST':
        form = forms.agency_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('agency:agency_forms')
    else:
            form = forms.agency_forms(instance=post)
            context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_agency(request, pk):
    post = get_object_or_404(Agency, pk=pk)
    post.delete()
    return redirect('agency:agency_forms')
