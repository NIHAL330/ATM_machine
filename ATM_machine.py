
# welcome message
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '0000']
amounts = [88500, 330490, 50950]
count = 0

print("  ⌜                                 ⌝")
print("      ⟫ WELCOME TO ATM MACHINE ⟪    ")
print("  ⌞                                 ⌟")
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print()
        print('⁜ INVALID USERNAME ✖ ⁜')
        print()

# pin entry
while count < 3:
    print()
    pin = input('PLEASE ENTER YOUR PIN NUMBER: ')
    if pin.isdigit():
        if user == 'user1':
            if pin == pins[0]:
                break
            else:
                count += 1
                print()
                print('⁜ INVALID PIN ✖ ⁜ ')
                print()

        if user == 'user2':
            if pin == pins[1]:
                break
            else:
                count += 1
                print()
                print('⁜ INVALID PIN ✖ ⁜')
                print()

        if user == 'user3':
            if pin == pins[2]:
                break
            else:
                count += 1
                print()
                print('⁜ INVALID PIN ✖ ⁜')
                print()
    else:
        print()
        print('⁜ PIN CONSISTS OF 4 DIGITS ⁜')
        print()
        count += 1

if count == 3:
    print()
    print('⁜ 3 UNSUCCESSFUL PIN ATTEMPTS, EXITING ⁜')
    print('!!!!! YOUR CARD HAS BEEN BLOCKED ⊘ !!!!!')
    print('⁜ PLEASE CONTACT WITH YOUR BANK ⁜')
    print()
    exit()

print()
print('⁜ LOGIN SUCCESSFUL ✔, CONTINUE ⁜')
print()
print()
print('      ',str.capitalize(users[n]), 'WELCOME TO ATM')
print('     ————⟦  ATM SYSTEM  ⟧————        ')

# Main menu
while True:
    print()
    response = input(
        'SELECT FROM FOLLOWING OPTIONS: \nBalance : [B] \nWithdraw : [W] \nDeposit : [D]  \nChange PIN : [P]  \nQuit : [Q] \nType The Letter Of Your Choices: ').lower()
    print()
    valid_responses = ['b', 'w', 'd', 'p', 'q']
    response = response.lower()
    if response == 'b':
        print()
        print('⁜',str.capitalize(users[n]), 'YOU HAVE ', amounts[n], 'RUPEES ON YOUR ACCOUNT ⁜')
        print()

    elif response == 'w':
        print()
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print()
        if cash_out % 10 != 0:
            print()
            print('⁜ AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEES NOTES ⁜')
            print()
        elif cash_out > amounts[n]:
            print()
            print('⁜ YOU HAVE INSUFFICIENT BALANCE ✖ ⁜')
            print()
        else:
            amounts[n] = amounts[n] - cash_out
            print()
            print('⁜ YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES ⁜')
            print()

    elif response == 'd':
        print()
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
        print()
        if cash_in % 10 != 0:
            print()
            print('⁜ AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 10 RUPEES NOTES ⁜')
            print()
        else:
            amounts[n] = amounts[n] + cash_in
            print()
            print('⁜ YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES ⁜')
            print()
    elif response == 'p':
        print()
        new_pin = int(input('ENTER A NEW PIN: '))
        print("————————————————————")
        new_ppin = int(input('CONFIRM NEW PIN: '))
        print()
        if new_ppin != new_pin:
                print()
                print('⁜ PIN MISMATCH ✖ ⁜')
                print()
        else:
                pins[n] = new_pin
                print()
                print('⁜ NEW PIN SAVED ✔ ⁜')
                print()
    elif response == 'q':
        print('⁜ THANK YOU FOR USING THIS ATM ⁜')
        print()
        exit()
    else:
        print()
        print('⁜ RESPONSE NOT VALID ⁜')
        print()