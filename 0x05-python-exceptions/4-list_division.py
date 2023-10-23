#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if list_length < 0:
        raise ValueError("list_length must be non-negative")

    result_list = []
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(
                my_list_2[i], (int, float)
            ):
                result_list.append(my_list_1[i] / my_list_2[i])
            else:
                print("wrong type")
                result_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
        except TypeError:
            print("wrong type")
            result_list.append(0)

    return result_list
