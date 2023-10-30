def is_straight(hand, table):
    tmp_hand = convert_name(hand)
    tmp_table = convert_name(table)
    #Check if straight
    straight_calc=[]
    for i in range(len(table)):
        if i < 2:
            straight_calc.append((int(tmp_hand[i][0]), int(tmp_table[i][-1])))
        if i < 5:
            straight_calc.append((int(tmp_table[i][0]), int(tmp_table[i][-1])))
    #[(2, 1),(3,1),(5,1),(4,3), (6,2),(11,1),(12,1)]]
    straight_calc.sort()
    start=straight_calc[0]
    temp=1
    longest = [start]  # Used for finding longest sequence of consecutive numbers
    for r in range(1,len(straight_calc)):
        if straight_calc[r][0] == start[0]+temp:
            longest.append(straight_calc[r])
            temp += 1
        else:
            start = straight_calc[r]
            longest = [start]
            temp = 1
        #Check if Straight flush
        if len(longest) == 5:
            s = longest[0][1]
            while len(longest) > 0:
                if longest[0][1] == s:
                    del longest[0]
                else:
                    #Straight
                    return 6 + int(tmp_hand[0][0])/100. + int(tmp_table[1][0])/100.
            if start[0] == 10:
                #Royal Flush
                return 10 + int(tmp_hand[0][0]) / 100. + int(tmp_table[1][0]) / 100.
            #Straight Flush
            return 9 + int(tmp_hand[0][0]) / 100. + int(tmp_table[1][0]) / 100.
    return int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.

def is_pair(hand,table):
    tmp_hand = convert_name(hand)
    tmp_table = convert_name(table)
    max_pair=0
    all_pairs = {}
    for i in range(len(tmp_table)):
        if i < 2:
            all_pairs[tmp_hand[i][0]] = 1 + all_pairs.get(tmp_hand[i][0], 0)
        if i < 5:
            all_pairs[tmp_table[i][0]] = 1 + all_pairs.get(tmp_table[i][0], 0)
        max_pair = max(max_pair, all_pairs[tmp_table[i][0]], all_pairs[tmp_table[i][0]])
    if 4 in all_pairs.values():
        #Four of a kind
        return 7+int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.
    elif 3 in all_pairs.values():
        if 2 in all_pairs.values():
            #Full House
            return 6 + int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.
        #Three of a kind
        return 3 + int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.
    elif 2 in all_pairs.values():
        if list(all_pairs.values()).count(2) == 2:
            #Two Pair
            return 2 + int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.
        #Pair
        return 1 + int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.
    return int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.

def is_flush(hand,table):
    tmp_hand = convert_name(hand)
    tmp_table = convert_name(table)
    all_suites={}
    for i in range(len(tmp_table)):
        if i < 2:
            all_suites[tmp_hand[i][-1]] = 1+all_suites.get(tmp_hand[i][-1], 0)
        if i < 5:
            all_suites[tmp_table[i][-1]] = 1+all_suites.get(tmp_table[i][-1], 0)
    for i,y in all_suites.items():
        if y == 5:
            return 5+int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.
    return int(tmp_hand[0][0]) / 100. + int(tmp_hand[1][0]) / 100.


def convert_name(cards):
    tmp = []
    for i in cards:
        tmp.append(i.split(" "))
    for i in range(len(tmp)):
        if tmp[i][0] == "J":
            tmp[i][0] = "11"
        elif tmp[i][0] == "K":
            tmp[i][0] = "12"
        elif tmp[i][0] == "Q":
            tmp[i][0] = "13"
        elif tmp[i][0] == "A":
            tmp[i][0] = "14"
    return tmp