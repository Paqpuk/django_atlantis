import django_tables2 as tables
from django.utils.html import format_html
from .models import HILs
from django.urls import reverse
from django_tables2.utils import A


class HILsTable(tables.Table):
    delete = tables.Column(accessor=A('pk'), verbose_name='Delete')

    class Meta:

        attrs = {"class": "display table table-bordered table-head-bg-info table-bordered-bd-info mt-4",
                 "id": "basic-datatables"}
        model = HILs
        fields = ("name", "station", "responsible", "delete")
        orderable = False
        show_footer = False

    def render_delete(self, record):
        return format_html('<a href="delete/{id}/">{id}</a>', id=record.id)
