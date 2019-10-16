from django.shortcuts import render
from django.views.generic import ListView, View


class HomeView(View):
    template = 'ecommerce/home.html'
