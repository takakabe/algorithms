class selection_sort():
  def __init__(self, array):
    self.random_array = array

  def sort(self):
    result_array = []
    for i in range(len(self.random_array)):
      min_index = 0
      for j in range(1, len(self.random_array)):
        if self.random_array[min_index] > self.random_array[j]:
          min_index = j
      result_array.append(self.random_array[min_index])
      self.random_array = self.random_array[:min_index] + self.random_array[min_index+1:]
    return(result_array)

def main():
  selection_sort(random_array).sort()

if __name__ == '__main__':
  random_array = [8,4,3,7,6,5,2,1,]
  main()
  