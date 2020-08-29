from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Post

class MainListView(ListView):
    template_name = 'main.html'
    queryset = Post.objects.all()[1:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = Post.objects.first()
        return context

class PostView(DetailView):
    model = Post
    template_name = 'post.html'

class PostCreate(CreateView):
    model = Post
    template_name = 'post_form.html'
    success_url = reverse_lazy('main')
    fields = [ 'post_title', 'post_text', 'image' ]