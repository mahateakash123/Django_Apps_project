from django.contrib import admin

from BookApp.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher_year', 'price']

admin.site.register(Book, BookAdmin)
