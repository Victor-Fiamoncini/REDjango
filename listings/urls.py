# Imports
from django.urls import path
from . import views

# Pages urls
urlpatterns = [
	path('', views.index, name='listings'),
	path('<int:listing_id>', views.listing, name='listing'),
]
