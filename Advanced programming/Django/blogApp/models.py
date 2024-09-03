from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150,primary_key=True)
    content = models.TextField()
    publish_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
