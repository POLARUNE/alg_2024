# from data_unsorted import numbers
# from data_unsorted_a_lot import numbers
from vis import QuickSortVisualizer as Visualizer
# from vis import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  print('before:', array)
  count = len(array)

  print('after :', array)

if __name__ == '__main__':
  seed('Hello')
  vis = Visualizer('Quick Sort')
  while True:
    count = randint(20, 40)
    array = [ randint(1, 99) for _ in range(count) ]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break
