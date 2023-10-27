#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
  new_list = []
  for i in range(list_length):
    try:
      if i >= len(my_list_1) or i >= len(my_list_2):
        raise IndexError("out of range")
      try:
        x = my_list_1[i] / my_list_2[i]
      except ZeroDivisionError:
        x = 0
        print("division by 0")
      except TypeError:
        x = 0
        print("wrong type")
      finally:
        new_list.append(x)
    except IndexError:
       print("out of range")
       new_list.append(0)
  return new_list

