def next_bigger(value: int):
    if(value > 9):
        list_of_digits = [digit for digit in str(value)]
        list_of_digits[-1], list_of_digits[-2] = list_of_digits[-2], list_of_digits[-1]
        new_value = int(''.join(list_of_digits))
        if(new_value > value):
            return new_value
    return -1


if __name__ == "__main__":
    print(next_bigger(12))
    print(next_bigger(513))
    print(next_bigger(2017))
    print(next_bigger(9))
    print(next_bigger(111))
    print(next_bigger(531))
