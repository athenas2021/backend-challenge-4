from .views import SummaryView
from django.urls import path


urlpatterns = [
    path(r'<int:month>/<int:year>/', SummaryView.as_view(), name='summary')
]
