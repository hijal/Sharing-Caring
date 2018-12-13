from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class DetailViewPage(DetailView):
    model = Article
    template_name = 'article_detail.html'
class UpdateViewPage(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'body']
class DeleteViewPage(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class CreateViewPage(CreateView):
    model = Article
    template_name ='article_new.html'
    fields = ['title', 'body', 'author']