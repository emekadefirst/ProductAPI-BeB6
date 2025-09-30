from django.urls import path
from .views import (
    categories,
    category,
    create_category,
    update_category,
    delete_category,
    ImageListCreateView,
    ImageRetrieveUpdateDeleteView,
    ProductCreateListView,
    ProductUpdateRetrieveDeleteView,
)

urlpatterns = [
    # Category URLs (Function-based views)
    path("categories/", categories, name="categories"),
    path("categories/<uuid:id>/", category, name="category"),
    path("categories/create/", create_category, name="create-category"),
    path("categories/<uuid:id>/update/", update_category, name="update-category"),
    path("categories/<uuid:id>/delete/", delete_category, name="delete-category"),

    # Image URLs (Class-based APIViews)
    path("images/", ImageListCreateView.as_view(), name="image-list-create"),
    path("images/<uuid:pk>/", ImageRetrieveUpdateDeleteView.as_view(), name="image-detail"),

    # Product URLs (Generic Class-based views)
    path("products/", ProductCreateListView.as_view(), name="product-list-create"),
    path("products/<uuid:id>/", ProductUpdateRetrieveDeleteView.as_view(), name="product-detail"),
]
