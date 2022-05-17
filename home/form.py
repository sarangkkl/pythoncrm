from django import forms

from .models import Followup
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField

class Follow_up_form(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","cols":"10"}))
    class Meta:
        model = Followup
        fields = '__all__'

