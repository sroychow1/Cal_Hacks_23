import reflex as rx
from Cal_Hacks_23 import styles
from Cal_Hacks_23.state import feedState
from Cal_Hacks_23 import styles

def post(post) -> rx.Component: 
    return rx.box(
        rx.text(post.id),
        rx.text(post.text),
        rx.text(post.link),
        rx.text(post.yes_flag_count),
        rx.text(post.no_flag_count),
        rx.divider(**styles.box_style),
    )