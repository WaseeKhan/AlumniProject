from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class AddAlumni(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    portal_join_date = models.DateTimeField(auto_now_add=True, null=True)
    profession = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    dp = models.ImageField(upload_to='dp/', null=True)
    batch = models.PositiveIntegerField(default=current_year(),
                                        validators=[MinValueValidator(1984), max_value_current_year], )
    icoInsta = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class HomeSlider(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='SlidePics/', blank=True)

    def __str__(self):
        return self.title


class NewsUpdate(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    link = models.CharField(max_length=100, null=True, blank=True)
    src = models.ImageField(upload_to='notice/', blank=True)

    def __str__(self):
        return self.title