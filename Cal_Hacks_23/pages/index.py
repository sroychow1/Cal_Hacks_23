"""The home page of the app."""

import reflex as rx
from Cal_Hacks_23 import styles
from Cal_Hacks_23.templates import template
from Cal_Hacks_23.components.feed import feed
from Cal_Hacks_23.state import feedState




@template(route="/", title="CalHacks2023 App", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    # with open("README.md", encoding="utf-8") as readme:
    #     content = readme.read()
    # return rx.markdown(content, component_map=styles.markdown_style)

    feed_state = feedState()

    for i in range(5):
        feed_state.add_post()
    

    return rx.vstack(
            rx.box(rx.text("CalHacks_2023 WebApp", **styles.text_title_style)),
            feed(feed_state),
            **styles.app
        )
