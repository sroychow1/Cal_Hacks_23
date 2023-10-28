"""Base state for the app."""
from typing import List, Dict
import json

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

    # post: Post = Post(id=1, text="testing TEXT", link="texting LINK", yes_flag_count=0, no_flag_count=0)

    curr_number: int = 0
    feed: List[str] = []
    # feed: List[List[str]] =  []


    def add_post(self):
        print("add_post called")
        # post = Post(id=self.curr_number, text="testing TEXT", link="texting LINK", yes_flag_count=0, no_flag_count=0)
        self.curr_number += 1

        post: Dict[str, str] = {
            "id": self.curr_number,
            "text": "testing Text",
            "link": "testing Link",
            "yes_flag_count": 0,
            "no_flag_count": 0
        }

        post_JSON = str(post)

        # post = [["some ID"]]

        self.feed.append(post_JSON)



    