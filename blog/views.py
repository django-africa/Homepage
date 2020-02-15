
from __future__ import absolute_import
from django.views import generic
from .forms  import CkEditorForm
from django.views.generic import DetailView
from .models import PostModel

try:
    from django.urls import reverse_lazy
except ImportError:  # Django < 2.0
    from django.core.urlresolvers import reverse_lazy


class CkEditorFormView(generic.FormView):
    form_class = CkEditorForm
    template_name = 'form.html'

    def form_valid(self, form):
            self.object = form.save()
            return super(CkEditorFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home_view')

ckeditor_form_view = CkEditorFormView.as_view()

class PostDetailView (DetailView):
        template_name = 'detail.html'
        model = PostModel
        pk_url_kwarg = 'pk' 
        query_pk_and_slug = True
        slug_url_kwarg = 'slug'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['blog'] = PostModel.objects.get(id=self.kwargs['pk'])
            return context