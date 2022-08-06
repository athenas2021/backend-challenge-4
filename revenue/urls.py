
from revenue import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', views.RevenueViewSet, basename='revenue')

# urlpatterns = [
#     path('', include(router.urls))
# ]
