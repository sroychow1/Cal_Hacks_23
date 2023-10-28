import reflex as rx
from Cal_Hacks_23 import styles

def post(text: str) -> rx.Component: 
    return rx.box(
        rx.text(text),
        **styles.text_style
    )