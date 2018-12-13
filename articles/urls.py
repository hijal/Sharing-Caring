from django.urls import path
from .views import ArticleListView, UpdateViewPage, DetailViewPage, DeleteViewPage, CreateViewPage

urlpatterns =[
    path('', ArticleListView.as_view(), name = 'article_list'),
    path('<int:pk>/edit/', UpdateViewPage.as_view(), name = 'article_edit'),
    path('<int:pk>',DetailViewPage.as_view(), name = 'article_detail'),
    path('<int:pk>/delete/', DeleteViewPage.as_view(), name = 'article_delete'),
    path('new/', CreateViewPage.as_view(), name = 'article_new'),
]