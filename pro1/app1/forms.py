from django import forms
from .models import Person,Customer

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields='__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        Model=Customer
        fields='__all__'

        