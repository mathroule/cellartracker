=====
Usage
=====

To use CellarTracker from the console::

    $ cellartracker [-h] -u USERNAME -p PASSWORD
                    [-t {List,Inventory,Notes,PrivateNotes,Purchase,Pending,Consumed,Availability,Tag,ProReview,Bottles,FoodTag}]
                    [-f {html,xml,tab,csv}]


To use CellarTracker in a project::

    from cellartracker import cellartracker
    
    client = cellartracker.CellarTracker(username, password)
    client.get_list()           # Return List
    client.get_inventory()      # Return Inventory
    client.get_notes()          # Return Notes
    client.get_private_notes()  # Return PrivateNotes
    client.get_purchase()       # Return Purchase
    client.get_pending()        # Return Pending
    client.get_consumed()       # Return Consumed
    client.get_availability()   # Return Availability
    client.get_tag()            # Return Tag
    client.get_pro_review()     # Return ProReview
    client.get_bottles()        # Return Bottles
    client.get_food_tag()       # Return FoodTag
