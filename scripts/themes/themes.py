import abc
from django import forms


class AbstractTheme(abc.ABC):
    """
    A template for a theme
    """
    @classmethod
    @abc.abstractmethod
    class TableMeta:
        """
        The 'Meta' class that is normally used by the django_tables2.tables.Table class
        """
        attrs = {
            "class": "display table table-bordered table-head-bg-info table-bordered-bd-info mt-4",
            "id": "basic-datatables"
        }
        orderable = False

    @property
    @abc.abstractmethod
    class FormClass(forms.ModelForm):
        """
        A custom class with super().init() to overwrite desired
        ModelForm attributes in accordance to the theme
        """
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


class Atlantis(AbstractTheme):
    class TableMeta:
        attrs = {
            "class": "display table table-bordered table-head-bg-info table-bordered-bd-info mt-4",
            "id": "basic-datatables"
        }
        orderable = False

    class FormClass(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


