"""
Production code - This is the application code that we are testing.
This module contains the business logic for determining if it's Friday.
"""


def is_it_friday(today):
    """
    Determines if today is Friday.
    
    Args:
        today (str): The day of the week
        
    Returns:
        str: "TGIF" if today is Friday, "Nope" otherwise
    """
    return "TGIF" if today == "Friday" else "Nope"
