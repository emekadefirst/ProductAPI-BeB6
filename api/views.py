from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Category, Image, Product, ImageSerializer, CategorySerializer, ProductSerializer



"""Function Based View (FBV) using rest_framwork decorator 'api_view' """

@api_view(['GET'])
def categories(request):
    cats = Category.objects.all()
    serializer = CategorySerializer(cats, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category(request, id):
    cat = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(cat)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_category(request, id):
    cat = get_object_or_404(Category, id=id)
    cat.delete()
    return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_category(request, id):
    cat = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        title = serializer['title']
        cat.title = title
        cat.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)



"""Class Based View using APIView module from rest_framework"""


class ImageListCreateView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    

class ImageRetrieveUpdateDeleteView(APIView):
    def get_image(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        image = self.get_image(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        image = self.get_image(pk)
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        image = self.get_image(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


"""Generic Class Based View using the generic module from rest_framework"""


class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductUpdateRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'