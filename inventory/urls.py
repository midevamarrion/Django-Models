from django.urls import path
from .views import product_upload_view
from .views import products_list
from .views import product_detail
from .views import product_update_view


urlpatterns= [
    path("products/upload/", product_upload_view ,name="product_upload_view"),
    path("products/list" , products_list , name="products_list"),
    path("products/<int:id>/",product_detail,name="product_detail"),
    path("products/edit/<int:id>",product_update_view,name="product_update"),
]
