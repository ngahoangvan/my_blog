from rest_framework import generics, permissions
from .models import Skill
from .serializers import SkillSerializer


class SkillListAPIView(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Skill.objects.all()
