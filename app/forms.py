from django import forms
from app.models import LogTable
class CalForm(forms.ModelForm):
    class Meta:
        model=LogTable
        fields=['operand1','operator','operand2']