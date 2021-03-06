from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

from .forms import PostForm
from .models import Post

class BaseView(TemplateView):
	template_name = 'blog/base.html'

class PostListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = '/'

class PostUpdateView(UpdateView):
	fields = ['title', 'text']
	model = Post
	template_name = 'blog/post_edit.html'

	def get_success_url(self):
		return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostCreateView(CreateView):
	template_name = 'blog/post_edit.html'
	model = Post
	fields = ['title', 'text']

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.published_date = timezone.now()
		return super(PostCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse('post_detail', kwargs={'pk': self.object.pk})

