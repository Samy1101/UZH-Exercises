plain_text = "b CD,. ew32"
shift_by = -1
encoded = ""

if shift_by >= 26 or shift_by < 0:
    shift_by %= 26

for i in plain_text:
    ascii_value = ord(i.lower()) + shift_by
    if ascii_value > ord("z"):
        ascii_value = ord(i) - (26 - shift_by)

    if i.isalpha():
        if i.isupper():
            encoded += chr(ascii_value).upper()
        if i.islower():
            encoded += chr(ascii_value)
    else:
        encoded += i

print(encoded)
