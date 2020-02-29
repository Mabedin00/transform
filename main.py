from display import *
from draw import *
from matrix import *
from parser import *

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

def parse_file( fname, points, transform, screen, color ):
    with open(fname, "r") as scripts:
        lines = scripts.readlines()
    lines = [l.strip() for l in lines]
    l = 0
    while (l < len(lines)):
        # print(lines[l], l)
        if (lines[l] == "line"):
            args = lines[l + 1].split(" ")
            args = [int(x) for x in args]
            l += 1
            add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
        elif (lines[l] == "ident"):
            ident(transform)
        elif (lines[l] == "scale"):
            args = lines[l + 1].split(" ")
            args = [int(x) for x in args]
            l += 1
            transform = make_scale(args[0], args[1], args[2])
        elif (lines[l] == "move"):
            args = lines[l + 1].split(" ")
            args = [int(x) for x in args]
            l += 1
            transform = make_translate(args[0], args[1], args[2])
        elif (lines[l] == "rotate"):
            args = lines[l + 1].split(" ")
            l += 1
            transform = make_rotate(args[0], int(args[1]))
        elif (lines[l] == "apply"):
            matrix_mult(transform, points)
        elif (lines[l] == "display"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif (lines[l] == "save"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_ppm(screen, lines[l+1])
            l += 1
        else:
            break
        l += 1
    return


parse_file("script", edges, transform, screen, color)
