from collections import OrderedDict


def read_data(file):
    looping = True
    phrase = ''
    while looping:
        char = file.read(1)
        if char == "," or char == "" or char == "\n":
            looping = False
        else:
            phrase += char
    return phrase


user_input = ''
item_list = []
purchases = []
input_list = []
quantities = []
subs = []

with open("Stock.csv", "r") as f:
    Looping = True
    while Looping:
        pin_variable = read_data(f)
        desc_variable = read_data(f)
        price_variable = read_data(f)
        item = [pin_variable, desc_variable, price_variable]
        item_list.append(item)
        if pin_variable == '':
            print("End of file reached.")
            Looping = False

item_list = item_list[:-1]

while user_input != "STOP":
    print("Enter pin to search for: ")
    user_input = input().upper()
    if user_input == "STOP":
        break

    for i in range(len(item_list)):
        if user_input == item_list[i][0]:
            break
    else:
        input_list.append(user_input)
        purchases.append([user_input, "Not found", "0"])

    for i in range(len(item_list)):
        if user_input not in input_list:
            if user_input == item_list[i][0]:
                input_list.append(user_input)
                purchase = item_list[i]
                purchases.append(purchase)
        else:
            if user_input == item_list[i][0]:
                input_list.append(user_input)

for i in range(len(purchases)):
    if purchases[i][1] == "Not found":
        quantities.append(0)
    else:
        value = input_list.count(purchases[i][0])
        quantities.append(value)

input_list = list(OrderedDict.fromkeys(input_list))
quantity_dict = dict(zip(input_list, quantities))

if len(input_list) > 0:
    print()
    tab = "\t"
    print("Pin:{0}Name:{0}{0}Price:{0}Quantity:{0}Sub-Total:".format(tab))
    # print("Pin:" + "\t" + "Name:" + "\t"*2 + "Price:" + "\t" + "Quantity:" + "\t" + "Sub-Total:")
    print("-"*50)

for i in range(len(purchases)):
    quantity = quantity_dict.get(purchases[i][0], 0)
    sub = int(purchases[i][2]) * int(quantity_dict.get(purchases[i][0], 0))
    subs.append(int(sub))
    if sub > 0:
        print(
            purchases[i][0] + "\t" +
            purchases[i][1] + "\t"*2 +
            purchases[i][2] + "\t"*2 +
            str(quantity) + ("\t"*3) + "{:03}".format(sub)
        )
    elif sub == 0:
        print(
            purchases[i][0] + "\t" +
            purchases[i][1]
        )
    else:
        print("Something went horribly wrong.")

total = (sum(subs))
if total > 0:
    total = total / 100
    print("-"*50)
    print("TOTAL:" + "\t"*9 + "£{:.2f}".format(total))
else:
    print("Nothing to display.")
