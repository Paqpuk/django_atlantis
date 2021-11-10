from django_tables2 import SingleTableView
from .models import HILs
from .tables import HILsTable
from .forms import HILsModalForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from bootstrap_modal_forms.generic import BSModalCreateView


class HILsListView(SingleTableView):
    SingleTableView.table_pagination = False
    model = HILs
    table_class = HILsTable
    template_name = 'table_view/hils.html'


class BookCreateView(BSModalCreateView):
    template_name = 'table_view/create_hils.html'
    form_class = HILsModalForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('hils')


def delete(request, hil_id):
    HILs.objects.filter(id=hil_id).delete()
    return redirect('hils')
