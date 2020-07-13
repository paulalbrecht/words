from django.db import models


class Recommendation(models.Model):
    # Fields
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    recommender = models.CharField(max_length=255)
    source = models.URLField()
    amazon_link = models.URLField()
    description = models.CharField(max_length=255)
    rec_type = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    publish_year = models.CharField(max_length=255)
    on_list = models.CharField(max_length=255)
    review_excerpt = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        unique_together = (("title", "author", "recommender"),)
