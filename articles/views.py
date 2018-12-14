from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    login_url = 'login'
    template_name = 'article_list.html'

class DetailViewPage(LoginRequiredMixin, DetailView):
    model = Article
    login_url = 'login'
    template_name = 'article_detail.html'
class UpdateViewPage( LoginRequiredMixin, UpdateView):
    model = Article
    login_url = 'login'
    template_name = 'article_edit.html'
    fields = ('title', 'body')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteViewPage(LoginRequiredMixin, DeleteView):
    model = Article
    login_url = 'login'
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CreateViewPage(LoginRequiredMixin,CreateView):
    model = Article
    template_name ='article_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)