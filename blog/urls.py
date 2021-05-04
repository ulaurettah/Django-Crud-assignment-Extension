from django.urls import path
from.views import BlogListView, BlogDetailView, BlogUpdateView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='post_about'),
    path('post/int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateview.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detal'),
    path('', BlogListView.as_view(), name='done'),
]