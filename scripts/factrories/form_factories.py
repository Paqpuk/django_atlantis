from __future__ import annotations
from django import forms
from django.forms import modelform_factory
from bootstrap_modal_forms.forms import BSModalModelForm
from ..themes import themes

class AtlantisModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AtlantisModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def __str__(self):
        return self.__class__.__name__


class AtlantisModalModelForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(AtlantisModalModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def __str__(self):
        return self.__class__.__name__


def formfield_callback(f, **kwargs):
    """
    Custom field to form callback, since the default one from django.forms
    doesn't pass the field validators to the final fieldform
    :param f: field
    :param kwargs: attributes like 'widget'
    :return:
    """
    # mapping = {
    #     "IntegerField": forms.IntegerField
    # }
    # if type(f).__name__ in mapping:
    #     return mapping[type(f).__name__](validators=f.validators, **kwargs)
    if hasattr(forms, type(f).__name__):
        return getattr(forms, type(f).__name__)(validators=f.validators, **kwargs)
    return forms.CharField(validators=f.validators, **kwargs)


def get_model_fields(model):
    return [field.name for field in model._meta.fields if field.auto_created is False]


def form_factory(model, theme: type = themes.Atlantis,
                 exclude=('id',), widgets: dict = dict(), modal=False, **kwargs) -> forms.ModelForm:
    """
    Factory function used to get specific theme form.
    :param theme: used theme e.g. Atlantis
    :param model: model from models.py
    :param exclude: fields from model to not display in the form
    :param widgets: mapping of field names to widget (ex: {'name': forms.Textarea})
    :param modal: use BSModalModelForm class or not
    :return: form instance if theme was found else default form instance is returned
    """
    # Check if user implemented abstracted properties
    _ = theme()  # will raise TypeError if 'forms_widget_attrs' is missing

    for field in get_model_fields(model):
        if field not in widgets:
            widgets[field] = forms.TextInput
    for widget in widgets:
        widgets[widget] = widgets[widget](attrs=theme.forms_widget_attrs)

    cls = modelform_factory(model=model,
                            form=BSModalModelForm if modal else forms.ModelForm,
                            exclude=list(exclude),
                            widgets=widgets,
                            formfield_callback=formfield_callback,
                            **kwargs)

    return cls

