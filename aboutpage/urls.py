from django.urls import path, include
from .views import AboutPageView

urlpatterns = [
    path('', AboutPageView.as_view(), name="about" )
]
