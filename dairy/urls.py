from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = (
    path('', ArticleListView.as_view(), name='article-list'),
    path('task/create/', ArticleCreateView.as_view(), name='article-create'),
    path('dairy/<int:pk>/detail', ArticleDetailView.as_view(), name='article-detail'),
    path('task/<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
    #path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
)
