from django.urls import path
from .views import Link

urlpatterns = [
		path('', Link, name = 'KT')
]
