from django import forms
from .models import *

class ResponseForm(forms.ModelForm):
    class Meta:
        model = InterviewResponse
        fields = ('company', 'job_profile','name','rounds','questions','compensation','rating')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude =()
