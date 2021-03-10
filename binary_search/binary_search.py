import argparse
import math

class binary_search():
  def __init__(self, array, value):
    self.array = array
    self.value = value

  def search(self):
    min_index = 0
    max_index = len(self.array) - 1
    mid_index = 1 + (max_index + min_index) / 2
    while min_index <= max_index:
      if self.array[mid_index] == self.value:
        return(mid_index)
      if self.value < self.array[mid_index]:
        max_index = mid_index - 1
      else:
        min_index = mid_index + 1
      mid_index = (max_index + min_index) / 2

def main():
  binary_search(array, value).search()

if __name__ == '__main__':
  array = [1,3,5,11,12,13,17,22,25,28,]
  value = 28
  main()
