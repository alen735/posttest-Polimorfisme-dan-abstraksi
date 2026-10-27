class Orang:
    def __init__(self, nama, nik):
        self.nama = nama
        self.nik = nik

    def tampilkan_peran(self):
        pass

    def __str__(self):
        return f"Nama: {self.nama} | NIK: {self.nik}"


class Pasien(Orang):
    def __init__(self, nama, nik, no_rm, keluhan):
        super().__init__(nama, nik)
        self.no_rm = no_rm
        self.keluhan = keluhan

    def tampilkan_peran(self):
        print(f"[Pasien] {self.nama} (No. RM: {self.no_rm}) - Keluhan: {self.keluhan}")


class Dokter(Orang):
    def __init__(self, nama, nik, id_dokter, spesialisasi):
        super().__init__(nama, nik)
        self.id_dokter = id_dokter
        self.spesialisasi = spesialisasi

    def tampilkan_peran(self):
        print(f"[Dokter] Dr. {self.nama} (ID: {self.id_dokter}) - Spesialis: {self.spesialisasi}")


class PembayaranTransfer:
    def proses_bayar(self, jumlah):
        print(f"-> Memproses pembayaran sebesar Rp {jumlah:,} via Transfer Bank (Virtual Account).")


class PembayaranDompetDigital:
    def proses_bayar(self, jumlah):
        print(f"-> Memproses pembayaran sebesar Rp {jumlah:,} via QRIS / E-Wallet.")


def bayar_layanan_klinik(metode_pembayaran, total_biaya):
    metode_pembayaran.proses_bayar(total_biaya)


if __name__ == "__main__":
    print("=" * 60)
    print(" 1. DEMONSTRASI POLIMORFISME VIA PEWARISAN & LOOP")
    print("=" * 60)
    
    daftar_entitas = [
        Pasien("Andi", "6471012345678901", "RM-001", "Demam Berdarah"),
        Dokter("dr.Budi", "6471111111111111", "DOC-101", "Penyakit Dalam")
    ]

    for entitas in daftar_entitas:
        entitas.tampilkan_peran()

    print("\n" + "=" * 60)
    print(" 2. DEMONSTRASI OPERATOR OVERLOADING (__str__)")
    print("=" * 60)
    pasien_baru = Pasien("Dewi Lestari", "6471012345678901", "RM-002", "Sakit Kepala")
    print("Memanggil objek langsung menggunakan magic method __str__:")
    print(pasien_baru)

    print("\n" + "=" * 60)
    print(" 3. DEMONSTRASI DUCK TYPING")
    print("=" * 60)
    transfer = PembayaranTransfer()
    qris = PembayaranDompetDigital()

    bayar_layanan_klinik(transfer, 150000)
    bayar_layanan_klinik(qris, 75000)
    print("=" * 60)
