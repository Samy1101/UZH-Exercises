# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.


def survival_rates(dataset):
    result_tuple = [[None, None], [None, None]]
    male_child = 0
    male_child_surv = 0
    male_adult = 0
    male_adult_surv = 0
    female_child = 0
    female_child_surv = 0
    female_adult = 0
    female_adult_surv = 0

    for records in dataset[1]:
        records = [v for i, v in enumerate(records) if i not in frozenset((1, 2, 5))]
        if records[1] == "male":
            if records[2] <= 15:
                male_child += 1
                if records[0]:
                    male_child_surv += 1
            if records[2] > 15:
                male_adult += 1
                if records[0]:
                    male_adult_surv += 1

        if records[1] == "female":
            if records[2] <= 15:
                female_child += 1
                if records[0]:
                    female_child_surv += 1
            if records[2] > 15:
                female_adult += 1
                if records[0]:
                    female_adult_surv += 1

    if male_child > 0:
        survival_rate = round(male_child_surv/male_child * 100, 1)
        result_tuple[0][0] = survival_rate

    if male_adult > 0:
        survival_rate = round(male_adult_surv / male_adult * 100, 1)
        result_tuple[1][0] = survival_rate

    if female_child > 0:
        survival_rate = round(female_child_surv / female_child * 100, 1)
        result_tuple[0][1] = survival_rate

    if female_adult > 0:
        survival_rate = round(female_adult_surv / female_adult * 100, 1)
        result_tuple[1][1] = survival_rate

    result_tuple[0] = tuple(result_tuple[0])
    result_tuple[1] = tuple(result_tuple[1])

    return tuple(result_tuple)

# You can play around with your solution from within this block.
if __name__ == '__main__':
    # Investigate the 'titanic.csv' file before you attempt a submission. You might
    # want to download the file to your machine and open it with the functions that
    # you have written in Task 1+2. The following example is not complete...
    print(survival_rates((
        ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
        [
            (True, '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'female', 38, 71.2833),
            (False, '3', 'Heikkinen Miss. Laina', 'female', 26, 7.925),
            (True, "1", "blabla", "male", 33, 25.0),
            (True, "1", "blabla", "male", 15, 25.0),
            (False, "1", "blabla", "male", 15, 25.0),
            (False, "1", "blabla", "male", 15, 25.0)

            # ...
        ]
    )))
