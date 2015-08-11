import scene

g_color_red = scene.Color(1, 0, 0)
g_color_blue = scene.Color(0, 0, 1)
g_color_white = scene.Color(1, 1, 1)

class MyScene(scene.Scene):
    def __init__(self):
        scene.run(self)

    def setup(self):
        self.lines = []
        self.stroke_color = g_color_white
        self.button_blue = self.make_button_blue()
        self.button_red = self.make_button_red()
        self.add_layer(self.button_blue)
        self.add_layer(self.button_red)
        self.add_layer(self.make_button_restart())

    def make_button_blue(self):
        button = scene.Button(scene.Rect(self.size.w/2-155, self.size.h/2-245, 75, 50))
        button.background = g_color_blue
        button.stroke = g_color_white
        button.action = self.turn_blue
        return button

    def make_button_red(self):
        button = scene.Button(scene.Rect(self.size.w/2-35, self.size.h/2-245, 75, 50))
        button.background = g_color_red
        button.stroke = g_color_white
        button.action = self.turn_red
        return button

    def make_button_restart(self):
        button = scene.Button(scene.Rect(self.size.w/2+85, self.size.h/2-245, 75, 50))
        button.background = g_color_white
        button.stroke = g_color_white
        button.action = self.restart
        return button

    def restart(self):
        MyScene()

    def turn_red(self):
        self.stroke_color = self.button_red.background = g_color_red

    def turn_blue(self):
        self.stroke_color = self.button_blue.background = g_color_blue

    def draw(self):
        scene.background(0,0,0)
        self.root_layer.update(self.dt)
        self.root_layer.draw()
        scene.fill(1,1,1)
        scene.stroke(*self.stroke_color)
        scene.stroke_weight(4)
        scene.rect(0,180,320,15)
        scene.rect(0,290,320,15)
        scene.rect(92,87,15,310)
        scene.rect(208,87,15,310)
        for l in self.lines:
            scene.line(*l)

    def touch_moved(self, touch):
        x = touch.location.x
        y = touch.location.y
        ppos = touch.prev_location
        self.lines.append((ppos.x, ppos.y, x, y))

MyScene()
