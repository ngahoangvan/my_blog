from rest_framework import generics, permissions, status
from rest_framework.response import Response
from authentication.models import User
from .serializers import DashboardSerializer


class DashboardAPIView(generics.GenericAPIView):
    serializer_class = DashboardSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        """
        Get bio of Admin user for homepage
        """
        admin_user = User.objects.get(is_superuser=True)  # me

        return Response(
            data=DashboardSerializer(admin_user).data, status=status.HTTP_200_OK
        )
