from django.urls import path
from arts.views  import ArtsView, ArtView

urlpatterns = [
    path('', ArtsView.as_view()),
    path('/<int:art_id>', ArtView.as_view()),
]