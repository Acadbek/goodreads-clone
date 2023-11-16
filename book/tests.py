from django.test import TestCase
from django.urls import reverse
from book.models import Book


class BookListTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))
        self.assertContains(response, 'No books found.')

    def test_book_list(self):
        Book.objects.create(
            title='Book1', description='Description1', isbn='123123123')
        Book.objects.create(
            title='Book2', description='Description2', isbn='22222222222')
        Book.objects.create(
            title='Book3', description='Description3', isbn='333333333')

        response = self.client.get(reverse('books:list'))
        books = Book.objects.all()

        for book in books:
            self.assertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(
            title='Book1', description='Description1', isbn='123123123')

        response = self.client.get(
            reverse('books:detail', kwargs={'id': book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)