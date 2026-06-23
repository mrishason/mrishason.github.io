from django.db import migrations


def seed_initial_content(apps, schema_editor):
    Profile = apps.get_model("portfolio", "Profile")
    Topic = apps.get_model("portfolio", "Topic")

    Profile.objects.get_or_create(
        pk=1,
        defaults={
            "full_name": "Ibrahim Mrisha",
            "professional_title": "FullStack Developer",
            "location": "Tanzania",
            "organization": "Technology",
            "email": "ibrahim.mrisha@yahoo.com",
            "github_url": "https://github.com/mrishason/",
            "linkedin_url": "https://www.linkedin.com/in/mr-mrisha-754436155/",
            "short_bio": (
                "I am a passionate FullStack Developer and technology enthusiast focused on "
                "creating useful, reliable, and human-centered digital experiences."
            ),
        },
    )

    for order, name in enumerate(
        [
            "Software Engineering",
            "Web Development",
            "Django",
            "Open Source",
            "Artificial Intelligence",
        ],
        start=1,
    ):
        Topic.objects.get_or_create(name=name, defaults={"order": order})


def remove_initial_content(apps, schema_editor):
    Topic = apps.get_model("portfolio", "Topic")
    Topic.objects.filter(
        name__in=[
            "Software Engineering",
            "Web Development",
            "Django",
            "Open Source",
            "Artificial Intelligence",
        ]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_initial_content, remove_initial_content),
    ]
