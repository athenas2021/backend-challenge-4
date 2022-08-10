from expenditure import views
from rest_framework.routers import SimpleRouter
from django.urls import path

expenditure_router = SimpleRouter()
expenditure_router.register(r'', views.ExpenditureViewSet, basename='expenditure')

urlpatterns = [
    path(r'<int:month>/<int:year>/', views.ExpenditureByMonthView.as_view(), name='expenditure-by-month')
]
