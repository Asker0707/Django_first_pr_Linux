from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwnerOrReadOnly
from filters import AdvertisementFilter
from django_filters import rest_framework as filters


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_class = AdvertisementFilter
    filter_backends = (filters.DjangoFilterBackend,)
    ordering_fields = ['created_at', 'updated_at']
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        
        
    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    