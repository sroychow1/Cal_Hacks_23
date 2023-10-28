"""Base state for the app."""

import reflex as rx


class feedState(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
    feed = [
        "text 1",
        "text 2",
        "text 3",
        "text 4",
        "text 5",
    ]

    def add_post(self, item: str):
        self.feed += [item]