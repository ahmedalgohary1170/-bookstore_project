from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Book







class BookList(ListView):
    model=Book



class BookDetail(DetailView):
    model=Book