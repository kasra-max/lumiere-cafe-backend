from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, MenuItem
from .serializers import MenuItemSerializer, CategorySerializer

class MenuItemListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.filter(is_active=True)
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset

@api_view(['GET'])
def featured_items(request):
    items = MenuItem.objects.filter(is_featured=True, is_active=True)[:4]
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)