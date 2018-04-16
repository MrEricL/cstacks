from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

t = new_matrix() ###	FIX THIS
ident(t)

stack = [t]

parse_file( 'script', stack, edges, polygons, transform, screen, color )
