from abc import ABC, abstractmethod

class Orang(ABC):
    total_orang = 0

    def __init__(self, nama, nik, alamat):
        self.nama = nama
        self.__nik = nik
        self._alamat = alamat
        Orang.total_orang += 1

    @property
    def nik(self):
        return self.__nik

    @nik.setter
    def nik(self, val):
        if len(val) != 16:
            raise ValueError("NIK harus 16 digit!")
        self.__nik = val

    def info_dasar(self):
        return f"Nama: {self.nama}, Alamat: {self._alamat}"

    @abstractmethod
    def tampilkan_info(self):
        pass

    @abstractmethod
    def get_peran(self):
        pass

class Pasien(Orang):
    def __init__(self, nama, nik, alamat, no_rm, riwayat_penyakit, golongan_darah):
        super().__init__(nama, nik, alamat)
        self.no_rm = no_rm
        self.riwayat_penyakit = riwayat_penyakit
        self.golongan_darah = golongan_darah

    def tampilkan_info(self):
        print(f"[Pasien] {self.info_dasar()} | No RM: {self.no_rm}, Riwayat: {self.riwayat_penyakit}, Gol. Darah: {self.golongan_darah}")

    def get_peran(self):
        return "Pasien"

class Dokter(Orang):
    def __init__(self, nama, nik, alamat, id_dokter, spesialisasi, status_kerja):
        super().__init__(nama, nik, alamat)
        self.id_dokter = id_dokter
        self.spesialisasi = spesialisasi
        self.status_kerja = status_kerja

    def tampilkan_info(self):
        print(f"[Dokter] {self.info_dasar()} | Spesialis: {self.spesialisasi}, ID: {self.id_dokter}, Status: {self.status_kerja}")

    def get_peran(self):
        return "Dokter"

class RekamMedis:
    def __init__(self, tanggal, diagnosa):
        self.tanggal = tanggal
        self.diagnosa = diagnosa

class Klinik:
    def __init__(self, nama_klinik):
        self.nama_klinik = nama_klinik
        self.daftar_dokter = []

    def tambah_dokter(self, dokter):
        self.daftar_dokter.append(dokter)

    def info_klinik(self):
        print(f"\n--- Informasi Klinik: {self.nama_klinik} ---")
        print("Daftar Dokter yang Bertugas:")
        for dokter in self.daftar_dokter:
            dokter.tampilkan_info()

if __name__ == "__main__":
    print("=== 4. BUKTI ABSTRAKSI (Uji Gagal Instansiasi Abstract Class) ===")
    try:
        orang_gagal = Orang("Uji Coba", "1234567890123456", "Jl. Merdeka")
    except TypeError as e:
        print(f"Berhasil Mencegah Instansiasi:\n-> TypeError: {e}\n")

    print("=== PENGUJIAN SISTEM KLINIK OOP (DENGAN ABC) ===")
    p1 = Pasien("Andi", "6471012345678901", "Jl. Mulawarman", "RM-001", "Panas", "O")
    d1 = Dokter("Dr. Budi", "6471111111111111", "Jl. P. Antasari", "DOC-101", "Penyakit Dalam", "Tetap")
    d2 = Dokter("Dr. Dewi", "6471222222222222", "Jl. Lambung Mangkurat", "DOC-102", "Anak", "Kontrak")
    
    print("\n--- Uji Implementasi Abstract Method & Method Konkret ---")
    p1.tampilkan_info()
    print(f"Peran Sistem: {p1.get_peran()}")
    
    d1.tampilkan_info()
    print(f"Peran Sistem: {d1.get_peran()}")

    klinik_sehat = Klinik("Klinik Sehat Bersama")
    klinik_sehat.tambah_dokter(d1)
    klinik_sehat.tambah_dokter(d2)
    klinik_sehat.info_klinik()

    print("\n--- Uji Rekam Medis (Komposisi) ---")
    rm = RekamMedis("2026-10-07", "Demam Berdarah")
    print(f"Pasien {p1.nama} dengan No RM {p1.no_rm} mendapat diagnosa: {rm.diagnosa} pada tanggal {rm.tanggal}.")
