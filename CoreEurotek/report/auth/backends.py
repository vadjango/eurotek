import logging

from trench.backends.base import AbstractMessageDispatcher
from trench.responses import DispatchResponse, SuccessfulDispatchResponse, FailedDispatchResponse
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from django.utils.translation import gettext_lazy as _
from trench.settings import TWILIO_VERIFIED_FROM_NUMBER


class TwoFactorMessageDispatcher(AbstractMessageDispatcher):
    _SMS_BODY = _("Your verification code is: ")
    _SUCCESS_DETAILS = _("SMS message with MFA code has been sent.")

    def dispatch_message(self) -> DispatchResponse:
        try:
            client = Client()
            client.messages.create(
                body=self._SMS_BODY + self.create_code(),
                to=self._to.as_e164,
                from_=self._config.get(TWILIO_VERIFIED_FROM_NUMBER),
            )
            return SuccessfulDispatchResponse(details=self._SUCCESS_DETAILS)
        except TwilioRestException as cause:
            logging.error(cause, exc_info=True)
            return FailedDispatchResponse(details=cause.msg)
