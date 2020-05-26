=============
CellarTracker
=============


.. image:: https://img.shields.io/pypi/v/cellartracker.svg
        :target: https://pypi.python.org/pypi/cellartracker

.. image:: https://img.shields.io/travis/mathroule/cellartracker.svg
        :target: https://travis-ci.com/mathroule/cellartracker

.. image:: https://readthedocs.org/projects/cellartracker/badge/?version=latest
        :target: https://cellartracker.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/mathroule/cellartracker/shield.svg
     :target: https://pyup.io/repos/github/mathroule/cellartracker/
     :alt: Updates



Python package to export CellarTracker data.


* Free software: MIT license
* Documentation: https://cellartracker.readthedocs.io.


Features
--------

Using [CellarTracker exporting data](https://support.cellartracker.com/article/29-exporting-data) capabilities.

.. list-table:: Choosing the data to export
   * - Value, Description
     - List, Wine Summary (default)
     - Inventory, Individual Bottles
     - Notes, Your Tasting Notes
     - PrivateNotes, Your Private Notes 
     - Purchase, Your Purchases
     - Pending, Your Pending Purchases (Futures)
     - Consumed, Your Consumed Bottles
     - Availability, Ready to Drink (Drinkability) report
     - Tag, Wishlists
     - ProReview, Your manually-entered Professional Reviews
     - Bottles, A special raw view showing all bottles with a BottleState parameter (-1 for pending, 1 for in-stock, 0 for consumed)
     - FoodTags, Your food pairing tags


Choosing the export format:
+-------+----------------------------------------+
| Value | Description                            |
+-------+----------------------------------------+
| html  | HTML output (default if not specified) |
+-------+----------------------------------------+
| xml   | XML-based output                       |
+-------+----------------------------------------+
| tab   | Tab-delimited text                     |
+-------+----------------------------------------+
| csv   | Comma Separated Values                 |
+-------+----------------------------------------+

Usage
-----
  .. code-block:: bash
    usage: cellartracker [-h] -u USERNAME -p PASSWORD
                         [-t {List,Inventory,Notes,PrivateNotes,Purchase,Pending,Consumed,Availability,Tag,ProReview,Bottles,FoodTag}]
                         [-f {html,xml,tab,csv}]


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
