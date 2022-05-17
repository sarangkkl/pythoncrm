from django.contrib.auth.decorators import login_required
from .models import Customer,Service_list,Services
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect




def add_service(request,id):
    if request.method =="POST":
        price = request.POST.get('price')
        name = request.POST.get('name')
        cust = Customer.objects.get(id=id)
        try:
            y = Service_list.objects.get(belongs_to=cust)
        except:
            y = Service_list.objects.create(belongs_to = cust)
            y.save()
        z = Services.objects.create(belongs_to=cust,service = y,name=name,price=price)
        z.save()
        messages.info(request,"The Service is added successfully")
        return redirect(f'/billings/customer_service/{id}')

def delete_service(request,id):
    service = Services.objects.get(id=id)
    service.delete()
    messages.info(request,"The Service Has been deleted successfully")
    previous_url = request.META.get('HTTP_REFERER', '/billings/customer_list')
    return HttpResponseRedirect(previous_url)
