import os

#gibt nur 2.75 Punkte. Fehler noch nicht gefunden.

def get_average_grade(path):
    if not os.path.exists(path):
        return None

    file = open(path, 'r')
    str_nmbr = ""
    float_nmbr = 0.0
    sum = 0
    counter = 0
    average = 0

    for line in file.readlines():
        for c in line:
            if c == "#":
                break
            continue

        colon_idx = line.find(":")

        for i in line[colon_idx:]:
            if i.isdigit() or i == ".":
                str_nmbr += i
            if i == ":":
                counter += 1
                str_nmbr = ""

        if float_nmbr != float(str_nmbr):
            float_nmbr = float(str_nmbr)
            sum += float_nmbr

    average = sum / counter

    return average


# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(get_average_grade("public/my_grades.txt"))