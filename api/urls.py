from django.urls import path
from .views import MovieListView, MovieDetail

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]