import os
from PIL import Image
from manim import *

# -------------------------------------------------------
# Scene 1: Creates partial_movie_files + png
# -------------------------------------------------------

class TestMovie(Scene):
    def construct(self):
        # This creates intermediate frame images in partial_movie_files
        circle = Circle().set_color(RED)
        square = Square().set_color(BLUE)

        self.play(Create(circle), run_time=1)
        self.play(Transform(circle, square), run_time=1)
        self.wait()

        # This triggers LaTeX and creates media/Tex/*
        tex = MathTex(r"\int_a^b f(x)\,dx")
        self.play(Write(tex))

        # ------------------------------
        # Generate a test photo
        # ------------------------------
        test_square = Square().set_color(GREEN)
        self.add(test_square)
        self.wait(0.5)

        # Get current frame as numpy array
        frame = self.renderer.get_frame()

        # Save manually under media/images/manim_test/
        images_dir = "media/images/manim_test"
        os.makedirs(images_dir, exist_ok=True)
        image_path = os.path.join(images_dir, "test_image.png")

        # Save as PNG
        im = Image.fromarray(frame)
        im.save(image_path)
        print(f"Test image saved at: {image_path}")


# -------------------------------------------------------
# Scene 2: Creates partial_scene_files using cache
# -------------------------------------------------------

class TestCache(Scene):
    def construct(self):
        text = Text("Cached Scene Example")
        self.play(FadeIn(text))
        self.wait()
