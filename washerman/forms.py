from django import forms


CHOICES = (
    ('Drycleaning','Drycleaning'),
    ("Commercial Laundry","Commercial Laundry"),
)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    name.widget.attrs.update({
        'class':'form-control form-control-lg form-control-a',
        'placeholder':'Your Name'
        })
    email = forms.EmailField()
    email.widget.attrs.update({
        'class':'form-control form-control-lg form-control-a',
        'placeholder':'Your Email'
        })
    subject = forms.CharField(max_length=100)
    subject.widget.attrs.update({
        'class':'form-control form-control-lg form-control-a',
        'placeholder':'Subject'
        })
    message = forms.CharField(widget=forms.Textarea)
    message.widget.attrs.update({
        'class':'form-control',
        'cols':'45',
        'rows':'8',
        'placeholder':'Message'
        })

class ScheduleForm(forms.Form):
    name = forms.CharField(max_length=100)
    name.widget.attrs.update({
        'class':'form-control form-control-lg form-control-a',
        'placeholder':'Your Name'
        })
    email = forms.EmailField()
    email.widget.attrs.update({
        'class':'form-control form-control-lg form-control-a',
        'placeholder':'Your Email'
        })
    address = forms.CharField(max_length=100)
    address.widget.attrs.update({
        'class':'form-control form-control-lg form-control-a',
        'placeholder':'Home Address'
        })
    phone =  forms.CharField(max_length=13)
    phone.widget.attrs.update({
        'class':'form-control form-control-lg form-control-a',
        'placeholder':'Phone Number'
        })
    service = forms.ChoiceField(choices=CHOICES)
    service.widget.attrs.update({
        'class':'form-control form-control-lg form-control-a',
        'id':'Type',
        })