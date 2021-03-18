def quick_sort(random_array):
  smaller = []
  bigger = []
  if len(random_array) <= 1:
    return(random_array)
  else:
    pivot = random_array[0]
    smaller = [ i for i in random_array[1:] if pivot >= i ]
    bigger = [ i for i in random_array[1:] if pivot <= i ]
    return(quick_sort(smaller) + [pivot] + quick_sort(bigger))

if __name__ == '__main__':
  random_array = [5,4,3,7,6,8,2,1,]
  print(quick_sort(random_array))
