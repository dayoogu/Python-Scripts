#By: Adedayo Ogunnoiki
from scene import *
from random import *

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
		self.points = self.psize
	
	def touch_began(self, touch):
		self.x1, self.y1 = touch.location

	def touch_moved(self, touch):
		self.x, self.y = touch.location
		self.count = 1

	def movecells(self):
		for p in self.particles:
			p.update()
			if self.x > self.x1:
				addx=(self.x-self.x1)/30
				self.newcellx=p.x+addx
			if self.x < self.x1:
				subx=(self.x-self.x1)/30
				self.newcellx=p.x+subx
			if self.y > self.y1:
				addy=(self.y-self.y1)/30
				self.newcelly=p.y+addy
			if self.y < self.y1:
				suby=(self.y-self.y1)/30
				self.newcelly=p.y+suby
			
			while self.newcellx != p.x and self.newcellx > p.x and self.lw < self.plocx:
				p.x += 1
				self.lw += 0.02
				self.rw += 0.02
				
			while self.newcellx != p.x and self.newcellx < p.x and self.rw > self.plocx:
				p.x-= 1
				self.lw -= 0.02
				self.rw -= 0.02
				
			while self.newcelly != p.y and self.newcelly > p.y and self.bh < self.plocy:
				p.y += 1
				self.bh += 0.02
				self.th += 0.02
				
			while self.newcelly != p.y and self.newcelly < p.y and self.th > self.plocy:
				p.y -= 1
				self.bh -= 0.02
				self.th -= 0.02
				
		for b in self.bots:
			if b.x > self.rw:
				b.x -= 2
					
			elif b.x < self.lw:
				b.x += 2
					
			if b.y < self.bh:
				b.y += 2
					
			elif b.y > self.th:
				b.y -= 2
				
	def keep_in_bounds(self):
		global attackx, attacky
		for p in self.particles:
			p.update()
			p.draw()	
			if attackx > self.rw or attackx < self.lw or attacky > self.th or attacky < self.bh:
				self.particles.remove(p)
				for p in range(1):
					self.particles.append(Particle(self.size))
					
	def bound_block(self):
		rect(self.rw+self.psize, self.bh-self.size.h/2, self.size.w, self.size.h*3)
		rect(self.lw-self.size.w/2, self.bh-self.size.h/2, self.size.w/2, self.size.h*3)
		rect(self.lw-self.size.w/2, self.bh-self.size.h/2, self.size.w*3, self.size.h/2)
		rect(self.lw, self.th+self.psize, self.size.w*2+self.psize, self.size.h/2)
	
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
					b.bsize += 0.5
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
				self.points += 1
				for p in range(1):
					self.particles.append(Particle(self.size))
				self.keep_in_bounds()
		self.bots_life()
		self.player = Rect(self.plocx, self.plocy, self.psize, self.psize)
		fill(*self.colour)
		ellipse(*self.player)
		fill(0,0,0)
		self.bound_block()
		text('Score: %i' % self.points, x=self.size.w/4, y=self.size.h/4*3.6, font_size=20)
		
	def should_rotate(self, orientation):
		return True
	
run(Intro())
