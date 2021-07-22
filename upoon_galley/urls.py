from django.urls import path, include

urlpatterns = [
    path('arts', include('arts.urls')),
]