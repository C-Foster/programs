import csv

with open('patrons.csv', 'r') as data_file:
    html_out = '<ul>\n'
    reader = csv.DictReader(data_file)
    next(reader)
    for line in reader:
        if line["first"] == 'No Reward':
            break
        html_out += f'\t<li>{line["first"]} {line["last"]}</li>\n'
    html_out += '</ul>'
    print(html_out)
