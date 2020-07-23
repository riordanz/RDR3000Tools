import os.path
from RDRTools import *
from html2text import *
from sys import argv

def web_by_help():
    print("[-] pahe => pahe.in")
    print("[-] terbit21 => terbit21.cool")
    print("[-] kuyhaa => kuyhaa-me.com")
    print("[-] gigapb => gigapurbalingga.com")
    print("[-] oploverz => oploverz.in")
    print("[-] nimegami => nimegami.com")

def web_ba_help():
    print("[-] mediafire => mediafire.com")

def type_help():
    print("[-] bypass => for bypass website")
    print("[-] batch => for download many file from famous website downloader")

def help():
    print("[+] How to use : ")
    print("[-] python cli.py type website")
    print("\n[+] Type : ")
    type_help()
    print("\n[+] Website For Bypass : ")
    web_by_help()
    print("\n[+] Website For Batch Downloader : ")
    web_ba_help()

def do(typ, web, url):
    by = Bypasser()
    ba = BatchDownloader()

    if typ == "bypass":
        if web == "pahe":
            return by.pahe(url)
        elif web == "kuyhaa":
            return by.kuyhaa(url)
        elif web == "gigapb":
            return by.gigapurbalingga(url)
        elif web == "oploverz":
            return by.oploverz(url)
        elif web == "nimegami":
            return by.nimegami(url)
        else:
            return False
    elif typ == "batch":
        if web == "mediafire":
            folder = input("Folder : ")
            ba.mediafire_cli(url, folder)
        else:
            return False
    else:
        return False

if len(argv) < 3:
    help()
    exit()

web_by = ["pahe", "terbit21", "kuyhaa", "gigapb", "oploverz", "nimegami"]
web_ba = ["mediafire"]
types = ["bypass", "batch"]
inp = False

if argv[1] not in types or argv[2] not in web_by+web_ba:
    help()
    exit()

if argv[1] == "bypass":
    if argv[2] not in web_by:
        help()
        exit()
    if argv[2] == "terbit21":
        film = Bypasser().terbit21("search", input("Cari Judul Film : "))
        for i, c in enumerate(film['results']):
            print("[%s] %s" % (str(i+1), c['title']))
        select = "RDRTools"
        while not select.isdigit():
            select = input("Pilih Film : ")
            if not select.isdigit():
                print("Pilih Angka Yang Ada !!!")
        select = int(select)
        print(html2text(Bypasser().terbit21("get_link", film['results'][select - 1]['slug'])))
    else:
        inp = input("URL / File : ")
else:
    if argv[2] not in web_ba:
        help()
        exit()
    inp = input("URL / File : ")

if inp:
    data = [inp]
    if os.path.isfile(inp):
        data = open(inp).read().split("\n")
    for url in data:
        print(do(argv[1], argv[2], url))
    