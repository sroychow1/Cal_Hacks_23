import reflex as rx
from Cal_Hacks_23.state import feedState
from Cal_Hacks_23.components.post import post

def feed() -> rx.Component:
    
    return rx.vstack(
        # rx.foreach(
        #     feedState.feed,
        #     post
        # )
        rx.foreach(
            feedState.feed,
            post
        )
    )