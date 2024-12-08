from django.contrib import admin

from .models import Award, Skill, Project, Technology, Teammate, Message, Service
# Register your models here.


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Technology)
class TechnoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Teammate)
class TeammateAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'job')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title', )