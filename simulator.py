from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



window = 0
width, height = 500, 400


start_id = 0;

def assign_id():

	start_id = start_id + 1
	return start_id

class Point:

	def __init__(self, x_val, y_val):

		self.id = assign_id()

		self.x = x_val
		self.y = y_val

class Line:

	def __init__(self, point_1, point_2):
		
		self.id = assign_id()

		self.point1 = point_1
		self.point2 = point_2

# 	array_reference
# 	
#	[[x1, y1], [x2, y2], [x3, y3], [x4, y4], ... ]
#

class allowed_area:

	def __init__(self, array_reference, keep_boolean = True):

		self.array_ref = array_reference
		self.keep_bool = keep_boolean


############# these are examples #############

def draw_rect_example(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def draw_tri_example(x, y, width, height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x, y + height)
    glEnd()

def draw_polygon_example():
	glBegin(GL_POLYGON)
	glVertex2f(10, 10)
	glVertex2f(20, 20)
	glVertex2f(30, 40)
	glVertex2f(20, 40)
	glVertex2f(10, 20)
	glEnd()

############# these are examples #############

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width, height)

    glColor3f(0.0, 0.0, 1.0)
    
    ###################################
    # uncomment these to check it out #
    ###################################

    draw_rect_example(10, 10, 200, 100)
    #draw_tri_example(10, 10, 200, 100)
    #draw_polygon_example()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)

window = glutCreateWindow("Lawn Mower Simulator")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()  