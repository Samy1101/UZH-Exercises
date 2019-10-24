import csv
# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def read_csv(path):

    data_list = []

    with open(path, 'r') as csv_file:
        csv_read = csv.reader(csv_file)

        for line in csv_read:
            if len(line) != 0:
                data_list.append(tuple(line))

    return data_list

# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(read_csv("public/example.csv"))