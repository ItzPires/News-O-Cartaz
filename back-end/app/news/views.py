from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from .permissions import IsAdminOrReadOnly

from sentence_transformers import SentenceTransformer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        data = request.data

        # Get News from DB
        news = News.objects.all()

        # Load pre-trained model
        model = SentenceTransformer("distiluse-base-multilingual-cased-v1")

        # Get sentences
        sentences = [n.title for n in news]
        title = [data['title']]

        # Calculate embeddings
        sentences_embeddings = model.encode(sentences)
        title_embedding = model.encode(title)
        similarities = model.similarity(title_embedding, sentences_embeddings)
        
        # Get indexs of news with similarity > 0.8
        indexes = [i for i, s in enumerate(similarities[0]) if s > 0.8]

        # If there are similar news, return them
        if indexes:
            similar_news = [news[i] for i in indexes]
            #serializer = NewsSerializer(similar_news, many=True)
            #print(serializer.data)
            data['related_news'] = [n.id for n in similar_news]
    
        serializer = NewsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save() # save the news
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)