from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'products': products,
        'category': category,
        'categories': categories
    }
    template = 'shop/product/list.html'
    return render(request, template, context)
