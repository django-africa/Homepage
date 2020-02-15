from .models import Contact
from django.forms import ModelForm, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _

class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['submited_date']
        widgets = {
            'first_name': TextInput(attrs={"class" : "text-black"}),
            'last_name': TextInput(attrs={"class" : "text-black"}),
            'email': TextInput(attrs={"class" : "text-black"}),
            'subject': TextInput(attrs={"class" : "text-black"}),
            'message': Textarea(attrs={'cols': 80, 'rows': 10, 'class': "text-black"}),
        }
        error_messages = {
            'email': {
                'invalid': _("Enter a Valid Email Address"),
            },
        }

        form_class = {
            'first_name': 'form-control rounded-0',
            'last_name': 'form-control rounded-0',
            'email': 'form-control rounded-0',
            'subject': 'form-control rounded-0',
            'message': 'form-control rounded-0',
        }
