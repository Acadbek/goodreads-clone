from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from book.models import Book


def truncate_text(text, max_length=10):
    if len(text) > max_length:
        return text[:4] + '...'
    else:
        return text


class BooksView(LoginRequiredMixin, View):
    def get(self, request):
        books = Book.objects.all()

        return render(request, 'book/list.html', {'books': books})


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, 'book/detail.html', {'book': book})
