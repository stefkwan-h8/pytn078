nama_lengkap = "Cindy Mutia"
hobi = ["sky diving", "rock climbing", "coding"]
motor = {}
tahun_lahir = 1990

def menyapa(nama="Cindy"):
    if (type(nama) != type('')):
        return 
    
    return "halo " + nama


class Array:
    pass

if (__name__ == '__main__'):
    import sys

    # print("ini module Cindy!")

    # print(sys.argv)

    if (len(sys.argv)> 1):
        if (sys.argv[1] == "sapa"):
            if (len(sys.argv)>2):
                nama = sys.argv[2]
                hasil = menyapa(nama)
            else:
                hasil = menyapa()

            print(hasil)
