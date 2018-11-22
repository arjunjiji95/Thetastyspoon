#from django.db.models import Count
from django.shortcuts import render, redirect
from feedback.models import Feedback
from branchmanager.models import Branchmanager
#import matplotlib.pyplot as plt
#from .fusioncharts import FusionCharts

def fedd(request):
    login_id = request.session['logid']

    model_object = Branchmanager.objects.get(id=login_id)
    model_object1=Feedback.objects.filter(branch_id=model_object.branch_id)
    #quant = Feedback.objects.filter(user_id=login_id).aggregate(quan=Count(feedbackcontent="Good"))
    #plt.plot(quant)


    return render(request, "viewfeedback/Viewfeedback.html", {'data': model_object1})
