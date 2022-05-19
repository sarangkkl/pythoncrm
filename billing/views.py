from billing.form import Billing_Edit_Form
from billing.models import Customer
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
from .models import Bill,Customer,Services
from .form import Billing_Edit_Form

# Create your views here.

def add_customer_page(request):
    return render(request,'billing/add_customer.html')

def customer_service(request,id):
    cust = Customer.objects.get(id=id)
    service = Services.objects.filter(belongs_to=cust)
    context = {"cust":cust,"service":service}
    return render(request,"billing/custumer_service.html",context)

def create_customer_handle(request):
    if request.method == "POST":
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        email_1 = request.POST.get('email_1')
        email_2 = request.POST.get('email_2')
        number = request.POST.get('number')
        period = request.POST.get('period')
        f_date = request.POST.get('date')
        f_month = request.POST.get('month')
        f_year = request.POST.get('year')
        recuring_time = request.POST.get('recuring_time')
        pin_code = request.POST.get('pin_code')
        amount = request.POST.get('amount')
        r_amount = request.POST.get('recuring_amount')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        documents = request.FILES.get('documents')
        x = Customer.objects.create(name = name,company_name = company_name,email_1 = email_1,email_2 = email_2,mobile_no = number,period = period,recuring_time = recuring_time,pin_code = pin_code,total_amount = amount,recuring_amount = r_amount,state = state,city = city,address_1 = address,documents=documents,next_payment_date= f_date,next_payment_month=f_month,next_payment_year = f_year)
        x.save()
        return HttpResponse("The customer have been succesfully created")

    else:
        return HttpResponse("Baby only post method is allowed")

# def refresh_dashboard(request):
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()

#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     file =FileResponse(buffer, as_attachment=True, filename='hello.pdf')
#     # print(f"the total customers are {all_customer}")
#     return redirect("/")

def refresh_dashboard(request):
    date = datetime.datetime.now().strftime ("%Y%m%d")
    # date = "20211205"
    print("The today date is",date)
    # m = datetime.date.today()
    # print(f"the date is {m}")
    customer = Customer.objects.filter(staus = "active")
    for i in customer:
        # print(f"the next time testing will be {int(i.next_payment_month)+1}")
        # print(i.eligible)
        cust_pay_date = f"{i.next_payment_year}{i.next_payment_month}{i.next_payment_date}"
        # print(f"the next payment date is  {cust_pay_date} and current date is {date}")
        
        if cust_pay_date <= date:
            x = Bill.objects.create(name = i.name,status ="unpaid",price = i.recuring_amount,generate_date = datetime.date.today())
            x.save()
            obj = i
            if(i.recuring_time == 1):
                if(i.next_payment_month != 12):
                    obj.next_payment_month = str(int(obj.next_payment_month)+1) 
                else:
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 1
            elif(i.recuring_time == 3):
                if(i.recuring_time+int(i.next_payment_month) <=12):
                    obj.next_payment_month = str(int(obj.next_payment_month) +3)
                elif(i.recuring_time+int(i.next_payment_month ==13)):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 1
                elif(i.recuring_time+int(i.next_payment_month ==14)):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 2
                elif(i.recuring_time+int(i.next_payment_month ==15)):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 3
            elif(i.recuring_time == 6):
                if((i.recuring_time+int(i.next_payment_month)) <=12):
                    obj.next_payment_month = obj.next_payment_month +6
                elif((i.recuring_time+int(i.next_payment_month)) ==13):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 1
                elif((i.recuring_time+int(i.next_payment_month)) ==14):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 2
                elif((i.recuring_time+int(i.next_payment_month)) ==15):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 3
                elif((i.recuring_time+int(i.next_payment_month)) ==16):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 4
                elif((i.recuring_time+int(i.next_payment_month)) ==17):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 5
                elif((i.recuring_time+int(i.next_payment_month)) ==18):
                    obj.next_payment_year = obj.next_payment_year +1
                    obj.next_payment_month = 6
            elif(i.recuring_time == 12):
                obj.next_payment_year = obj.next_payment_year+1

            if(obj.next_payment_month ==1):
                obj.next_payment_month = "01"
            elif(obj.next_payment_month ==2):
                obj.next_payment_month = "02"
            elif(obj.next_payment_month ==3):
                obj.next_payment_month = "03"
            elif(obj.next_payment_month ==4):
                obj.next_payment_month = "04"
            elif(obj.next_payment_month ==5):
                obj.next_payment_month = "05"
            elif(obj.next_payment_month ==6):
                obj.next_payment_month = "06"
            elif(obj.next_payment_month ==7):
                obj.next_payment_month = "07"
            elif(obj.next_payment_month ==8):
                obj.next_payment_month = "08"
            elif(obj.next_payment_month ==9):
                obj.next_payment_month = "09"
            # elif(i.recuring_time+int(i.next_payment_month) <=12):

            # obj.next_payment.strftime("%Y%(m+1)%d")
            # obj.eligible = False
            obj.save()
            # print(f"the date is {date} and the obtain from the customer is {period}")
            # print(f"this customer  {i.name} bill need to be generated")
    # print(f"the date is {datetime.datetime.now()}")
    return redirect('/')
    # template_path = 'billing/bill_pdf.html'
    # context = {'myvar': 'this is your template context'}
    # # Create a Django response object, and specify content_type as pdf
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # # find the template and render it.
    # template = get_template(template_path)
    # html = template.render(context)

    # # create a pdf
    # pisa_status = pisa.CreatePDF(
    #    html, dest=response)
    # # return render(request,'billing/bill_pdf.html')
    # # if error then show some funy view
    # if pisa_status.err:
    #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response

def customer_list(request):
    customer = Customer.objects.filter(staus ="active")
    context = {"customer":customer}
    return render(request,'billing/customer_list.html',context)

def edit_customer(request,id):
    cust = Customer.objects.get(id = id)
    context = {"customer":cust}
    return render(request,"billing/edit_customer.html",context)

def bill_list(request):
    bill = Bill.objects.filter(status = "unpaid")
    context = {"bill":bill}
    return render(request,"billing/bill_list.html",context)


def bill_edit(request,id):
    bill_obj = Bill.objects.get(id = id)
    cust = bill_obj.belongs_to
    # cust = Customer.objects.get(id=id)
    # bill = Bill.objects.filter(belongs_to = cust)
    bill_form = Billing_Edit_Form
    context = {"bill":bill_obj,"bill_form":bill_form}
    return render(request,"billing/bill_edit.html",context)

def save_bill_edit(request):
    if request.method == "POST":
        id = request.POST.get("_id")
        status = request.POST.get("status")
        bill_obj = Bill.objects.get(id = id)
        bill_obj.status = status
        bill_obj.save()
        return redirect('/')
    else:
        return HttpResponse("Babe dont play with me")
        