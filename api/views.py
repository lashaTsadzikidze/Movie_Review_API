from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer