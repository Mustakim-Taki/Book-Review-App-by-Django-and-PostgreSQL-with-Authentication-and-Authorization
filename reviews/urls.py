# reviews/urls.py
from django.urls import path
from . import views



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
