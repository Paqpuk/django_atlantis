import django_tables2 as tables
from django.utils.html import format_html


class Action:
    accessor = tables.Column(accessor=tables.utils.A('pk'), verbose_name='Action')
    '<button class="btn btn-default"><a href="delete/{id}/">Delete</a></button>'
    @staticmethod
    def render_accessor(record):
        return format_html('<button type="button" class="delete-book bs-modal btn btn-sm btn-danger" '
                           'data-form-url="delete/{id}">'
                           '<span class="fa fa-trash"></span>'
                           '</button>'
                           '<button type="button" class="update-book bs-modal btn btn-sm btn-primary"'
                           ' data-form-url="update/{id}">'
                           '<i class="fa fa-info"></i>'
                           '</button>', id=record.id)

    def __str__(self):
        return __class__.__name__
