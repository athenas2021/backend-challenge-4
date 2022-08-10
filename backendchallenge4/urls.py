from django.contrib import admin
from django.urls import path, include
# from revenue.urls import *
from revenue.urls import revenue_router
from expenditure.urls import expenditure_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('revenue/', include(revenue_router.urls)),
    path('revenue/', include('revenue.urls')),
    path('expenditure/', include(expenditure_router.urls)),
    path('expenditure/', include('expenditure.urls')),
    path('summary/', include('summary.urls')),
]
