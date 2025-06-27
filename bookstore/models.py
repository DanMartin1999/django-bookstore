from django.db import models
from django.utils import timezone  # Import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=100, default="Unknown")

    class Meta:
        db_table = 'authors'  # Use the new table name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, default="Unknown")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'books'  # Use the new table name

class Video(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, default="Unknown")  # Add default value
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    publisher = models.CharField(max_length=100, default="Unknown")
    release_date = models.DateField(default='1900-01-01')  # Add default value

    class Meta:
        db_table = 'videos'  # Use the new table name

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True, primary_key=True)
    first_name = models.CharField(max_length=50, default="Unknown") 
    last_name = models.CharField(max_length=50, default="Unknown")  # Add default value
    email = models.EmailField(blank=True) 
    
    class Meta:
        db_table = 'students'  # Use the actual table name

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)  # Use 'transaction_id' as the primary key
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.SET_NULL)  # Don't delete book on transaction deletion
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.SET_NULL)  # Don't delete video on transaction deletion
    checkout_date = models.DateField(default=timezone.now)  
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True) # Add return date

    def __str__(self):
        item = self.book.title if self.book else self.video.title
        return f"{item} borrowed by {self.student}"
    
    class Meta:
        db_table = "transactions"

class Resources(models.Model):  # Rename NewModel to a more meaningful name
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "resources"
