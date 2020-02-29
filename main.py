from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# add_edge(edges, 0, 0, 0, 100, 0, 0)
# add_edge(edges, 100, 0, 0, 100, 100, 0)
# add_edge(edges, 100, 100, 0, 0, 100, 0)
#
# transform = make_translate(100, 100, 0)
# matrix_mult(transform, edges)
#
# ident(transform)
# transform = make_scale(2,2,2)
# matrix_mult(transform, edges)
#
#
#
# draw_lines(edges, screen, color)
# display(screen)
#
#


parse_file( 'script', edges, transform, screen, color )
