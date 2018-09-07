import string
import secrets


def char_input():
    """Choose password character options and return list of choices."""
    char_list = []
    chars = [
        string.ascii_uppercase, string.ascii_lowercase,
        string.digits, "!@#$%^&*"
    ]
    input_list = [
        "uppercase letters (A-Z)", "lowercase letters (a-z)",
        "numbers (0-9)", "special characters (!@#$%^&*)"
    ]

    for i in range(4):
        while True:
            choice = input(
                "Include {}?  'yes' or 'no': "
                .format(input_list[i])
            ).lower()
            if choice == "yes":
                char_list.append(chars[i])
                break
            elif choice == "no":
                break
            else:
                print("Ah ah ah, you didn't say the magic word!")
    return char_list


def new_pwd(char_list):
    """Choose length of password and return password as string."""
    while True:
        try:
            length = int(input("Length of password (5-40): "))
            if length < 5:
                print("Password too short! Please try again.")
            elif length > 40:
                print("Password too long! Please try again.")
            else:
                break
        except ValueError:
            print("Ah ah ah, you didn't say the magic word!")

    password = []
    for i in range(length):
        password.append(secrets.choice(secrets.choice(char_list)))
    return "".join(password)


def main():
    print("Your password: {}".format(new_pwd(char_input())))


if __name__ == "__main__":
    main()
