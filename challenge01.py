'''
Python challenge 1
'''


def main():
    encryption = ""
    shift = 2
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    for c in text:
        # check if character is an lowercase letter
        if c.islower():

            c_index = ord(c) - ord("a")

            # perform the shift
            new_index = (c_index + shift) % 26

            # convert to new character
            new_unicode = new_index + ord("a")

            new_character = chr(new_unicode)

            # append to encrypted string
            encryption = encryption + new_character

        else:

            # since character is not lowercase, leave it as it is
            encryption += c

    print("Plain text:", text)

    print("Encrypted text:", encryption)


if __name__ == '__main__':
    main()
