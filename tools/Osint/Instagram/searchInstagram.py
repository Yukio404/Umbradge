from colorama import init, Fore, Back, Style
from tools.Osint.Instagram.instagramSearchTool import instagramSearchTool
from tools.Osint.Instagram.shortUrl import shortUrl

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def searchInstagram():
    user = input("Username: ")
    urlProfil = "https://instagram.com/" + user

    insta = instagramSearchTool()
    insta.getInfo(user)

    name = insta.name
    userId = insta.id
    images = insta.profi_pic_hd
    images = shortUrl(images)
    username = insta.username
    private = insta.private
    followers = insta.followers
    friend = insta.friends
    publication = insta.medias
    bio = insta.biography
    url = insta.url
    email = insta.email
    adresse = insta.adresse
    phone = insta.phone

    print("\n[%s]\n" % (username))
    print(found + "Name: %s" % (name))
    print(found + "Pictures: %s" % (images))
    print(found + "ID: %s" % (userId))
    print(found + "Protected: %s" % (private))
    print(found + "Followers: %s | Following: %s" % (followers, friend))
    print(found + "Post: %s" % (publication))
    print(found + "Bio: %s" % (bio))

    if url:
        print(found + "Url: %s" % (url))
    if email:
        print(found + "Email: %s" % (email))
    if phone:
        print(found + "Phone: %s" % (phone))
    if adresse:
        print(found + "Location: %s" % (adresse))
    if not private:
        print("\n" + question + " Do You Want To Download The 12 Last Pictures ?")

        while True:
            choice = input("\n [y/N]: ")

            if choice == "" or choice.upper() == "N":
                break
            elif choice.upper() == "Y":
                print("\n" + question + "Where Do You Want To Save The Pictures ?")
                defaultPath = os.getcwd()
                print(Fore.YELLOW + "Default Path: " + defaultPath + Fore.RESET)
                path = input("\n Path: ")
                print("\n" + wait + "We Are Downloading The %s's pictures \n" % (user))

                if not path:
                    path = defaultPath

                pictureInfo = insta.get_picturesInfo(urlProfil)

                for i in pictureInfo:
                    media = pictureInfo[i]['display']
                    typeMedia = pictureInfo[i]['type_media']
                    date = pictureInfo[i]['date']
                    view = pictureInfo[i]['info']
                    loc = pictureInfo[i]['localisation']
                    filename = user+'_'+str(i)+".jpg"
                    if not loc:
                        loc = ''

                    insta.downloadPictures(media, path, filename)
                    print("(%s) %s %s [%s] %s Downloaded." % (str(i), typeMedia, date, view, loc))

                print("\n"+found+" Download Finish")
                break
