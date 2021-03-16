def binary_search(max_index, min_index):
  mid_index = (max_index + min_index) // 2
  if array[mid_index] == value:
    return(mid_index)
  if value < array[mid_index]:
    max_index = mid_index - 1
  else:
    min_index = mid_index + 1
  return(binary_search(max_index, min_index))

if __name__ == '__main__':
  array = [1,3,5,11,12,13,17,22,25,28,]
  value = 5
  min_index = 0
  max_index = len(array) - 1

  print(binary_search(max_index,min_index))


