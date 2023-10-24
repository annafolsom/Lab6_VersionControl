def encode(user_password):  # AMF - Defined a new function.
    enc_list = list(user_password)  # AMF - Created a list separating the digits "123" --> ["1", "2", "3"]
    index = 0
    index_2 = 0
    index_3 = 0
    for element in enc_list:  # AMF - Loop to change the string into integers ["1", "2", "3"] --> [1, 2, 3]
        enc_list[index] = int(element)
        index += 1
    for element in enc_list:  # AMF - Loop to add 3 to integers [1, 2, 3] --> [3, 5, 6]
        enc_list[index_2] = element + 3
        index_2 += 1
    for element in enc_list:  # AMF -  Loop to change the integers to strings [3, 5, 6] --> ["3", "5", "6"]
        enc_list[index_3] = str(element)
        index_3 += 1
    encoded_number = "".join(enc_list)
    return encoded_number


if __name__ == '__main__':
    password = None
    encoded_password = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_input = int(input("Please enter an option:"))

        if user_input == 1:
            password = input("Please enter your password to encode:")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif user_input == 2:
            # Next two lines should be added to main logic once decode() is finished.
            # decoded_password = decode(encoded_password)
            # print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            pass

        elif user_input == 3:
            break
