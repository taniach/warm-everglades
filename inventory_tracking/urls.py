from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('viewCategory/<category_id>', views.view_category, name='view_category'),
	path('catergoryForm', views.get_category, name='get_category'),
	path('catergoryForm/<category_id>', views.get_category, name='get_category'),
	path('deleteCategory/<category_id>', views.delete_category, name='delete_category'),
	path('productForm', views.get_product, name='get_product'),
	path('productForm/<product_id>', views.get_product, name='get_product'),
	path('deleteProduct/<product_id>', views.delete_product, name='delete_product'),
	path('search', views.search, name='search'),
]