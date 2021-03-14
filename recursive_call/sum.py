def sum_num(num_list):
  if len(num_list) == 0:
    return(0)
  else:
    return(num_list[0] + sum_num(num_list[1:]))

print(sum_num([1,2,3,4,]))
