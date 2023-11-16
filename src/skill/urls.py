from django.urls import path
from .views import SkillListAPIView

urlpatterns = [path("", SkillListAPIView.as_view(), name="list skill")]
