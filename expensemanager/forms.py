from django import forms
from .models import Transaction




class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        widgets = {
            'date': forms.TextInput(attrs={'type':'date'}),
        }
        fields = ['date', 't_type', 'category', 'amount']


