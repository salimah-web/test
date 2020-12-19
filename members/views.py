from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView,UpdateView,CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import signupform,edit_form,password_form,update_profile_page,create_profile_form
from django.contrib.auth.views import PasswordChangeView
from theblog.models import Profile
# Create your views here.

class Profile_page(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Profile_page,self).get_context_data(*args, **kwargs)

        page_user=get_object_or_404(Profile, id= self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class create_profile_page(CreateView):
    model = Profile
    template_name = 'registration/create_profile_page.html'
    fields = ['bio','profile_pic','twitter','instagram','facebook']
    #form_class = create_profile_form

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class Edit_profile_page(UpdateView):
    model=Profile
    form_class = update_profile_page
    template_name = 'registration/edit_profile_page.html'
    # fields=['bio','profile_pic','twitter','instagram','facebook']
    success_url = reverse_lazy('home')

class PasswordChangeview(PasswordChangeView):
    form_class = password_form
    template_name = 'registration/password.html'
    success_url = reverse_lazy('login')

class registrationform(generic.CreateView):
    form_class = signupform
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class editform(generic.UpdateView):
    form_class = edit_form
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def log_out(request):
    return render(request, 'logout.html')