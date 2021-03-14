def count_num(num_list):
  if len(num_list) == 0:
    return(0)
  else:
    return(1 + count_num(num_list[1:]))

print(count_num([1,2,3,4,,]))
