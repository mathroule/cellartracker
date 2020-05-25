from .api import CellarTrackerAPI

from .enum import CellarTrackerFormat, DEFAULT_FORMAT, CellarTrackerTable, DEFAULT_TABLE

class CellarTrackerClient(object):

    def __init__(self, username: None, password: None):
        """Initialize the client object."""
        self._api = CellarTrackerAPI()
        self._username = username
        self._password = password

    def get(self, table:CellarTrackerTable=DEFAULT_TABLE, format:CellarTrackerFormat=DEFAULT_FORMAT):
        """Get data."""
        return self._api.execute(params={
            "User": self._username,
            "Password": self._password,
            "Table": table,
            "Format": format,
            "Location": 1
        })
