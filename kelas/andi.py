nama_lengkap = "Andhika Tedja"
hobi = ["makan", "minum", "dance"]
motor = {
    "brand": "Yamaha",
    "warna": "silver",
    "tahun": 2012
}
tahun_lahir = 1980

def menyapa(nama="Andi"):
    if (type(nama) != type('')):
        return 
    
    return "halo " + nama


class Array:
    pass

if (__name__ == '__main__'):
    import sys

    # print("ini module Andi!")

    # print(sys.argv)

    if (len(sys.argv)> 1):
        if (sys.argv[1] == "sapa"):
            if (len(sys.argv)>2):
                nama = sys.argv[2]
                hasil = menyapa(nama)
            else:
                hasil = menyapa()

            print(hasil)
