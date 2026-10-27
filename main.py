class Pasien:
    def __init__(self, nama):
        self.nama = nama

class Dokter:
    def __init__(self, nama, spesialisasi):
        self.nama = nama
        self.spesialisasi = spesialisasi

    def periksa_pasien(self, pasien):
        print(f"Dr. {self.nama} ({self.spesialisasi}) sedang memeriksa pasien bernama {pasien.nama}.")


if __name__ == "__main__":
    pasien1 = Pasien("Andi")
    pasien2 = Pasien("Siti")

    dokter1 = Dokter("Budi", "Penyakit Dalam")
    dokter2 = Dokter("Dewi", "Anak")

    dokter1.periksa_pasien(pasien1)
    dokter2.periksa_pasien(pasien2)
