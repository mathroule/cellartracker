import logging
import requests

from .const import BASE_URL, NOT_LOGGED_REPONSE
from .errors import AuthenticationError, CannotConnect

_LOGGER = logging.getLogger(__name__)


class CellarTrackerAPI(object):

    def __init__(self):
        """Initialize the client object."""
        self._data = {}

    def execute(self, url=BASE_URL, params={}):
        """Execute a request."""
        try:
            _LOGGER.info("Connecting to %s", url)

            reponse = requests.get(url, params)

            if reponse.text.__contains__(NOT_LOGGED_REPONSE):
                _LOGGER.error("Credentials for CellarTracker are not valid")
                raise AuthenticationError

            _LOGGER.info("Successfully connected to %s", url)
            return reponse.text
        except requests.exceptions.RequestException:
            _LOGGER.error("Failed to connected to %s", url)
            raise CannotConnect
