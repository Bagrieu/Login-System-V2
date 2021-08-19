from time import sleep
cont = 0
while True:
    if cont == 0:
        # if is your first time in the system you gonna see this
        print('-=' * 10)
        print('Welcome to my menu system, summoner!')
        print('-=' * 10)
        print('''Choose an option:\n(' 1 ') Login in the system.\n(' 2 ') Register in the system.\n(' 0 ') To say goodbye.''')
        print('-=' * 10)
        menu_res = str(input('Put your option: ')).strip().lower()[0]
        if menu_res == '0':
            #exit
            break
        # elif menu_res == 1:#Login
        #     #Function login system
        # elif menu_res == 2:# register
        #     #Function register
    else:
        _continue = str(input('''Wish continue?\n(' Y ') Yes.\n(' N ') No.\nOption:''')).strip().lower()[0]
        if _continue in 'yn':
            if _continue == 'y':
                print('-=' * 10)
                print('Welcome back buddy xD!')
                print('-=' * 10)
                print('''Choose an option:\n(' 1 ') Login in the system.\n(' 2 ') Register in the system.\n(' 0 ') To say goodbye.''')
                menu_res = str(input('Put another option: ')).strip().lower()[0]
                if menu_res == '0':
                    print('Closing SYsTeEe.....m')
                    sleep(1)
                    print('c')
                    sleep(1)
                    print('c.')
                    sleep(1)
                    print('c..')
                    sleep(1)
                    print('you')
                    sleep(1)
                    print('lateer!')
                    sleep(1)
                    break
            else:
                print('Closing SYsTeEe.....m')
                sleep(1)
                print('c')
                sleep(1)
                print('c.')
                sleep(1)
                print('c..')
                sleep(1)
                print('you')
                sleep(1)
                print('lateer!')
                sleep(1)
                break
        else:
            _continue = str(input('''Do you want to continue?\n(' Y ') means Yes.\n(' N ') means No.\nYou Option: ''')).strip().lower()[0]
    if cont == 0:
        cont += 1
        # Stopping the count
