import reflex as rx
from Cal_Hacks_23.state import feedState
from Cal_Hacks_23.components.post import post
from Cal_Hacks_23.state import Post
from typing import List
from Cal_Hacks_23.state import feedState


def feed() -> rx.Component:
    
    feed_state = feedState()

    for i in range(5):
        # print(i)
        feed_state.add_post()
        print()
    

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