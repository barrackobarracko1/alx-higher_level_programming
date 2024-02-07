#!/usr/bin/python3
"""This defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Display a list in sorted ascending order."""
        print(sorted(self))
