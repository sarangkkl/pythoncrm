
from django.urls import path
from home import views,agent_view

urlpatterns = [
    path('',views.index,name="index"),

    # create agent
    path('create_agent_page',views.create_agent_page,name="create_agent_page"),
    path('create_agent',views.create_agent,name="create_agent"),


    path('signup_page',views.signup_page,name="signup_page"),
    path('login_page',views.login_page,name="login_page"),
    path('signup_handle',views.signup_handle,name="signup_handle"),
    path('login_handle',views.login_handle,name="login_handle"),
    path('logout_handle',views.logout_handle,name="logout_handle"),

    #Lead handleing  

    path('create_lead',views.create_lead_page,name="create_lead"),
    path('follow_up/<int:id>',views.follow_up,name="follow_up"),
    path('update_lead/<int:id>',views.update_lead,name="update_lead"),
    path('update_lead_handle/<int:id>',views.update_lead_handle,name="update_lead_handle"),
    # path('update_lead',views.update_lead,name="update_lead"),
    path('creat_handle_lead',views.creat_handle_lead,name="creat_handle_lead"),
    path('lead_list',views.lead_list,name="lead_list"),


    # follow up handleing
    path('add_follow_up/<int:id>',views.add_follow_up,name="add_follow_up"),

    # agent handleing
    path('agent_login_page',views.agent_login_page,name="agent_login_page"),
    path('agent_list',views.agent_list,name="agent_list"),
    path('agent_login_handle',views.agent_login_handle,name="agent_login_handle"),
    path('agent_home',views.agent_home,name="agent_home"),

    

]