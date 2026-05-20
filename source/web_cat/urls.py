from django.urls import path
from web_cat.views import index, cat_stats

# , about, contacts
urlpatterns = [
    path('', index),
    path('cat_stats/', cat_stats),
]