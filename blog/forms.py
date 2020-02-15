from __future__ import absolute_import

from django.forms import ModelForm, Textarea, TextInput
from .models import PostModel

from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField


class CkEditorForm(ModelForm):
    # ckeditor_upload_example = RichTextUploadingFormField(config_name="my-custom-toolbar")
    class Meta:
        model = PostModel
        exclude = ['pub_date', 'slug']
        widgets = {
            'title': TextInput(attrs={"class" : "text-black"}),
            'content': Textarea(attrs={'cols': 80, 'rows': 10, 'class': "text-black"}),
        }
    