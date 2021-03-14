def sum_num(num_list):
  if len(num_list) == 0:
    return(0)
  else:
    num = num_list.pop()
    return(num + sum_num(num_list))

print(sum_num([1,2,3,4,]))
