from django.urls import path
from billing import views
from . import service

urlpatterns = [
    path('add_customer_page',views.add_customer_page,name="add_customer_page"),
    path('create_customer_handle',views.create_customer_handle,name="create_customer_handle"),
    path('refresh_dashboard',views.refresh_dashboard,name="refresh_dashboard"),
    path('customer_list',views.customer_list,name="customer_list"),



    # customer services
    path('customer_service/<int:id>',views.customer_service,name="customer_service"),
    path('add_service/<int:id>',service.add_service,name="add_service"),
    path('delete_service/<int:id>',service.delete_service,name="delete_service"),
    path('edit_customer/<int:id>',views.edit_customer,name="edit_customer"),




    # bill list handleing
    path('bill_list',views.bill_list,name="bill_list"),
    path('bill_edit/<int:id>',views.bill_edit,name="bill_edit"),
    path('savebill_edit',views.save_bill_edit,name="save_bill_edit"),


]