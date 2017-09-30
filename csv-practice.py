import csv

with open('patrons.csv', newline='') as data_file:
    reader = csv.DictReader(data_file)

    header = next(reader)
    lines = []

    for line in reader:
        if line['first'] == 'No Reward':
            break
        lines.append(line)

    for line in lines:
        print(f'{line["first"]} {line["last"]}')
