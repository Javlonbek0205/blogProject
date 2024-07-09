from django.urls import path
from .views import BlogListView, BlogDetailView, BlogPostNewView, BlogPostEditView, BlogDelateView

urlpatterns = [
  path('post/<int:pk>/delate', BlogDelateView.as_view(), name = 'delate_post'),
  path('post/<int:pk>/edit', BlogPostEditView.as_view(), name='post_edit'),
  path('/post/new/', BlogPostNewView.as_view(), name= 'new_post' ),
  path('',BlogListView.as_view(), name= 'home'),
  path('post/<int:pk>/', BlogDetailView.as_view(), name= 'post_detail')


]