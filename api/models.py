import uuid
from django.utils import timezone
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

class Image(BaseModel):
    image = models.ImageField(upload_to="Product")

class Category(BaseModel):
    title = models.CharField(max_length=155, unique=True)

class Product(BaseModel):
    title = models.CharField(max_length=155, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    images = models.ManyToManyField(Image)

