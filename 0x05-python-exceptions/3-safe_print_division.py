#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result:", result)
    except Exception as e:
        print(f"{e}")
    finally:
        if result is not None:
            print("Inside result:", result)
    return result
