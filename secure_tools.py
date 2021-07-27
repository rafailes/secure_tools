while True:
    from hashlib import sha256
    import os
    import string
    import random
    import socket as s
    import time
    logo = """







 _____ _____ _____ _   _______ _____ _____ _____  _____ _      _____ /
/  ___|  ___/  __ \ | | | ___ \  ___|_   _|  _  ||  _  | |    /  ___|/
\ `--.| |__ | /  \/ | | | |_/ / |__   | | | | | || | | | |    \ `--. /
 `--. \  __|| |   | | | |    /|  __|  | | | | | || | | | |     `--. \/
/\__/ / |___| \__/\ |_| | |\ \| |___  | | \ \_/ /\ \_/ / |____/\__/ //
\____/\____/ \____/\___/\_| \_\____/  \_/  \___/  \___/\_____/\____/ /
                                 ______
                                |______|

    [1]secure your files with xor chiffrement
    [2]scan my port
    [3]creat a robust passwords
    [4]decrypt file encrypted with first option

    """
    print(logo)
    choix = input("choose an option: ")

    def dechiffrement():
        enter = input("enter the file to encrypt with extension ex: (test.crypt): ")
        sortie = input("enter a finally file name: ")
        password = input("enter password: ")
        password = sha256(password.encode("utf-8")).digest()
        with open(enter,'rb') as f_enter:
            with open(sortie,'wb') as f_sortie:
                i = 0
                while f_enter.peek():
                    c = ord(f_enter.read(1))
                    j = i % len(password)
                    b = bytes([c^password[j]])
                    f_sortie.write(b)
                    i = i +1
                    time.sleep(2)
        print("[*]file was encrypted")
    def chiffrement():
        f = open("password_backup.txt", "a+")
        enter = input("enter the file to encrypt with extension without extension expamle (test.txt = test): ")
        sortie = input("enter a finally file name with extension example(test.crypt): ")
        f.write(sortie)
        f.write(" : ")
        password = input("enter password: ")
        f.write(password)
        f.write("\n")
        password = sha256(password.encode("utf-8")).digest()
        with open(enter,'rb') as f_enter:
            with open(sortie,'wb') as f_sortie:
                i = 0
                while f_enter.peek():
                    c = ord(f_enter.read(1))
                    j = i % len(password)
                    b = bytes([c^password[j]])
                    f_sortie.write(b)
                    i = i +1

        print("[*]file was encrypted")


        f.close()
        path = os.getcwd()
        print("one file with your password was created if you d'ont remender your password", path)


        time.sleep(2)


    def ports_scanner():
        ip = input("enter your ip addres: ")
        port_list = [20, 21, 22, 80, 8080, 53, 445]
        for port in port_list:
            sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            connec = sock.connect_ex((ip, port))
            if connec == 0:
                print("[*]port ", port, "is open!")

            else:
                print("[-]port", port, "is close")

    def secure_passwords():
        liste = string.ascii_letters+string.digits
        size = 3
        return''.join(random.choice(liste)for x in range(20))

    if choix == "3":
        site = input ("enter a service of use this password example(facebook,gmail,instagram): ")
        n = 0

        rep2 = print("your password is : ", secure_passwords())
        save = input("for save password paste here and press enter: ")
        f = open("passwords.txt", "a+")
        f.write("\n")
        f.write(site)
        f.write(" : ")
        f.write(save)
        f.write("\n")
        f.close()
        path = os.getcwd()
        print("[*]one file with your password was created in ", path)
        time.sleep(2)
    if choix == "1":
        chiffrement()

    if choix == "2":
        ports_scanner()

    if choix == "4":
        dechiffrement()