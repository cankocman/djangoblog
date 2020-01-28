
#from 
## Create your views here.
#def post_detail(request, post_id):
#  pk = post_id
#  post = get_object_or_404(Post, id=pk, draft=False)
#  comments = post.comments.all()
#  form = CommentForm(request.POST or None)
#  context = {
#    'post' : post,
#    'comments' : comments,
#    'form' : form
#  }
#  
#  if request.method =="POST":
#    if form.is_valid():
#      form.instance.post = post
#      form.save()
#      messages.add_message(request, messages.SUCCESS, "Successfully added.")
#      
#      return redirect('post_detail', post_id=post.id)
#  
#  return render(request, 'article/post_detail.html', context)
#
#def homepage(request):
#  queryset = []
#  for post in Post.objects.all():
#    post.content = post.content[:700]
#    queryset.append(post)
#  return render(request, 'article/index.html', {'posts' : queryset})
#
#def create_post(request):
#  form = ArticleForm(data=request.POST or None)
#  if request.method =='POST':
#    if form.is_valid():
#      #header = form.cleaned_data.get()
#      header = form.cleaned_data['header']
#      content = form.cleaned_data['content']
#      liked = form.cleaned_data['liked']
#      draft = form.cleaned_data['draft']
#      post = Post.objects.create(
#        header=header, content=content, liked=liked, draft=draft, owner=request.user
#      )
#      post.save()
#      return HttpResponse('nesne yaratıldı')
#  else:
#    return render(request, 'article/create_post.html', { 'form' : form })
#
#def createPostMF(request):
#  form = ArticleModelForm(request.POST or None)
#  if request.method =='POST':
#    if form.is_valid():
#      form.instance.owner = request.user
#      form.save()
#      return render(request, 'article/post_created.html', { 'form' : form })
#  return render(request, 'article/create_post.html', { 'form' : form })
#
"""

CLASS BASED VIEWS

"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from article.models import Post, Comment, Created
from article.forms import ArticleForm, ArticleModelForm, CommentForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class Homepage(ListView):
  model = Post
  template_name = 'article/index.html'
  queryset = Post.objects.all()
  context_object_name = 'posts'

class ArticleCreateView(CreateView):
    model = Post
    # fields = '__all__'
    form_class = ArticleModelForm
    template_name = "article/create_post.html"
    success_url = reverse_lazy('anasayfa')
    def form_valid(self, form):
      form.instance.owner = self.request.user
      form.save()
      return super().form_valid(form)
from django.shortcuts import reverse
class ArticleDetailView(DetailView, SuccessMessageMixin, FormView):
  model = Post
  template_name = "article/post_detail.html"
  pk_url_kwarg = "post_id"
  context_object_name = "post"  
  form_class = CommentForm
  success_url = reverse_lazy('homepage')
  success_message = "Comment has successfully created."


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post = self.object
    context['comments'] = post.comments.all()
    return context

  def form_valid(self, form):
    self.object = self.model.objects.get(id = self.kwargs["post_id"])
    form.instance.post = self.object
    form.save()
    return super().form_valid(form)