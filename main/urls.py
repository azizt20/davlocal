from django.urls import path, include

from .views import home,solutions,services
urlpatterns = [
    path('', home, name='home'),
    path('solutions/', solutions, name='solutions'),
    path('services/', services, name='services'),
]
