from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    description = models.TextField()
    url = models.URLField()
    image_url = models.URLField()
    related_news = models.ForeignKey(
        'self',  # Same model
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # If the related news is deleted, set this field to NULL
        related_name='related_new'  # Name of the reverse relation from the related object back to this one
    )

    def __str__(self):
        return self.title
