from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Product, ProductImage


class HomeView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'ecommerce/home.html'
    paginate_by = 6
