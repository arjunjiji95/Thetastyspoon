from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Employee


def emp(request):
    login_id = request.session['logid']
    model_object = Employee.objects.filter(branchmanager_id=login_id)
    if request.method == 'POST':
        form = forms.employee_forms(request.POST, request.FILES)
        if form.is_valid():
            empObj = form.cleaned_data
            name = empObj['employeename']
            house = empObj['employeehouse']
            place = empObj['employeeplace']
            city = empObj['employeecity']
            district = empObj['employeedistrict']
            state = empObj['employeestate']
            pin = empObj['employeepin']
            dob = empObj['employeedob']
            age = empObj['employeeage']
            doj = empObj['employeedoj']
            contact = empObj['employeecontact']
            email = empObj['employeeemail']
            username = empObj['employeeusername']
            pwd = empObj['employeepassword']
            stafftype_id = empObj['stafftype_id']

            a = Employee(employeename=name, employeehouse=house, employeeplace=place, employeecity=city,
                         employeedistrict=district,
                         employeestate=state, employeepin=pin, employeedob=dob, employeeage=age, employeedoj=doj,
                         employeecontact=contact, employeeemail=email, employeeusername=username, employeepassword=pwd,
                         stafftype_id=stafftype_id, branchmanager_id=login_id)
            a.save()

            return redirect('employee:employee_forms')
    else:
        form = forms.employee_forms

    return render(request, "employeeregistration/Employeeregistration.html", {'form': form, 'data': model_object})


def edit_emp(request, pk):
    login_id = request.session['logid']
    model_objects = Employee.objects.filter(branchmanager_id=login_id)
    template = 'employeeregistration/Employeeregistration.html'
    post = get_object_or_404(Employee, pk=pk)
    # model_objects = Feedback.objects.all()
    if request.method == 'POST':
        form = forms.employee_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('employee:employee_forms')
    else:
        form = forms.employee_forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_objects,
        }
    return render(request, template, context)


def delete_emp(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    post.delete()
    return redirect('employee:employee_forms')
