"""Base state for the app."""
from typing import List


import reflex as rx


class Post(rx.Base):
    id: str
    username: str
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
    feed: List[Post] = []


    def get_feeds(self):
        return self.__getattribute__('feed')


    def add_post(self):
        # print("add_post called")
        post = Post(
            id=self.curr_number, 
            username="john cabob", 
            text=f"testing TEXT {self.curr_number}", 
            link=f"testing LINK {self.curr_number}", 
            yes_flag_count=0, 
            no_flag_count=0)
        
        self.curr_number += 1

        self.feed.append(post)



    