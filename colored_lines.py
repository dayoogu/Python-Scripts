import collections, scene

# define a new data type with two fields: color and line
ColoredLine = collections.namedtuple('ColoredLine', 'color line')

class MyScene(scene.Scene):
    def __init__(self):
        scene.run(self)

    def setup(self):
        self.colored_lines = [
            ColoredLine(scene.Color(1, 0, 0), (  0,   0,  49,  49)),
            ColoredLine(scene.Color(0, 1, 0), ( 50,  50,  99,  99)),
            ColoredLine(scene.Color(0, 0, 1), (100, 100, 149, 149)),
            ColoredLine(scene.Color(1, 1, 1), (150, 150, 199, 199)) ]
        # print(self.colored_lines[0])  # if you want to see what one looks like

    def draw(self):
        scene.background(0,0,0)
        scene.stroke_weight(4)

        for colored_line in self.colored_lines:
            scene.stroke(*colored_line.color)
            scene.line(*colored_line.line)

MyScene()
