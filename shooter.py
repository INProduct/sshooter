from kivy.app import App
from kivy.core.window import Window
import sys

if sys.platform.startswith('linux'):
    import pyscreenshot as ImageGrab
else:
    from PIL import ImageGrab


class ShooterApp(App):

    def build(self):
        pass

    def shoot(self):
        print(self.root.ids["'x_pos'"].text)
        props = [self.root.ids["'x_pos'"].text, self.root.ids["'y_pos'"].text, self.root.ids["'width'"].text, self.root.ids["'height'"].text]
        numbs = []
        for p in props:
            try:
                n = int(p)
            except:
                n = None
            numbs.append(n)
        if all(numbs):
            im = ImageGrab.grab(bbox=tuple(numbs))
        else:
            im = ImageGrab.grab()
        im.show()


if __name__ == '__main__':
    app = ShooterApp()
    app.title = 'INProduct ShooteR'

    Window.size = (500, 100)
    app.run()
