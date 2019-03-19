from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Category, Product, Transaction
from .forms import CategoryForm, ProductForm, SearchForm
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


def get_product(request, product_id=None):
    if product_id:
        product = Product.objects.get(pk=product_id)
    else:
        product = None

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('view_category', args=(form.cleaned_data.get('categoryID').id,) ))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm(instance=product)

    return render(request, 'productForm.html', {'form': form, 'product_id': product_id})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    category_id = product.categoryID.id
    product.delete()

    return HttpResponseRedirect(reverse('view_category', args=(category_id,) ))


def search(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(description__icontains=query).distinct()
    else:
        products = []

    context = {'products' : products, 'q' : query}
    return render(request, 'searchProducts.html', context)