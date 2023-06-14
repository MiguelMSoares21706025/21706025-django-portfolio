from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

# ------BLOG-------------------------------------------------------------------------------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    Business = 'Business'
    Technology = 'Technology'
    Entertainment = 'Entertainment'
    Lifestyle = 'Lifestyle'
    Travel = 'Travel'
    Sports = 'Sports'
    Other = 'Other'

    CHOICES_TYPE = [
        (Business, "Business"),
        (Technology, 'Technology'),
        (Entertainment, 'Entertainment'),
        (Lifestyle, 'Lifestyle'),
        (Travel, 'Travel'),
        (Sports, 'Sports'),
        (Other, 'Other')
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/static/portfolio/images/', default='url("../images/backiee-5769412.jpg")')
    area = models.CharField(max_length=15, choices=CHOICES_TYPE, default="Business")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors', default='')
    brief_description = models.CharField(max_length=500)
    sub_title1 = models.CharField(max_length=100, null=True, blank=True, default='')
    description1 = models.CharField(max_length=1000, null=True, blank=True, default='')
    sub_title2 = models.CharField(max_length=100, null=True, blank=True, default='')
    description2 = models.CharField(max_length=1000, null=True, blank=True, default='')
    date = models.DateField()

    def __str__(self):
        return self.title


# ------COURSES----------------------------------------------------------------------------------------------------------
class Certification(models.Model):
    certification = models.CharField(max_length=50)

    def __str__(self):
        return self.certification


class OtherCourse(models.Model):
    course = models.CharField(max_length=70)

    def __str__(self):
        return self.course


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Academic(models.Model):
    academic = models.CharField(max_length=50)

    def __str__(self):
        return self.academic


class CurricularUnit(models.Model):
    curricular_unit = models.CharField(max_length=50, default='')
    link = models.URLField()
    year = models.CharField(max_length=5, default='')
    semester = models.CharField(max_length=5, default='1')
    ects = models.IntegerField(default=1)
    responsible_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='responsible_teachers',
                                            null=True, blank=True, default='')
    additional_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='additional_teachers',
                                           null=True, blank=True, default='')
    ranking = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    academic = models.ForeignKey(Academic, on_delete=models.CASCADE, related_name='curricular_units')

    def __str__(self):
        return self.curricular_unit


# -------PROJECTS--------------------------------------------------------------------------------------------------------
class Project(models.Model):
    title = models.CharField(max_length=50, default='')
    curricular_unit = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to='portfolio/static/portfolio/images/', default='url("../images/backiee-5769412.jpg")')

    def __str__(self):
        return self.title


# -------WEB DEV--------------------------------------------------------------------------------------------------------
class Subject(models.Model):
    name = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name


class Tech_BackEnd(models.Model):
    name = models.CharField(max_length=10, default='')
    release_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    author = models.CharField(max_length=50, default='')
    logo = models.ImageField(upload_to='portfolio/images/')
    website_link = models.URLField()
    description = models.CharField(max_length=800, default='')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, related_name='be_techs')

    def __str__(self):
        return self.name


class Tech_FrontEnd(models.Model):
    name = models.CharField(max_length=10, default='')
    release_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    author = models.CharField(max_length=50, default='')
    logo = models.ImageField(upload_to='portfolio/images/')
    website_link = models.URLField()
    description = models.CharField(max_length=800, default='')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, related_name='fe_techs')

    def __str__(self):
        return self.name


class Tech_Other(models.Model):
    name = models.CharField(max_length=10, default='')
    release_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    author = models.CharField(max_length=50, default='')
    logo = models.ImageField(upload_to='portfolio/images/')
    website_link = models.URLField()
    description = models.CharField(max_length=800, default='')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, related_name='other_techs')

    def __str__(self):
        return self.name

