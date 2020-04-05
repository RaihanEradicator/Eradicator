import os
print("===============CopyRight==============")
print("APLIKASI PENGHITUNGAN SISA HASIL USAHA")
print("======================================")
NamaKoperasi = str(input("Nama KOPERASI : "))
NamaAnggota = str(input ("Nama Anggota : "))
SHU = int(input ("Sisa Hasil Usaha : Rp "))
print ("\n")
pilihan = 0
print ('Masukkan 1 jika menghitung SHU "Simpanan" ')
print ('Masukkan 2 jika menghitung SHU "Usaha" ')
pilih = int(input("Masukkan Pilihan : "))
SHUsimpanan = 0
SHUTUsaha = 0
#System History
Pilihan1 = False
Pilihan2 = False
#sistem Looping
ulang = True
while (ulang == True):
    os.system('cls')
    if (pilih == 1):
        print("Perhitungan SHU Jasa Modal ", NamaAnggota," Copyright-----------------------------------------------")
        print("Masukkan Jumlah Simpanan KOPERASI ",NamaKoperasi," : ")
        TotalSimpanan = int (input ())
        print("Masukkan jumlah Simpanan ", NamaAnggota, " : ")
        SimpananAnggota = int(input ())
        print("Masukkan persentase jasa modal (--- PER SERATUS ---) : ")
        PersentaseSimpanan = int(input ())
        PersentaseSimpanan = PersentaseSimpanan /100
        print("\n")
        SHUsimpanan = SimpananAnggota / TotalSimpanan * PersentaseSimpanan * SHU
        print ("SHU Simpanan " ,NamaAnggota ," = " ,SimpananAnggota ," / " ,TotalSimpanan," * " ,PersentaseSimpanan," * " ,SHU)
        print("SHU Simpanan " ,NamaAnggota ," = ", SHUsimpanan)
        #Pilihan Satu sudah pernah
        Pilihan1 = True

        if (Pilihan2 == False):
            ERROR = True
            while(ERROR == True): #Penanggulangan Jika Pengguna Memasukkan angka selain 1 atau 2
                ERROR = False
                Mau = int(input('Apakah Anda Ingin Menghitung SHU Usaha Juga ? IYA klik "1" , TIDAK klik "2"'))
                os.system('cls')
                if (Mau == 1):
                    ERROR = False
                    pilih = 2
                    ulang = True
                elif(Mau == 2):
                    ERROR = False
                    ulang = False
                else:
                    os.system('cls')
                    print("ERROR[][][][][][][][][][][][][][][][][][][][][][]")
                    print("Pilih __1__ atau __2__")
                    ERROR = True
        else:
            ulang = False


    elif(pilih == 2):
        print("Perhitungan SHU Jasa Usaha ",NamaAnggota," copyright--------------------------------------------")
        print("Masukkan Jumlah Transaksi Usaha KOPERASI ", NamaKoperasi, " : ")
        TotalTUsaha = int(input())
        print("Masukkan Jumlah Transaksi Usaha ", NamaAnggota, " : ")
        TUsahaAnggota = int(input())
        print("Masukkan persentase jasa Usaha ",NamaAnggota,"(--- PER SERATUS ---) : ")
        PersentaseTUsaha = int(input())
        PersentaseTUsaha = PersentaseTUsaha / 100
        print("\n")
        SHUTUsaha = TUsahaAnggota / TotalTUsaha * PersentaseTUsaha * SHU
        print("SHU Transaksi Usaha ", NamaAnggota, " = ", TUsahaAnggota, " / ", TotalTUsaha, " * ", PersentaseTUsaha,
              " * ", SHU)
        print("SHU Transaksi Usaha ", NamaAnggota, " = ", SHUTUsaha)
        Pilihan2 = True
        
        #copyright@rRaihan


        if (Pilihan1 == False):
            ERROR = True
            while (ERROR == True):  # Penanggulangan Jika Pengguna Memasukkan angka selain 1 atau 2
                Mau = int(input('Apakah Anda Ingin Menghitung SHU Usaha Juga ? IYA klik "1" , TIDAK klik "2"'))
                if (Mau == 1):
                    ERROR = False
                    pilih = 1
                    ulang = True
                elif(Mau == 2):
                    ERROR = False
                    ulang = False
                else:
                    os.system('cls')
                    print("ERROR[][][][][][][][][][][][][][][][][][][][][][]")
                    print("Pilih __1__ atau __2__")
                    ERROR = True
        else:
            ulang = False
    else:
        print ("pilihan anda tidak ditemukkan")

os.system('cls')
print ("Jumlah Sisa Hasil Usaha Yang didapatkan oleh ",NamaAnggota," adalah")
SHUtotal = SHUsimpanan + SHUTUsaha
print("SHU ",NamaAnggota," =  SHU simpanan  + SHU Usaha")
print("SHU ",NamaAnggota," = Rp ", SHUsimpanan, " + Rp ",SHUTUsaha)
print("SHU ",NamaAnggota," = Rp ",SHUtotal)
print ("Raihan@Copyright")
