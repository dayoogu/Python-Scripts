#By: Adedayo Ogunnoiki
from scene import *
from random import *
import sys

class Particle(Rect):
	def __init__(self, wh):
		global particlew, particleh
		particlew = wh.w
		particleh = wh.h
		self.x = randint(particlew*-1, particlew)
		self.y = randint(particleh*-1, particleh)
		self.colour = Color(random(), random(), random())
		self.cells=Rect(self.x, self.y, 10, 10)

	def update(self):
		self.cells=Rect(self.x, self.y, 10, 10)

	def draw(self):
		fill(*self.colour)
		ellipse(*self.cells)
		global attackx, attacky
		attackx, attacky = self.x, self.y

class Bots(Rect):
	def __init__(self, wh):
		self.w = wh.w
		self.h = wh.h
		self.x = randint(self.w*-1, self.w)
		self.y = randint(self.h*-1, self.h)
		self.colour = Color(random(), random(), random())
		self.bsize=11

	def update(self):
		self.attackers=Rect(self.x, self.y, self.bsize, self.bsize)

	def draw(self):
		fill(*self.colour)
		ellipse(*self.attackers)

class Intro(Scene):
	def setup(self):
		self.count = 0
		self.psize = 11
		self.plocx = self.size.w/2 - self.psize/2
		self.plocy = self.size.h/2 - self.psize/2
		self.player = Rect(self.plocx, self.plocy, self.psize, self.psize)
		self.colour = Color(random(), random(), random())
		self.particles = [Particle(self.size) for i in xrange(50)]
		self.bots = [Bots(self.size)]
		self.lw=self.size.w*-1
		self.rw=self.size.w
		self.bh=self.size.h*-1
		self.th=self.size.h
		
		self.split = Button(Rect(self.size.w/8, self.size.h/16, 80, 80))
		self.split.background = Color(0,0,0,0)
		self.split.stroke = Color(0,0,0,0)
		self.split.image = 'ionicons-code-working-24'
		self.split.action = self.split_player
		self.add_layer(self.split)
		
	def split_player(self):
		if self.psize/2 > 10:
			print("yas, bitch yas")

	def touch_began(self, touch):
		global x1, y1
		x1, y1 = touch.location

	def touch_moved(self, touch):
		global x, y
		x, y = touch.location
		self.count = 1

	def movecells(self):
		global x, y, x1, y1, particlew, particleh
		for p in self.particles:
			if x1 > x and self.lw < self.plocx:
				p.x += 2
				self.lw += 0.04
				self.rw += 0.04
				particlew += 0.04

			if x1 < x and self.rw > self.plocx:
				p.x -= 2
				self.lw -= 0.04
				self.rw -= 0.04
				particlew -= 0.04

			if y1 > y and self.bh < self.plocy:
				p.y += 2
				self.bh += 0.04
				self.th += 0.04
				particleh += 0.04
	
			if y1 < y and self.th > self.plocy:
				p.y -= 2
				self.bh -= 0.04
				self.th -= 0.04
				particleh -= 0.04
		
			for b in self.bots:
				if b.x > self.rw:
					b.x -= 1
				elif b.x < self.lw:
					b.x += 1
				if b.y < self.bh:
					b.y += 1
				elif b.y > self.th:
					b.y -= 1
					
	def keep_in_bounds(self):
		for p in self.particles:
			p.update()
			p.draw()	
			if p.x > self.rw or p.x < self.lw or p.y > self.th or p.y < self.bh:
				self.particles.remove(p)
				for p in range(1):
					self.particles.append(Particle(self.size))
					
	def bots_life(self):
		for b in self.bots:
			b.update()
			b.draw()
			if b.x < attackx and b.x < self.rw:
				b.x += 2
			elif b.x > attackx and b.x > self.lw:
				b.x -= 2
			if b.y < attacky and b.y < self.th:
				b.y += 2
			elif b.y > attacky and b.y > self.bh:
				b.y -= 2
				
			for p in self.particles:
				if b.attackers.intersects(p.cells):
					self.particles.remove(p)
					b.bsize+=0.5
					for p in range(1):
						self.particles.append(Particle(self.size))
					self.keep_in_bounds()

				if self.player.intersects(b.attackers):
					if int(b.bsize) > int(self.psize):
						self.die()
					if int(self.psize) > int(b.bsize):
						self.psize += b.bsize
					
	def die(self):
		sys.exit()
		
	def draw(self):
		background(0.00, 0.05, 0.20)
		self.split.background = Color(0,0,0,0)
		self.split.draw()
		global attackx, attackx
		self.plocx = self.size.w/2 - self.psize/2
		self.plocy = self.size.h/2 - self.psize/2
		if self.count == 1:
			self.movecells()
		for p in self.particles:
			p.update()
			p.draw()
			if self.player.intersects(p.cells):
				self.particles.remove(p)
				self.psize += 0.2
				for p in range(1):
					self.particles.append(Particle(self.size))
				self.keep_in_bounds()
		self.bots_life()
		self.player = Rect(self.plocx, self.plocy, self.psize, self.psize)
		fill(*self.colour)
		ellipse(*self.player)
		
	def should_rotate(self, orientation):
		return True
		
run(Intro())
