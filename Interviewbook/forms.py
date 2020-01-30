from django import forms
from django.forms import ModelForm, Textarea
from .models import *
from django.contrib.auth.models import User

class ResponseForm(ModelForm):
    class Meta:
        model = InterviewResponse
        fields = ('company','job_profile','rounds','questions','compensation','rating')
        widgets = {
            'questions': Textarea(attrs={'rows': 5}),
        }

    def save(self, user_id ,commit=True,):
        form = super(ResponseForm, self).save(commit=False)
        form.name = User.objects.get(pk=user_id)
        if commit:
            form.save()
            return form

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude =()

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body', )