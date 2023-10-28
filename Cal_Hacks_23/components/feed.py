import reflex as rx
from Cal_Hacks_23.state import feedState
from Cal_Hacks_23 import styles
from Cal_Hacks_23.components.post import post
from Cal_Hacks_23.state import feedState


def feed(feed_state: feedState) -> rx.Component:

    return rx.vstack(
        *[post(p.username, p.text, p.link) for p in feed_state.get_feeds()],
        **styles.feed_content
    )