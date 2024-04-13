import sketchingpy
import latk

width = 500
height = 500
sketch = sketchingpy.Sketch2D(width, height)
sketch.clear("#FFFFFF")

latk = latk.Latk("latk_logo.latk")

def render(sketch):
    for layer in latk.layers:
        for frame in layer.frames:
            for stroke in frame.strokes:
                r = int(stroke.color[0] * 255)
                g = int(stroke.color[1] * 255)
                b = int(stroke.color[2] * 255)
                col = rgb_to_hex(r,g,b)

                points = []
                for point in stroke.points:
                    x = int(width/2.65) + int(point.co[1] * width/2)
                    y = int(height/2) - int(point.co[2] * height/2)
                    points.append((x,y))
                if (len(points) > 1):
                    draw_line(points, col)

def rgb_to_hex(r, g, b):
	return '#%02x%02x%02x' % (r, g, b)

def draw_line(points, col):
	sketch.clear_fill()
	sketch.set_stroke(col)
	sketch.set_stroke_weight(5)
	shape_outer = sketch.start_shape(points[0][0], points[0][1])

	for point in points:
		shape_outer.add_line_to(point[0], point[1])

	shape_outer.end()
	sketch.draw_shape(shape_outer)

def get_mouse():
	mouse = sketch.get_mouse()
	x = mouse.get_pointer_x()
	y = mouse.get_pointer_y()
	return x, y

sketch.on_step(render)

sketch.show()