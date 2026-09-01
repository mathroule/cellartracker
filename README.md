# cellartracker

Python package to export data from [CellarTracker](https://www.cellartracker.com), the wine cellar management platform.

[![PyPI](https://img.shields.io/pypi/v/cellartracker.svg)](https://pypi.python.org/pypi/cellartracker)
[![License](https://img.shields.io/pypi/l/cellartracker.svg)](https://github.com/mathroule/cellartracker/blob/main/LICENSE)

## Install

```bash
pip install cellartracker
```

## Quick Start

```python
from cellartracker import cellartracker

ct = cellartracker.CellarTracker('your_handle', 'your_password')

# Get your full inventory
inventory = ct.get_inventory()
print(f"Your cellar: {len(inventory)} bottles")

# First bottle
bottle = inventory[0]
print(f"{bottle['Vintage']} {bottle['Wine']} — ${bottle['Price']}")
```

## Available Methods

### Inventory & Wines
| Method | Returns | Description |
|--------|---------|-------------|
| `get_inventory()` | `list[dict]` | Full inventory with valuations, scores, purchase details |
| `get_list()` | `list[dict]` | Current wine list with stock levels |
| `get_bottles()` | `list[dict]` | Every bottle individually (for state tracking) |
| `get_availability()` | `list[dict]` | Drinkability report with drinking windows |

### Purchase & Consumption
| Method | Returns | Description |
|--------|---------|-------------|
| `get_purchase()` | `list[dict]` | Purchase history with store, price, quantity |
| `get_consumed()` | `list[dict]` | Consumption history |
| `get_pending()` | `list[dict]` | Pending deliveries |

### Reviews & Tags
| Method | Returns | Description |
|--------|---------|-------------|
| `get_notes()` | `list[dict]` | Public tasting notes and ratings |
| `get_private_notes()` | `list[dict]` | Your private tasting notes |
| `get_pro_review()` | `list[dict]` | Professional critic scores |
| `get_tag()` | `list[dict]` | Wish list / tagged wines |
| `get_food_tag()` | `list[dict]` | Food pairing tags |

## Common Fields

Each bottle in `get_inventory()` includes these useful fields:

| Field | Description |
|-------|-------------|
| `iWine` | Unique wine ID (for API operations) |
| `Wine` | Wine name |
| `Vintage` | Vintage year |
| `Producer` | Producer / winery |
| `Varietal` | Grape variety |
| `Country` / `Region` | Origin |
| `Price` | Purchase price |
| `Valuation` | Current market valuation |
| `StoreName` | Where purchased |
| `PurchaseDate` | Date of purchase |
| `Location` | Storage location |
| `Size` | Bottle size (750ml, 1.5L, etc.) |
| `CT` | Community score |
| `CNotes` | Number of community tasting notes |

## CLI Usage

```bash
# Export your inventory as tab-separated data
cellartracker --username=your_handle --password=your_password --table=Inventory

# Export purchase history as CSV
cellartracker --username=your_handle --password=your_password --table=Purchase --format=csv
```

Available tables: `List`, `Inventory`, `Notes`, `PrivateNotes`, `Purchase`, `Pending`, `Consumed`, `Availability`, `Tag`, `ProReview`, `Bottles`, `FoodTag`

Available formats: `tab`, `csv`, `xml`, `html`

## Authentication

Your CellarTracker **handle** is required — this is your username, not your email address. If you sign in at cellartracker.com as "coop789", that's your handle.

## Data Source

This package uses CellarTracker's [official export functionality](https://support.cellartracker.com/article/29-exporting-data) to access your data via the `xlquery.asp` endpoint.

## License

MIT license.
