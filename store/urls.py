from django.urls import path
from .views import view_products, product_page


urlpatterns = [

    path('', view_products, name='products'),
    path('<int:id>', product_page, name='product-page'),

]