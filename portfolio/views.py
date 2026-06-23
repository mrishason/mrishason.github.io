from django.shortcuts import render

from .models import Conference, Education, Experience, Profile, Project, Publication, Skill, Topic


def get_profile():
    return Profile.objects.first()


def home(request):
    context = {
        "profile": get_profile(),
        "projects": Project.objects.filter(is_visible=True),
        "conferences": Conference.objects.filter(is_visible=True),
        "topics": Topic.objects.filter(is_visible=True),
        "publications": Publication.objects.filter(is_visible=True),
    }
    return render(request, "portfolio/home.html", context)


def cv(request):
    context = {
        "profile": get_profile(),
        "experiences": Experience.objects.filter(is_visible=True),
        "education_items": Education.objects.filter(is_visible=True),
        "skills": Skill.objects.filter(is_visible=True),
        "projects": Project.objects.filter(is_visible=True),
    }
    return render(request, "portfolio/cv.html", context)
