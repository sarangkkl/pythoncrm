from billing.models import Bill
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Agent, Followup, Organization,Source,Lead
from .form import *
from django.contrib.auth import logout,login
from billing.views import Customer
# from somewhere import handle_uploaded_file
# Create your views here.

@login_required(login_url='login_page')
def index(request):
    all_customer = Customer.objects.all()
    bills = Bill.objects.all()
    organization=get_object_or_404(Organization,user=User.objects.get(username=request.user.username))
    month_income = 0
    annual_income = 0
    outstanding_amount = 0
    for m in bills:
        if m.status =="unpaid":
            outstanding_amount = outstanding_amount+m.price

    for i in all_customer:
        annual_income = annual_income +i.total_amount
        if i.recuring_time == 1:
            print(f"the value of recuring amount is {i.recuring_amount} for {i.name}")
            month_income = month_income + i.recuring_amount
        else:
            pass
    context = {"user":organization,"month_income":month_income,"annual_income":annual_income,"outstanding_amount":outstanding_amount}
    return render(request,"home/index.html",context)
    

def create_agent_page(request):
    return render(request,"home/create_agent.html")



def signup_page(request):
    return render(request,"home/signup.html")


def login_page(request):
    return render(request,"home/login.html")


def create_agent(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        agent_img=request.FILES.get('user_img')

        if(pass1 != pass2):
            return HttpResponse("Password does not matches")
        else:
            x = User.objects.create(username = username,first_name = fname,last_name = lname,is_staff = False,email = email)
            x.set_password(pass1)
            x.save()
            y = Agent(user = x,name = fname,organization="adsoptimiser",image = agent_img)
            y.save()
            return HttpResponse(" the user created succesfully and also the agent ccreated succesfully ")
    else:
        return HttpResponse("Error 404")


def create_lead_page(request):
    agent = Agent.objects.all
    source = Source.objects.all
    print(f"the agents are {agent}")
    print(f"the sorce list  are {source}")
    
    context = {"agent":agent,"source":source}
    return render(request,'home/create_lead.html',context)


def signup_handle(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass')
        pass2 = request.POST.get('re_pass')
        pass2 = request.POST.get('re_pass')
        check = request.POST.get('agree-term')

        if(pass1 != pass2):
            return HttpResponse("Babe your passwod does not matches please try again")
        else:
            x = User.objects.create(email = email,username = email,first_name = name,is_staff = False)
            # x = User.objects.create(name,email,pass1)
            x.set_password(pass1)
            x.save()
            y = Organization(user = x,name = name)
            y.save()
        # print(f"lets varify the data name = {name},{check}")
        return HttpResponse("Babe you have succesfully created your account")
    else:
        return HttpResponse("Babe something goes wrong")

def login_handle(request):
    if request.method == "POST":
        username = request.POST.get('your_name')
        password = request.POST.get('your_pass')
        # username = email
        # print(f"{username} and pasword is {password}")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            return HttpResponse("Babe try again you are not authenticated")
    else:
        return HttpResponse("babe only post method applicable")


# logout handle
def logout_handle(request):
    logout(request)
    return HttpResponse("The user have been logged out successfully")




# leads related function

def creat_handle_lead(request):
    if request.method == "POST":
        organization=get_object_or_404(Organization,user=User.objects.get(username=request.user.username))
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        number = request.POST.get('number')
        assign= request.POST.get('assign')
        source_o= request.POST.get('source')
        followup= request.POST.get('followup')

        x = Lead.objects.create(name=name,organ = organization,mobile_no = number,source = source_o,subject = subject,message = followup,email= email,assign_to = assign)
        x.save()
        return HttpResponse("The lead has been created successfully")
    else:
        return HttpResponse("Babe you are going wrong ")


def lead_list(request):
    organization=get_object_or_404(Organization,user=User.objects.get(username=request.user.username))
    lead = Lead.objects.filter(organ = organization)
    fresh_count = 0
    open_count = 0
    pending_count = 0
    for i in lead:
        if i.state == "fresh":
            fresh_count = fresh_count +1
        elif i.state == "open":
            open_count = open_count+1
        elif i.state == "pending":
            pending_count = pending_count +1
        
    # print(f"the total no of fresh status is {fresh_count} and open status is {open_count} and the pending staus is {pending_count}")
    
    context ={'leads':lead,'fresh_count':fresh_count,'open_count':open_count,'pending_count':pending_count}
    return render(request,'home/leads_list.html',context)


def update_lead(request,id):
    leads = Lead.objects.get(id = id)
    followup = Followup.objects.all
    agent = Agent.objects.all
    source = Source.objects.all
    # print(f"the leads are {leads}")
    context = {"lead":leads,"followup":followup,"agent":agent,"source":source,"id":id}
    
    return render(request,"home/update_lead.html",context)

def update_lead_handle(request,id):
    if request.method == "POST":
        organization=get_object_or_404(Organization,user=User.objects.get(username=request.user.username))
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        number = request.POST.get('number')
        assign= request.POST.get('assign')
        source_o= request.POST.get('source')
        # followup= request.POST.get('followup')
        status= request.POST.get('state')
        pending_close= request.POST.get('pending_close')

        x = Lead.objects.get(id = id)
        x.name =  name
        x.subject =  subject
        x.email =  email
        x.number =  number
        x.assign_to =  assign
        x.source =  source_o
        x.number =  number
        x.state = status
        x.closed_or_pending = pending_close
        x.save()
        print(f"the get object is {x}")

        # Lead.objects.get(id = id).update(name=name,organ = organization,mobile_no = number,source = source_o,subject = subject,message = followup,email= email,assign_to = assign,state = status,closed_or_pending = pending_close)
        # x.save()
        return HttpResponse("The lead has been updated successfully")
    else:
        return HttpResponse("Babe you are going wrong ")


@login_required(login_url='login_page')
def follow_up(request,id):
    form = Follow_up_form()
    leads = Lead.objects.get(id=id)
    fleads= leads.followup_set.all()
    print(f"the name of the lead is {fleads}")
    context = {"lead":leads,"followup":fleads,"form":form}
    
    return render(request,'home/followup.html',context)

@login_required(login_url='login_page')
def add_follow_up(request,id):
    if request.method == "POST":
    #     upload_file(request):
    # if request.method == 'POST':
    #     form = Follow_up_form(request.POST, request.FILES)
    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES['file'])
    #         return HttpResponseRedirect('/success/url/')
    # else:
        # form = UploadFileForm()
        body = request.POST.get('body')
        follow_file=request.FILES.get('follow_file')
        follow_image = request.FILES.get('follow_image')
        # body = form.cleaned_data.get('body')
        # follow_file=form.cleaned_data.get('follow_file')
        # follow_image = form.cleaned_data.get('follow_image')
        # print(f"the image is {follow_image} the file is {follow_file} the body is {body}")
        # form = Follow_up_form.(request.POST)
        # if form.is_valid():
            
            # form.save()


        organization=get_object_or_404(Organization,user=User.objects.get(username=request.user.username))
        
        leads = Lead.objects.get(id=id)
        fleads= leads.followup_set.all()
        name = organization.name
        # print(f"the image is {follow_image} the file is {follow_file} the body is {body}")
        x = Followup.objects.create(body = body,follow_file = follow_file,follow_image = follow_image,f_lead = leads,created_by = name)
        # x = Followup.objects.create(body = body,f_lead = leads,created_by = name)
        x.save()
        context = {"lead":leads,"followup":fleads}
        
        # print(f"the main content is \n {main}")
        return redirect(f"/follow_up/{id}",context)
    else:
        return HttpResponse("only post method is allowed")





# agent views start here
def agent_login_page(request):
    return render(request,'home/agent_login.html')

def agent_login_handle(request):
    if request.method == "POST":
        username = request.POST.get('your_name')
        password = request.POST.get('your_pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('agent_home') 
        else:
            return HttpResponse("Babe try again you are not authenticated")
    else:
        return HttpResponse("babe only post method applicable")

def agent_home(request):
    agent=get_object_or_404(Agent,user=User.objects.get(username=request.user.username))
    # agent = request.user
    lead = Lead.objects.filter(assign_to = agent)
    # print(f"the name of the agent is {agent}")
    fresh_count = 0
    open_count = 0
    pending_count = 0
    for i in lead:
        if i.state == "fresh":
            fresh_count = fresh_count +1
        elif i.state == "open":
            open_count = open_count+1
        elif i.state == "pending":
            pending_count = pending_count +1
        
    # print(f"the total no of fresh status is {fresh_count} and open status is {open_count} and the pending staus is {pending_count}")
    
    context ={'leads':lead,'fresh_count':fresh_count,'open_count':open_count,'pending_count':pending_count,'agent':agent}
    return render(request,'home/agent_home.html',context)
    # return render(request,'home/agent_home.html')

def agent_list(request):
    organization=get_object_or_404(Organization,user=User.objects.get(username=request.user.username))
    lead = Lead.objects.filter(organ = organization)
    fresh_count = 0
    open_count = 0
    pending_count = 0
    lead_count = lead.count()
    for i in lead:
        if i.state == "fresh":
            fresh_count = fresh_count +1
        elif i.state == "open":
            open_count = open_count+1
        elif i.state == "pending":
            pending_count = pending_count +1
    
    team=get_object_or_404(Organization,user=User.objects.get(username=request.user.username))
    agents = Agent.objects.filter(organization = team)
    context = {'agent':agents,'fresh_count':fresh_count,'open_count':open_count,'pending_count':pending_count,'lead_count':lead_count}
    return render(request,'home/agent_list.html',context)