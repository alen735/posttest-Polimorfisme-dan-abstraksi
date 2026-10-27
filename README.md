1.Relasi UML (Class diagram sederhana)




<img width="442" height="282" alt="Untitled Diagram drawio (1)" src="https://github.com/user-attachments/assets/feb99ba6-187f-4f66-bb81-a3fca012576e" />

Assosiasi
Relasi : Antara class Dokter dan class pasien
penjelasan : Hubungan umum antar kelas yang dimana objek-objek saling berinteraksi atau terhubung ( seperti dokter dan pasien dalam layanan pemeriksaan).

Agregasi
Relasi : Antara classklinik dan class dokter
penjelasan : Hubungan antara klinik dan dokter, dimana klinik tetap memiliki daftar dokter, tetapi jika objek klinik dihapus, objek dokter tetap dapat eksis dan bekerja secara mandiri.

Komposisi
Relasi : Antara class pasien dan rekam medis
Penjelasan : Hubungan antarapasien dan rekam medis, dimana rekam medis merupakan bagian mutlak yang melekat pada pasien , jika pasien data pasien dihapus dari sistem, catatan rekam medis spesifik miliknya juga ikut terhapus.

2.Abstraksi (Abstract Base Class)
bukti abstract class yang tidak dapat diinstansiasi


if __name__ == "__main__":
    
    print("=== 4. BUKTI ABSTRAKSI (Uji Gagal Instansiasi Abstract Class) ===")
    try:
        orang_gagal = Orang("Uji Coba", "1234567890123456", "Jl. Merdeka")
    except TypeError as e:
        print(f"Berhasil Mencegah Instansiasi:\n-> TypeError: {e}\n")

Hasil output :

<img width="598" height="307" alt="Hasil output" src="https://github.com/user-attachments/assets/458b2b70-b2a5-4315-a9ee-bb8e7302a329" />
