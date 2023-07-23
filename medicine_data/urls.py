from django.urls import path
from . import views
urlpatterns = [
    path("pharmacies/",views.give_result),
]