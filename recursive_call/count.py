def count_num(num_list,count):
  if len(num_list) == 0:
    return(count)
  else:
    num_list.pop()
    count += 1
    return(count_num(num_list,count))

print(count_num([1,2,3,4,,], 0))
