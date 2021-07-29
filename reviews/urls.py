from django.urls    import path

from arts.views     import ArtsView, ArtView
from reviews.views  import ReviewView

urlpatterns = [
    path('', ArtsView.as_view()),
    path('/<int:art_id>', ArtView.as_view()),
    path('/<int:art_id>/reviews', ReviewView.as_view())
]