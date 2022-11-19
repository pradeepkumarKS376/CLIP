import datetime
from django.shortcuts import render,redirect
from General.models import General_Models
from General.Forms import General_Form
import win32com.client
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

Success_count = General_Models.objects.filter(Select = True).count()
overdue_count = General_Models.objects.filter(Due_date__lt=datetime.datetime.today()).count()
Inprogress_count = General_Models.objects.filter(Select= False).count()
Inprogress_count = Inprogress_count - overdue_count
Select_data_Request = General_Models.objects.filter(Select = False)
General_Header = General_Models._meta.get_fields()
data = General_Models.objects.all()
Header = General_Models._meta.get_fields()

def GeneralView(request):
    data = General_Models.objects.all()
    Data_Dig = {'GeneralView': data, 'GeneralHeader': Header, 'Success_count': Success_count,
                'Inprogress_count': Inprogress_count, 'overdue_count': overdue_count}
    return render(request,"General\View.html" , context=Data_Dig)

def GeneralCreate(request):
    data_Form = General_Form()
    if request.method == 'POST':
        Form = General_Form(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect("../View")
    Data_Dig = {'GeneralView': data,'GeneralCreate': data_Form, 'Success_count': Success_count,
                'Inprogress_count': Inprogress_count, 'overdue_count': overdue_count}
    return render(request, "General\Create.html", context=Data_Dig)

def Email(request):
    Select_data = General_Models.objects.filter(Select=False)
    a = "<html><head> </head><body><table border=1 class=table table-striped table-hover>"
    c = "</table></body></html>"
    b = ""
    for Select_datas in Select_data:
        Temp = "<tr><td>"+ Select_datas.Audit_Requests
        b =  b + Temp + "</td></tr>"
    d = a+b+c
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'pradeepkumar.ks@bahwancybertek.com'
    mail.Subject = 'Sample Email'
    mail.HTMLBody = d
    mail.Attachments.Add("C:/Users/Pradeep/Downloads/Client Portal development/Year end PBC list.xlsx")
    #mail.CC = 'pradeepkumar.ks@bahwancybertek.com'
    mail.Send()
    data_dict = {'GeneralView': data}
    return render(request, "General\View.html", context=data_dict)

def Homepage(request):
    piechart(request)
    Data_Dig = {'GeneralView': data,'Success_count': Success_count, 'Inprogress_count': Inprogress_count,'overdue_count':overdue_count}
    return render(request,"Home.html" , context=Data_Dig)

def piechart(request):
    sizes = [Inprogress_count, Success_count, overdue_count]
    # mylabels = ["InProgress", "Success", "Over Due"] , labels=mylabels
    myexplode = [0, 0, 0]
    mycolors = ["#33b5e5", "green", "red"]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=myexplode, colors=mycolors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig('media/sale_purchase_peichart.png', dpi=100)
    plt.show()
    Data_Dig = {'Success_count': Success_count,'Inprogress_count': Inprogress_count, 'overdue_count': overdue_count}
    return render(request, "Home.html", context=Data_Dig)

def GeneralUpdate(request,id):
    data1 = General_Models.objects.get(id=id)
    if request.method == 'POST':
        Forms = General_Form(request.POST, instance=data1)
        print(Forms)
        if Forms.is_valid():
            Forms.save()
            return redirect("../View/")
        #else:
            #return redirect("../Create/")
    Data_Dig = {'GeneralView': data, 'GeneralHeader': Header, 'Success_count': Success_count,
                'Inprogress_count': Inprogress_count, 'overdue_count': overdue_count,'GeneralUpdate':data1}
    return render(request, 'General/Update.html', context=Data_Dig)

def GeneralDelete(request,id):
    data = General_Models.objects.get(id=id)
    data.delete()
    return redirect("../View/")
