"""Enum for CellarTracker."""

from enum import Enum


class CellarTrackerFormat(Enum):
    html = "html"
    xml = "xml"
    tab = "tab"
    csv = "csv"


class CellarTrackerTable(Enum):
    List = "List"
    Inventory = "Inventory"
    Notes = "Notes"
    PrivateNotes = "PrivateNotes"
    Purchase = "Purchase"
    Pending = "Pending"
    Consumed = "Consumed"
    Availability = "Availability"
    Tag = "Tag"
    ProReview = "ProReview"
    Bottles = "Bottles"
    FoodTag = "FoodTag"
