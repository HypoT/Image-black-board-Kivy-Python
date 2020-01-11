from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


class MoveableImage(Scatter):
    My_Global = Image(source='python_discord_logo.png')

    def __init__(self, **kwargs):
        super(MoveableImage, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        if not self._keyboard:
            return
        for item, value in kwargs:
            print("%s and %s" % (item, value))
        self.add_widget(self.My_Global)
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
        moveImg = MoveableImage()
        m = Scatter()
        f = FloatLayout()
        k = BoxLayout(orientation='vertical')
        loadBtn = TextInput(text="python_discord_logo.png", size_hint_y=None, height=50)
        loadBtn.bind(text=self.add_image)
        f.add_widget(m)
        m.add_widget(moveImg)
        k.add_widget(loadBtn)
        k.add_widget(f)
        return k

    def add_image(self, instance, text):
        MoveableImage.My_Global.source = text
        MoveableImage.My_Global.reload()
        print('new thing...')


if __name__ == '__main__':
    MoveTheImage().run()
