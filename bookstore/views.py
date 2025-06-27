#from django.shortcuts import render
#from .models import Author

#def index(request):
#    authors = Author.objects.all()
#    context = {
#        'authors': authors,
#    }
#    return render(request, 'bookstore/index.html', context)

# Dummy function to prevent errors in urls.py
#def new_model_list(request):
#    return render(request, 'bookstore/new_model_list.html')
#
#from django.shortcuts import render
#from .models import Author, Book, Video, Student, Transaction, NewModel

#from django.shortcuts import render
#from .models import Author, Book, NewModel  # Make sure your models are imported correctly

#def index(request):
#    authors = Author.objects.all()  # Query the database for authors
#    books = Book.objects.all()     # Query the database for books

#    print("Authors:", authors)     # Print the results for debugging
#    print("Books:", books)         

#    return render(request, 'index.html', {'authors': authors, 'books': books})

from django.shortcuts import render
from .models import Author, Book, Video, Student, Transaction

def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    videos = Video.objects.all()
    students = Student.objects.all()
    transactions = Transaction.objects.all()

    # Pass all data to the template
    return render(request, 'index.html', {
        'authors': authors,
        'books': books,
        'videos': videos,
        'students': students,
        'transactions': transactions,
    })




#def index(request):
#    authors = Author.objects.all()
#    books = Book.objects.all()
#    videos = Video.objects.all()
#    students = Student.objects.all()
#    transactions = Transaction.objects.all()
#   return render(request, 'index.html', {'authors': authors, 'books': books, 'videos': videos, 'students': students, 'transactions': transactions})

#def new_model_list(request):
#    new_models = NewModel.objects.all()  # Fetch data from the database
#    return render(request, 'new_model_list.html', {'new_models': new_models})  # Render a template

#from django.shortcuts import render
#from .models import Author, Book  # Assuming you have these models

#def index(request):
#    authors = Author.objects.all()
#    books = Book.objects.all()
#    return render(request, 'index.html', {'authors': authors, 'books': books})
