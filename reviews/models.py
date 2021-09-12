from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from wagtail.snippets.models import register_snippet


@register_snippet
class Review(models.Model):
    content = models.TextField(null=False, blank=False, max_length=500)
    rating = models.PositiveBigIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.content
