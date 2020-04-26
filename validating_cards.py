# Name:- Abhay Kumar Modi

for _ in range(int(input())):
    card_num = input()
    if card_num[0] != '4' and card_num[0] != '5' and card_num[0] != '6':
        print('Invalid')
        continue
    dig_count = 0
    consec = 1
    prev = card_num[0]
    loop_broken = False
    for i in range(len(card_num)):
        if card_num[i] != '-':
            if i != 0 and card_num[i] == prev:
                consec += 1
            else:
                consec = 1
            if card_num[i] != '-':
                prev = card_num[i]
        if consec >= 4:
            print('Invalid')
            loop_broken = True
            break
        if ord(card_num[i]) < 48 or ord(card_num[i]) > 57:
            if (i != 4 and i != 9 and i != 14) or card_num[i] != '-':
                print('Invalid')
                loop_broken = True
                break
        else:
            dig_count += 1
    if not loop_broken:
        if dig_count != 16:
            print('Invalid')
        else:
            print('Valid')