from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactModelForm


class HomeView(FormView):
        template_name = 'base.html'
        form_class = ContactModelForm

        def form_valid(self, form):
                self.object = form.save()
                return super(HomeView, self).form_valid(form)

        def get_success_url(self):
                return reverse_lazy('home:home_view')