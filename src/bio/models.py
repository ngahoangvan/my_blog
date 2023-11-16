from django.db import models

from authentication.models import User


# Create your models here.
class Bio(models.Model):
    user = models.OneToOneField(
        to=User, related_name="bio", on_delete=models.CASCADE, null=True, blank=True
    )
    introduction = models.CharField(
        verbose_name="introduction", max_length=512, null=True, blank=True
    )
    position = models.CharField(max_length=64, blank=True)
    skills = models.ManyToManyField(
        to="skill.Skill",
        through="BioSkill",
        related_name="bio_skills",
        blank=True,
        symmetrical=False,
    )

    def __str__(self) -> str:
        return self.user.__str__()


class BioSkill(models.Model):
    bio = models.ForeignKey(
        to=Bio,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        to="skill.Skill",
        on_delete=models.CASCADE,
    )
    is_proficient = models.BooleanField(verbose_name="is proficient", default=True)


class SocialMedia(models.TextChoices):
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    GITHUB = "github"
    LINKEDIN = "linkedin"


class SocialMediaIcon(models.TextChoices):
    FACEBOOK = "fa fa-facebook"
    INSTAGRAM = "fa fa-instagram"
    GITHUB = "fa fa-github"
    LINKEDIN = "fa fa-linkedin"


class BioSocial(models.Model):
    bio = models.ForeignKey(
        to=Bio,
        related_name="socials",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=16, choices=SocialMedia.choices)
    link = models.CharField(max_length=64, null=True)

    @property
    def icon(self):
        return f"fa fa-{self.name}"

    def __str__(self) -> str:
        return self.name


class BioHobby(models.Model):
    bio = models.ForeignKey(
        to=Bio,
        related_name="hobbies",
        on_delete=models.CASCADE,
    )
    emoji = models.CharField(max_length=5, null=True)
    description = models.CharField(max_length=256)


class BioExperience(models.Model):
    bio = models.ForeignKey(
        to=Bio,
        related_name="experiences",
        on_delete=models.CASCADE,
    )
    company = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    location = models.CharField(max_length=64)
    responsibility = models.JSONField()

    def __str__(self) -> str:
        return self.company
