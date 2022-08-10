from expenditure import views
from rest_framework.routers import SimpleRouter
from django.urls import path

expenditure_router = SimpleRouter()
expenditure_router.register(r'', views.ExpenditureViewSet, basename='expenditure')
# expenditure_router.register(r'<int:month>/<int:year>/', views.ExpenditureViewSet, basename='expenditure-by-month')
# expenditure_router.register(r'(?P<teste1>[^/.]+)/(?P<teste2>[^/.]+)', views.ExpenditureViewSet.teste, basename='-mandatory')
# expenditure_router.register(r'<str:id1>/<str:id2>/', views.teste, basename='mandatory')
urlpatterns = [
    # path('despesas/<int:ano>/<int:mes>/', ListaDespesasMes.as_view()),
    path(r'<int:month>/<int:year>/', views.ExpenditureByMonthView.as_view(), name='expenditure-by-month')
]