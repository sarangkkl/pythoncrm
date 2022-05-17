from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Agent,Lead,Organization,Source,Followup

# Register your models here.
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(Organization)
admin.site.register(Source)
admin.site.register(Followup)

