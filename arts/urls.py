from django.urls import path

from arts.views import ArtsFilterView

urlpatterns = [
    path('/filter', ArtsFilterView.as_view()),

]