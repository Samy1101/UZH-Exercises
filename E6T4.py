# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.


def visualize(records):
    all_class = 0
    first_class = 0
    second_class = 0
    third_class = 0
    first_surv = 0
    second_surv = 0
    third_surv = 0


    for record in records[1]:
        record = record[:2]

        if record[1] == 1:
            all_class += 1
            first_class += 1
            if record[0]:
                first_surv += 1

        if record[1] == 2:
            all_class += 1
            second_class += 1
            if record[0]:
                second_surv += 1

        if record[1] == 3:
            all_class += 1
            third_class += 1
            if record[0]:
                third_surv += 1

    first_total = round(first_class / all_class * 100, 1)
    first_tot_char = 7 + round(first_total / 5)
    second_total = round(second_class / all_class * 100, 1)
    second_tot_char = 7 + round(second_total / 5)
    third_total = round(third_class / all_class * 100, 1)
    third_tot_char = 7 + round(third_total / 5)

    first_alive = round(first_surv / first_class * 100, 1)
    first_ali_char = 7 + round(first_alive / 5)
    second_alive = round(second_surv / second_class * 100, 1)
    second_ali_char = 7 + round(second_alive / 5)
    third_alive = round(third_surv / third_class * 100, 1)
    third_ali_char = 7 + round(third_alive / 5)

    first_tot_str = "Total |                    | %s" % first_total + "%"
    first_tot_str =first_tot_str[:6] + first_tot_str[6:first_tot_char].replace(" ", "*") + first_tot_str[first_tot_char:]

    first_ali_str = "Alive |                    | %s" % first_alive + "%"
    first_ali_str = first_ali_str[:6] + first_ali_str[6:first_ali_char].replace(" ", "*") + first_ali_str[first_ali_char:]

    second_tot_str = "Total |                    | %s" % second_total + "%"
    second_tot_str =second_tot_str[:6] + second_tot_str[6:second_tot_char].replace(" ", "*") + second_tot_str[second_tot_char:]

    second_ali_str = "Alive |                    | %s" % second_alive + "%"
    second_ali_str = second_ali_str[:6] + second_ali_str[6:second_ali_char].replace(" ", "*") + second_ali_str[second_ali_char:]

    third_tot_str = "Total |                    | %s" % third_total + "%"
    third_tot_str =third_tot_str[:6] + third_tot_str[6:third_tot_char].replace(" ", "*") + third_tot_str[third_tot_char:]

    third_ali_str = "Alive |                    | %s" % third_alive + "%"
    third_ali_str = third_ali_str[:6] + third_ali_str[6:third_ali_char].replace(" ", "*") + third_ali_str[third_ali_char:]

    return "\n".join(["== 1st Class ==", first_tot_str, first_ali_str, "== 2nd Class ==", second_tot_str, second_ali_str,
                      "== 3rd Class ==", third_tot_str, third_ali_str])



# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(visualize((
        ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
        [
            (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'female', 38, 71.2833),
            (True, 2, 'Flunky Mr Hazelnut', 'female', 18, 51.2),
            (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
        ]
    )))
