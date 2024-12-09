class DaftarNilaiMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah(self, nama, nim, jurusan, nilai):
        mahasiswa = {'nama': nama, 'nim': nim, 'jurusan': jurusan, 'nilai': nilai}
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Mahasiswa dengan nama {nama} telah ditambahkan.")

    def tampilkan(self):
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            for i, mahasiswa in enumerate(self.daftar_mahasiswa, start=1):
                print(f"{i}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, Jurusan: {mahasiswa['jurusan']}, Nilai: {mahasiswa['nilai']}")

    def hapus(self, nama):
        self.daftar_mahasiswa = [mahasiswa for mahasiswa in self.daftar_mahasiswa if mahasiswa['nama'] != nama]
        print(f"Mahasiswa dengan nama {nama} telah dihapus.")

    def ubah(self, nama, nama_baru=None, nim_baru=None, jurusan_baru=None, nilai_baru=None):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nama'] == nama:
                if nama_baru:
                    mahasiswa['nama'] = nama_baru
                if nim_baru:
                    mahasiswa['nim'] = nim_baru
                if jurusan_baru:
                    mahasiswa['jurusan'] = jurusan_baru
                if nilai_baru:
                    mahasiswa['nilai'] = nilai_baru

                print(f"Data mahasiswa dengan nama {nama} telah diubah.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

daftar_nilai = DaftarNilaiMahasiswa()

daftar_nilai.tambah("Coki", "1223", "Teknik Informatika", "80")
daftar_nilai.tambah("Lala", "1224", "Teknik Informatika", "95")
daftar_nilai.tambah("Citra", "1225", "Teknik Informatika", "90")
daftar_nilai.tambah("Rizal", "1226", "Teknik Informatika", "88")
daftar_nilai.tambah("Putri", "1227", "Teknik Informatika", "92")

daftar_nilai.tampilkan()

daftar_nilai.hapus("Lala")

daftar_nilai.tampilkan()

daftar_nilai.ubah("Citra", nama_baru="Sarah", nim_baru="1228", jurusan_baru="Teknik Informatika", nilai_baru="94")

daftar_nilai.tampilkan()
