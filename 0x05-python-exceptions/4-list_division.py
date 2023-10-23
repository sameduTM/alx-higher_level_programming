#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            if i < len(my_list_1) and i < len(my_list_2):
                element1 = my_list_1[i]
                element2 = my_list_2[i]

                if isinstance(element1, (int, float)) and isinstance(
                    element2, (int, float)
                ):
                    if element2 != 0:
                        result.append(element1 / element2)
                    else:
                        print("division by 0")
                        result.append(0)
                else:
                    print("wrong type")
                    result.append(0)
            else:
                print("out of range")
                result.append(0)
    except Exception as e:
        print("An unexpected error occurred:", e)

    return result
