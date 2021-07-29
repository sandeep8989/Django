from django import forms
from .models import show


class Fun(forms.ModelForm):
    class Meta:
        model = show
        fields = "__all__"
