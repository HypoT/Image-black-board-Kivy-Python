from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.uix.image import Image

kv = '''
<DragImage>:
    # Define the properties for the DragImage
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

FloatLayout:
    # Define the root widget
    DragImage:
        size_hint: 0.25, 0.2
        source: 'image/python_discord_logo.png'
'''


class DragImage(DragBehavior, Image):
    pass


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    TestApp().run()