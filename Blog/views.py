from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

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

	def get_success_url(self):
		return reverse('post_detail', kwargs={'pk': self.object.pk})

"""
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('Blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
"""

