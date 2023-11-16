from rest_framework import serializers
from authentication.models import User
from bio.serializers import BioSerializer


class DashboardSerializer(serializers.ModelSerializer):
    bio = BioSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "avatar",
            "first_name",
            "last_name",
            "date_of_birth",
            "initials",
            "bio",
        ]
