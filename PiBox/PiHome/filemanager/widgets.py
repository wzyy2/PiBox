from django import forms
from django.utils.safestring import mark_safe

from settings import FILEMANAGER_CKEDITOR_JS

def filemanager_config(url):
  d = {}
  d['filebrowserBrowseUrl'] = url
  d['filebrowserImageBrowseUrl'] = url
  d['filebrowserWidth'] = 800
  d['filebrowserHeight'] = 500
  return d

class CKEditorWidget(forms.Textarea):
  def __init__(self, attrs={}, config = {}, filemanager_url=''):
    """ config : CKEditor config
        filemanager_url : for user to 'browse server'
        In config : toolbar = 'Basic'/'Standard'/'Full'
    """
    default = {
      'toolbar': 'Standard',
      'height': 250,
      'width': 900
    }
    default.update(config)
    if filemanager_url:
      default.update(filemanager_config(filemanager_url))
    self.config = default
    return super(CKEditorWidget, self).__init__(attrs)

  class Media:
    js = (
      FILEMANAGER_CKEDITOR_JS,
    )

  def render(self, name, value, attrs=None):
    rendered = super(CKEditorWidget, self).render(name, value, attrs)
    div = "<div style='height:20px'></div>"
    return rendered+mark_safe(div+
      u"""<script type="text/javascript">
            document.addEventListener('DOMContentLoaded', function() {
              CKEDITOR.replace('%s',%s);
            }, false);
          </script>
      """%(attrs['id'], self.config))

