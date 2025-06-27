from django.contrib import admin
from .models import Author, Book, Video, Student, Transaction, Resources

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Video)
admin.site.register(Student)
admin.site.register(Transaction)
admin.site.register(Resources)

