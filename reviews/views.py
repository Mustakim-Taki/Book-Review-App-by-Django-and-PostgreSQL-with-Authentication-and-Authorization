from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required 
from .models import Review 
from .forms import ReviewForm 
from .models import Book
from django.http import Http404 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BookForm
# Create your views here.


# Registration view

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'reviews/login.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')


# Account page view

@login_required
def account(request):
    reviews = Review.objects.filter(user=request.user)  # User-specific reviews
    books = Book.objects.all()  # All books, for admin and review selection

    # If the user is an admin, fetch all reviews
    all_reviews = Review.objects.all() if request.user.is_staff else None

    return render(request, 'reviews/account.html', {
        'reviews': reviews,
        'books': books,
        'all_reviews': all_reviews,  # Pass all reviews for admin actions
    })


def home(request):
    books = Book.objects.all()
    reviews = Review.objects.all()
    return render(request, 'reviews/home.html', {'books': books, 'reviews': reviews})



@staff_member_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')  # Redirect to the account page
    else:
        form = BookForm()
    return render(request, 'reviews/add_book.html', {'form': form})



@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Allow admins to delete any review
    if request.user.is_staff or request.user == review.user:
        review.delete()
        return redirect('account')
    else:
        raise Http404("You are not authorized to delete this review.")






@login_required
def edit_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.user != review.user:
        return redirect('home')  # Prevent other users from editing

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})




def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()
                return redirect('book_detail', book_id=book.id)
        else:
            return redirect('login')  # Redirect to login if not authenticated
    else:
        form = ReviewForm()
    return render(request, 'reviews/book_detail.html', {'book': book, 'form': form})



@staff_member_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('account')  # Redirect to the account page


@staff_member_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = BookForm(instance=book)

    return render(request, 'reviews/edit_book.html', {'form': form, 'book': book})

@staff_member_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('account')



@login_required
def add_review(request, book_id):
    # Fetch the book by ID
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save the review but don't commit yet
            review = form.save(commit=False)
            review.user = request.user  # Set the current user
            review.book = book  # Associate the review with the book
            review.save()  # Save the review
            return redirect('home')  # Redirect to the home page after saving the review
    else:
        form = ReviewForm()  # Empty form for GET request

    return render(request, 'reviews/add_review.html', {'form': form, 'book': book})


