##CAPSTONE PROJECT_MODUL 1
##DATABASE KARYAWAN
##PROGRAM YANG BERSISI CRUD (CREATE, READ, UPDATE dan DELETE)

## Menu dalam program :
# #   1. Tambah data karyawan
# #   2. Lihat Semua Data Karyawan
# #   3. Update Data Karyawan
# #   4. Hapus Data Karyawan
# #   5. Keluar


# Inisialisasi data karyawan sebagai list of dictionaries
karyawan_list = []

# Fungsi untuk menambahkan karyawan baru dengan validasi
def add_karyawan():
    while True:
        try:
            id = int(input("Masukkan ID (hanya angka): "))
            if any(karyawan['id'] == id for karyawan in karyawan_list):
                print("ID sudah digunakan. Silakan gunakan ID lain.")
                continue
            break
        except ValueError:
            print("ID harus berupa angka. Silakan coba lagi.")

    while True:
        nama = input("Masukkan Nama: ")
        if not nama.isalpha():
            print("Nama hanya boleh mengandung alfabet. Silakan coba lagi.")
        else:
            break

    while True:
        gender = input("Masukkan Gender (Male/Female atau Pria/Wanita): ").capitalize()
        if gender not in ['Male', 'Female', 'Pria', 'Wanita']:
            print("Gender hanya bisa 'Male', 'Female', 'Pria' atau 'Wanita'. Silakan coba lagi.")
        else:
            break

    while True:
        usia = input("Masukkan Usia : ")
        if not usia.isdigit():
            print("Hanya Boleh memasukan angka !")
        else:
            break

    while True:        
        alamat = input("Masukkan Alamat: ")
        if not alamat.isalpha():
            print("Hanya boleh memasukkan alfabet. Silahkan coba lagi")
        else:
            break
    
    while True:
        nomor_telepon = input("Masukan Nomor Telepon :")
        if not nomor_telepon.isdigit():
            print("Hanya boleh memasukan angka !")
        else:
            break

    while True:
        departemen = input("Masukkan Departemen: ")
        if not departemen.isalpha():
            print("Departemen hanya boleh mengandung alfabet. Silakan coba lagi.")
        else:
            break

    karyawan = {
        'id': id,
        'nama': nama,
        'gender': gender,
        'usia': usia,
        'alamat': alamat,
        'nomor_telepon' :nomor_telepon,
        'departemen': departemen,
        
    }
    karyawan_list.append(karyawan)
    print("Karyawan berhasil ditambahkan!")

# Fungsi untuk membaca semua data karyawan
def read_karyawan():
    if not karyawan_list:
        print("Tidak ada data karyawan.")
    else:
        # Cetak header tabel
        print("="*95)
        print(f"{'ID':<5} {'Nama':<20} {'Gender':<10} {'Usia':<10} {'Alamat':<20} {'Nomor_Telepon' :<15} {'Departemen':<15} ")
        print("="*95)
        # Cetak setiap karyawan dalam bentuk tabel
        for karyawan in karyawan_list:
            print(f"{karyawan['id']:<5} {karyawan['nama']:<20} {karyawan['gender']:<10} {karyawan['usia']:<10} {karyawan['alamat']:<20} {karyawan['nomor_telepon']:<15} {karyawan['departemen']:<15}")

# Fungsi untuk memperbarui data karyawan
def update_karyawan():
    try:
        id = int(input("Masukkan ID karyawan yang akan diupdate: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for karyawan in karyawan_list:
        if karyawan['id'] == id:
            print("Karyawan ditemukan. Silakan masukkan data baru.")
            while True:
                nama = input("Masukkan Nama baru : ")
                if not nama.isalpha():
                    print("Nama hanya boleh mengandung alfabet. Silakan coba lagi.")
                else:
                    break

            while True:
                gender = input("Masukkan Gender baru (Male/Female atau Pria/Wanita): ").capitalize()
                if gender not in ['Male', 'Female', 'Pria', 'Wanita']:
                    print("Gender hanya bisa 'Male', 'Female', 'Pria' atau 'Wanita'. Silakan coba lagi.")
                else:
                    break

            while True:
                usia = input("Masukkan Usia baru : ")
                if not usia.isdigit():
                    print("Hanya Boleh memasukan angka !")
                else:
                    break

            while True:
                alamat = input("Masukan Alamat baru :")
                if not alamat.isalpha():
                    print("Hanya boleh memasukkan alfabet. Silahkan coba lagi")
                else:
                    break
            
            while True:
                nomor_telepon = input("Masukan Nomor Telepon baru:")
                if not nomor_telepon.isdigit():
                    print("Hanya boleh memasukan angka !")
                else:
                    break

            while True:
                departemen = input("Masukkan Departemen baru : ")
                if not departemen.isalpha():
                    print("Departemen hanya boleh mengandung alfabet. Silakan coba lagi.")
                else:
                    break
            
        
            karyawan['nama'] = nama
            karyawan['gender'] = gender
            karyawan['usia'] = usia
            karyawan['alamat'] = alamat
            karyawan['nomor_telepon'] = nomor_telepon
            karyawan['departemen'] = departemen
            print("Karyawan berhasil diupdate!")
            return
    print("Karyawan dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus data karyawan
def delete_karyawan():
    try:
        id = int(input("Masukkan ID karyawan yang akan dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for karyawan in karyawan_list:
        if karyawan['id'] == id:
            karyawan_list.remove(karyawan)
            print("Karyawan berhasil dihapus!")
            return
    print("Karyawan dengan ID tersebut tidak ditemukan.")


# Menu utama
def display_menu():
    print("\n                 ======== SELAMAT DATANG DI APLIKASI DATA KARYAWAN ======== \n")
    print("==== Menu Utama ====")
    print("1. Tambah Data Karyawan")
    print("2. Lihat Semua Data Karyawan")
    print("3. Update Data Karyawan")
    print("4. Hapus Data Karyawan")
    print("5. Keluar")

def main():
    while True:
        display_menu()
        pilih_menu = input("Pilih opsi: ")

        if pilih_menu == '1':
            add_karyawan()
        
        elif pilih_menu == '2':
            read_karyawan()
        
        elif pilih_menu == '3':
            update_karyawan()
        
        elif pilih_menu == '4':
            delete_karyawan()
        
        elif pilih_menu == '5':
            print("Keluar dari program...")
            break
        
        else:
            print("Opsi tidak valid. Silakan coba lagi.")


main()
