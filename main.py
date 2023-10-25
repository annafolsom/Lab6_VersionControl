# Encode() is created by Annalisa Folsom.
# Date: October 23, 2023
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
        if enc_list[index_2] >= 10:  # AMF - If adding 3 to a number is two digits, then take the num in the ones place.
            enc_list[index_2] = enc_list[index_2] % 10
        index_2 += 1

    for element in enc_list:  # AMF -  Loop to change the integers to strings [3, 5, 6] --> ["3", "5", "6"]
        enc_list[index_3] = str(element)
        index_3 += 1
    encoded_number = "".join(enc_list)
    return encoded_number

# Decode () is created by Deepak Guggilam
# Date: October 24. 2023


def decode(encoded_password):
    dec_list = list(encoded_password)   # Convert the encoded password to a list
    index = 0
    for element in dec_list:   # convert each digit in the list into an integer
        dec_list[index] = int(element)
        index += 1

    for index in range(len(dec_list)):
        dec_list[index] = (dec_list[index] - 3) % 10
# subtract 3 from each integer and make sure numbers are around 0-9 no negative numbers

    decoded_password = "".join(map(str, dec_list))
# join the all the characters into a single string using map function to apply it to each element in the dec_list
    return decoded_password


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
            if encoded_password is not None:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            else:
                print("You need to encode a password first.\n")

        elif user_input == 3:
            break
