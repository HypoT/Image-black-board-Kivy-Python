from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.scatter import Scatter


class MoveableImage(Image, Scatter):

    def __init__(self, **kwargs):
        super(MoveableImage, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        if not self._keyboard:
            return
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.x -= 10
        elif keycode[1] == 'right':
            self.x += 10
        elif keycode[1] == 'up':
            self.y += 10
        elif keycode[1] == 'down':
            self.y -= 10
        elif keycode[1] == 'w':
            self.scale = self.scale * 1.1
        elif keycode[1] == 's':
            self.scale = self.scale * 0.8
        else:
            return False
        return True


class MoveTheImage(App):

    def build(self):
        move_img = MoveableImage(source='python_discord_logo.png')
        m = Scatter()
        m.add_widget(move_img)
        return m


if __name__ == '__main__':
    MoveTheImage().run()
