print("====================================")
print("********** Justice League **********")
print("====================================")
username = input("Masukkan username anda:")

def usernameyaa():
    if(username == "brucewyne"):
        print("===== WELCOME", username, "=====")
        print("1. Tambah Anggota Justice League")
        print("2. Hapus Anggota Justice League")
        print("3. TampilkanAnggota Justice League")
        print("4. Exit")
    elif(username == "victorstone"):
        print("===== WELCOME", username, "=====")
        print("1. Tambah Anggota Justice League")
        print("2. Hapus Anggota Justice League")
        print("3. TampilkanAnggota Justice League")
        print("4. Exit")
    elif(username == "ciscoramon"):
        print("===== WELCOME", username, "=====")
        print("1. Tambah Anggota Justice League")
        print("2. Hapus Anggota Justice League")
        print("3. TampilkanAnggota Justice League")
        print("4. Exit")
    else:
        print("Access Denied")
        exit()
usernameyaa()

pilihananda = input("Masukkan pilihan anda : ")

while True:
    if(pilihananda == "1"):
        namaanggotabaru = input("Nama Anggota baru : ")
        print("data '", namaanggotabaru, "'", "berhasil ditambahkan")
        pilihananda = input("Masukkan pilihan anda : ")
    elif(pilihananda == "2"):
        anggotadihapus = input("Anggota yang akan dihapus : ")
        if(anggotadihapus == "brucewyne"):
            print("data '", anggotadihapus, "'", "berhasil dihapus")
            pilihananda = input("Masukkan pilihan anda : ") 
        elif(anggotadihapus == "victorstone"):
            print("data '", anggotadihapus, "'", "berhasil dihapus")
            pilihananda = input("Masukkan pilihan anda : ")
        elif(anggotadihapus == "ciscoramon"):
            print("data '", anggotadihapus, "'", "berhasil dihapus")
            pilihananda = input("Masukkan pilihan anda : ")
        else:
            exit()
    elif(pilihananda == "3"):
        print("Daftar Anggota Justice Leauge :")
        print("|",namaanggotabaru, "|")
        pilihananda = input("Masukkan pilihan anda : ")
    elif(pilihananda == "4"):
        print("see u next time MR.", username, "GLHF")
        exit()
    else:
        print("Access Error")
        exit()
