from django.shortcuts import render
from .models import Category, Product, Transaction

# Create your views here.
def home(request):
	all_categories = Category.objects.all()

	context = {'all_categories' : all_categories}
	return render(request, 'home.html', context)