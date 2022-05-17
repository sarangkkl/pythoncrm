from django import forms

from .models import Bill
from django.forms import ModelForm
# from ckeditor_uploader.fields import RichTextUploadingField

class Billing_Edit_Form(ModelForm):
    # body = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","cols":"10"}))
    class Meta:
        model = Bill
        fields = '__all__'
