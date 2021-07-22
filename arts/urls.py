from django.urls import path
from arts.views import CategoryListView

urlpatterns = [
    path('/categorylist', CategoryListView.as_view())
] 