from .models import HILs
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms


class HILsModalForm(BSModalModelForm):
    class Meta:
        model = HILs
        fields = ['name', 'station', 'responsible']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "station": forms.TextInput(attrs={"class": "form-control"}),
            "responsible": forms.Textarea(attrs={"class": "form-control"})
        }

