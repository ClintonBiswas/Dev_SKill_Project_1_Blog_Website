from django import forms
from .models import Blog, Comment

class BlogAddForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'blog_image', 'description',)

class BlogComment(forms.ModelForm):
    # text = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Comment
        fields = ('text',)
       