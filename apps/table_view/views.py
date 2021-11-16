import django_tables2 as tables
import random
from django_tables2.utils import A
from django.utils.html import format_html
from django_tables2 import SingleTableView
from scripts.factrories.tables_factory import table_factory
from scripts.themes.extra_columns import Delete, Add
from scripts.themes.themes import Atlantis
from django.views import View
from scripts.factrories.form_factories import form_factory
from django import forms
from django.shortcuts import render
from django.views.generic import base
from pip._internal import req

from .models import HILs
from .forms import HILsModalForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalDeleteView, BSModalUpdateView


class Action:
    accessor = tables.Column(accessor=A('pk'), verbose_name='Action')
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


class HILsListView(SingleTableView):
    extra_content = {"chart_data": [random.randint(1, 100) for i in range(12)],
                     "card_header": format_html('<div class="card-header">Chart title</div>')}
    table_pagination = False
    model = HILs
    table_class = table_factory(model=model,
                                extra_columns=[Action])
    template_name = 'table_view/table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_content)
        return context

    def get(self, request, *args, **kwargs):
        g = super().get(request, *args, **kwargs)
        a = BookCreateView.as_view()(request, *args, **kwargs)
        return g


class BookCreateView(BSModalCreateView):
    template_name = 'table_view/modal_create.html'
    form_class = HILsModalForm
    success_message = 'Success: HIL was created.'
    success_url = reverse_lazy('hils')


class HilManager(base.ContextMixin, View):

    form = form_factory(model=HILs,
                        theme=Atlantis,
                        widgets={"responsible": forms.Textarea})

    def get(self, request):
        form = self.form
        return render(request, 'table_view/create_form.html', {
            'form': form,
            'form_title': "Add new HIL"
        })

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
        return render(request, 'table_view/create_form.html', {
            'form': form,
            'form_title': "Add new HIL",
        })


class HILDeleteView(BSModalDeleteView):
    model = HILs
    template_name = 'table_view/modal_delete.html'
    success_message = 'Success: HIL was deleted.'
    success_url = reverse_lazy('hils')


class HILUpdateView(BSModalUpdateView):
    model = HILs
    template_name = 'table_view/modal_update.html'
    form_class = HILsModalForm
    success_message = 'Success: HIL was updated.'
    success_url = reverse_lazy('hils')
