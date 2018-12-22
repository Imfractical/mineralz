from django.db import models

MAX_LENGTH = 100


class Mineral(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    image_filename = models.CharField(max_length=MAX_LENGTH)
    image_caption = models.CharField(blank=True, max_length=MAX_LENGTH)
    category = models.CharField(blank=True, max_length=MAX_LENGTH)
    formula = models.CharField(blank=True, max_length=MAX_LENGTH)
    strunz_classification = models.CharField(blank=True, max_length=MAX_LENGTH)
    crystal_system = models.CharField(blank=True, max_length=MAX_LENGTH)
    unit_cell = models.CharField(blank=True, max_length=MAX_LENGTH)
    color = models.CharField(blank=True, max_length=MAX_LENGTH)
    crystal_symmetry = models.CharField(blank=True, max_length=MAX_LENGTH)
    cleavage = models.CharField(blank=True, max_length=MAX_LENGTH)
    mohs_scale_hardness = models.CharField(blank=True, max_length=MAX_LENGTH)
    luster = models.CharField(blank=True, max_length=MAX_LENGTH)
    streak = models.CharField(blank=True, max_length=MAX_LENGTH)
    diaphaneity = models.CharField(blank=True, max_length=MAX_LENGTH)
    optical_properties = models.CharField(blank=True, max_length=MAX_LENGTH)
    refractive_index = models.CharField(blank=True, max_length=MAX_LENGTH)
    crystal_habit = models.CharField(blank=True, max_length=MAX_LENGTH)
    specific_gravity = models.CharField(blank=True, max_length=MAX_LENGTH)
    group = models.CharField(blank=True, max_length=MAX_LENGTH)
