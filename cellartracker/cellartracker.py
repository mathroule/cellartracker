"""Main module."""
import csv
import logging

from io import StringIO

from .client import CellarTrackerClient
from .enum import CellarTrackerFormat, CellarTrackerTable

_LOGGER = logging.getLogger(__name__)


class CellarTracker(object):
    """
    CellarTracker is the class handling the CellarTracker data export.
    """

    def __init__(self, username: None, password: None):
        self.client = CellarTrackerClient(username, password)

    def get_list(self):
        """Get list."""
        return self._get_data(table=CellarTrackerTable.List)

    def get_inventory(self):
        """Get inventory."""
        return self._get_data(table=CellarTrackerTable.Inventory)

    def get_notes(self):
        """Get notes."""
        return self._get_data(table=CellarTrackerTable.Notes)

    def get_private_notes(self):
        """Get private notes data."""
        return self._get_data(table=CellarTrackerTable.PrivateNotes)

    def get_purchase(self):
        """Get purchase data."""
        return self._get_data(table=CellarTrackerTable.Purchase)

    def get_pending(self):
        """Get pending."""
        return self._get_data(table=CellarTrackerTable.Pending)

    def get_consumed(self):
        """Get consumed."""
        return self._get_data(table=CellarTrackerTable.Consumed)

    def get_availability(self):
        """Get availability."""
        return self._get_data(table=CellarTrackerTable.Availability)

    def get_tag(self):
        """Get tag."""
        return self._get_data(table=CellarTrackerTable.Tag)

    def get_pro_review(self):
        """Get pro review."""
        return self._get_data(table=CellarTrackerTable.ProReview)

    def get_bottles(self):
        """Get bottles."""
        return self._get_data(table=CellarTrackerTable.Bottles)

    def get_food_tag(self):
        """Get food tag."""
        return self._get_data(table=CellarTrackerTable.FoodTag)

    def _get_data(self, table: CellarTrackerTable):
        """Get data."""
        return _parse_data(
            self.client.get(table=table, format=CellarTrackerFormat.tab)
        )


def _parse_data(data: str):
    reader = csv.DictReader(StringIO(data), dialect="excel-tab")
    results = []
    for row in reader:
        result = {}
        for key, value in row.items():
            result[key] = value

        results.append(result)

    return results
