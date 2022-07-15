import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class touch(Widget):
    def __init__(self, **kwargs):
        super(touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0)
            Line(points=(100, 100, 200, 200, 300, 300))
            Color(1, 0, 0, 1)
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Down", touch)
        
    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Move", touch)

class MyApp(App):
    def build(self):
        return  touch()

if __name__ == "__main__":
    MyApp().run()