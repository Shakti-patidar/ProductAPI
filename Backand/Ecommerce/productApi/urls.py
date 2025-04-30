from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.create_product, name='product'),
   # path('products/<int:pk>', views.delete_product, name='delete_product'),
    path('products/<int:pk>', views.modify_product, name='modify_product'),
    path('add-product-page/', views.add_product_page, name='add_product_page'),
    path('product-list/', views.product_list_page, name='product_list_page'),

]
