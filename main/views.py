from django.views.generic.edit import FormView
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = ContactForm
    success_url = "/"
    
    def form_valid(self, form):
        logger.debug("Form is valid")
        form.send_mail()
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning("Form is invalid: %s", form.errors)
        return super().form_invalid(form)
    
    def post(self, request, *args, **kwargs):
        logger.debug("POST data: %s", request.POST)
        return super().post(request, *args, **kwargs)


# Create your views here.
