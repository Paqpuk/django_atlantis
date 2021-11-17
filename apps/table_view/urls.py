from django.urls import path, re_path
from .views import HILsListView, BookCreateView, HilManager, HILDeleteView, HILUpdateView, LineChartView, LineChartJSONView

urlpatterns = [
    path('hils/', HILsListView.as_view(extra_context={
        'title': 'HILs',
        'table_name': "HIL configurations",
        'formurl': '/hils/create/',
        'modal': True
    }),
         name="hils"),

    # path('hils/create/', BookCreateView.as_view(extra_context={"title": "Add new HIL"}), name="add_hil"),

    path('hils/create/', BookCreateView.as_view(extra_context={"form_title": "Add new HIL"}), name="add_hil"),
    path('hils/delete/<int:pk>', HILDeleteView.as_view(), name='delete_book'),
    path('hils/update/<int:pk>', HILUpdateView.as_view(extra_context={"form_title": "Edit HIL"}), name='update_book'),
    path('chartJSON', LineChartJSONView.as_view(), name="line_chart_json"),
    path('chart', LineChartView.as_view())
]
