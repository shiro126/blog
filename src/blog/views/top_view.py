from django.views.generic import TemplateView
from django.utils.functional import cached_property
from blog.models import Entry

class TopView(TemplateView):
    template_name = "blog/top.html"

    @cached_property
    def entries(self):
        return Entry.objects.filter(is_deleted=False).order_by('-post_dt')
