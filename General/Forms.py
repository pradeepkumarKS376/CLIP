from django import forms
from General.models import General_Models

Status_CHOICES = (
    ('InProgress','InProgress'),
    ('Over Due', 'Over Due'),
    ('Success','Success'),
)

class General_Form(forms.ModelForm):
    Status = forms.CharField(max_length=500, widget=forms.Select(choices=Status_CHOICES),required = False)
    Audit_Requests = forms.CharField(max_length=500, widget=forms.TextInput(),required = True)
    Date_Requested = forms.DateField(widget=forms.SelectDateWidget(),required = False)
    Due_date = forms.DateField(widget=forms.SelectDateWidget(),required = False)
    Client_contact = forms.EmailField(max_length=254, widget=forms.EmailInput(),required = False)
    Date_Received = forms.DateField(widget=forms.SelectDateWidget(),required = False)
    Other_Comments = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),required = False)
    WT_Comment = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),required = False)
    Select = forms.BooleanField(widget=forms.CheckboxInput(), required=False )
    class Meta:
        model = General_Models
        read_only_fields = 'id'
        fields = '__all__'