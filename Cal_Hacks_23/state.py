"""Base state for the app."""
from typing import List

import reflex as rx


class Post(rx.Base):
    id: str
    text: str
    link: str
    yes_flag_count: str
    no_flag_count: str

class feedState(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    # """

    # testPost = Post(id=1, text="testing TEXT", link="texting LINK", yes_flag_count=0, no_flag_count=0)

    feed: list[Post] = []

    
    def add_post(self):
        print("testing")
        post = Post(id=1, text="testing TEXT", link="texting LINK", yes_flag_count=0, no_flag_count=0)
        print(type(post))
        # print(len(self.feed))
        # print("Testing")
        self.feed.append(post)
        # print("Feed created")
    