from django.urls import path
from article.views import ArticleCreateView, ArticleDetailView
urlpatterns = [
  path('create', ArticleCreateView.as_view(), name="post_create"),
  path('detail/<int:post_id>/', ArticleDetailView.as_view(), name="post_detail"),
]