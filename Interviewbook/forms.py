from django.forms import ModelForm, Textarea
from .models import *

class ResponseForm(ModelForm):
    class Meta:
        model = InterviewResponse
        fields = ('name','company','job_profile','rounds','questions','compensation','rating')
        widgets = {
            'questions': Textarea(attrs={'cols': 115, 'rows': 5}),
        }

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude =()
