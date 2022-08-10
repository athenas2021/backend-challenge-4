
from revenue import views
from rest_framework.routers import SimpleRouter
from django.urls import path

revenue_router = SimpleRouter()
revenue_router.register(r'', views.RevenueViewSet, basename='revenue')

urlpatterns = [
    path(r'<int:month>/<int:year>/', views.RevenueByMonthView.as_view(), name='revenue-by-month')
]
