with open('input.txt', 'r') as f:
    data = f.read()
    spelled_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n = 0
    for n in range(0,10):
        data = data.replace(str(spelled_numbers[n]), ((str(spelled_numbers[n])[0]) + (str(n)) + str(spelled_numbers[n])[-1] ))

    i = 0
    sum = 0
    first_digit = 0
    second_digit = 0
    first_digit_found = False
    for i in range(0, len(data)):
        if data[i] == '\n':
            first_digit_found = False
            sum += int(f'{first_digit}{second_digit}')
            first_digit = 0
            second_digit = 0

        if data[i].isnumeric():
            second_digit = data[i]
            if first_digit_found is False:
                first_digit = data[i]
                first_digit_found = True
        
    print(sum)