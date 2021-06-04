from django import forms
from django.forms import ClearableFileInput
from Timeline.models import Post

class PostForm(forms.ModelForm):
    content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}),required=True)
    caption = forms.CharField(widget=forms.Textarea(attrs={'class':'file','placeholder':'caption...'}), required=False)

    class Meta:
        model = Post
        fields = ('content','caption')
