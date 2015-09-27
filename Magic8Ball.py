#coding: utf-8
import motion, random, scene

use_motion = True

choices = (
"Go for it!",
"No way, Jose!",
"I'm not sure.\nAsk me again.",
"Fear of the\nunknown is\nwhat imprisons\nus.",
"It would be\nmadness to\ndo that!",
"Makes no\ndifference to\nme, do or don't\n- whatever.",
"Yes, I think on\nbalance, that is\nthe right choice.")

help_text = '''Ask me for
advice, then
tap the screen.
Or click the ❎
at the top
right of the
screen to exit.'''

def random_color():
    return scene.Color(random.random(), random.random(), random.random())

class Particle(object):
    def __init__(self, wh):
        self.w = wh.w
        self.h = wh.h
        self.x = random.randint(0, self.w)
        self.y = random.randint(0, self.h)
        self.vx = random.randint(-10, 20)
        self.vy = random.randint(-10, 20)
        self.colour = random_color()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.98
        self.vy *= 0.98
        if self.x > self.w:
            self.x = self.w
            self.vx *= -1
        elif self.x < 0:
            self.x = 0
            self.vx *= -1
        if self.y > self.h:
            self.y = self.h
            self.vy *= -1
        elif self.y < 0:
            self.y = 0
            self.vy *= -1

    def draw(self):
        scene.fill(*self.colour)
        scene.rect(self.x, self.y, 8, 8)

class ParticleScene(scene.Scene):
    def __init__(self):
        scene.run(self)

    def setup(self):
        self.center = self.bounds.center()
        self.particles = [Particle(self.size) for i in xrange(200)]

    def draw(self):
        for p in self.particles:
            p.update()
            p.draw()
        for t in self.touches.values():
            for p in self.particles:
                tx, ty = t.location.x, t.location.y
                d = (p.x - tx)*(p.x - tx)+(p.y - ty)*(p.y - ty)
                d = scene.sqrt(d)
                p.vx = p.vx - 5/d*(p.x-tx)
                p.vy = p.vy - 5/d*(p.y-ty)
                p.colour = random_color()

class MyScene(ParticleScene):
    def draw(self):
        scene.background(0.00, 0.05, 0.20)
        super(MyScene, self).draw()
        s = 45 if self.size.w > 100 else 7
        scene.text('Welcome to\nMyMagic8Ball\n\n\n', 'Futura', s, *self.center)
        t = 100 if self.size.w > 100 else 7
        scene.text('\n🎱', 'Futura', t, *self.center)
        s = 27 if self.size.w > 100 else 7
        scene.text('\n\n\n\n\n\n\n\n\n\n\n\nBy: Adedayo Ogunnoiki', 'Futura', s, *self.center)

    def touch_ended(self, touch):
        Help()

class Help(ParticleScene):
    def draw(self):
        scene.background(0.00, 0.05, 0.20)
        super(Help, self).draw()
        #scene.tint(*random_color())
        s = 45 if self.size.w > 100 else 7
        scene.text(help_text, 'Futura', s, *self.center)

    def touch_ended(self, touch):
        Advice()

class Advice(ParticleScene):
    def setup(self):
        super(Advice, self).setup()
        self.answer = random.choice(choices)
        if use_motion:
            motion.start_updates()

    def stop(self):
        if use_motion:
            motion.stop_updates()

    def draw(self):
        x,y,z = motion.get_attitude() if use_motion else scene.gravity()
        r,g,b = abs(x), abs(y), abs(z)
        scene.background(r, g, b)
        super(Advice, self).draw()
        scene.tint(1-r, 1-g, 1-b)
        scene.text(self.answer, 'Futura', 45, *self.center)

    def touch_ended(self, touch):
        Advice()

MyScene()
