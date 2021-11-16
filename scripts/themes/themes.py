import abc


class AbstractTheme(abc.ABC, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def table_meta_attrs(self):
        """
        Dict with attributes for the django_tables2.tables.Table Meta
        Example:
        table_meta_attrs = {
        "attrs": {
            "class": "display table table-bordered table-head-bg-info table-bordered-bd-info mt-4",
            "id": "basic-datatables"
            },
        "orderable": False
        }
        """
        pass

    @property
    @abc.abstractmethod
    def forms_widget_attrs(self):
        """
        Dict with widget attributes to be added all widgets in form
        Example:
        forms_widget_attrs = {"class": "form-control"}
        """
        pass


class Atlantis(AbstractTheme):
    table_meta_attrs = {
        "attrs": {
            "class": "display table table-bordered table-head-bg-info table-bordered-bd-info mt-4",
            "id": "basic-datatables"
        },
        "orderable": False
    }
    forms_widget_attrs = {"class": "form-control"}


