# Tugas_Kriptografi_Raja Muhammad Musa-2008096026-_TI-4A
print ("----------------------------------+ Program Enkripsi dan Deskripsi Caesar +-----------------------------------------")

abjad= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def enkripsi(abjad):
    str = input("String : ")
    key = int(input("Key : "))

    str =str.lower()
    result=''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            encrypt = (n + key) 
            convert = abjad[encrypt]
            result  = result + convert
        else :
            result = result + ' '

    print(f"Result :  {result}")

def dekripsi(abjad):
    str = input("String : ")
    key = int(input("Key : "))

    str =str.lower()
    result=''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            decrypt = (n - key) 
            convert = abjad[decrypt]
            result  = result + convert
        else :
            result = result + ' '

    print(f"Result :  {result}")

pilihan ='y'

while (pilihan == 'y'):
    print("Menu yang tersedia : ")
    print("01. Enkripsi Data")
    print("02. Dekripsi Data")
    print("03. Keluar")

    menu=input ("Menu yang dipilih : ")
    print("----------")

    if menu == '1':
        print("Menu Enkripsi Data")
        enkripsi(abjad)
    elif menu == '2':
        print("Menu Dekripsi Data")
        dekripsi(abjad)
    elif menu == '3':
        print("Program Selesai, Terimakasih :)")
        break
    else :
        print("Maaf, Menu Tidak Ditemukan :(")

    print("-----------------------------------")
    pilihan = input("Apakah ingin Melanjutkan? (y/n) : ")
    print("-----------------------------------")