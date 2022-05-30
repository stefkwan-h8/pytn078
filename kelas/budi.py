nama_lengkap = "Budi Budiman"
hobi = ["sepeda", "bulutangkis", "kick boxing"]
motor = {}
tahun_lahir = 2000

def menyapa(nama="Budi"):
    if (type(nama) != type('')):
        return 
    
    return "halo " + nama


class Array:
    pass

if (__name__ == '__main__'):
    import sys

    # print("ini module Budi!")

    # print(sys.argv)

    if (len(sys.argv)> 1):
        if (sys.argv[1] == "sapa"):
            if (len(sys.argv)>2):
                nama = sys.argv[2]
                hasil = menyapa(nama)
            else:
                hasil = menyapa()

            print(hasil)
