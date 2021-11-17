# builtins
import random
# django
from django import forms
from django.shortcuts import render
from django.views.generic import base
from django.views import View
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# django plugins
from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalDeleteView, BSModalUpdateView
from django_tables2 import SingleTableView
from chartjs.views.lines import BaseLineChartView
# factorio
from scripts.factrories.form_factories import form_factory
from scripts.factrories.tables_factory import table_factory
from scripts.themes.themes import Atlantis
# local imports
from .tables import Action
from .models import HILs


class LineChartJSONView(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

    def get_datasets(self):
        datasets = super().get_datasets()
        for dataset in datasets:
            if dataset["name"] == "Central":
                dataset.update(self.get_dataset_options(0, (11, 252, 3)))
            elif dataset["name"] == "Eastside":
                dataset.update(self.get_dataset_options(0, (34, 51, 240)))
            elif dataset["name"] == "Westside":
                dataset.update(self.get_dataset_options(0, (232, 184, 28)))
        return datasets


class LineChartView(TemplateView):
    template_name = 'table_view/chart.html'


HILsModalForm = form_factory(model=HILs, theme=Atlantis,
                             widgets={'responsible': forms.Textarea},
                             form=BSModalModelForm)


class HILsListView(SingleTableView):
    extra_content = {"chart_data": [random.randint(1, 100) for i in range(12)],
                     "card_header": format_html('<div class="card-header">Chart title</div>')}
    table_pagination = False
    model = HILs
    table_class = table_factory(model=model,
                                extra_columns=[Action])
    template_name = 'table_view/table.html'

    chart = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_content)
        context["chart"] = self.chart
        return context

    def get(self, request, *args, **kwargs):
        self.chart = LineChartView.as_view()(request, *args, **kwargs).rendered_content
        g = super().get(request, *args, **kwargs)
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
