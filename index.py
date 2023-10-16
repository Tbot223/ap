import os
import googletrans
import time

def index():
    print("****** 실행할 기능 선택 ******")
    print("""
    * * * * * * * * * * * * * * *
    *                           *
    *    1. 끄기 (말 그대로)    *
    *    2. 번역 (google API)   *
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
        print(f"번역한 문장이나 단어(ko to en) : {string} -> {translator.translate(string, dest='en').text}")
        print("")
        print("------------------------------")
        time.sleep(5)
        index()
    elif AorB == "B" or AorB == "b":
        print(f"번역한 문장이나 단어(en to ko) : {string} -> {translator.translate(string, dest='ko').text}")
        print("")
        print("------------------------------")
        time.sleep(5)
        index()

def exit():
    os.system("pause")

DBpath = os.getcwd()+"/DB"

index()
