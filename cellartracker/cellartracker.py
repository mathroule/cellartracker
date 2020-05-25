"""Main module."""

import logging

from .client import CellarTrackerClient

_LOGGER = logging.getLogger(__name__)

class CellarTracker(object):
    """
    CellarTracker is the class handling the CellarTracker data export.
    """

    def __init__(self, username: None, password: None):
        if username and password:
            self.client = CellarTrackerClient(username, password)
        elif username or password:
            _LOGGER.warning('Either username or password missing, not using authentication.')
