def web():
    path = input('Enter The Path Where You Want The ShellCode\'s File Must To Be: ')
    os.system('cp tools/webShell.php ' + path)
    time.sleep(3)
    print('\nI will return to the main menu in: ')
    print('\n5, ')
    time.sleep(1)
    print('4, ')
    time.sleep(1)
    print('3, ')
    time.sleep(1)
    print('2, ')
    time.sleep(1)
    print('1')
    exit()
