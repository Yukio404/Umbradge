def httpProxy():
    ip = input('Proxy\'s IP Adress: ')
    port = input('Proxy\'s Port: ')
    os.system('export http_proxy=http://' + ip + ':' + port)
    exit()
