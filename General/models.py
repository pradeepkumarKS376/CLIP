from django.db import models

# Create your models here.
class General_Models(models.Model):
    Status = models.CharField(max_length=500, null=True)
    Audit_Requests = models.CharField(max_length=500, null=False)
    Date_Requested = models.DateField(null=True)
    Due_date =models.DateField(null=True)
    Client_contact = models.EmailField(max_length=254,null=True)
    Date_Received =models.DateField(null=True)
    Other_Comments = models.CharField(max_length=500, null=True)
    WT_Comment = models.CharField(max_length=500, null=True)
    Select = models.BooleanField('Select',default=False)

def __str__(self):
    return "General_Models Audit_Requests" + Audit_Requests