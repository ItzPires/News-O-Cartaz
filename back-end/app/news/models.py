from django.db import models
from django.utils.timezone import now

class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    datetime = models.DateTimeField(default=now)
    description = models.TextField(blank=True)
    url = models.URLField(unique=True)
    image_url = models.URLField(blank=True)
    related_news = models.ForeignKey(
        'self',  # Same model
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # If the related news is deleted, set this field to NULL
        related_name='related_new'  # Name of the reverse relation from the related object back to this one
    )

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return self.title
