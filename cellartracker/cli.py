"""Console script for CellarTracker."""

import argparse
import sys
import json

from .cellartracker import CellarTracker
from .enum import CellarTrackerFormat, CellarTrackerTable


TABLE_DESCRIPTIONS = {
    "Inventory": "Full inventory with valuations and scores",
    "List": "Current wine list with stock levels",
    "Purchase": "Purchase history",
    "Consumed": "Consumption history",
    "Bottles": "Individual bottle records",
    "Notes": "Public tasting notes",
    "PrivateNotes": "Private tasting notes",
    "Pending": "Pending deliveries",
    "Availability": "Drinkability / drinking windows",
    "Tag": "Wish list / tagged wines",
    "ProReview": "Professional critic reviews",
    "FoodTag": "Food pairing tags",
}


def main():
    """Console script for CellarTracker."""
    parser = argparse.ArgumentParser(
        description="Export your CellarTracker wine data.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  cellartracker -u myhandle -p mypass --table=Inventory\n"
            "  cellartracker -u myhandle -p mypass --table=Purchase --format=csv\n"
            "  cellartracker -u myhandle -p mypass --table=Inventory --json\n"
        ),
    )
    parser.add_argument(
        "-u", "--username",
        required=True,
        help="CellarTracker handle (your username, not email)",
    )
    parser.add_argument(
        "-p", "--password",
        required=True,
        help="CellarTracker account password",
    )
    parser.add_argument(
        "-t", "--table",
        required=False,
        help="Data table to export",
        choices=sorted(CellarTrackerTable.__members__.keys()),
        default="List",
    )
    parser.add_argument(
        "-f", "--format",
        required=False,
        help="Output format from the API",
        choices=sorted(CellarTrackerFormat.__members__.keys()),
        default="tab",
    )
    parser.add_argument(
        "--json",
        required=False,
        action="store_true",
        help="Output as formatted JSON",
    )
    parser.add_argument(
        "--list-tables",
        required=False,
        action="store_true",
        help="List available tables and exit",
    )

    args = parser.parse_args()

    if args.list_tables:
        print("Available tables:")
        for name, desc in sorted(TABLE_DESCRIPTIONS.items()):
            print(f"  {name:15s}  {desc}")
        return 0

    try:
        ct = CellarTracker(args.username, args.password)
        table_enum = CellarTrackerTable[args.table]
        format_enum = CellarTrackerFormat[args.format]

        response = ct.client.get(table=table_enum, format=format_enum)

        if args.json:
            # Parse tab/CSV data back to structured format
            data = ct._get_data(table=table_enum)
            print(json.dumps(data, indent=2, default=str))
        else:
            print(response)
        return 0
    except BaseException as exp:
        print(f"Error: {exp}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
