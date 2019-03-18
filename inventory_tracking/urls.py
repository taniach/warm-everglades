from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('viewCategory/<category_id>', views.view_category, name='view_category'),
	path('catergoryForm', views.get_category, name='get_category'),
	path('catergoryForm/<category_id>', views.get_category, name='get_category'),
	path('deleteCategory/<category_id>', views.delete_category, name='delete_category'),
]