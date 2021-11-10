from django.urls import path, re_path
from .views import HILsListView, BookCreateView, delete

urlpatterns = [
    path('hils/', HILsListView.as_view(extra_context={
        'title': 'HILs',
        'formurl': '/create_hils/'
    }),
         name="hils"),
    path('create_hils/', BookCreateView.as_view(extra_context={"title": "Add new HIL"}), name="add_hil"),
    re_path('hils\/delete\/(?P<hil_id>\d+)\/', delete, name="delete")
]
