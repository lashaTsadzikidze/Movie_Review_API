from rest_framework import generics
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import permissions
from rest_framework.exceptions import NotFound

# Create your views here.
class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        movie = Movie.objects.get(pk=self.kwargs['movie_id'])
        serializer.save(user=self.request.user, movie=movie)

class ReviewDestroyView(generics.DestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Review.objects.filter(pk=pk)