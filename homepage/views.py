from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView

from blog.models import PostModel
from django.urls import reverse_lazy
from .forms import ContactModelForm


class HomeView(FormView, ListView):
        template_name = 'base.html'
        model = PostModel
        form_class = ContactModelForm

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['post'] = PostModel.objects.all()[:3]
                return context

        def form_valid(self, form):
                self.object = form.save()
                return super(HomeView, self).form_valid(form)

        def get_success_url(self):
                return reverse_lazy('home_view')
