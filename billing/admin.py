from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(Services)
admin.site.register(Service_list)
