from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutUsView(TemplateView):
    template_name = 'about.html'

class ContactUsView(TemplateView):
    template_name = 'contact.html'