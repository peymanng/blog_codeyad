from django.views.generic import TemplateView
from posts.models import Post

class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        slider_posts = Post.objects.all().order_by('-pub_date')[:6]
        context['slider_posts'] = slider_posts
        return context

class AboutUsView(TemplateView):
    template_name = 'about.html'

class ContactUsView(TemplateView):
    template_name = 'contact.html'