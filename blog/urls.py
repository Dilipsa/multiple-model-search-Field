from django.urls import path
from .views import HomeView
urlpatterns = [

    path('<slug>/', HomeView.as_view(), name='home'),
]
