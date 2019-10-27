# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def preprocess(records):

    head_line = records.pop(0)
    record_list = []

    survived_values = ["Survived", "survived", "yes", "Yes", "true", "True", "T", "Alive"]
    male_values = ["male", "Male", "m", "M", ]

    for record in records:
        record = list(record)

        if "" in record[:-1] or "undefined" in record[:-1] or "unknown" in record[:-1]:
            continue

        if record[0] in survived_values:
            record[0] = True

        else:
            record[0] = False

        if len(str(record[1])) != 1:
            continue
        elif 0 > int(record[1]) or 3 < int(record[1]):
            continue
        else:
            record[1] = int(record[1])

        if record[3] in male_values:
            record[3] = "male"
        else:
            record[3] = "female"

        if float(record[4]) <= 0.0 or float(record[4]) > 100.0:
            continue
        else:
            record[4] = float(record[4])

        if record[-1] == "" or record[-1] == "undefined" or float(record[-1]) < 0:
            record[-1] = 25.0

        record[-1] = float(record[-1])

        record_list.append(tuple(record))

    result = (head_line, record_list)
    return result


# You can play around with your solution from within this block.
if __name__ == '__main__':
    # Investigate the 'titanic.csv' file before you attempt a submission. You might
    # want to download the file to your machine and open it with the function that
    # you have written in Task 1. The following example is not complete...
    titanic = [
        ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
        ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
        ('no', '3', 'Braund Ms. Maria', 'Female', '22', ''),
        ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
        ('', '3', 'Vander Planke Miss. Augusta Maria', 'female', '', ''),
        ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')
        # ...
    ]

    print(preprocess(titanic))
