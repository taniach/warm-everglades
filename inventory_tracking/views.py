from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Category, Product, Transaction
from .forms import CategoryForm
from django.urls import reverse

# Create your views here.
def home(request):
    all_categories = Category.objects.all()

    context = {'all_categories' : all_categories}
    return render(request, 'home.html', context)


def view_category(request, category_id):
    products = Product.objects.filter(categoryID=category_id)
    category = Category.objects.get(pk=category_id)

    context = {'products' : products, 'category' : category}
    return render(request, 'viewCategory.html', context)

def get_category(request, category_id=None):
    if category_id:
        category = Category.objects.get(pk=category_id)
    else:
        category = None

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('home', args=None))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CategoryForm(instance=category)

    return render(request, 'categoryForm.html', {'form': form, 'category_id': category_id})

def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('home', args=None))
