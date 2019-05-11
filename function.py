def kotak():
    print('Masukan Sisi')
    sisi = input()
    hasil= int(sisi)*int(sisi)
    print(hasil)
    menu()

def persegi():
    print('Masukan panjang')
    panjang = input()
    print ('Masukan lebar')
    lebar = input()
    hasil = int(panjang)*int(lebar)
    print(hasil)
    menu()

def menu():
    print('Silahkan Masukan Pilihan')
    print('[1] Menghitung Kotak')
    print('[2] Menghitung Persegi')
    pilih=input()
    if pilih=='1':
        kotak()
    elif pilih=='2':
        persegi()
    else:
        print('Masukan Anda Salah')
        menu()
menu()
