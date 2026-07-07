"""Main module for CellarTracker read API.

Provides the CellarTracker class for exporting data from CellarTracker
via the xlquery.asp export endpoint.
"""

import csv
import logging
from io import StringIO
from typing import Any, Optional

from .client import CellarTrackerClient
from .enum import CellarTrackerFormat, CellarTrackerTable

_LOGGER = logging.getLogger(__name__)


class CellarTracker(object):
    """CellarTracker data export client.

    Provides read-only access to CellarTracker data via the official
    export endpoint. Each method returns a list of dicts with the
    fields available for that table.

    Args:
        username: CellarTracker handle (not email)
        password: CellarTracker account password

    Example:
        >>> from cellartracker import cellartracker
        >>> ct = cellartracker.CellarTracker('myhandle', 'mypassword')
        >>> inventory = ct.get_inventory()
        >>> len(inventory)
        82
        >>> inventory[0]['Wine']
        'Château Lafite Rothschild'
    """

    def __init__(self, username: str, password: str):
        self.client = CellarTrackerClient(username, password)

    def get_list(self) -> list[dict[str, Any]]:
        """Get your current wine list with stock levels.

        Returns a list of wines currently in your cellar with
        quantity, location, and size information.

        Keys include: iWine, Wine, Vintage, Location, Quantity, Size
        """
        return self._get_data(table=CellarTrackerTable.List)

    def get_inventory(self) -> list[dict[str, Any]]:
        """Get full inventory with valuations and purchase details.

        The most comprehensive table. Returns all bottles with
        pricing, valuation, store, purchase date, tasting scores,
        and community stats.

        Keys include: iWine, Wine, Vintage, Location, Price, Valuation,
        StoreName, PurchaseDate, Size, Varietal, Producer, Country,
        CT (community score), and many more.
        """
        return self._get_data(table=CellarTrackerTable.Inventory)

    def get_notes(self) -> list[dict[str, Any]]:
        """Get public tasting notes.

        Returns community tasting notes with ratings.
        Keys include: iNote, iWine, Vintage, Wine, Note, Rating, Date
        """
        return self._get_data(table=CellarTrackerTable.Notes)

    def get_private_notes(self) -> list[dict[str, Any]]:
        """Get private tasting notes (your notes only)."""
        return self._get_data(table=CellarTrackerTable.PrivateNotes)

    def get_purchase(self) -> list[dict[str, Any]]:
        """Get purchase history.

        Returns all purchase records with store, price, quantity,
        and delivery status.

        Keys include: iWine, iPurchase, PurchaseDate, StoreName,
        Price, Quantity, Remaining, Size, Wine, Vintage
        """
        return self._get_data(table=CellarTrackerTable.Purchase)

    def get_pending(self) -> list[dict[str, Any]]:
        """Get pending deliveries (ordered but not yet received)."""
        return self._get_data(table=CellarTrackerTable.Pending)

    def get_consumed(self) -> list[dict[str, Any]]:
        """Get consumption history (bottles marked as consumed/drunk).

        Keys include: iConsumed, iWine, Vintage, Wine, Consumed, Type
        """
        return self._get_data(table=CellarTrackerTable.Consumed)

    def get_availability(self) -> list[dict[str, Any]]:
        """Get drinkability report with drinking windows.

        Keys include: iWine, Wine, Vintage, Available, BeginConsume,
        EndConsume, Type, Color, Varietal
        """
        return self._get_data(table=CellarTrackerTable.Availability)

    def get_tag(self) -> list[dict[str, Any]]:
        """Get wish list / tagged wines."""
        return self._get_data(table=CellarTrackerTable.Tag)

    def get_pro_review(self) -> list[dict[str, Any]]:
        """Get professional critic reviews (WA, WS, etc.)."""
        return self._get_data(table=CellarTrackerTable.ProReview)

    def get_bottles(self) -> list[dict[str, Any]]:
        """Get individual bottle records with state tracking.

        Returns every bottle individually (vs aggregated by wine).
        Keys include: BottleState, Barcode, iWine, Vintage, Wine,
        Location, Size

        Useful for tracking individual bottle movement and states.
        """
        return self._get_data(table=CellarTrackerTable.Bottles)

    def get_food_tag(self) -> list[dict[str, Any]]:
        """Get food pairing tags."""
        return self._get_data(table=CellarTrackerTable.FoodTag)

    def _get_data(self, table: CellarTrackerTable) -> list[dict[str, Any]]:
        """Fetch and parse tab-separated data from CellarTracker.

        Args:
            table: The table to export

        Returns:
            List of dicts with column names as keys
        """
        return _parse_data(
            self.client.get(table=table, format=CellarTrackerFormat.tab)
        )


def _parse_data(data: str) -> list[dict[str, str]]:
    """Parse tab-separated data from CellarTracker.

    Args:
        data: Raw tab-separated string from the export API

    Returns:
        List of dicts with header columns as keys
    """
    reader = csv.DictReader(StringIO(data), dialect="excel-tab")
    results = []
    for row in reader:
        result = {}
        for key, value in row.items():
            result[key] = value
        results.append(result)
    return results
