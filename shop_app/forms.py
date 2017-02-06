from django import forms

class FileForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='(max. 42 megabytes)',
        
    )
    
class InvoiceItemForm(forms.Form):
    code = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    quantity = forms.IntegerField()

class InvoiceForm(forms.Form):
    id = forms.CharField()
    customer = forms.CharField()
    bici = forms.CharField()
    