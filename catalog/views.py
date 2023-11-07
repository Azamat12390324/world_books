from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView




def index(request):
    text_head = "Bizning saytimizda siz kitoblarni elektron ko'rinishda olishingiz mumkin!"
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects
    num_authors = Author.objects.count()
    context = {"text_head" : text_head, 
               "books" : books, "num_books" : num_books,
               "num_instance" : num_instance,
               "num_instance_available" : num_instance_available,
               "authors" : authors, "num_authors" : num_authors
               }
    return render(request, 'index.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = "books.html"

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "book_detail.html"