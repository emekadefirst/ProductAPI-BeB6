from rest_framework import serializers
from .models import Category, Image, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source="category", write_only=True)
    image_ids = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), source="images", write_only=True)
    category = CategorySerializer(read_only=True)
    images = ImageSerializer(read_only=True)
    class Meta:
        model = Product
        fields = [
            "title",
            "category",
            "category_id",
            "image_ids",
            "description",
            "images",
            "price",
            "quantity"
        ]