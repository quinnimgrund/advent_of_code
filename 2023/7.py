with open('input.txt', 'r') as f:
    hands = f.read().split('\n')
    for i in range(len(hands)):
        hands[i] = hands[i].split(' ')
        hands[i][1] = int(hands[i][1])
    
    rank = []
    
    def cardvaluesort(cards):
        values = "J23456789TQKA"
        for i in range(len(cards)):
            cards[i][2] = 0
            for j in range(5):
                tmp = 1000**(5 - j)
                cards[i][2] += tmp * (values.rfind(cards[i][0][j]) + 1)
        cards.sort(key=lambda x: x[2])
        return(cards)
    
    def sorthands(hands):
        fives = []
        fours = []
        fulls = []
        threes = []
        twos = []
        ones = []
        highs = []
        for i in range(len(hands)):
            tempset = sorted(set(hands[i][0]))
            jless = sorted(set(hands[i][0]))
            if 'J' in jless:
                jless.remove('J')
            if len(jless) <= 1:
                hands[i].append(7)
                fives.append(hands[i])
            elif (len(tempset) == 2 and (hands[i][0].count(tempset[0]) == 4 or hands[i][0].count(tempset[1]) == 4)) or ((len(jless) == 2) and (hands[i][0].count(jless[0]) + hands[i][0].count('J') == 4 or hands[i][0].count(jless[1]) + hands[i][0].count('J') == 4)):
                hands[i].append(6)
                fours.append(hands[i])
            elif len(jless) == 2:
                hands[i].append(5)
                fulls.append(hands[i])
            elif (3 >= len(jless) >= 2) and (hands[i][0].count(jless[0]) + hands[i][0].count('J') == 3 or hands[i][0].count(jless[1]) + hands[i][0].count('J') == 3 or hands[i][0].count(jless[2]) + hands[i][0].count('J') == 3):
                hands[i].append(4)
                threes.append(hands[i])
            elif len(jless) == 3:
                hands[i].append(3)
                twos.append(hands[i])
            elif len(jless) == 4:
                hands[i].append(2)
                ones.append(hands[i])
            elif len(jless) == 5:
                hands[i].append(1)
                highs.append(hands[i])
            else:
                print(hands[i], 'not counted')
                
        hands.clear()
        fives = cardvaluesort(fives)
        fours = cardvaluesort(fours)
        fulls = cardvaluesort(fulls)
        threes = cardvaluesort(threes)
        twos = cardvaluesort(twos)
        ones = cardvaluesort(ones)
        highs = cardvaluesort(highs)
        
        for i in range(len(highs)):
            hands.append(highs[i])
        for i in range(len(ones)):
            hands.append(ones[i])
        for i in range(len(twos)):
            hands.append(twos[i])
        for i in range(len(threes)):
            hands.append(threes[i])
        for i in range(len(fulls)):
            hands.append(fulls[i])
        for i in range(len(fours)):
            hands.append(fours[i])
        for i in range(len(fives)):
            hands.append(fives[i])
        
        
        return(hands)
    
    hands = sorthands(hands)
    winnings = 0
    for i in range(len(hands)):
        winnings += hands[i][1] * (i + 1)
    print(winnings)