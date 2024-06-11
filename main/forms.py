from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_mail(self):
        logger.info("Sending email to customer service")
        
        # Debugging: Print out cleaned data
        logger.debug("Cleaned data: %s", self.cleaned_data)
        
        name = self.cleaned_data.get("name", "Unknown")
        message_content = self.cleaned_data.get("message", "No message provided.")
        message = "From: {0}\n{1}".format(name, message_content)
        
        send_mail(
            "site message",
            message,
            "site@cosmetics.domain",
            ["customerservice@cosmetics.domain"],
            fail_silently=False,
        )
