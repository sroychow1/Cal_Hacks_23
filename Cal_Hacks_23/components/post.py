import reflex as rx
from Cal_Hacks_23 import styles
from Cal_Hacks_23.state import feedState
from Cal_Hacks_23 import styles
from Cal_Hacks_23.state import Post
from typing import Dict
import json

def post(post_JSON: str) -> rx.Component: 
    
    post = json.loads(post_JSON)
    
    return rx.box(
    
        rx.divider(**styles.box_style),
    )