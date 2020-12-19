from .models import Post, category, Profile,Comment
from django import forms
cat = category.objects.all().values_list('name','name')
categories=[]
for i in cat:
    categories.append(i)
class add_category(forms.ModelForm):
    class Meta:
        model = category
        fields=('__all__')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','category', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.TextInput(attrs={'class':'form-control', 'id':'omari','value':'', 'type':'hidden'}),
            'category': forms.Select(choices=categories, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),      
        }

class commentform(forms.ModelForm):
    class Meta:
        model =Comment
        fields=('name', 'body',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class editpost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }