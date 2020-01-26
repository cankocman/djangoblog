from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from article.models import Post, Comment
from article.forms import ArticleForm
from article.forms import ArticleModelForm
# Create your views here.
def post_detail(request, post_id):
  pk = post_id
  #try:
  #  post = Post.objects.get(id=pk)
  #except Post.DoesNotExist:
  #  return HttpResponse("Sayfa bulunamadı.")
  post = get_object_or_404(Post, id=pk, draft=False)
  comments = post.comments.all()
  context = {
    'post' : post,
    'comments' : comments
  }
  return render(request, 'article/post_detail.html', context)

def homepage(request):
  queryset = []
  for post in Post.objects.all():
    post.content = post.content[:700]
    queryset.append(post)
  return render(request, 'article/index.html', {'posts' : queryset})

def create_post(request):
  form = ArticleForm(data=request.POST or None)
  if request.method =='POST':
    if form.is_valid():
      #header = form.cleaned_data.get()
      header = form.cleaned_data['header']
      content = form.cleaned_data['content']
      liked = form.cleaned_data['liked']
      draft = form.cleaned_data['draft']
      post = Post.objects.create(
        header=header, content=content, liked=liked, draft=draft, owner=request.user
      )
      post.save()
      return HttpResponse('nesne yaratıldı')
  else:
    return render(request, 'article/create_post.html', { 'form' : form })

def createPostMF(request):
  form = ArticleModelForm(request.POST or None)
  if request.method =='POST':
    if form.is_valid():
      form.instance.owner = request.user
      form.save()
      return HttpResponse('nesne yaratıldı.')
  return render(request, 'article/create_post.html', { 'form' : form })    