from uuid import uuid4

from django.db import models
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField


class ComicStrip(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        unique=True,
        editable=False
    )

    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title')
    date = models.DateField()
    image_url = models.URLField()

    def get_absolute_url(self):
        return reverse('comic-strip-detail', args=[str(self.slug)])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'
