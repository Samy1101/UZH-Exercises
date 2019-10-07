pwd = "QQaa99++"

valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-/*"

upper_case_count = 0
lower_case_count = 0
digit_count = 0
special_count = 0
are_characters_valid = True
is_valid = False

for c in pwd:
    if c not in valid_characters:
        are_characters_valid = False

for i in pwd:
    if i.isupper():
        upper_case_count += 1
    if i.islower():
        lower_case_count += 1
    if i.isdigit():
        digit_count += 1
    if i == "+" or i == "-" or i == "/" or i == "*":
        special_count += 1

if 8 <= len(pwd) <= 16 and are_characters_valid:
    if upper_case_count >= 2 and lower_case_count >= 2 and digit_count >= 2 and special_count >= 2:
        is_valid = True

print(is_valid)
print(upper_case_count, digit_count, lower_case_count, special_count)
