from .api import CellarTrackerAPI
from .enum import CellarTrackerFormat, CellarTrackerTable


class CellarTrackerClient(object):

    def __init__(self, username: str, password: str):
        """Initialize the client object.

        Args:
            username: CellarTracker handle
            password: CellarTracker account password
        """
        self._api = CellarTrackerAPI()
        self._username = username
        self._password = password

    def get(self, table: CellarTrackerTable, format: CellarTrackerFormat):
        """Get data."""
        return self._api.execute(params={
            "User": self._username,
            "Password": self._password,
            "Table": table.value,
            "Format": format.value,
            "Location": 1
        })
