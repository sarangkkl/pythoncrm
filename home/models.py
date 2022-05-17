# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=50,blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,blank=True)

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=20,blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,blank=True)
    image = models.ImageField(upload_to="Agents/images",blank = True)
    organization = models.ForeignKey(Organization,on_delete=models.PROTECT,blank=True,default="")
    def __str__(self):
        return self.name



class Lead(models.Model):
    status = (
        ("fresh","Fresh"),
        ("open","Open"),
        ("closed","Closed"),
        ("pending","Pending"),
    )
    closed_by = (
        ("low_budget","Low Budget"),
        ("we_cant_do","We Cant Do"),
        ("client","Client Converted"),
    )

    pending_by = ( 
        ("with_customer","With Customer"),
        ("with_process","With Process"),
        ("pending_on_us","Pending On Us"),
    )

    name = models.CharField(max_length=20,blank=True)
    email = models.CharField(max_length=30,default="")
    organ = models.ForeignKey(Organization,on_delete=models.PROTECT,blank=True,null=True)
    assign_to = models.CharField(max_length=30,default="")
    mobile_no = models.IntegerField(blank=True)
    subject = models.CharField(max_length=100,blank=True)
    message = models.TextField(blank=True)
    source = models.CharField(max_length=30,default="")
    # source = models.ForeignKey(Source,blank=True,on_delete=models.PROTECT,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(choices=status,max_length=20,blank=True,default="fresh")
    closed_or_pending = models.CharField(max_length=15,choices=closed_by,blank=True)
    # pending_by = models.CharField(max_length=15,choices=pending_by,blank=True)
    image=models.ImageField(upload_to="lead/images",blank = True)

    def __str__(self):
        return self.email

class Followup(models.Model):
    f_lead = models.ForeignKey(Lead,on_delete=models.CASCADE,blank=True,null=True)
    created_by = models.CharField(max_length=20,blank=True,null=True)
    # follow_file = models.FileField(blank=True,null=True)
    # follow_image = models.ImageField(blank=True,null=True)
    follow_file = models.FileField(upload_to = "followup",blank=True,null=True)
    follow_image = models.ImageField(upload_to = "followup",blank=True,null=True)
    # body = models.TextField(max_length=5000,blank=True,null=True)
    body = RichTextUploadingField(blank= True,null = True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.f_lead