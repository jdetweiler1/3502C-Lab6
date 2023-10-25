# Jackson Detweiler, COP 3502C, Lab 6 10/25

def encode(password):
    new_password = ""
    for i in range(0, len(password)):
        new_char = int(password[i]) + 3
        if new_char >= 10:
            new_password = new_password + (str(new_char)[-1])
        else:
            new_password = new_password + str(new_char)
    return new_password


def dencode(password):
    new_password = ""
    for i in range(0, len(password)):
        new_char = int(password[i]) - 3
        if new_char < 0:
            new_password = new_password + (str(new_char)[-1])
        else:
            new_password = new_password + str(new_char)
    return new_password


