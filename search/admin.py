from django.contrib import admin

# Register your models here.
from blog.models import Post
from courses.models import Lesson
from profiles.models import Profile

admin.site.register(Post)
admin.site.register(Lesson)
admin.site.register(Profile)
