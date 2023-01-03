print("===== Selamat datang di XXV =====")
tanggaltudey = input("Masukkan tanggal hari ini : ")
tanggaltudey = int(tanggaltudey)
print("")
print("-- Berikut genre film yang tersedia --")
print("1. Horror")
print("2. Action")
print("")
maugenreapa = input("Silahkan pilih mau nonton film bergenre apa : ")
print("")

def genre():
    if(maugenreapa == "1"):
        print("== Berikut piliihan film horror yang sedang tayang")
        print("1. The Devil's Light")
        print("2. Pengabdi Setan")
    elif(maugenreapa == "2"):
        print("== Berikut piliihan film horror yang sedang tayang")
        print("1. Black Panther: Wakanda Forever")
        print("2. Avatar: The Way of Water")
    else:
        print("Pilihan yang anda pilih tidak tersedia di bioskop ini")
        exit()
genre()

pilihfilmapa = input("Silahkan pilih mau nonton film apa : ")
tiketberapa = input("Mau memesan tiket sebanyak : ")
tiketberapa = int(tiketberapa)
hargatiket = tiketberapa*25000
diskongenap = hargatiket-hargatiket*0.02
diskonganjil = hargatiket-hargatiket*0.05

def tiket():
    if(tanggaltudey%2 == 0):
        print("Total yang harus dibayar adalah Rp.", diskongenap)
    else:
        if(tiketberapa > 4):
            print("Total yang harus dibayar adalah Rp.", diskonganjil)
        else:
            print("Total yang harus dibayar adalah Rp.", hargatiket)
tiket()

