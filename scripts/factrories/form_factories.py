from __future__ import annotations
from django import forms
from django.forms import modelform_factory
from ..themes import themes


def formfield_callback(f, **kwargs):
    """
    Custom field to form callback, since the default one from django.forms
    doesn't pass the field validators to the final fieldform
    :param f: field
    :param kwargs: attributes like 'widget'
    :return:
    """
    if hasattr(forms, type(f).__name__):
        return getattr(forms, type(f).__name__)(validators=f.validators, **kwargs)
    return forms.CharField(validators=f.validators, **kwargs)


def get_model_fields(model):
    return [field.name for field in model._meta.fields if field.auto_created is False]


def form_factory(model, theme: type[themes.AbstractTheme] = themes.Atlantis,
                 exclude=('id',), widgets: dict = None,
                 form=forms.ModelForm, **kwargs) -> forms.ModelForm:
    """
    Factory function used to get specific theme form.
    :param theme: used theme e.g. Atlantis
    :param model: model from models.py
    :param exclude: fields from model to not display in the form
    :param widgets: mapping of field names to widget (ex: {'name': forms.Textarea})
    :param form: ModelForm class, provide other class for customization
    :return: form instance if theme was found else default form instance is returned
    """
    return modelform_factory(model=model,
                             form=type('', (theme.FormClass, form), {}),
                             exclude=list(exclude),
                             widgets=widgets if widgets else None,
                             formfield_callback=formfield_callback,
                             **kwargs)
