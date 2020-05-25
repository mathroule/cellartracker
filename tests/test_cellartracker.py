#!/usr/bin/env python

"""Tests for `cellartracker` package."""


import unittest
import requests
import requests_mock

from cellartracker.cellartracker import CellarTracker
from cellartracker.errors import AuthenticationError, CannotConnect


class TestCellartracker(unittest.TestCase):
    """Tests for `cellartracker` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @requests_mock.Mocker()
    def test_get_list(self, m):
        """Test get list."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=List&Format=tab&Location=1"
        file = open("./tests/fixtures/list.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_list()
        self.assertEqual([
            {'iWine': '684674', 'WineBarcode': 'W0684674_750ml', 'Quantity': '0', 'Pending': '3', 'Location': '', 'Bin': '', 'Size': '750ml', 'Price': '0', 'Valuation': '', 'MyValue': '0', 'WBValue': '', 'CTValue': '', 'MenuPrice': '0', 'Currency': 'EUR', 'Vintage': '2008', 'Wine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Libournais', 'Appellation': 'Pomerol', 'Producer': 'Pétrus', 'SortProducer': 'Pétrus', 'Type': 'Red', 'Varietal': 'Red Bordeaux Blend', 'MasterVarietal': 'Red Bordeaux Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '18-19+', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '96.625', 'MY': '', 'BeginConsume': '2018', 'EndConsume': '2046', 'UPC': ''},
            {'iWine': '118542', 'WineBarcode': 'W0118542_750ml', 'Quantity': '2', 'Pending': '0', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Price': '3500', 'Valuation': '3500', 'MyValue': '0', 'WBValue': '', 'CTValue': '', 'MenuPrice': '0', 'Currency': 'EUR', 'Vintage': '2003', 'Wine': 'Domaine de la Romanée-Conti La Tâche', 'Locale': 'France, Burgundy, Côte de Nuits, La Tâche Grand Cru', 'Country': 'France', 'Region': 'Burgundy', 'SubRegion': 'Côte de Nuits', 'Appellation': 'La Tâche Grand Cru', 'Producer': 'Domaine de la Romanée-Conti', 'SortProducer': 'Romanée-Conti, Domaine de la ', 'Type': 'Red', 'Varietal': 'Pinot Noir', 'MasterVarietal': 'Pinot Noir', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '94.4117647058823', 'MY': '', 'BeginConsume': '2013', 'EndConsume': '2029', 'UPC': ''},
            {'iWine': '1367113', 'WineBarcode': 'W1367113_750ml', 'Quantity': '6', 'Pending': '0', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Price': '230', 'Valuation': '230', 'MyValue': '0', 'WBValue': '', 'CTValue': '', 'MenuPrice': '0', 'Currency': 'EUR', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'Producer': "Château d'Yquem", 'SortProducer': "Yquem, Château d'", 'Type': 'White - Sweet/Dessert', 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '19-20', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '95.9782608695652', 'MY': '', 'BeginConsume': '2019', 'EndConsume': '2054', 'UPC': '810910020858'}
            ], data)

    @requests_mock.Mocker()
    def test_get_list_with_empty(self, m):
        """Test get list with empty."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=List&Format=tab&Location=1"
        file = open("./tests/fixtures/list_empty.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_list()
        self.assertEqual([], data)

    @requests_mock.Mocker()
    def test_get_list_with_invalid_credentials(self, m):
        """Test get list with invalid credentials."""
        url = "https://www.cellartracker.com/xlquery.asp?User=invalid-username&Password=invalid-password&Table=List&Format=tab&Location=1"
        file = open("./tests/fixtures/not_logged.html", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="invalid-username", password="invalid-password")
        with self.assertRaises(AuthenticationError):
            cellartracker.get_list()

    @requests_mock.Mocker()
    def test_get_list_with_error(self, m):
        """Test get list with error."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=List&Format=tab&Location=1"
        m.register_uri("GET", url, exc=requests.exceptions.ConnectTimeout)

        cellartracker = CellarTracker(username="test-username", password="test-password")
        with self.assertRaises(CannotConnect):
            cellartracker.get_list()
