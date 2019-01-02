"""mineral_catalog models"""
from django.db import models
from django.utils.text import slugify

MAX_LENGTH = 500


class Mineral(models.Model):
    """Model that describes a mineral in detail"""
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(unique=True, max_length=MAX_LENGTH)
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

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Mineral.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)
