from expenditure import views
from rest_framework.routers import SimpleRouter
from django.urls import path

expenditure_router = SimpleRouter()
expenditure_router.register(r'', views.ExpenditureViewSet, basename='expenditure')
# expenditure_router.register(r'(?P<teste1>[^/.]+)/(?P<teste2>[^/.]+)', views.ExpenditureViewSet.teste, basename='group-trainings-group-training-user-results-mandatory')
# expenditure_router.register(r'<str:id1>/<str:id2>/', views.teste, basename='group-trainings-group-training-user-results-mandatory')
urlpatterns = [
    path(r'<int:month>/<int:year>/', views.ExpenditureViewSet.searchExpenditureByMonth, name='expenditure-by-month')
]