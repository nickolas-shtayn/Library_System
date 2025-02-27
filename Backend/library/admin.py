from django.contrib import admin
from ..backend.models import Book, Borrower, Transaction

admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(Transaction)
