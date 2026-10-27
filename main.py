class Pemeriksaan:
    @staticmethod
    def periksa_pasien(dokter, pasien):
        print(f"Dr. {dokter.nama} memeriksa pasien {pasien.nama}.")
        print(f"Keluhan: {pasien.keluhan}")
        print(f"Diagnosa: {pasien.rekam_medis.diagnosa}")


class Klinik:
    def __init__(self, nama_klinik):
        self.nama_klinik = nama_klinik
        self.daftar_dokter = []

    def tambah_dokter(self, dokter):
        self.daftar_dokter.append(dokter)

    def info_klinik(self):
        print(f"Klinik: {self.nama_klinik}")
        for d in self.daftar_dokter:
            print(f"- {d.nama} ({d.spesialisasi})")


class RekamMedis:
    def __init__(self, id_rekam, diagnosa):
        self.id_rekam = id_rekam
        self.diagnosa = diagnosa


class Pasien:
    def __init__(self, nama, nik, keluhan, id_rekam, diagnosa):
        self.nama = nama
        self.nik = nik
        self.keluhan = keluhan
        self.rekam_medis = RekamMedis(id_rekam, diagnosa)


class Dokter:
    def __init__(self, nama, nik, spesialisasi):
        self.nama = nama
        self.nik = nik
        self.spesialisasi = spesialisasi


if __name__ == "__main__":
    klinik = Klinik("sehat bersama")
    
    dokter1 = Dokter("Budi", "123", "Penyakit dalam")
    klinik.tambah_dokter(dokter1)
    klinik.info_klinik()

    pasien1 = Pasien("Andi", "456", "Flu berat", "RM01", "ISPA")
    Pemeriksaan.periksa_pasien(dokter1, pasien1)
