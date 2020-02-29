from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname, "r") as scripts:
        lines = scripts.readlines()
    lines = [l.strip() for l in lines]
    l = 0
    while (l < len(lines)):
        print(lines[l], l)
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
            save_extension(screen, lines[l + 1])
            l += 1
        else:
            break
        l += 1
    return
