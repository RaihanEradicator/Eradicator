import os

a = 1
b = 1
while(a == 1):
    while(b == 1):
        print("===================================")
        print("||    Program Perubahan Sudut    ||")
        print("===================================")
        print()
        print("""Masukkan
    - sin
    - cos
    - tan
        """)
        Pilihan = None
        while Pilihan not in ("sin","cos","tan"):
            Pilihan = input("Masukkan jawaban : ") ###
            if Pilihan == "sin":
                Tipe = "sin"
            elif Pilihan == "cos":
                Tipe = "cos"
            elif Pilihan == "tan":
                Tipe = "tan"
            else:
                print("masukkan dengan benar ! (TANPA huruf KAPITAL)")
        print()
        Teta = int(input("Masukkan nilai teta : ")) ###
        Var = None
        if(Teta > 360 ):
            Dir = int(Teta/360)
            Var = Teta - 360 * Dir
            print(Teta," (derajat) = ",Var," (derajat)")
            if (Var < 90):  # Simple
                print()
                print("+++++++++++++++ Jawaban ++++++++++++++++")
                print("", Tipe, "(", Var, ")")
                if Tipe == "sin":
                    if Var == 0:
                        print("= 0")
                        break
                    elif Var == 30:
                        print("= 1/2")
                        break
                    elif Var == 45:
                        print("= 1/2 * akar 2")
                        break
                    elif Var == 60:
                        print("= 1/2 * akar 3")
                        break
                    elif Var  == 90:
                        print("= 1")
                        break

                elif Tipe == "cos":
                    if Var == 0:
                        print("= 1")
                        break
                    elif Var == 30:
                        print("= 1/2 * akar 3")
                        break
                    elif Var == 45:
                        print("= 1/2 * akar 2")
                        break
                    elif Var == 60:
                        print("= 1/2")
                        break
                    elif Var == 90:
                        print("= 0")
                        break

                elif Tipe == "tan":
                    if Var == 0:
                        print("= 0")
                        break
                    elif Var == 30:
                        print("= 1/3 * akar 3")
                        break
                    elif Var == 45:
                        print("= 1")
                        break
                    elif Var == 60:
                        print("= akar 3")
                        break
                    elif Var == 90:
                        print("= Tak Hingga")
                        break
        print("")
        if Tipe == "sin":
            if Teta == 0:
                print("= 0")
                break
            elif Teta == 30:
                print("= 1/2")
                break
            elif Teta == 45:
                print("= 1/2 * akar 2")
                break
            elif Teta == 60:
                print("= 1/2 * akar 3")
                break
            elif Teta == 90:
                print("= 1")
                break

        elif Tipe == "cos":
            if Teta == 0:
                print("= 1")
                break
            elif Teta == 30:
                print("= 1/2 * akar 3")
                break
            elif Teta == 45:
                print("= 1/2 * akar 2")
                break
            elif Teta == 60:
                print("= 1/2")
                break
            elif Teta == 90:
                print("= 0")
                break

        elif Tipe == "tan":
            if Teta == 0:
                print("= 0")
                break
            elif Teta == 30:
                print("= 1/3 * akar 3")
                break
            elif Teta == 45:
                print("= 1")
                break
            elif Teta == 60:
                print("= akar 3")
                break
            elif Teta == 90:
                print("= Tak Hingga")
                break

        elif Tipe == "cot":
            if Teta == 0:
                print("= Tak Hingga")
                break
            elif Teta == 30:
                print("= akar 3")
                break
            elif Teta == 45:
                print("= 1")
                break
            elif Teta == 60:
                print("= 1/3 * akar 3")
                break
            elif Teta == 90:
                print("atau  = 0")
                break
        print("""Masukkan
        1) jika menggunakan 0 & 180 (derajat)
        2) jika mengunakan 90 & 270 (derajat)
                """)
        Conversi = None
        while Conversi not in (1,2): #Perubahan Tipe
            Conversi = int(input("Masukkan jawaban : "))  ###
            if Conversi == 1 :
                None
            elif(Conversi == 2):
                if(Pilihan == "sin"):
                    Tipe = "cos"
                elif (Pilihan == "cos"):
                    Tipe = "sin"
                else:
                    Tipe = "cot"
            else:
                print("masukkan dengan angka yg tersedia di atas !")

        if (Conversi == 2): #Penghitungan Teta
            if (0 < Teta < 180):
                if(Teta < 90):
                    Hitung = 90 - Teta
                else:
                    Hitung = Teta - 90
            else :
                if (Teta < 270):
                    Hitung = 270 - Teta
                else:
                    Hitung = Teta - 270
        else:
            if (90 < Teta < 270):
                if (Teta < 180):
                    Hitung = 180 - Teta
                else:
                    Hitung = Teta - 180
            else:
                if (Teta < 360):
                    Hitung = 360 - Teta
                else:
                    Hitung = Teta - 360

        if (Tipe == "sin") : #sin # pemberian minus
            if (Conversi == 1):
                if (Teta > 180):
                    Negatif = True
                else:
                    Negatif = False
            else:
                if (Teta > 180):
                    Negatif = True
                else:
                    Negatif = False
        elif (Tipe == "cos"): #cos
            if (Conversi == 1):
                if (0 < Teta < 90 ,270 < Teta < 360):
                    Negatif = True
                else:
                    Negatif = False
            else:
                if (Teta > 180):
                    Negatif = True
                else:
                    Negatif = False
        else: #tan
            if (Conversi == 1):
                if (0 < Teta < 90 ,180 < Teta < 270):
                    Negatif = True
                else:
                    Negatif = False
            else:
                if (Teta > 180):
                    Negatif = True
                else:
                    Negatif = False

        print("a")
        print("+++++++++++++++ Jawaban ++++++++++++++++")
        #Penggabungan
        if(Negatif == True):
            print("  -",Tipe,"(",Hitung,")")
        else:
            print("",Tipe,"(",Hitung,")")
        if Negatif == False :
            if Tipe == "sin":
                if Hitung == 0:
                    print("= 0")
                    break
                elif Hitung == 30:
                    print("= 1/2")
                    break
                elif Hitung == 45:
                    print("= 1/2 * akar 2")
                    break
                elif Hitung == 60:
                    print("= 1/2 * akar 3")
                    break
                elif Hitung == 90:
                    print("= 1")
                    break
            elif Tipe == "cos":
                if Hitung == 0:
                    print("= 1")
                    break
                elif Hitung == 30:
                    print("= 1/2 * akar 3")
                    break
                elif Hitung == 45:
                    print("= 1/2 * akar 2")
                    break
                elif Hitung == 60:
                    print("= 1/2")
                    break
                elif Hitung == 90:
                    print("= 0")
                    break
            elif Tipe == "tan":
                if Hitung == 0:
                    print("= 0")
                    break
                elif Hitung == 30:
                    print("= 1/3 * akar 3")
                    break
                elif Hitung == 45:
                    print("= 1")
                    break
                elif Hitung == 60:
                    print("= akar 3")
                    break
                elif Hitung == 90:
                    print("= Tak Hingga")
        break
    print("=========================================================")
    print("      Apakah anda ingin menghitung lagi ?  iya / tidak   ")
    print("=========================================================")
    jawaban = None
    while jawaban not in ("iya","tidak"):
        jawaban = input("Masukkan jawaban : ")
        if jawaban == "iya":
            b = 1
        elif jawaban == "tidak":
            a = 2
        else:
            print("Masukkan 'iya' atau 'tidak' ")
    os.system('cls')
print("-------------    Program Ditutup    ----------------")
