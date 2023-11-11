from django.urls import path
from catalog import views
# from catalog.views import BookListView



urlpatterns = [
    path("", views.index, name='index'),
    path("books/", views.BookListView.as_view(), name="books"),
    path("<int:pk>/books/", views.BookDetailView.as_view(), name="book-detail"),
    path("authors/", views.AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]