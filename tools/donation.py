import random

class colors:
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    WHITE = '\033[37m'
    RANDOM = random.choice([BLUE, GREEN, WHITE])

def donation():
    logo = colors.RANDOM + '''
      ____                    _   _
     |  _ \  ___  _ __   __ _| |_(_) ___  _ __
     | | | |/ _ \| '_ \ / _` | __| |/ _ \| '_ \\
     | |_| | (_) | | | | (_| | |_| | (_) | | | |
     |____/ \___/|_| |_|\__,_|\__|_|\___/|_| |_|
     '''
    print(logo)
    print("If You Like My Project You Can Donate To My Monero's Wallet With This Adress: 41sKFAdaJFaWrcvGSbVPa2cdForXPufks2GdTFFtrMfoQfjeXJW7XnCaVDRPvUApgWQa26JNvmaBXP8HpRcz2ep23CBo7GU")
    exit()
