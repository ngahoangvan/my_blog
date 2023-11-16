from rest_framework import serializers
from .models import Bio, BioExperience, BioHobby, BioSocial
from skill.serializers import SkillSerializer


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioExperience
        fields = [
            # "id",
            "company",
            "position",
            "start_date",
            "end_date",
            "location",
            "responsibility",
        ]


class BioHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = BioHobby
        fields = ["emoji", "description"]


class BioSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioSocial
        fields = ["name", "link", "icon"]


class BioSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    socials = BioSocialSerializer(many=True)
    hobbies = BioHobbySerializer(many=True)

    class Meta:
        model = Bio
        fields = [
            "introduction",
            "position",
            "skills",
            "experiences",
            "socials",
            "hobbies",
        ]
