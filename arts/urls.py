from django.urls import path
from arts.views  import ArtsView

urlpatterns = [
    path('', ArtsView.as_view()),
]