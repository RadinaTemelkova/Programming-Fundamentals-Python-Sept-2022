def password_validator(current_password):
    password_is_valid = True
    digit_counter = 0
    letter_counter = 0
    current_result = []

    if not (6 <= len(current_password) <= 10):
        password_is_valid = False
        current_result.append("Password must be between 6 and 10 characters")

    for symbol in current_password:
        if 48 <= ord(symbol) <= 57:
            digit_counter += 1
        elif 97 <= ord(symbol) <= 90 or 65 <= ord(symbol) <= 122:
            letter_counter += 1
        else:
            password_is_valid = False
            current_result.append("Password must consist only of letters and digits")
            break

    if not (digit_counter >= 2 and letter_counter >= 1):
        password_is_valid = False
        current_result.append("Password must have at least 2 digits")

    if password_is_valid:
        print("Password is valid")

    return current_result


password = input()
final_result = password_validator(password)
print("\n".join(final_result))


