# python3 -m cProfile -o output.txt hw06.py

import pstats

p = pstats.Stats('output.txt')
p.print_stats()