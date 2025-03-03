from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonationViewSet, CharityViewSet, login_view, donation_analytics
from .charts import combined_charts

router = DefaultRouter()
router.register(r'donations', DonationViewSet)
router.register(r'charities', CharityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('analytics/', donation_analytics, name='donation-analytics'),
    path('charts/', combined_charts, name='charts'),
]
