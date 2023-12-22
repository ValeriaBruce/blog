from django.forms import ModelForm
from .models import Post
class postForm(ModelForm):
    class Meta :
        model = Post
        fields= ['title','brief','content','category']