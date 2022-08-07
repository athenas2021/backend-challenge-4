
from revenue import views
from rest_framework.routers import SimpleRouter

revenue_router = SimpleRouter()
revenue_router.register(r'', views.RevenueViewSet, basename='revenue')
