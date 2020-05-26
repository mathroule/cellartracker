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
            {'iWine': '118542', 'WineBarcode': 'W0118542_750ml', 'Quantity': '1', 'Pending': '0', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Price': '3500', 'Valuation': '3500', 'MyValue': '0', 'WBValue': '', 'CTValue': '', 'MenuPrice': '0', 'Currency': 'EUR', 'Vintage': '2003', 'Wine': 'Domaine de la Romanée-Conti La Tâche', 'Locale': 'France, Burgundy, Côte de Nuits, La Tâche Grand Cru', 'Country': 'France', 'Region': 'Burgundy', 'SubRegion': 'Côte de Nuits', 'Appellation': 'La Tâche Grand Cru', 'Producer': 'Domaine de la Romanée-Conti', 'SortProducer': 'Romanée-Conti, Domaine de la ', 'Type': 'Red', 'Varietal': 'Pinot Noir', 'MasterVarietal': 'Pinot Noir', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '94.4117647058823', 'MY': '', 'BeginConsume': '2013', 'EndConsume': '2029', 'UPC': ''},
            {'iWine': '1367113', 'WineBarcode': 'W1367113_750ml', 'Quantity': '5', 'Pending': '0', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Price': '230', 'Valuation': '230', 'MyValue': '0', 'WBValue': '', 'CTValue': '', 'MenuPrice': '0', 'Currency': 'EUR', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'Producer': "Château d'Yquem", 'SortProducer': "Yquem, Château d'", 'Type': 'White - Sweet/Dessert', 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '19-20', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '95.9782608695652', 'MY': '', 'BeginConsume': '2019', 'EndConsume': '2054', 'UPC': '810910020858'}
            ], data)

    @requests_mock.Mocker()
    def test_get_list_with_empty_result(self, m):
        """Test get list with empty result."""
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

    @requests_mock.Mocker()
    def test_get_inventory(self, m):
        """Test get inventory."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Inventory&Format=tab&Location=1"
        file = open("./tests/fixtures/inventory.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_inventory()
        self.assertEqual([
            {'iWine': '684674', 'Barcode': '0129197314', 'Location': '(pending)', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '0', 'Price': '0', 'NativePrice': '0', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '5/25/2020', 'BottleNote': '', 'Vintage': '2008', 'Wine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Libournais', 'Appellation': 'Pomerol', 'Producer': 'Pétrus', 'SortProducer': 'Pétrus', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Varietal': 'Red Bordeaux Blend', 'MasterVarietal': 'Red Bordeaux Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '18-19+', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '96.625', 'CNotes': '9', 'MY': '', 'PNotes': '', 'BeginConsume': '2018', 'EndConsume': '2046'},
            {'iWine': '684674', 'Barcode': '0129197315', 'Location': '(pending)', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '0', 'Price': '0', 'NativePrice': '0', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '5/25/2020', 'BottleNote': '', 'Vintage': '2008', 'Wine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Libournais', 'Appellation': 'Pomerol', 'Producer': 'Pétrus', 'SortProducer': 'Pétrus', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Varietal': 'Red Bordeaux Blend', 'MasterVarietal': 'Red Bordeaux Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '18-19+', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '96.625', 'CNotes': '9', 'MY': '', 'PNotes': '', 'BeginConsume': '2018', 'EndConsume': '2046'},
            {'iWine': '684674', 'Barcode': '0129197316', 'Location': '(pending)', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '0', 'Price': '0', 'NativePrice': '0', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '5/25/2020', 'BottleNote': '', 'Vintage': '2008', 'Wine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Libournais', 'Appellation': 'Pomerol', 'Producer': 'Pétrus', 'SortProducer': 'Pétrus', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Varietal': 'Red Bordeaux Blend', 'MasterVarietal': 'Red Bordeaux Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '18-19+', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '96.625', 'CNotes': '9', 'MY': '', 'PNotes': '', 'BeginConsume': '2018', 'EndConsume': '2046'},
            {'iWine': '118542', 'Barcode': '0129196204', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '3500', 'Price': '3500', 'NativePrice': '3500', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '4/8/2020', 'BottleNote': '', 'Vintage': '2003', 'Wine': 'Domaine de la Romanée-Conti La Tâche', 'Locale': 'France, Burgundy, Côte de Nuits, La Tâche Grand Cru', 'Country': 'France', 'Region': 'Burgundy', 'SubRegion': 'Côte de Nuits', 'Appellation': 'La Tâche Grand Cru', 'Producer': 'Domaine de la Romanée-Conti', 'SortProducer': 'Romanée-Conti, Domaine de la ', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Varietal': 'Pinot Noir', 'MasterVarietal': 'Pinot Noir', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '94.4117647058823', 'CNotes': '20', 'MY': '', 'PNotes': '', 'BeginConsume': '2013', 'EndConsume': '2029'},
            {'iWine': '1367113', 'Barcode': '0129197436', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '230', 'Price': '230', 'NativePrice': '230', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '11/6/2019', 'BottleNote': '', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'Producer': "Château d'Yquem", 'SortProducer': "Yquem, Château d'", 'Type': 'White - Sweet/Dessert', 'Color': 'White', 'Category': 'Sweet/Dessert', 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '19-20', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '95.9782608695652', 'CNotes': '55', 'MY': '', 'PNotes': '', 'BeginConsume': '2019', 'EndConsume': '2054'},
            {'iWine': '1367113', 'Barcode': '0129197437', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '230', 'Price': '230', 'NativePrice': '230', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '11/6/2019', 'BottleNote': '', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'Producer': "Château d'Yquem", 'SortProducer': "Yquem, Château d'", 'Type': 'White - Sweet/Dessert', 'Color': 'White', 'Category': 'Sweet/Dessert', 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '19-20', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '95.9782608695652', 'CNotes': '55', 'MY': '', 'PNotes': '', 'BeginConsume': '2019', 'EndConsume': '2054'},
            {'iWine': '1367113', 'Barcode': '0129197438', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '230', 'Price': '230', 'NativePrice': '230', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '11/6/2019', 'BottleNote': '', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'Producer': "Château d'Yquem", 'SortProducer': "Yquem, Château d'", 'Type': 'White - Sweet/Dessert', 'Color': 'White', 'Category': 'Sweet/Dessert', 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '19-20', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '95.9782608695652', 'CNotes': '55', 'MY': '', 'PNotes': '', 'BeginConsume': '2019', 'EndConsume': '2054'},
            {'iWine': '1367113', 'Barcode': '0129197439', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '230', 'Price': '230', 'NativePrice': '230', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '11/6/2019', 'BottleNote': '', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'Producer': "Château d'Yquem", 'SortProducer': "Yquem, Château d'", 'Type': 'White - Sweet/Dessert', 'Color': 'White', 'Category': 'Sweet/Dessert', 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '19-20', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '95.9782608695652', 'CNotes': '55', 'MY': '', 'PNotes': '', 'BeginConsume': '2019', 'EndConsume': '2054'},
            {'iWine': '1367113', 'Barcode': '0129197440', 'Location': 'Cellar', 'Bin': '', 'Size': '750ml', 'Currency': 'EUR', 'ExchangeRate': '1', 'Valuation': '230', 'Price': '230', 'NativePrice': '230', 'NativePriceCurrency': 'EUR', 'StoreName': 'Unknown', 'PurchaseDate': '11/6/2019', 'BottleNote': '', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'Producer': "Château d'Yquem", 'SortProducer': "Yquem, Château d'", 'Type': 'White - Sweet/Dessert', 'Color': 'White', 'Category': 'Sweet/Dessert', 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'WA': '', 'WS': '', 'IWC': '', 'BH': '', 'AG': '', 'WE': '', 'JR': '', 'RH': '', 'JG': '', 'GV': '', 'JK': '', 'LD': '', 'CW': '', 'WFW': '', 'PR': '', 'SJ': '', 'WD': '19-20', 'RR': '', 'JH': '', 'MFW': '', 'WWR': '', 'IWR': '', 'CHG': '', 'TT': '', 'TWF': '', 'DR': '', 'FP': '', 'JM': '', 'PG': '', 'WAL': '', 'CT': '95.9782608695652', 'CNotes': '55', 'MY': '', 'PNotes': '', 'BeginConsume': '2019', 'EndConsume': '2054'}
            ], data)

    @requests_mock.Mocker()
    def test_get_inventory_with_empty_result(self, m):
        """Test get inventory with empty result."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Inventory&Format=tab&Location=1"
        file = open("./tests/fixtures/inventory_empty.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_inventory()
        self.assertEqual([], data)

    @requests_mock.Mocker()
    def test_get_inventory_with_invalid_credentials(self, m):
        """Test get inventory with invalid credentials."""
        url = "https://www.cellartracker.com/xlquery.asp?User=invalid-username&Password=invalid-password&Table=Inventory&Format=tab&Location=1"
        file = open("./tests/fixtures/not_logged.html", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="invalid-username", password="invalid-password")
        with self.assertRaises(AuthenticationError):
            cellartracker.get_inventory()

    @requests_mock.Mocker()
    def test_get_inventory_with_error(self, m):
        """Test get inventory with error."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Inventory&Format=tab&Location=1"
        m.register_uri("GET", url, exc=requests.exceptions.ConnectTimeout)

        cellartracker = CellarTracker(username="test-username", password="test-password")
        with self.assertRaises(CannotConnect):
            cellartracker.get_inventory()

    @requests_mock.Mocker()
    def test_get_purchase(self, m):
        """Test get purchase."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Purchase&Format=tab&Location=1"
        file = open("./tests/fixtures/purchase.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_purchase()
        self.assertEqual([
            {'iWine': '684674', 'iPurchase': '123799475', 'PurchaseDate': '5/25/2020', 'DeliveryDate': '5/25/2020', 'StoreName': 'Unknown', 'Currency': 'EUR', 'ExchangeRate': '1', 'Price': '0', 'NativePrice': '0', 'NativePriceCurrency': 'EUR', 'Quantity': '3', 'Remaining': '3', 'OrderNumber': '', 'Delivered': 'False', 'Size': '750ml', 'SortSize': '12', 'Vintage': '2008', 'Wine': 'Pétrus', 'SortWine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Producer': 'Pétrus', 'Varietal': 'Red Bordeaux Blend', 'MasterVarietal': 'Red Bordeaux Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Libournais', 'Appellation': 'Pomerol', 'cLabels': '788'},
            {'iWine': '118542', 'iPurchase': '123864434', 'PurchaseDate': '4/8/2020', 'DeliveryDate': '4/8/2020', 'StoreName': 'Unknown', 'Currency': 'EUR', 'ExchangeRate': '1', 'Price': '3500', 'NativePrice': '3500', 'NativePriceCurrency': 'EUR', 'Quantity': '2', 'Remaining': '1', 'OrderNumber': '', 'Delivered': 'True', 'Size': '750ml', 'SortSize': '12', 'Vintage': '2003', 'Wine': 'Domaine de la Romanée-Conti La Tâche', 'SortWine': 'Romanée-Conti, Domaine de la La Tâche', 'Locale': 'France, Burgundy, Côte de Nuits, La Tâche Grand Cru', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Producer': 'Domaine de la Romanée-Conti', 'Varietal': 'Pinot Noir', 'MasterVarietal': 'Pinot Noir', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Burgundy', 'SubRegion': 'Côte de Nuits', 'Appellation': 'La Tâche Grand Cru', 'cLabels': '484'},
            {'iWine': '1367113', 'iPurchase': '123864410', 'PurchaseDate': '11/6/2019', 'DeliveryDate': '11/6/2019', 'StoreName': 'Unknown', 'Currency': 'EUR', 'ExchangeRate': '1', 'Price': '230', 'NativePrice': '230', 'NativePriceCurrency': 'EUR', 'Quantity': '6', 'Remaining': '5', 'OrderNumber': '', 'Delivered': 'True', 'Size': '750ml', 'SortSize': '12', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'SortWine': "Yquem, Château d'", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Type': 'White - Sweet/Dessert', 'Color': 'White', 'Category': 'Sweet/Dessert', 'Producer': "Château d'Yquem", 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'cLabels': '2199'}
        ], data)

    @requests_mock.Mocker()
    def test_get_purchase_with_empty_result(self, m):
        """Test get purchase with empty result."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Purchase&Format=tab&Location=1"
        file = open("./tests/fixtures/purchase_empty.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_purchase()
        self.assertEqual([], data)

    @requests_mock.Mocker()
    def test_get_purchase_with_invalid_credentials(self, m):
        """Test get purchase with invalid credentials."""
        url = "https://www.cellartracker.com/xlquery.asp?User=invalid-username&Password=invalid-password&Table=Purchase&Format=tab&Location=1"
        file = open("./tests/fixtures/not_logged.html", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="invalid-username", password="invalid-password")
        with self.assertRaises(AuthenticationError):
            cellartracker.get_purchase()

    @requests_mock.Mocker()
    def test_get_purchase_with_error(self, m):
        """Test get purchase with error."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Purchase&Format=tab&Location=1"
        m.register_uri("GET", url, exc=requests.exceptions.ConnectTimeout)

        cellartracker = CellarTracker(username="test-username", password="test-password")
        with self.assertRaises(CannotConnect):
            cellartracker.get_purchase()

    @requests_mock.Mocker()
    def test_get_pending(self, m):
        """Test get pending."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Pending&Format=tab&Location=1"
        file = open("./tests/fixtures/pending.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_pending()
        self.assertEqual([
            {'iWine': '684674', 'iPurchase': '123799475', 'PurchaseDate': '5/25/2020', 'DeliveryDate': '5/25/2020', 'StoreName': 'Unknown', 'Currency': 'EUR', 'ExchangeRate': '1', 'Price': '0', 'NativePrice': '0', 'NativePriceCurrency': 'EUR', 'Quantity': '3', 'Remaining': '3', 'OrderNumber': '', 'Delivered': 'False', 'Size': '750ml', 'SortSize': '12', 'Vintage': '2008', 'Wine': 'Pétrus', 'SortWine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Producer': 'Pétrus', 'Varietal': 'Red Bordeaux Blend', 'MasterVarietal': 'Red Bordeaux Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Libournais', 'Appellation': 'Pomerol', 'cLabels': '788'}
        ], data)

    @requests_mock.Mocker()
    def test_get_pending_with_empty_result(self, m):
        """Test get pending with empty result."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Pending&Format=tab&Location=1"
        file = open("./tests/fixtures/pending_empty.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_pending()
        self.assertEqual([], data)

    @requests_mock.Mocker()
    def test_get_pending_with_invalid_credentials(self, m):
        """Test get pending with invalid credentials."""
        url = "https://www.cellartracker.com/xlquery.asp?User=invalid-username&Password=invalid-password&Table=Pending&Format=tab&Location=1"
        file = open("./tests/fixtures/not_logged.html", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="invalid-username", password="invalid-password")
        with self.assertRaises(AuthenticationError):
            cellartracker.get_pending()

    @requests_mock.Mocker()
    def test_get_pending_with_error(self, m):
        """Test get pending with error."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Pending&Format=tab&Location=1"
        m.register_uri("GET", url, exc=requests.exceptions.ConnectTimeout)

        cellartracker = CellarTracker(username="test-username", password="test-password")
        with self.assertRaises(CannotConnect):
            cellartracker.get_pending()

    @requests_mock.Mocker()
    def test_get_consumed(self, m):
        """Test get consumed."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Consumed&Format=tab&Location=1"
        file = open("./tests/fixtures/consumed.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_consumed()
        self.assertEqual([
            {'iConsumed': '129197435', 'iWine': '1367113', 'Type': 'White - Sweet/Dessert', 'Consumed': '5/21/2020', 'ConsumedYear': '2020', 'ConsumedQuarter': 'Q2', 'ConsumedMonth': '5', 'ConsumedDay': '21', 'ConsumedWeekday': '5', 'Size': '750ml', 'SortSize': '12', 'ShortType': 'Drank', 'Currency': 'EUR', 'ExchangeRate': '1', 'Value': '230', 'Price': '230', 'NativePrice': '230', 'NativePriceCurrency': 'EUR', 'MenuPrice': '0', 'cNotes': '0', 'iNote': '', 'cLabels': '2199', 'NativeRevenue': '0', 'NativeRevenueCurrency': 'EUR', 'Revenue': '0', 'RevenueCurrency': 'EUR', 'RevenueExchangeRate': '1', 'ConsumptionNote': 'Excellent!', 'PurchaseNote': '', 'BottleNote': '', 'Location': 'Cellar', 'Bin': '', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'SortWine': "Yquem, Château d'", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Color': 'White', 'Category': 'Sweet/Dessert', 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes'},
            {'iConsumed': '129196205', 'iWine': '118542', 'Type': 'Red', 'Consumed': '5/1/2020', 'ConsumedYear': '2020', 'ConsumedQuarter': 'Q2', 'ConsumedMonth': '5', 'ConsumedDay': '1', 'ConsumedWeekday': '6', 'Size': '750ml', 'SortSize': '12', 'ShortType': 'Drank', 'Currency': 'EUR', 'ExchangeRate': '1', 'Value': '3500', 'Price': '3500', 'NativePrice': '3500', 'NativePriceCurrency': 'EUR', 'MenuPrice': '0', 'cNotes': '0', 'iNote': '', 'cLabels': '484', 'NativeRevenue': '0', 'NativeRevenueCurrency': 'EUR', 'Revenue': '0', 'RevenueCurrency': 'EUR', 'RevenueExchangeRate': '1', 'ConsumptionNote': 'Absolutely fantastic wine!', 'PurchaseNote': '', 'BottleNote': '', 'Location': 'Cellar', 'Bin': '', 'Vintage': '2003', 'Wine': 'Domaine de la Romanée-Conti La Tâche', 'SortWine': 'Romanée-Conti, Domaine de la La Tâche', 'Locale': 'France, Burgundy, Côte de Nuits, La Tâche Grand Cru', 'Color': 'Red', 'Category': 'Dry', 'Varietal': 'Pinot Noir', 'MasterVarietal': 'Pinot Noir', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Burgundy', 'SubRegion': 'Côte de Nuits', 'Appellation': 'La Tâche Grand Cru'}
        ], data)

    @requests_mock.Mocker()
    def test_get_consumed_with_empty_result(self, m):
        """Test get consumed with empty result."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Consumed&Format=tab&Location=1"
        file = open("./tests/fixtures/consumed_empty.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_consumed()
        self.assertEqual([], data)

    @requests_mock.Mocker()
    def test_get_consumed_with_invalid_credentials(self, m):
        """Test get consumed with invalid credentials."""
        url = "https://www.cellartracker.com/xlquery.asp?User=invalid-username&Password=invalid-password&Table=Consumed&Format=tab&Location=1"
        file = open("./tests/fixtures/not_logged.html", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="invalid-username", password="invalid-password")
        with self.assertRaises(AuthenticationError):
            cellartracker.get_consumed()

    @requests_mock.Mocker()
    def test_get_consumed_with_error(self, m):
        """Test get consumed with error."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Consumed&Format=tab&Location=1"
        m.register_uri("GET", url, exc=requests.exceptions.ConnectTimeout)

        cellartracker = CellarTracker(username="test-username", password="test-password")
        with self.assertRaises(CannotConnect):
            cellartracker.get_consumed()

    @requests_mock.Mocker()
    def test_get_availability(self, m):
        """Test get availability."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Availability&Format=tab&Location=1"
        file = open("./tests/fixtures/availability.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_availability()
        self.assertEqual([
            {'iWine': '684674', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Available': '8.93877551020408E-02', 'Linear': '0.248135209139836', 'Bell': '0.119183673469388', 'Early': '0.119183673469388', 'Late': '8.93877551020408E-02', 'Fast': '0.744897959183674', 'TwinPeak': '0.446938775510204', 'Simple': '0.111111111111111', 'Purchases': '0', 'ActualPurchases': '0', 'Pending': '3', 'ActualPending': '3', 'LocalQuantityActual': '0', 'LocalQuantity': '0', 'Consumed': '0', 'ActualConsumed': '0', 'Inventory': '3', 'ActualInventory': '3', 'Vintage': '2008', 'Wine': 'Pétrus', 'SortWine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Producer': 'Pétrus', 'Varietal': 'Red Bordeaux Blend', 'MasterVarietal': 'Red Bordeaux Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Libournais', 'Appellation': 'Pomerol', 'PersonalBegin': '', 'PersonalEnd': '', 'WABegin': '', 'WAEnd': '', 'WSBegin': '', 'WSEnd': '', 'IWCBegin': '', 'IWCEnd': '', 'AGBegin': '', 'AGEnd': '', 'TWFBegin': '', 'TWFEnd': '', 'BGBegin': '', 'BGEnd': '', 'WEBegin': '', 'WEEnd': '', 'JRBegin': '', 'JREnd': '', 'DRBegin': '', 'DREnd': '', 'PGBegin': '', 'PGEnd': '', 'WALBegin': '', 'WALEnd': '', 'FTLOPBegin': '', 'FTLOPEnd': '', 'JGBegin': '', 'JGEnd': '', 'ComBegin': '2018', 'ComEnd': '2046', 'BeginConsume': '1/1/2018', 'EndConsume': '12/31/2046', 'Source': 'Community', 'WA': '', 'WAWeb': '', 'WASort': '', 'WS': '', 'WSWeb': '', 'WSSort': '', 'BG': '', 'BGWeb': '', 'BGSort': '', 'IWC': '', 'IWCWeb': '', 'IWCSort': '', 'AG': '', 'AGWeb': '', 'AGSort': '', 'FTLOP': '', 'FTLOPWeb': '', 'FTLOPSort': '', 'BR': '', 'BRWeb': '', 'BRSort': '', 'GV': '', 'GVWeb': '', 'GVSort': '', 'LF': '', 'LFWeb': '', 'LFSort': '', 'JK': '', 'JKWeb': '', 'JKSort': '', 'JG': '', 'JGWeb': '', 'JGSort': '', 'LD': '', 'LDWeb': '', 'LDSort': '', 'CW': '', 'CWWeb': '', 'CWSort': '', 'WE': '', 'WEWeb': '', 'WESort': '', 'JR': '', 'JRWeb': '', 'JRSort': '', 'WFW': '', 'WFWWeb': '', 'WFWSort': '', 'PR': '', 'PRWeb': '', 'PRSort': '', 'SJ': '', 'SJWeb': '', 'SJSort': '', 'WD': '18-19+', 'WDWeb': 'http://www.thewinedoctor.com/bordeaux/petrus.shtml', 'WDSort': '94', 'GA': '', 'GAWeb': '', 'GASort': '', 'RR': '', 'RRWeb': '', 'RRSort': '', 'JH': '', 'JHWeb': '', 'JHSort': '', 'MFW': '', 'MFWWeb': '', 'MFWSort': '', 'WWR': '', 'WWRWeb': '', 'WWRSort': '', 'IWR': '', 'IWRWeb': '', 'IWRSort': '', 'CHG': '', 'CHGWeb': '', 'CHGSort': '', 'TT': '', 'TTWeb': '', 'TTSort': '', 'TWF': '', 'TWFWeb': '', 'TWFSort': '', 'DR': '', 'DRWeb': '', 'DRSort': '', 'FP': '', 'FPWeb': '', 'FPSort': '', 'JM': '', 'JMWeb': '', 'JMSort': '', 'PG': '', 'PGWeb': '', 'PGSort': '', 'WAL': '', 'WALWeb': '', 'WALSort': '', 'PNotes': '', 'PScore': '', 'PScoreSort': '', 'CNotes': '9', 'CScore': '96.625', 'CScoreSort': '96.625'},
            {'iWine': '118542', 'Type': 'Red', 'Color': 'Red', 'Category': 'Dry', 'Available': '-0.186046511627907', 'Linear': '-0.12951030927835', 'Bell': '-0.186046511627907', 'Early': '0.247209302325581', 'Late': '-0.541782945736434', 'Fast': '0.571472868217054', 'TwinPeak': '-0.202790697674418', 'Simple': '0.1', 'Purchases': '2', 'ActualPurchases': '2', 'Pending': '0', 'ActualPending': '0', 'LocalQuantityActual': '1', 'LocalQuantity': '1', 'Consumed': '1', 'ActualConsumed': '1', 'Inventory': '1', 'ActualInventory': '1', 'Vintage': '2003', 'Wine': 'Domaine de la Romanée-Conti La Tâche', 'SortWine': 'Romanée-Conti, Domaine de la La Tâche', 'Locale': 'France, Burgundy, Côte de Nuits, La Tâche Grand Cru', 'Producer': 'Domaine de la Romanée-Conti', 'Varietal': 'Pinot Noir', 'MasterVarietal': 'Pinot Noir', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Burgundy', 'SubRegion': 'Côte de Nuits', 'Appellation': 'La Tâche Grand Cru', 'PersonalBegin': '', 'PersonalEnd': '', 'WABegin': '', 'WAEnd': '', 'WSBegin': '', 'WSEnd': '', 'IWCBegin': '', 'IWCEnd': '', 'AGBegin': '', 'AGEnd': '', 'TWFBegin': '', 'TWFEnd': '', 'BGBegin': '', 'BGEnd': '', 'WEBegin': '', 'WEEnd': '', 'JRBegin': '', 'JREnd': '', 'DRBegin': '', 'DREnd': '', 'PGBegin': '', 'PGEnd': '', 'WALBegin': '', 'WALEnd': '', 'FTLOPBegin': '', 'FTLOPEnd': '', 'JGBegin': '', 'JGEnd': '', 'ComBegin': '2013', 'ComEnd': '2029', 'BeginConsume': '1/1/2013', 'EndConsume': '12/31/2029', 'Source': 'Community', 'WA': '', 'WAWeb': '', 'WASort': '', 'WS': '', 'WSWeb': '', 'WSSort': '', 'BG': '', 'BGWeb': '', 'BGSort': '', 'IWC': '', 'IWCWeb': '', 'IWCSort': '', 'AG': '', 'AGWeb': '', 'AGSort': '', 'FTLOP': '', 'FTLOPWeb': '', 'FTLOPSort': '', 'BR': '', 'BRWeb': 'http://www.wine-searcher.com/find/conti+tache/2003/ANY/USD?referring_site=BRP', 'BRSort': '0', 'GV': '', 'GVWeb': '', 'GVSort': '', 'LF': '', 'LFWeb': '', 'LFSort': '', 'JK': '', 'JKWeb': '', 'JKSort': '', 'JG': '', 'JGWeb': '', 'JGSort': '', 'LD': '', 'LDWeb': '', 'LDSort': '', 'CW': '', 'CWWeb': '', 'CWSort': '', 'WE': '', 'WEWeb': '', 'WESort': '', 'JR': '', 'JRWeb': '', 'JRSort': '', 'WFW': '', 'WFWWeb': '', 'WFWSort': '', 'PR': '', 'PRWeb': '', 'PRSort': '', 'SJ': '', 'SJWeb': '', 'SJSort': '', 'WD': '', 'WDWeb': '', 'WDSort': '', 'GA': '', 'GAWeb': '', 'GASort': '', 'RR': '', 'RRWeb': '', 'RRSort': '', 'JH': '', 'JHWeb': '', 'JHSort': '', 'MFW': '', 'MFWWeb': '', 'MFWSort': '', 'WWR': '', 'WWRWeb': '', 'WWRSort': '', 'IWR': '', 'IWRWeb': '', 'IWRSort': '', 'CHG': '', 'CHGWeb': '', 'CHGSort': '', 'TT': '', 'TTWeb': '', 'TTSort': '', 'TWF': '', 'TWFWeb': '', 'TWFSort': '', 'DR': '', 'DRWeb': '', 'DRSort': '', 'FP': '', 'FPWeb': '', 'FPSort': '', 'JM': '', 'JMWeb': '', 'JMSort': '', 'PG': '', 'PGWeb': '', 'PGSort': '', 'WAL': '', 'WALWeb': '', 'WALSort': '', 'PNotes': '', 'PScore': '', 'PScoreSort': '', 'CNotes': '20', 'CScore': '94.4117647058823', 'CScoreSort': '94.4117647058823'},
            {'iWine': '1367113', 'Type': 'White - Sweet/Dessert', 'Color': 'White', 'Category': 'Sweet/Dessert', 'Available': '-0.766808640097353', 'Linear': '-0.766808640097353', 'Bell': '-0.888', 'Early': '-0.888', 'Late': '-0.916', 'Fast': '-0.3', 'TwinPeak': '-0.58', 'Simple': '0.142857142857143', 'Purchases': '6', 'ActualPurchases': '6', 'Pending': '0', 'ActualPending': '0', 'LocalQuantityActual': '5', 'LocalQuantity': '5', 'Consumed': '1', 'ActualConsumed': '1', 'Inventory': '5', 'ActualInventory': '5', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'SortWine': "Yquem, Château d'", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Producer': "Château d'Yquem", 'Varietal': 'Sémillon-Sauvignon Blanc Blend', 'MasterVarietal': 'Sémillon-Sauvignon Blanc Blend', 'Designation': 'Unknown', 'Vineyard': 'Unknown', 'Country': 'France', 'Region': 'Bordeaux', 'SubRegion': 'Sauternais', 'Appellation': 'Sauternes', 'PersonalBegin': '', 'PersonalEnd': '', 'WABegin': '', 'WAEnd': '', 'WSBegin': '', 'WSEnd': '', 'IWCBegin': '', 'IWCEnd': '', 'AGBegin': '', 'AGEnd': '', 'TWFBegin': '', 'TWFEnd': '', 'BGBegin': '', 'BGEnd': '', 'WEBegin': '', 'WEEnd': '', 'JRBegin': '', 'JREnd': '', 'DRBegin': '', 'DREnd': '', 'PGBegin': '', 'PGEnd': '', 'WALBegin': '', 'WALEnd': '', 'FTLOPBegin': '', 'FTLOPEnd': '', 'JGBegin': '', 'JGEnd': '', 'ComBegin': '2019', 'ComEnd': '2054', 'BeginConsume': '1/1/2019', 'EndConsume': '12/31/2054', 'Source': 'Community', 'WA': '', 'WAWeb': '', 'WASort': '', 'WS': '', 'WSWeb': '', 'WSSort': '', 'BG': '', 'BGWeb': '', 'BGSort': '', 'IWC': '', 'IWCWeb': '', 'IWCSort': '', 'AG': '', 'AGWeb': '', 'AGSort': '', 'FTLOP': '', 'FTLOPWeb': '', 'FTLOPSort': '', 'BR': '', 'BRWeb': '', 'BRSort': '', 'GV': '', 'GVWeb': '', 'GVSort': '', 'LF': '', 'LFWeb': '', 'LFSort': '', 'JK': '', 'JKWeb': '', 'JKSort': '', 'JG': '', 'JGWeb': '', 'JGSort': '', 'LD': '', 'LDWeb': '', 'LDSort': '', 'CW': '', 'CWWeb': '', 'CWSort': '', 'WE': '', 'WEWeb': '', 'WESort': '', 'JR': '', 'JRWeb': '', 'JRSort': '', 'WFW': '', 'WFWWeb': '', 'WFWSort': '', 'PR': '', 'PRWeb': '', 'PRSort': '', 'SJ': '', 'SJWeb': '', 'SJSort': '', 'WD': '19-20', 'WDWeb': 'http://www.thewinedoctor.com/bordeaux/yquem.shtml', 'WDSort': '96', 'GA': '', 'GAWeb': '', 'GASort': '', 'RR': '', 'RRWeb': '', 'RRSort': '', 'JH': '', 'JHWeb': '', 'JHSort': '', 'MFW': '', 'MFWWeb': '', 'MFWSort': '', 'WWR': '', 'WWRWeb': '', 'WWRSort': '', 'IWR': '', 'IWRWeb': '', 'IWRSort': '', 'CHG': '', 'CHGWeb': '', 'CHGSort': '', 'TT': '', 'TTWeb': '', 'TTSort': '', 'TWF': '', 'TWFWeb': '', 'TWFSort': '', 'DR': '', 'DRWeb': '', 'DRSort': '', 'FP': '', 'FPWeb': '', 'FPSort': '', 'JM': '', 'JMWeb': '', 'JMSort': '', 'PG': '', 'PGWeb': '', 'PGSort': '', 'WAL': '', 'WALWeb': '', 'WALSort': '', 'PNotes': '', 'PScore': '', 'PScoreSort': '', 'CNotes': '55', 'CScore': '95.9782608695652', 'CScoreSort': '95.9782608695652'}
        ], data)

    @requests_mock.Mocker()
    def test_get_availability_with_empty_result(self, m):
        """Test get availability with empty result."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Availability&Format=tab&Location=1"
        file = open("./tests/fixtures/availability_empty.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_availability()
        self.assertEqual([], data)

    @requests_mock.Mocker()
    def test_get_availability_with_invalid_credentials(self, m):
        """Test get availability with invalid credentials."""
        url = "https://www.cellartracker.com/xlquery.asp?User=invalid-username&Password=invalid-password&Table=Availability&Format=tab&Location=1"
        file = open("./tests/fixtures/not_logged.html", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="invalid-username", password="invalid-password")
        with self.assertRaises(AuthenticationError):
            cellartracker.get_availability()

    @requests_mock.Mocker()
    def test_get_availability_with_error(self, m):
        """Test get availability with error."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Availability&Format=tab&Location=1"
        m.register_uri("GET", url, exc=requests.exceptions.ConnectTimeout)

        cellartracker = CellarTracker(username="test-username", password="test-password")
        with self.assertRaises(CannotConnect):
            cellartracker.get_availability()

    @requests_mock.Mocker()
    def test_get_bottles(self, m):
        """Test get bottles."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Bottles&Format=tab&Location=1"
        file = open("./tests/fixtures/bottles.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_bottles()
        self.assertEqual([
            {'BottleState': '-1', 'iWine': '684674', 'Vintage': '2008', 'Wine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Quantity': '1', 'BottleSize': '750ml', 'Location': '(n/a)', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '5/25/2020', 'DeliveryDate': '5/25/2020', 'BottleCost': '0', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '-1', 'iWine': '684674', 'Vintage': '2008', 'Wine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Quantity': '1', 'BottleSize': '750ml', 'Location': '(n/a)', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '5/25/2020', 'DeliveryDate': '5/25/2020', 'BottleCost': '0', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '-1', 'iWine': '684674', 'Vintage': '2008', 'Wine': 'Pétrus', 'Locale': 'France, Bordeaux, Libournais, Pomerol', 'Quantity': '1', 'BottleSize': '750ml', 'Location': '(n/a)', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '5/25/2020', 'DeliveryDate': '5/25/2020', 'BottleCost': '0', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '0', 'iWine': '118542', 'Vintage': '2003', 'Wine': 'Domaine de la Romanée-Conti La Tâche', 'Locale': 'France, Burgundy, Côte de Nuits, La Tâche Grand Cru', 'Quantity': '1', 'BottleSize': '750ml', 'Location': 'Cellar', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '4/8/2020', 'DeliveryDate': '4/8/2020', 'BottleCost': '3500', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '5/1/2020', 'ConsumptionType': 'Drank from my cellar', 'ShortType': 'Drank', 'ConsumptionNote': 'Absolutely fantastic wine!', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '0', 'iWine': '1367113', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Quantity': '1', 'BottleSize': '750ml', 'Location': 'Cellar', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '11/6/2019', 'DeliveryDate': '11/6/2019', 'BottleCost': '230', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '5/21/2020', 'ConsumptionType': 'Drank from my cellar', 'ShortType': 'Drank', 'ConsumptionNote': 'Excellent!', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '1', 'iWine': '118542', 'Vintage': '2003', 'Wine': 'Domaine de la Romanée-Conti La Tâche', 'Locale': 'France, Burgundy, Côte de Nuits, La Tâche Grand Cru', 'Quantity': '1', 'BottleSize': '750ml', 'Location': 'Cellar', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '4/8/2020', 'DeliveryDate': '4/8/2020', 'BottleCost': '3500', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '1', 'iWine': '1367113', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Quantity': '1', 'BottleSize': '750ml', 'Location': 'Cellar', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '11/6/2019', 'DeliveryDate': '11/6/2019', 'BottleCost': '230', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '1', 'iWine': '1367113', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Quantity': '1', 'BottleSize': '750ml', 'Location': 'Cellar', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '11/6/2019', 'DeliveryDate': '11/6/2019', 'BottleCost': '230', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '1', 'iWine': '1367113', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Quantity': '1', 'BottleSize': '750ml', 'Location': 'Cellar', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '11/6/2019', 'DeliveryDate': '11/6/2019', 'BottleCost': '230', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '1', 'iWine': '1367113', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Quantity': '1', 'BottleSize': '750ml', 'Location': 'Cellar', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '11/6/2019', 'DeliveryDate': '11/6/2019', 'BottleCost': '230', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''},
            {'BottleState': '1', 'iWine': '1367113', 'Vintage': '2011', 'Wine': "Château d'Yquem", 'Locale': 'France, Bordeaux, Sauternais, Sauternes', 'Quantity': '1', 'BottleSize': '750ml', 'Location': 'Cellar', 'Bin': '', 'Store': 'Unknown', 'PurchaseDate': '11/6/2019', 'DeliveryDate': '11/6/2019', 'BottleCost': '230', 'BottleCostCurrency': 'EUR', 'BottleNote': '', 'PurchaseNote': '', 'ConsumptionDate': '', 'ConsumptionType': '', 'ShortType': '', 'ConsumptionNote': '', 'ConsumptionRevenue': '', 'ConsumptionRevenueCurrency': ''}
        ], data)

    @requests_mock.Mocker()
    def test_get_bottles_with_empty_result(self, m):
        """Test get bottles with empty result."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Bottles&Format=tab&Location=1"
        file = open("./tests/fixtures/bottles_empty.tsv", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="test-username", password="test-password")
        data = cellartracker.get_bottles()
        self.assertEqual([], data)

    @requests_mock.Mocker()
    def test_get_bottles_with_invalid_credentials(self, m):
        """Test get bottles with invalid credentials."""
        url = "https://www.cellartracker.com/xlquery.asp?User=invalid-username&Password=invalid-password&Table=Bottles&Format=tab&Location=1"
        file = open("./tests/fixtures/not_logged.html", "r")
        m.register_uri("GET", url, status_code=200, text=file.read())
        file.close

        cellartracker = CellarTracker(username="invalid-username", password="invalid-password")
        with self.assertRaises(AuthenticationError):
            cellartracker.get_bottles()

    @requests_mock.Mocker()
    def test_get_bottles_with_error(self, m):
        """Test get bottles with error."""
        url = "https://www.cellartracker.com/xlquery.asp?User=test-username&Password=test-password&Table=Bottles&Format=tab&Location=1"
        m.register_uri("GET", url, exc=requests.exceptions.ConnectTimeout)

        cellartracker = CellarTracker(username="test-username", password="test-password")
        with self.assertRaises(CannotConnect):
            cellartracker.get_bottles()
