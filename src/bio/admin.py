from django.contrib import admin
from .models import Bio, BioSkill, BioExperience, BioSocial, BioHobby

# from skill.models import Skill

# Register your models here.


class BioExperienceInline(admin.TabularInline):
    model = BioExperience
    extra = 2


class BioSkillInline(admin.TabularInline):
    model = BioSkill
    extra = 2


class BioSocialInline(admin.TabularInline):
    model = BioSocial
    extra = 2


class BioHobbyInline(admin.TabularInline):
    model = BioHobby
    extra = 2


class BioAdmin(admin.ModelAdmin):
    inlines = [BioSkillInline, BioExperienceInline, BioSocialInline, BioHobbyInline]
    filter_horizontal = ("skills",)


admin.site.register(Bio, BioAdmin)
