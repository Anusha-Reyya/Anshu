from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # Custom GET method to filter items by price (example)
    @action(detail=False, methods=['get'])
    def expensive_items(self, request):
        expensive_items = Item.objects.filter(price__gte=1000)
        serializer = self.get_serializer(expensive_items, many=True)
        return Response(serializer.data)

    # Custom POST method for bulk creation (example)
    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
