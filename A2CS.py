def decimal_to_binary(number):
    number = int(number)
    binary = ""

    while number > 0:
        leftover = number % 2
        binary = binary + str(leftover)
        number = number // 2
    return binary


def binary_to_decimal(number):
    number = int(number)
    decimal = 0
    power = 0
    while number > 0:
        leftover = number % 10
        decimal += leftover * 2 ** power
        number = number // 10
        power += 1

    return decimal


def decimal_to_hex(number):
    number = int(number)
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_list = []
    while number > 0:
        leftover = number % 16
        if leftover in hex_dict:
            hex_list.append(hex_dict[leftover])
        else:
            hex_list.append(leftover)
        number = number // 16
    return hex_list


def hex_to_decimal(hex_list):
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    decimal = 0
    power = 0
    for number in hex_list:
        if number in hex_dict:
            decimal += hex_dict[number] * 16 ** power
        else:
            decimal += int(number) * 16 ** power
        power += 1
    return decimal
def main():
    while True:
        number = input("enter a number: ")

        if number.startswith('0x'):
            number = number[2:].upper()
            print("your decimal number is: ", hex_to_decimal(number))
            break

        elif number.startswith('0b'):
            number = number[2:]
            print("your decimal number is: ", binary_to_decimal(number))
            break
        else:
            print("your decimal number is: ", decimal_to_binary(number))
            break

    while True:
        continue_game = input("do you want to continue? ")
        if continue_game != "yes":
            print("goodbye")
            break
        else:
            main()
main()


