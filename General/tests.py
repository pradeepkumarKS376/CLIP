from django.test import TestCase
from models import *

# Create your tests here.

def GeneralUpdateAll(request):
    if request.method == 'POST':
        for key in request.POST.getlist('id'):
            print(key)
            product_update = General_Models.objects.get(id=key)
            form = General_Form(request.POST, instance=product_update)
            print(form)
            if form.is_valid():
                form.save()
    Data_Dig = {'GeneralView': data, 'GeneralHeader': Header, 'Success_count': Success_count,'Inprogress_count': Inprogress_count, 'overdue_count': overdue_count}
    return render(request,"General/UpdateAll.html", context=Data_Dig)
