from expenditure import views
from rest_framework.routers import SimpleRouter

expenditure_router = SimpleRouter()
expenditure_router.register(r'', views.ExpenditureViewSet, basename='expenditure')
