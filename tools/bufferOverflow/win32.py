def win32():
    path = input('Enter The Path Where You Want The Win32 BufferOverflow\'s File Must To Be: ')
    print("Don't Forget To Change The IP And The Port In The BufferOverflow's File")
    os.system('cp /home/yukio/Bureau/Umbradge/tools/bufferOverflow/win32BufferOverflow.py ' + path)
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