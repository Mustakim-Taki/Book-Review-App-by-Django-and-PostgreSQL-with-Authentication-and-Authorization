# reviews/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
#from .views import BookViewSet, ReviewViewSet

from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    ReviewListCreateView,
    ReviewRetrieveUpdateDestroyView,
)




# router = DefaultRouter()
# router.register(r'books', BookViewSet)  # /api/books/
# router.register(r'reviews', ReviewViewSet) 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account, name='account'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('review/add/<int:book_id>/', views.add_review, name='add_review'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('review/add/<int:book_id>/', views.add_review, name='add_review'),


]


urlpatterns += [
   
    # Admin-specific views
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),

    # Review management
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    # Existing URLs...
]

urlpatterns += [ 
    path('book/add/', views.add_book, name='add_book'),

]

urlpatterns += [
    # Books API
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),

    # Reviews API
    path('api/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-retrieve-update-destroy'),
]
# urlpatterns += [
#     path('api/', include(router.urls)),  # API endpoints
#     # Add your existing frontend routes here
# ]
