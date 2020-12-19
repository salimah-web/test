from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post,category,Profile,Comment
from .forms import PostForm,editpost,add_category,commentform
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name =  'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu=category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))

def article_category(request, cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'article_category.html',{'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

class details(DetailView):
    model = Post
    template_name = 'detail.html'
    def get_context_data(self, *args, **kwargs):
        context= super(details, self).get_context_data(*args, **kwargs)
        stuff= get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes= stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class categoryform(CreateView):
    model = category
    template_name = 'category.html'  
    form_class=add_category

class createview(CreateView):
    model = Post
    template_name = 'create.html'  
    form_class=PostForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class commentview(CreateView):
    model = Comment
    template_name = 'comment.html'  
    form_class= commentform

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    


class update(UpdateView):
    model = Post
    template_name = 'update.html'  
    form_class=editpost
    

class delete(DeleteView):
    model = Post
    template_name = 'delete.html' 
    success_url=reverse_lazy('home')


