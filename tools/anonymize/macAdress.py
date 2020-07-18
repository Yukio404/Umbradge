def macAdress():

    choice = input("Do You Want to Chose You're Next MAC's Adress (default's choice = n) ? <y/n>")

    if choice == 'n' or 'N' or 'no' or 'NO':
        device = input("Do You Now Your Network's Device's Type ? <y/n>")
        if device == 'y' or 'Y' or 'yes' or 'YES':
            device = input("Network's Device's Type: ")
            print('\n')
            os.system('ifconfig \t' + device + '\tdown')
            os.system('macchanger -r ' + device)
            os.system('ifconfig\t' + device + '\tup')
            exit()
        if device == 'n' or 'N' or 'no' or 'NO':
            print("To Now Your Network's Device's Type, type 'ifconfig'")
            exit()

    if choice == 'y' or 'Y' or 'yes' or 'YES':
        macAdress = input("Fill Your Next Adress: ")
        device = input("Do You Now Your Network's Device's Type ? <y/n>")
        if device == 'y' or 'Y' or 'yes' or 'YES':
            device = input("Network's Device's Type: ")
            os.system('ifconfig ' + device + ' down')
            os.system('macchanger --mac ' + macAdress, device)
            os.system('ifconfig' + device + ' up')
            exit()
        if device == 'n' or 'N' or 'no' or 'NO':
            print("To Now Your Network's Device's Type, type 'ifconfig'")
            exit()
