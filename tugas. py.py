class Buku:
    def init(self,judul,penulis,genre,
status):
    self.judul = judul
    self.penulis = penulis
    self.genre = genre
    self.status = status


def str(self):
    retur f"{self.judul}-{self.penulis}
({self.genre})-.Status:
{self.status}"


class perpustakaan:
     def_init(self):
         self.koleksi_buku[]

         
     def chehk_ketersediaan(self):
         if not self.buku.tersedia:
            prin(f"Buku {self.buku.judul}'
     tidak tersedia untuk di pinjam.")


    def tampilan_buku(self):
        if self.koleksi_buku:
             print(buku)
         else:
           prin("koleksi buku masih kosong.")


    def cari_buku(self,judul):
        for buku in self.koleksi_buku:
         if buku.judul.lower()==judul.
         lower():
             print(buku)
             retur
        print(f"Buku dengan judul)
            '{judul}'tidak di temukan.")

              
                  if buku.status == "Tersedia":
                  buku.status == "Dipinjam"
                  anggota.buku_pinjaman.a
            .append(buku)
             prin(f"Buku'{buku}'berhasil dipinjam oleh{anggota.nama}.")
             else:
                prin(f"buku'{buku.judul}'tidak tersedia untuk dipinjam."}
            return
              
            class Anggota:
                def_inif_(self,nama,ID):
                    self.nama = nama
                self.ID = ID
                self.buku_pinjamkan =[]

                def tampilkan_buku_pinjaman(self):
                if self.buku_pinjaman:
                    prin(f"--Buku Pinjaman:)
                         {self.nama}--")
            for buku in
                         selp.buku_pinjaman:
                         print(Buku)
                         else
                   prin(f"{self.nama}tidakmemiliki buku pinjaman.")

                         class Catatan_pinjaman:
                         def init(self,id_buku,id_anggota, tanggal_pinjaman,tanggal):
                                 self.id_buku        = id_buku
                                 self.id_anggota     = id_anggota
                         self.tanggal_pinjaman=
                    tanggal_pinjaman
                         self.tanggal_kembali=
                         tanggal_kembali

                         def main():
                         #Buat beberapa buku
                             buku 1 =Buku(".Bumi","Tere liye",
                        Fiski","Tersedia")
                    Buku2 = Buku(".Laskar Pelangi","Andrea Hirata","Fiksi","Tersedia")
                        Buku3 = Buku(".Filosofi Terbang","Dewi Lestari","Fiski","Dipinjam")

                        # Buat anggota
                        anggota1 =Anggota("Adi", 12345)
                        anggota2 =anggota("Adu", 56789)

                        #jalankan program

                        prin("\n-- Menu perpustakaan --")
                        prin("\1. Tampilkan Daftar Buku")
                        prin("\2. Cari buku")
                        prin("\3. pinjam buku")
                        prin("\4. Kembalikan")
                        angka = int(input("pilih menu :"()
                                          
                        if angka == 1 :
                            perputakaan.tampilakan_buku()
                        elif angka == 2:
                            judul = input("Masukan judul buku:")
                        perpustakaan.cari_buku(judul elif angka == 3:
                            perpustakaan.tampilkan_buku()judul = input("judul buku yang akan di pinjam:")
                        perpustakan.pinjam_buku(judul,anggota1)
                            elifangka == 4:
                        prin("daftar buku yang sudah di pinjam:")
                            prin("1.Filosifi terbang")
                        ank = int(input("pilih berdasarkan angka :"))
                            if ank == 1:
                        prin("Trima kasih sudah mengambil bukunya")
                            else:
                                prin("Maaf buku yang anad kembalikan tidak terdaftar di parpus kami")
                            else:
                                prin("Anda salah memilih.")

                            if_name_=="main".
                                main()
                        
                    
                    
                            
                                 
