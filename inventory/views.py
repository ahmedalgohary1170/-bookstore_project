from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView , CreateView
from .models import Book












class BookList(ListView):
    model=Book



class BookDetail(DetailView):
    model=Book



class BookCreate(CreateView):
    model = Book
    fields = ["author","title","category","description","image","price","stock"]

    template_name = "inventory/book_create.html"
    success_url ="/list"





class BookUpdate(UpdateView):
    model = Book
    fields = ["title","category","description","image","price","stock"]
    template_name = "inventory/book_update.html"
    success_url ="/list"



