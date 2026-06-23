from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class OrderedModel(models.Model):
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_visible = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ("order", "-id")


class Profile(models.Model):
    full_name = models.CharField(max_length=120, default="Ibrahim Mrisha")
    professional_title = models.CharField(max_length=160, default="FullStack Developer")
    location = models.CharField(max_length=120, default="Tanzania")
    organization = models.CharField(max_length=160, blank=True, default="Technology")
    email = models.EmailField(default="ibrahim.mrisha@yahoo.com")
    phone = models.CharField(max_length=40, blank=True)
    website = models.URLField(blank=True)
    github_url = models.URLField(blank=True, default="https://github.com/mrishason/")
    linkedin_url = models.URLField(
        blank=True,
        default="https://www.linkedin.com/in/mr-mrisha-754436155/",
    )
    profile_photo = models.ImageField(upload_to="profile/", blank=True)
    short_bio = models.TextField(
        default=(
            "I am a passionate FullStack Developer and technology enthusiast focused on "
            "creating useful, reliable, and human-centered digital experiences."
        )
    )
    about_paragraph_1 = models.TextField(
        blank=True,
        default=(
            "My work combines thoughtful design with practical engineering. From responsive "
            "websites and modern applications to scalable systems, I approach every project "
            "with curiosity, attention to detail, and a commitment to continuous improvement."
        ),
    )
    about_paragraph_2 = models.TextField(
        blank=True,
        default=(
            "Beyond writing code, I value collaboration and knowledge sharing. I am always "
            "interested in meeting other builders, exploring new ideas, and contributing to "
            "technology communities that create meaningful opportunities."
        ),
    )
    about_paragraph_3 = models.TextField(
        blank=True,
        default=(
            "I am open to new challenges and collaborations. Let's connect and build "
            "something thoughtful together."
        ),
    )
    cv_summary = models.TextField(
        blank=True,
        help_text="Professional summary displayed at the top of the generated CV.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile & CV contact details"
        verbose_name_plural = "Profile & CV contact details"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.pk and Profile.objects.exists():
            self.pk = Profile.objects.first().pk
            kwargs.pop("force_insert", None)
        super().save(*args, **kwargs)

    @property
    def initials(self):
        return "".join(part[0] for part in self.full_name.split()[:2]).upper()


class Experience(OrderedModel):
    job_title = models.CharField(max_length=160)
    organization = models.CharField(max_length=180)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(
        blank=True,
        help_text="Use a new line for each achievement or responsibility.",
    )

    class Meta(OrderedModel.Meta):
        verbose_name = "Work experience"
        verbose_name_plural = "Work experience"
        ordering = ("-start_date", "order")

    def __str__(self):
        return f"{self.job_title} — {self.organization}"


class Education(OrderedModel):
    qualification = models.CharField(max_length=180)
    institution = models.CharField(max_length=180)
    field_of_study = models.CharField(max_length=180, blank=True)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name_plural = "Education"
        ordering = ("-end_date", "-start_date", "order")

    def __str__(self):
        return f"{self.qualification} — {self.institution}"


class Skill(OrderedModel):
    CATEGORY_CHOICES = [
        ("technical", "Technical"),
        ("tool", "Tools & platforms"),
        ("language", "Languages"),
        ("soft", "Professional"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="technical")
    proficiency = models.PositiveSmallIntegerField(
        default=80,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="A value from 1 to 100.",
    )

    class Meta(OrderedModel.Meta):
        ordering = ("category", "order", "name")

    def __str__(self):
        return self.name


class Topic(OrderedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(OrderedModel):
    title = models.CharField(max_length=160)
    category = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    technologies = models.CharField(
        max_length=240,
        blank=True,
        help_text="Example: Django, PostgreSQL, JavaScript",
    )
    project_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    featured = models.BooleanField(default=False)

    class Meta(OrderedModel.Meta):
        ordering = ("-featured", "order", "-id")

    def __str__(self):
        return self.title


class Conference(OrderedModel):
    title = models.CharField(max_length=180)
    organizer = models.CharField(max_length=160, blank=True)
    event_date = models.DateField()
    location = models.CharField(max_length=140, blank=True)
    description = models.TextField(blank=True)
    event_url = models.URLField(blank=True)

    class Meta(OrderedModel.Meta):
        ordering = ("-event_date", "order")

    def __str__(self):
        return self.title


class Publication(OrderedModel):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=160, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    summary = models.TextField(blank=True)
    publication_url = models.URLField(blank=True)

    class Meta(OrderedModel.Meta):
        ordering = ("-publication_date", "order")

    def __str__(self):
        return self.title
