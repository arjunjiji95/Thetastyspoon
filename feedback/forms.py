from django import forms
from . import models


class feedback_forms(forms.ModelForm):

    class Meta:
        model = models.Feedback
        fields = ['feedbackcontent', 'feedbackdate', 'branch_id']