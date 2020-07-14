def httpsProxy():
    ip = input('Proxy\'s IP Adress: ')
    port = input('Proxy\'s Port: ')
    os.system('export https_proxy=https://' + ip + ':' + port)
    exit()
