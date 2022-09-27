from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>', views.product_detail, name='product-detail'),
    # path('like/<int:pk>', views.product_like, name='product-like'),
    path('create-product/', views.create_product, name = "create-product"),
    path('dashboard-products', views.dash_products, name = "dash_products"),
    path("update-product/<int:pk>/", views.update_product, name="update-product"),
    path("delete-product/<int:pk>/", views.delete_product, name="delete-product"),
    path('category/<int:pk>', views.category_detail, name="category_detail"),



]