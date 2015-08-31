from django.conf.urls import url

from .views import BaseView, PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView

urlpatterns = [
	url(r'^$', PostListView.as_view(), name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post_detail'),
	url(r'^post/new/$', PostCreateView.as_view(), name="post_new"),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', PostUpdateView.as_view(), name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/remove/$', PostDeleteView.as_view(), name="post_remove"),
]