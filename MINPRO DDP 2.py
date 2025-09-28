print("Sabrina Azhmalia Nisa")
print("NIM 2509116051")
print("Ssitem Informasi B")

print("=== Halo >< Selamat Datang di Dapur Resep Ariana! ===")

print("Login sebagai:")
print("1. Manager")
print("2. Karyawan")

def login():
    try:
        choice = input("masukkan nomor: ")
        if choice == "1":
            username_pengguna = "manager ariana"
            password_pengguna = "bos123"
            
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            while True:   
                if username == username_pengguna and password == password_pengguna:
                    print("Login berhasil")
                    print("=== Selamat Datang Manager Ariana! ===") 
                    print("1. Lihat Resep")       
                    print("2. Ubah Resep")
                    print("3. Tambah Resep")
                    print("4. Hapus Resep")
                    print("5. Keluar")
                    manager_choice = input("Ingin melakukan apa nih manager yg terhormat? (1/2/3/4/5): ")
                    
                    # Daftar Resep Masakan yang Tersedia
                    Resep = {
                "Cireng": {
                    "Bahan": ["Tepung tapioka", "Tepung terigu", "Garam", "Air panas"],
                    "Langkah": "Campur semua bahan, bentuk adonan sesuai selera, goreng di minyak panas, cireng siap dinikmati."
                },
                "Pisang keju": {
                    "Bahan": ["Buah pisang", "Keju", "Susu kental manis", "Gula palem"],
                    "Langkah": "Kupas pisang, belah, taburi keju, susu, gula palem, pisang keju siap dinikmati."
                }
            }
                    
                    if manager_choice == "1":
                            print("Daftar resep yang tersedia: ")
                            print("Cireng, Pisang keju")
                            Nama = input("Masukkan resep: ")
                            if Nama == "Cireng":
                                print("Bahan:")
                                for bahan in Resep["Cireng"]["Bahan"]:
                                    print("-", bahan)
                                print("Langkah:")
                                print(Resep["Cireng"]["Langkah"])
                            elif Nama == "Pisang keju":
                                print("Bahan:")
                                for bahan in Resep["Pisang keju"]["Bahan"]:
                                    print("-", bahan)
                                print("Langkah:")
                                print(Resep["Pisang keju"]["Langkah"])
                            else:
                                print("Resep tidak ada!")                        
                    elif manager_choice == "2":
                        Nama = input("Apakah anda ingin mengupdate resep?: (ya/tidak)")
                        if Nama == "ya":
                            print("Memperbarui nama resep!")
                            Nama_Lama = input("Masukkan nama resep yang ingin diupdate: ")
                            if Nama_Lama in Resep:
                                Nama_Baru = input("Masukkan nama baru yang ingin dipakai: ")
                                Resep[Nama_Baru] = Resep.pop(Nama_Lama)
                                print(f"Resep {Nama_Lama} telah diubah menjadi {Nama_Baru}")
                        elif Nama == "tidak":
                            print("Baiklah!")
                        else:
                            print("Resep apaan tuh? gak ada bos!")
                    elif manager_choice == "3":
                        Buat = input("Apakah anda ingin menambahkan resep?: (ya/tidak)")
                        if Buat == "ya":
                            Resep_Baru = input("Masukkan nama resep yang baru: ")
                            Bahan = []
                            print("Masukkan bahannya (ketik 'selesai' jika sudah): ")
                            while True:
                                item = input("- ")
                                if item.lower() == 'selesai':
                                    Bahan.append(item)
                                    break
                            print("Masukkan langkah-langkahnya (ketik 'selesai' jika sudah): ")
                            Langkah = []
                            while True:
                                cara = input("- ")
                                if cara.lower() == 'selesai':
                                    Langkah.append(cara)
                                    break
                                    
                            New_Resep ={
                                "Nama" : Resep_Baru,
                                "Bahan" : Bahan,
                                "Langkah" : Langkah
                            }
                            
                            Resep.update(New_Resep)
                            print("Resep berhasil ditambahkan!")
                        elif Buat == "tidak":
                            print("Baiklah!")
                        else:
                            print("Tidak valid!")
                    elif manager_choice == "4":
                        Hapus = input("Masukkan resep yang ingin dihapus: (Cireng, Pisang keju)" )
                        if Hapus in Resep:
                            del Resep[Hapus]
                            print(f"Resep '{Hapus}' sudah terhapus!")
                        else:
                            print("Resep tidak ada!")
                    elif manager_choice == "5":
                        print("Terima kasih, have a nice day!")  
                        break  
                    else:
                        print("Tidak valid!") 
                        break
                else:
                    print("Login gagal")
                    break                
        elif choice == "2":
            nama_pengguna = "karyawan grande"
            sandi_pengguna = "kerja247"
                
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            while True:   
                if username == nama_pengguna and password == sandi_pengguna:
                    print("Login berhasil")
                    print("=== Hai! Selamat Datang dan Selamat Bekerja!") 
                    print("1. Lihat Resep")
                    print("2. Keluar") 
                    karyawan_choice = input("Ingin melakukan apa nih? (1/2): ") 
                        
                    # Daftar Resep Masakan yang Tersedia
                    Resep = {
                "Cireng": {
                    "Bahan": ["Tepung tapioka", "Tepung terigu", "Garam", "Air panas"],
                    "Langkah": "Campur semua bahan, bentuk adonan sesuai selera, goreng di minyak panas, cireng siap dinikmati."
                },
                    "Pisang keju": {
                    "Bahan": ["Buah pisang", "Keju", "Susu kental manis", "Gula palem"],
                    "Langkah": "Kupas pisang, belah, taburi keju, susu, gula palem, pisang keju siap dinikmati."
                }
            }
                        
                    if karyawan_choice == "1":
                        print("Daftar resep yang tersedia: ")
                        print("Cireng, Pisang keju")
                        Nama = input("Masukkan resep: ")
                        if Nama == "Cireng":
                            print("Bahan:")
                            for bahan in Resep["Cireng"]["Bahan"]:
                                print("-", bahan)
                            print("Langkah:")
                            print(Resep["Cireng"]["Langkah"])
                        elif Nama == "Pisang keju":
                            print("Bahan:")
                            for bahan in Resep["Pisang keju"]["Bahan"]:
                                print("-", bahan)
                            print("Langkah:")
                            print(Resep["Pisang keju"]["Langkah"])
                        else:
                            print("Resep tidak ada!")
                    elif karyawan_choice == "2":
                        print("Terima kasih, have a nice day!") 
                        break  
                    else:
                        print("Tidak valid!") 
                        break
                else:
                    print("Login gagal")
                    break
        else:
            print("Tidak valid!")
    except KeyboardInterrupt:
        print("JANGAN TEKAN CTRL + C YA!")

login()
