with open('input.txt', 'r') as f:
    data = f.read()
    data = data.replace(' ','').replace('red','r').replace('blue','b').replace('green','g').replace(';','').replace('game','')
    sum = 0
    ready = False
    red, green, blue = 0, 0, 0
    analyze = ''
    game = 0
    for i in range(0,len(data)):
        if data[i] == '\n':
            sum += (red * blue * green)
            red, green, blue = 0, 0, 0
            game += 1
        if ready is True:
            if data[i].isnumeric():
                analyze = str(data[i])
                i += 1
                if data[i].isnumeric():
                    analyze = analyze + str(data[i])
                    i += 1
                if data[i] == 'r' and int(analyze) > red:
                    red = int(analyze)
                elif data[i] == 'b' and int(analyze) > blue:
                    blue = int(analyze)
                elif data[i] == 'g' and int(analyze) > green:
                    green = int(analyze)    
        if data[i] == ':':
            ready = True
print(sum)