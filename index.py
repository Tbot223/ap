import os
import googletrans
import time
import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

path = os.getcwd()
DBpath = f"{path}/DB"

#보조 함수들
def translate_f(words):
    list = os.listdir(DBpath+"/번역_기능_DB/")
    listnum = len(list)
    if listnum == 5:
        os.remove(f"{DBpath}/번역_기능_DB/{list[0]}")
    os.chdir(DBpath+"/번역_기능_DB")
    title = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{title}.txt", "w", encoding="utf-8") as file:
        file.write(words)

#메인 함수들
def index():
    if "DB" not in os.listdir(path):
        os.mkdir("DB")
    list = ["번역_기능_DB", "양방향_암호화_DB"]
    DBlist = os.listdir(DBpath)
    if  list[0] not in DBlist or list[1] not in DBlist:
        os.mkdir("번역_기능_DB")
        os.mkdir("양방향_암호화_DB")
    print("""
    ****** 실행할 기능 선택 ******
          
    * * * * * * * * * * * * * * *
    *                           *
    *    1. 끄기 (말 그대로)    *
    *    2. 번역 (google API)   *
    *    3. 암호화와 복호화     *
    *                           *
    * * * * * * * * * * * * * * *""")

    print("")
    print("")
    functionC = input("모듈 번호 입력 : ")
    print("")
    print("")

    if functionC == "1":
        exit()
    elif functionC == "2":
        translate()
    elif functionC == "3":
        enc()
    else:
        print('잘못된 입력입니다. 다시 입력해보세요.')
        print("")
        print("")
        index()

def translate():
    translator = googletrans.Translator()
    AorB = input("영어로 변역이면 A, 한국어로 번역이면 B : ")
    print("")
    print("------------------------------")
    print("")
    string = input("번역할 문장이나 단어 입력 : ")
    print("")
    print("------------------------------")
    print("")
    if AorB == "A" or AorB == "a":
        a = translator.translate(string, dest='en').text
        print(f"번역한 문장이나 단어(ko to en) : {string} -> {a}")
        translate_f(a)
        print("DB에도 자동으로 저장됩니다.(최근 5회까지)")
        print("")
        print("------------------------------")
        time.sleep(5)
        index()
    elif AorB == "B" or AorB == "b":
        a = translator.translate(string, dest='ko').text
        print(f"번역한 문장이나 단어(en to ko) : {string} -> {a}")
        translate_f(a)
        print("DB에도 자동으로 저장됩니다.(최근 5회까지)")
        print("")
        print("------------------------------")
        time.sleep(5)
        index()
    else:
        print("잘못된 입력입니다. 다시 시도해보세요.")
        translate()

def exit():
    os.system("pause")

def enc():
    dncorenc = input('enc/dnc : ')
    print("")
    if dncorenc == "enc":
        private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,)

        public_key = private_key.public_key()

        message = input("메세지를 입력해주세요(olny en and num) : ")
        print("")
        message = message.encode('utf-8')
        encrypted = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("암호화된 문자열 : ", encrypted)
        time.sleep(2)
        print("")
        os.chdir(DBpath+"/양방향_암호화_DB")
        pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())   
        with open('encrypted.txt', 'wb') as file:
            file.write(encrypted)
        with open('private_key.pem', 'wb') as file:
            file.write(pem)
        print("개인 키, 암호화 문자열등은 DB에 저장되어있습니다.")
        print("")
        time.sleep(2)
        index()


    elif dncorenc == "dnc":
        os.chdir(DBpath+"/양방향_암호화_DB")
        with open("encrypted.txt", "rb") as file:
            encrypted = file.read()
        time.sleep(2)
        with open('private_key.pem', 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None)
        original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
        print("복호화된 문자열 :", original_message.decode('utf8'))
        time.sleep(5)
        index()
    else:
        print("잘못된 입력입니다. 다시입력하세요.")
        enc()
    

index()
