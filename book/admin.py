from django.contrib import admin

from .models import Book, Author, BookAuthor, Review

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAuthorAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(Review, ReviewAdmin)
