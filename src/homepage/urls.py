from django.urls import path
from .views import DashboardAPIView

urlpatterns = [
    path("author-info", DashboardAPIView.as_view(), name="public information")
]
