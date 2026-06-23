from django.contrib import admin

from .models import (
    Conference,
    Education,
    Experience,
    Profile,
    Project,
    Publication,
    Skill,
    Topic,
)


admin.site.site_header = "Ibrahim Mrisha Portfolio"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage website content"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Personal details",
            {
                "fields": (
                    "full_name",
                    "professional_title",
                    "profile_photo",
                    "location",
                    "organization",
                )
            },
        ),
        (
            "Contact & social links",
            {
                "fields": (
                    "email",
                    "phone",
                    "website",
                    "github_url",
                    "linkedin_url",
                )
            },
        ),
        (
            "Website biography",
            {
                "fields": (
                    "short_bio",
                    "about_paragraph_1",
                    "about_paragraph_2",
                    "about_paragraph_3",
                )
            },
        ),
        ("Generated CV", {"fields": ("cv_summary",)}),
    )

    def has_add_permission(self, request):
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("job_title", "organization", "start_date", "end_date", "is_current", "is_visible")
    list_filter = ("is_current", "is_visible")
    search_fields = ("job_title", "organization", "description")
    list_editable = ("is_visible",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("qualification", "institution", "start_date", "end_date", "is_visible")
    list_editable = ("is_visible",)
    search_fields = ("qualification", "institution", "field_of_study")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order", "is_visible")
    list_filter = ("category", "is_visible")
    list_editable = ("proficiency", "order", "is_visible")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "order", "is_visible")
    list_filter = ("featured", "is_visible")
    list_editable = ("featured", "order", "is_visible")
    search_fields = ("title", "description", "technologies")


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ("title", "organizer", "event_date", "location", "is_visible")
    list_editable = ("is_visible",)
    search_fields = ("title", "organizer", "description")


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "publication_date", "is_visible")
    list_editable = ("is_visible",)
    search_fields = ("title", "publisher", "summary")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_visible")
    list_editable = ("order", "is_visible")
