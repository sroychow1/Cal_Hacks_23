import reflex as rx
from Cal_Hacks_23 import styles




def post(username: str, text: str, link: str) -> rx.Component: 
    

    return rx.grid(
                rx.box(
                    rx.text(username),
                    rx.text(text),
                    rx.text(link),
                ),
                rx.divider(borderColor="black"),
                **styles.post_style,
            ) 