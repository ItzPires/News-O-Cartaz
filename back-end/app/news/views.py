from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from .permissions import IsAdminOrReadOnly

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]
