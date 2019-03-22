from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Category, Product
from .forms import CategoryForm, ProductForm, SearchForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    all_products = Product.objects.filter(user=request.user).order_by('quantity')

    context = {'all_products' : all_products}
    return render(request, 'home.html', context)


@login_required
def view_all_categories(request):
    all_categories = Category.objects.filter(user=request.user)

    context = {'all_categories' : all_categories}
    return render(request, 'categories.html', context)


@login_required
def view_category(request, category_id):
    products = Product.objects.filter(user=request.user, categoryID=category_id)
    category = Category.objects.filter(user=request.user).get(pk=category_id)

    context = {'products' : products, 'category' : category}
    return render(request, 'viewCategory.html', context)


# For add/edit category
@login_required
def get_category(request, category_id=None):
    if category_id:
        category = Category.objects.filter(user=request.user).get(pk=category_id)
    else:
        category = None

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.user = request.user
            new_category.save()

            return HttpResponseRedirect(reverse('categories', args=None))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CategoryForm(instance=category)

    return render(request, 'categoryForm.html', {'form': form, 'category_id': category_id})


@login_required
def delete_category(request, category_id):
    category = Category.objects.filter(user=request.user).get(pk=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('categories', args=None))


# For add/edit product
@login_required
def get_product(request, product_id=None):
    if product_id:
        product = Product.objects.filter(user=request.user).get(pk=product_id)
    else:
        product = None

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()

            #return HttpResponseRedirect(reverse('view_category', args=(form.cleaned_data.get('categoryID').id,) ))
            return HttpResponseRedirect(reverse('home', args=None))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm(instance=product)

    return render(request, 'productForm.html', {'form': form, 'product_id': product_id})


@login_required
def delete_product(request, product_id):
    product = Product.objects.filter(user=request.user).get(pk=product_id)
    category_id = product.categoryID.id
    product.delete()

    #return HttpResponseRedirect(reverse('view_category', args=(category_id,) ))
    return HttpResponseRedirect(reverse('home', args=None))


@login_required
def search(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(user=request.user, description__icontains=query).distinct()
    else:
        products = []

    context = {'products' : products, 'q' : query}
    return render(request, 'searchProducts.html', context)