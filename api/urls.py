from django.urls import path, include
from .views import MovieListView, MovieDetailView, ReviewCreateView, ReviewDestroyView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/reviews/', ReviewCreateView.as_view(), name='add-review'),
    path('movies/<int:movie_id>/reviews/<int:pk>/', ReviewDestroyView.as_view(), name='delete-view'),
]