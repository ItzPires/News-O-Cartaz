from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    description = models.TextField()
    url = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.title
