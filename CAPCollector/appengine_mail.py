"""A Django E-Mail backend for Google App Engine."""

__author__ = "shakusa@google.com (Steve Hakusa)"

import logging

from django.conf import settings
from django.core.mail.backends import base
from django.utils import text
#from google.appengine.api import app_identity
#from google.appengine.api import mail


class EmailBackend(base.BaseEmailBackend):
  """Django email backend for AppEngine's mail API."""

  def send_messages(self, email_messages):
    """Sends one or more EmailMessage objects and returns the number sent.

    Args:
      email_messages: A list of django.core.mail.EmailMessage objects.

    Returns:
      An int indicating the number of successfully sent messages.
    """
    num_sent = 0
    for email in email_messages:
      if self._send(email):
        num_sent += 1
    return num_sent

  def _send(self, email):
    """Send the message using the appengine mail API."""
    try:
      ae_email = self._convert_message(email)
      ae_email.send()
      logging.debug("Sent mail %s to %s", ae_email.subject, ae_email.to)
    except (ValueError, mail.Error) as err:
      logging.warn(err)
      if not self.fail_silently:
        raise
      return False
    return True

  def _convert_message(self, django_email):
    """Convert a Django EmailMessage to an App Engine EmailMessage."""
    return "converted email"    

  def _format_subject(self, subject):
    """Escape CR and LF characters, and limit length.

    RFC 2822"s hard limit is 998 characters per line. So, minus "Subject: "
    the actual subject must be no longer than 989 characters.

    Args:
      subject: A string containing the original subject.

    Returns:
      A string containing the formatted subject.
    """
    formatted_subject = subject.replace("\n", "\\n").replace("\r", "\\r")
    truncator = text.Truncator(formatted_subject)
    formatted_subject = truncator.chars(985)
    return formatted_subject
