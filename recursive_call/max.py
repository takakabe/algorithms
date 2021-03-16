def max_num(num_list):
  if len(num_list) == 1:
    return(num_list[0])
  else:
    return(num_list[0] if num_list[0] > num_list[1] else max_num(num_list[1:]))

print(max_num([10,5,3,4,]))
