from manim import *

class YukiScene(Scene):
    def construct(self):
        # Create the text "Yuki"
        yuki_text = Text("Yuki", font_size=144, color=GREEN)

        # Create a snowflake shape
        cat = SVGMobject("cat.svg")  # Ensure you have a cat.svg file in the same directory
        cat.set_fill(WHITE, opacity=0.8)
        cat.set_stroke(GREEN, width=2)
        cat.scale(0.5)
        cat.next_to(yuki_text, DOWN)

        # Animate the text and snowflake
        self.play(Write(yuki_text))
        self.play(FadeIn(cat, shift=UP))
        self.wait(2)