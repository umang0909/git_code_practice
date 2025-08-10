from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from .forms import BookForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def book_list(request):
    logger.info("Book list view was accessed.")
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books' : books})

@csrf_exempt
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'myapp/book_form.html', {'form': form})

@csrf_exempt
def book_update(request,pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'myapp/book_form.html', {'form' : form})

@csrf_exempt
def book_delete(request,pk):
    print("FDgbvdvgf")
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        print("Delete is working")
        book.delete()
        return redirect('book_list')
    return render(request, 'myapp/book_confirm_delete.html', {'book' : book})


