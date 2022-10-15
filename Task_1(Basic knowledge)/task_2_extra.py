def convert_to_ipv4(value: int):
    binary_value_in_list = list(bin(value)[2:]) # [2:] added to remove '0b' prefix at beggining
    if(len(binary_value_in_list) > 32):
         raise Exception("Value is bigger than 32-bit integer")
    while (len(binary_value_in_list) < 31): # fill with necessary zeros
        binary_value_in_list.insert(0, '0')
    first_value = int(''.join(binary_value_in_list[0:8]), 2)          # Generate first value in IPv4
    second_value = int(''.join(binary_value_in_list[0+8*1:8+8*1]), 2) # Generate second value in IPv4
    third_value = int(''.join(binary_value_in_list[0+8*2:8+8*2]), 2)  # Generate third value in IPv4
    forth_value = int(''.join(binary_value_in_list[0+8*3:8+8*3]), 2)  # Generate forth value in IPv4
    return f"{first_value}.{second_value}.{third_value}.{forth_value}"


if __name__ == "__main__":
    print(convert_to_ipv4(2149583361))
    print(convert_to_ipv4(32))
    print(convert_to_ipv4(0))

