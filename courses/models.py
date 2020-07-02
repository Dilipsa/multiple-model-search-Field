from django.db import models
from django.conf import settings

# blog.models
from django.db.models import Q


class CourseeManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(description__icontains=query) |
                         Q(slug__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


# courses.models
class Lesson(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    featured = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = CourseeManager()