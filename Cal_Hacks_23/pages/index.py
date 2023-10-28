"""The home page of the app."""

from Cal_Hacks_23 import styles
from Cal_Hacks_23.templates import template
from Cal_Hacks_23.components.post import post
from Cal_Hacks_23.components.feed import feed

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    # with open("README.md", encoding="utf-8") as readme:
    #     content = readme.read()
    # return rx.markdown(content, component_map=styles.markdown_style)
    
    return rx.vstack(
            feed()
        )
