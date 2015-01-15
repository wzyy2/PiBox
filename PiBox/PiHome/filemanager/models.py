from django.db import models
from django import forms
from .widgets import CKEditorWidget

class CKEditorField(models.TextField):
  def __init__(self, *args, **kwargs):
    """ arguments config,filemanager_url can be passed here
        for the same use as of CKEditorWidget.
    """
    self.config = kwargs.pop('config', {})
    self.filemanager_url = kwargs.pop('filemanager_url', '')
    super(CKEditorField, self).__init__(*args, **kwargs)

  def formfield(self, **kwargs):
    defaults = {
      'form_class': forms.CharField,
      'widget': CKEditorWidget(config=self.config, filemanager_url=self.filemanager_url)
    }
    defaults.update(kwargs)
    return super(CKEditorField, self).formfield(**defaults)
