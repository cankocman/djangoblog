from django import forms
from article.models import Post, Comment

class ArticleForm(forms.Form):
  header = forms.CharField(required=True)
  content = forms.CharField(widget=forms.Textarea)
  liked = forms.IntegerField(required=True)
  draft = forms.BooleanField(required=True)

class ArticleModelForm(forms.ModelForm):
  class Meta:
    model = Post
    #Imports All Fields
    #fields = '__all__'
    exclude = ['owner','image']
  
  def clean_header(self):
    header = self.cleaned_data.get('header')
    if Post.objects.filter(header=header).exists():
      raise forms.ValidationError("An article with this header already exists.")
    return header
  def clean_content(self):
    if len(self.cleaned_data.get("content")) < 50:
      raise forms.ValidationError("Content must include 50 characters at least.")
    return self.cleaned_data.get("content")

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['post']