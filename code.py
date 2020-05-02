from pyglet.gl import *
class Model:
	def __init__(self):
		self.batch = pyglet.graphics.Batch()

		
	def draw(self):
		self.batch.draw()
class Window(pyglet.window.Window):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.set_minimum_size(300,200)
		self.model = Model()

	def on_draw(self):
		self.clear()
		self.model.draw()
if __name__ == '__main__':
	window = Window(width = 400, height = 300, caption = 'Game', resizable = True)
	glClearColor(0.5,0.7,1,1)
	pyglet.app.run()
		
