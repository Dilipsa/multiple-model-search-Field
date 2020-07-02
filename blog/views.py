from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.
class HomeView(ListView):
    model = Post
    paginate_by = 4
    template_name = "post.html"
