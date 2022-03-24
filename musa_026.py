# Tugas_Kriptografi_raja muhammad musa-2008096026-_TI-4A
#n =  urutan abjad yang diinput
#key = kunci dari enkripsi atau deskripsi
#26 = jumlah seluruh dari huruf abjad


print ("----------------------------------+ Program Enkripsi dan Deskripsi Caesar +-----------------------------------------") 
#digunakan untuk mencetak ouput 

abjad= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#variabel abjad berfungsi untuk menampung nilai abjad yang ada

def enkripsi(abjad):            #def menjadi pertanda bahwa blok kode program (abjad) adalah sebuah fungsi
    str = input("String : ")    #variable string memerintahkan untuk menginput string enkripsi
    key = int(input("Key : "))  #key digunakan untuk pergeseran abjad (enkripsi)
                                #int digunakan untuk memasukkan key yang diinginkan

    str =str.lower()            #string dikonversi menjadi huruf kecil semua
    result=''                   #deklarasi variabel result dengan nilai awal adalah kosong

    for char in str:                    #membuat perulangan untuk pergeseran abjad dari string
        if char in abjad:               #abjad string dipecah 1 per 1 dan di cek apakah termasuk dalam value abjad
            n = abjad.index(char)       #jika ada maka nilai index dari abjad yang ditemukan disimpan dalam variabel n
            encrypt = (n + key) % 26    #rumus enkripsi
            convert = abjad[encrypt]    #konversi nilai string ke hasil enkripsi
            result  = result + convert  #abjad yang sudah dikonversi disimpan dalam variabel result dalam bentuk string
        else :                          #digunakan sebagai kondisi alternatif ketika semua kondisi awal tidak ada yang sesuai
            result = result + ' '       #jika abjad dari string tidak ditemukan dalam index abjad, maka akan dirubah ke dalam 
                                        #bentuk spasi

    print(f"Result :  {result}")        #hasil dari bentuk perulangan untuk enkripsi string ditampilkan

def dekripsi(abjad):                    #def menjadi pertanda bahwa blok kode program (abjad) adalah sebuah fungsi
    str = input("String : ")            #variable string memerintahkan untuk menginput string deskripsi
    key = int(input("Key : "))          #key digunakan untuk pergeseran abjad (deskripsi)

    str =str.lower()                    #string dikonversi menjadi huruf kecil semua
    result=''                           #deklarasi variabel result dengan nilai awal adalah kosong

    for char in str:                    #membuat perulangan untuk pergeseran abjad dari string
        if char in abjad:               #abjad string dipecah 1 per 1 dan di cek apakah termasuk dalam value abjad
            n = abjad.index(char)       #jika ada maka nilai index dari abjad yang ditemukan disimpan dalam variabel n
            decrypt = (n - key) % 26    #rumus deskripsi
            convert = abjad[decrypt]    #konversi nilai string ke hasil deskripsi
            result  = result + convert  #abjad yang sudah dikonversi disimpan dalam variabel result dalam bentuk string
        else :                          #digunakan sebagai kondisi alternatif ketika semua kondisi awal tidak ada yang sesuai.
            result = result + ' '       #jika abjad dari string tidak ditemukan dalam index abjad, maka akan dirubah ke dalam 
                                        #bentuk spasi

    print(f"Result :  {result}")        #hasil dari bentuk perulangan untuk enkripsi string ditampilkan

pilihan ='y'                            #jika memilih y

while (pilihan == 'y'):                 #digunakan untuk eksekusi perulangan selama ekspresi benar (memilih y)
    print("Menu yang tersedia : ")      #output dengan tampilan menu yang tersedia
    print("01. Enkripsi Data")          #output dengan tampilan 01. Enkripsi Data
    print("02. Dekripsi Data")          #output dengan tampilan02. Deskripsi Data
    print("03. Keluar")                 #output dengan tampilan 03. Keluar

    menu=input ("Menu yang dipilih : ") #variabel menu untuk memerintahkan menampilkan menu yang dipilih
    print("----------")

    if menu == '1':                     #program mengecek kondisi yang diberikan
        print("Menu Enkripsi Data")     #output dengan tampilan menu enkripsi data
        enkripsi(abjad)                 #enkripsi yang diberikan berupa abjad
    elif menu == '2':                   #program mengecek kondisi yang diberikan, jika terdapat kondisi tambahan 
                                        #ketika kondisi yang diberikan sebelumnya tidak sesuai
        print("Menu Dekripsi Data")     #output dengan tampilan menu deskripsi data
        dekripsi(abjad)                 #deskripsi yang diberikan berupa abjad
    elif menu == '3':                   #program mengecek kondisi yang diberikan, jika terdapat kondisi tambahan 
                                        #ketika kondisi yang diberikan sebelumnya tidak sesuai
        print("Program Selesai, Terimakasih :)") #output dengan tampilan program selesai, terimakasih :)
        break                           #perintah khusus yang digunakan untuk memaksa perulangan berhenti sebelum waktunya
    else :                              #kondisi alternatif ketika semua kondisi awal tidak ada yang sesuai 
        print("Maaf, Menu Tidak Ditemukan :(") #output dengan tampilan maaf, menu tidak ditemukan

    print("-----------------------------------")
    pilihan = input("Apakah ingin Melanjutkan? (y/n) : ")
    print("-----------------------------------")