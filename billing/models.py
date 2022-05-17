from django.db import models
from django.db.models.fields import DateField


# Create your models here.




class Customer(models.Model):
    states_of_customer = (
        ('active','Active'),
        ('disable','Disable'),
    )
    name = models.CharField(max_length=50,blank=True,null=True)
    company_name = models.CharField(max_length=50,blank=True,null=True)
    address_1 = models.CharField(max_length=500,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    email_1 = models.EmailField(blank=True,null=True)
    email_2 = models.EmailField(blank=True,null=True)
    mobile_no = models.CharField(max_length=14,blank=True,null=True)
    recuring_time = models.IntegerField()
    recuring_amount = models.IntegerField(blank=True,null=True)
    period = models.IntegerField()
    joining_date = models.DateField(auto_now_add=True,blank=True,null=True)
    total_amount = models.IntegerField(blank=True,null=True)
    next_payment_date = models.CharField(blank=True,null=True,max_length=3)
    next_payment_month = models.CharField(blank=True,null=True,max_length=3)
    next_payment_year = models.IntegerField(blank=True,null=True)
    eligible = models.BooleanField(blank= True,null=True)
    pin_code = models.CharField(max_length=14,blank=True,null=True)
    documents = models.FileField(upload_to="customer/documnets")
    staus = models.CharField(max_length=10,choices=states_of_customer,blank=True,null=True,default="active")
    def __str__(self):
        return self.name

class Bill(models.Model):
    option = (
        ('unpaid','Unpaid'),
        ('paid','Paid'),
    )
    belongs_to = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    generate_date = models.DateField(auto_now=True,editable=True,blank=True,null=True)
    due_date = models.DateField(blank=True,null=True)
    status = models.CharField(choices=option,max_length=10,blank=True,null=True)
    name = models.CharField(blank=True,null=True,max_length=20)
    pdf_file = models.FileField(upload_to = "bills/{name}",blank=True,null=True)

    # def __str__(self):
    #     return f"{self.name}-{self.generate_date}-{self.pk}"

class Service_list(models.Model):
    belongs_to = models.ForeignKey(Customer,blank=True,null=True,on_delete=models.CASCADE)
    uniqie_id = models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.belongs_to.name

class Services(models.Model):
    belongs_to = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    service = models.ForeignKey(Service_list,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name


class Documents(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
    name = models.CharField(max_length=50,blank=True,null=True)
    image = models.ImageField(upload_to='documents/{name}')
