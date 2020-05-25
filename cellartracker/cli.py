"""Console script for CellarTracker"""
import argparse
import sys

from .cellartracker import CellarTracker
from .enum import CellarTrackerFormat, CellarTrackerTable


def main():
    """Console script for CellarTracker"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username',
                        required=True,
                        help='Username from CellarTracker')
    parser.add_argument('-p', '--password',
                        required=True,
                        help='Password from CellarTracker')
    parser.add_argument('-t', '--table',
                        required=False,
                        help='Table from CellarTracker',
                        choices=CellarTrackerTable.__members__,
                        default=CellarTrackerTable.List.value)
    parser.add_argument('-f', '--format',
                        required=False,
                        help='Format from CellarTracker',
                        choices=CellarTrackerFormat.__members__,
                        default=CellarTrackerFormat.tab.value)
    args = parser.parse_args()

    try:
        cellartracker = CellarTracker(args.username, args.password)
        response = cellartracker.client.get(
            table=CellarTrackerTable[args.table],
            format=CellarTrackerFormat[args.format])
        print(response)
        return 0
    except BaseException as exp:
        print(exp)
        return 1


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
