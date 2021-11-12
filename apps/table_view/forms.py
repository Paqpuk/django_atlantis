from .models import HILs
from bootstrap_modal_forms.forms import BSModalModelForm
from scripts.forms.form_factories import *
from django import forms


HILsModalForm = model_form_creator(model_=HILs, theme='atlantis_modal')
HILsForm = model_form_creator(model_=HILs, theme='atlantis')


# class HILsModalForm(BSModalModelForm):
#     class Meta:
#         model = HILs
#         fields = ['name', 'station', 'responsible']
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control"}),
#             "station": forms.TextInput(attrs={"class": "form-control"}),
#             "responsible": forms.Textarea(attrs={"class": "form-control"})
#         }

