with open('input.txt') as f:
    data = f.read()
    length = len(data)
    winning_numbers = []
    owned_numbers = []
    proceed_winning = False
    proceed_owned = False
    analyze = ''
    sum = 0
    copies = 0
    line = 0
    height = 0
    for i in range(0, length):
        if data[i] == '\n':
            height += 1
    repeats = []
    for i in range(height):
        repeats.append(1)
    for i in range(0, length):
        copies = 0
        if data[i] == '\n':
            proceed_owned = False
            owned_numbers.append(int(analyze))
            for j in range(len(owned_numbers)):
                if owned_numbers[j] in winning_numbers:
                    copies += 1
            for l in range(repeats[line]):
                for k in range(copies):
                    repeats[line + k + 1] += 1
            line += 1       
            analyze = ''
            winning_numbers.clear()
            owned_numbers.clear()
            proceed_winning = False
            proceed_owned = False
        elif proceed_winning is True and proceed_owned is False:
            if data[i].isnumeric():
                analyze += data[i]
            elif not data[i].isnumeric() and analyze != '':
                winning_numbers.append(int(analyze))
                analyze = ''
        if proceed_winning is False and proceed_owned is True:
            if data[i].isnumeric():
                analyze += data[i]
            elif not data[i].isnumeric() and analyze != '':
                owned_numbers.append(int(analyze))
                analyze = ''
        elif data[i] == ':':
            proceed_winning = True
            analyze = ''
        elif data[i] == '|':
            proceed_winning = False
            proceed_owned = True
            analyze = ''
sum = 0
for n in range(len(repeats)):
    sum += repeats[n]
print(sum)