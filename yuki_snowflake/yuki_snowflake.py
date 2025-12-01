from manim import *

class YukiScene(Scene):
    def construct(self):
        # Create the text "Yuki"
        yuki_text = Text("Yuki", font_size=144, color=BLUE)

        # Create a snowflake shape
        snowflake = SVGMobject("snowflake.svg")  # Ensure you have a snowflake.svg file in the same directory
        snowflake.set_fill(WHITE, opacity=0.8)
        snowflake.set_stroke(BLUE, width=2)
        snowflake.scale(0.5)
        snowflake.next_to(yuki_text, DOWN)

        # Animate the text and snowflake
        self.play(Write(yuki_text))
        self.play(FadeIn(snowflake, shift=UP))
        self.wait(2)