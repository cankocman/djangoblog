from django import forms
from article.models import Post
class ArticleForm(forms.Form):
  header = forms.CharField(required=True)
  content = forms.CharField(widget=forms.Textarea)
  liked = forms.IntegerField(required=True)
  draft = forms.BooleanField(required=True)

class ArticleModelForm(forms.ModelForm):
  class Meta:
    model = Post
    #All Fields
    #fields = '__all__'
    exclude = ['owner','image']