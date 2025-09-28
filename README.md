# Mini-Projek-2-Dasar-Pemrograman
Sabrina Azhmalia Nisa (NIM 2509116051)
Tema = Sistem Resep Masakan

# Flowchart
![MINPRO 2](https://github.com/user-attachments/assets/06efa8e4-0eb8-4cab-82b1-0f38617f0ee8)
Ketika mulai, user akan diminta untuk memilih role sebagai manager atau karyawan. Jika menginput angka 1 yaitu sebagai manager, maka user harus memasukkan username dan password. Jika sudah, tampilan menu utama akan terlihat, yaitu 1. Lihat resep, 2. Ubah resep, 3. Tambah resep, 4. Hapus resep, dan 5. Keluar. Ketika menginput angka 1, outputnya adalah daftar resep akan terlihat. Resep yang tersedia adalah cireng, dan pisang keju. Jika mengetikkan nama resep, maka bahan dan cara pembuatannya akan terlihat, lalu sistem akan kembali ke menu utama. Jika user tidak menginput angka 1, melainkan angka 2, maka outputnya adalah sistem akan memberikan pilihan yes or no untuk mengupdate resep. Jika 'yes', maka outputnya adalah sistem akan mengarahkan untuk menginput nama resep yang akan diubah, lalu menginput nama resep yang baru, hasilnya nama resep berhasil diubah, dan kembali ke menu utama. Jika 'no', maka outputnya adalah sistem akan kembali ke menu utama. Jika user tidak menginput angka 2, melainkan angka 3, maka outputnya adalah sistem akan memberikan pilihan yes or no untuk menambahkan resep. Jika 'yes', maka outputnya adalah sistem meminta user untuk menginput nama resep yang baru, bahan-bahan yang baru, dan langkah-langkah pembuatan yang baru, hasilnya resep baru berhasil ditambahkan, dan sistem kembali ke menu utama. Jika 'no', maka outputnya adalah sistem akan kembali ke menu utama. Jika user tidak menginput angka 3, melainkan angka 4, maka outputnya adalah sistem akan meminta user untuk memasukkan nama resep yang ada untuk dihapus, dan saat sudah berhasil menghapus resep sistem akan kembali ke menu utama. Jika user tidak menginput angka 4, melainkan angka 5, maka outputnya adalah 'Terima kasih, have a nice day!' dan akan keluar dari sistem. Jika user menginput angka diluar 1 sampai 5, maka outputnya adalah 'Tidak valid!' dan sistem akan berakhir. Jika saat login user memilih untuk menginput angka 2 yaitu sebagai karyawan, maka user harus memasukkan username dan password. Jika sudah, tampilan menu utama akan terlihat, yaitu 1. Lihat resep, dan 2. Keluar. Jika user menginput angka 1, maka outputnya adalah daftar resep akan terlihat, yaitu cireng dan pisang keju. Persis sama seperti role manager. Jika user tidak menginput angka 1, melainkan angka 2, maka outputnya adalah 'Terima kasih, have a nice day!' dan akan keluar dari sistem. Jika user tidak menginput angka 1 atau 2, melainkan angka yang lain, maka outputnya adalah 'Tidak valid!' dan sistem akan berakhir. Begitu pun ketika login, jika user menginput angka diluar 1 dan 2, maka outputnya adalah 'Tidak valid!' dan sistem berakhir. Selesai.

# Code Pyhton
# Kondisi 1, Login Sebagai Manager (Create, Read, Update, Delete)
<img width="675" height="393" alt="login m berhsil" src="https://github.com/user-attachments/assets/9490162b-1273-43bf-8b11-db53f46f17a0" />

Ini adalah tampilan jika login berhasil sebagai manager, menu utama akan terlihat.

<img width="675" height="393" alt="lobin m ggl" src="https://github.com/user-attachments/assets/6f9c742c-4be6-42c1-a480-059991d45f35" />

Ini adalah tampilan jika input username dan passwordnya salah, maka login gagal dan sistem berhenti.

<img width="998" height="919" alt="input 1 m" src="https://github.com/user-attachments/assets/b3700bfe-034a-4a1a-97e5-90c6bd967656" />

Ketika menginput angka 1, maka tampilannya akan seperti gambar di atas. Daftar resep akan terlihat dan jika diinput maka menghasilkan bahan-bahan lengkap dengan cara pembuatannya. Dan sistem akan kembali ke menu utama. 

<img width="673" height="398" alt="input 1 m resep g ada" src="https://github.com/user-attachments/assets/b073257b-c38c-4001-ad77-676577979233" />

Ini adalah tampilan jika menginput nama resep yang tidak ada, lalu sistem akan kembali ke menu utama.

<img width="702" height="441" alt="input 2 m ya" src="https://github.com/user-attachments/assets/7559d315-b378-4706-bf80-4e78103f23fe" />

Ini adalah tampilan ketika menginput angka 2, sistem akan memberikan pilihan ya atau tidak. Dan jika memilih 'ya', maka tampilannya seperti gambar di atas. Lalu sistem akan kembali ke menu utama.

<img width="735" height="372" alt="input 2 m no" src="https://github.com/user-attachments/assets/11077a1c-d693-479b-a161-9b87f4535d16" />

Dan ini adalah tampilan jika tadi memilih 'tidak', sistem akan mengarahkan ke menu utama lagi.

<img width="819" height="577" alt="input 3 m ya" src="https://github.com/user-attachments/assets/005749b8-2b72-40e8-b822-25de5daa9a2b" />

Ini adalah tampilan jika menginput angka 3, sistem akan memberikan pilihan ya atau tidak. Jika user memilih 'ya', maka tampilannya akan seperti gambar di atas. Lalu sistem akan kembali ke menu utama.

<img width="696" height="370" alt="input 3 m no" src="https://github.com/user-attachments/assets/2b0a9336-b0ca-4ee8-8a1b-47c62ac55970" />

Dan ini adalah tampilan jika tadi user memilih 'tidak', sistem akan mengarahkan kembali ke menu utama.

<img width="725" height="354" alt="input 4 m" src="https://github.com/user-attachments/assets/1279b3bf-f1e1-45d0-b109-5b1091da8309" />

Ini adalah tampilan jika user menginput angka 4, sistem akan meminta user untuk memasukkan nama resep yang ingin dihapus, lalu sistem akan kembali ke menu utama.

<img width="730" height="447" alt="input 4 m reep g ada" src="https://github.com/user-attachments/assets/01b0aafb-1c63-4b5b-bcce-51abce60b919" />

Ini adalah tampilan jika menginput nama resep yang tidak ada.

<img width="601" height="200" alt="input 5 m" src="https://github.com/user-attachments/assets/4ffa0507-1b74-4390-98e5-d13139029110" />

Dan ini adalah tampilan jika user menginput angka 5, maka sistem akan berhenti.

<img width="627" height="448" alt="input m tidak vld" src="https://github.com/user-attachments/assets/7327c230-9572-493e-a50d-bc6ab600c233" />

Ketika menginput angka diluar angka 1 sampai 5, maka tampilannya akan seperti gambar di atas ini.

# Kondisi 2, Login Sebagai Karyawan (Read)
<img width="606" height="363" alt="login k brhaaasil" src="https://github.com/user-attachments/assets/86d927d2-ad45-47d4-a743-e2a17450b491" />

Ini adalah tampilan jika username dan password yang diinput benar, maka login berhasil.

<img width="546" height="242" alt="lohin k ggl" src="https://github.com/user-attachments/assets/e4dce7c6-e882-4fd4-81ba-2efd7c23e093" />

Dan ini adalah tampilan jika username dan password yang diinput salah, maka login gagal.

<img width="917" height="751" alt="input 1 k" src="https://github.com/user-attachments/assets/96f9b287-2594-47d6-b92f-2806d553710e" />

Ini adalah tampilan jika menginput angka 1, daftar resep akan terlihat dan jika diinput maka akan menghasilkan bahan-bahan lengkap dengan cara pembuatannya. Dan sistem akan kembali ke menu utama.

<img width="640" height="482" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/503ab7ba-88ae-4ccd-8632-4db09721aeaa" />

Ini adalah tampilan jika user menginput resep masakan yang tidak ada. Dan sistem akan langsung kembali ke menu utama.

<img width="470" height="134" alt="iput  2k" src="https://github.com/user-attachments/assets/7ac22a50-7e8a-44f5-a96c-2f17315b14c4" />

Dan ini adalah tampilan jika user menginput angka 2, maka sistem akan berhenti.

<img width="573" height="389" alt="input k tdk vld" src="https://github.com/user-attachments/assets/eaa92431-4824-4a49-903c-27257a399ab3" />

Sedangkan ini adalah tampilan ketika user menginput angka selain 1 dan 2, maka sistem akan langsung berhenti. 

# Kondisi 3, Error Handling
<img width="831" height="707" alt="error" src="https://github.com/user-attachments/assets/bf7f5a9e-0a59-439b-9238-b66fbef5f10e" />

Ini adalah tampilan jika user iseng menekan ctrl + c ketika program sedang berjalan.

# Kondisi 4, Input Tidak Valid
<img width="528" height="230" alt="login tdk valid" src="https://github.com/user-attachments/assets/b9ac44cb-dae8-411c-b3ab-378454fd93fa" />

Ini adalah tampilan ketika login user menginput angka selain 1 dan 2, maka sistem akan langsung berhenti.
