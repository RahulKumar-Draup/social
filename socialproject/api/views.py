from rest_framework.response import Response
from rest_framework.decorators import api_view
from socialproject.mainapp import models
from .serializers import GroupSerializer, PostSerializer, CommentSerializer



@api_view(['GET'])
def overview(request):
    api_urls = {
        'Create': 'add_data',
        'Update': 'update_data/<int:pk/>',
        'Delete': 'delete_data/<int:pk/>',
    }
    return Response(api_urls)


@api_view(['POST'])
def add_data(request):
    pass


@api_view(['GET'])
def get_data(request, pk):
    pass


@api_view(['UPDATE'])
def update_dataa(request, pk):
    pass


@api_view(['DELETE'])
def delete_data(request, pk):
    pass
