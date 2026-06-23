from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Experience, Profile, Project


class PublicPagesTests(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            full_name="Ibrahim Mrisha",
            professional_title="FullStack Developer",
            email="ibrahim@example.com",
        )

    def test_home_page_uses_database_content(self):
        Project.objects.create(
            title="Portfolio CMS",
            description="A database-powered portfolio.",
        )
        response = self.client.get(reverse("portfolio:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ibrahim Mrisha")
        self.assertContains(response, "Portfolio CMS")

    def test_cv_page_generates_from_profile_and_experience(self):
        Experience.objects.create(
            job_title="Software Developer",
            organization="Example Ltd",
            start_date=date(2024, 1, 1),
            description="Built useful software.",
        )
        response = self.client.get(reverse("portfolio:cv"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Curriculum Vitae")
        self.assertContains(response, "Example Ltd")

    def test_only_one_profile_is_kept(self):
        second = Profile.objects.create(full_name="Updated Name", email="new@example.com")
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(second.pk, self.profile.pk)
