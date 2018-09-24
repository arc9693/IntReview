from django import forms
from .models import InterviewResponse

class ResponseForm(forms.ModelForm):
    class Meta:
        model = InterviewResponse
        fields = ('company', 'job_profile','name','rounds','questions','compensation','rating')
