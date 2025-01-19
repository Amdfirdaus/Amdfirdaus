from prettytable import PrettyTable

databarang = []

def format_currency(value):
    return f"Rp{value:,.2f}"

def input_barang(databarang):
    while True:
        try:
            nama_barang = input("Nama barang: ")
            jumlah_barang = int(input("Jumlah barang: "))
            harga_barang = int(input("Harga barang: "))
            sub = harga_barang * jumlah_barang
            
            databarang.append({
                "nama barang": nama_barang,
                "jumlah barang": jumlah_barang,
                "harga barang": harga_barang,
                "SubTotal": sub
            })
            print("Barang berhasil dimasukkan")
            
        except ValueError:
            print("Input tidak valid! Pastikan memasukkan angka yang benar.")
        
        lanjut = input("Tambah barang lagi? (y/t): ").lower()
        if lanjut != 'y':
            break
    return databarang

def print_centered(text, width=50):
    print(text.center(width))

def cetak_transaksi(databarang):
    print_centered("    ANJAY STORE BANYUWANGI", 50)
    print_centered("    Jl. Jenderal Ahmad Yani No.80, Taman Baru", 50)
    print_centered("    Kec.Banyuwangi, Kabupaten Banyuwangi, Jawa Timur 68416", 50)
    table_transaksi = PrettyTable(["Nama Barang", "Jumlah Barang", "Harga Barang", "SubTotal"])
    
    total = 0
    for transaksi in databarang:
        total += transaksi["SubTotal"]
        
        table_transaksi.add_row([
            transaksi["nama barang"],
            transaksi["jumlah barang"],
            format_currency(transaksi["harga barang"]),
            format_currency(transaksi["SubTotal"])
        ])
        
    print(table_transaksi)
    print(f"Total: {format_currency(total)}")
    return total

def pembayaran(subtotal):
    while True:
        try:
            diskon = 0
            if subtotal >= 100000:
                diskon = subtotal * 0.50
            
            total_setelah_diskon = subtotal - diskon
            print(f"{'Total setelah diskon:' :<47}{format_currency(total_setelah_diskon)}")
            
            prompt = f"{'Pembayaran-Tunai:':<20}{'Rp':>29} "
            pembayaran = int(input(prompt))

            if pembayaran < total_setelah_diskon:
                print("Jumlah pembayaran kurang dari total yang harus dibayar! Silakan masukkan jumlah yang cukup.")
            else:
                kembalian = pembayaran - total_setelah_diskon
                print(f"{'Kembalian:' :<47}{format_currency(kembalian)}")
                return pembayaran, kembalian
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")

def menu(): 
    databarang = []
    while True:
        print("-" * 10)
        print("Menu Pilihan")
        print("-" * 10)
        print("1. Tambah barang")
        print("2. Cetak transaksi")
        print("3. Pembayaran")
        print("4. Selesai")
        pilih = input("Pilih menu (1-4): ")
        
        if pilih == "1":
            databarang = input_barang(databarang)
        elif pilih == "2":
            if databarang:
                cetak_transaksi(databarang)
            else:
                print("Belum ada barang yang dimasukkan!")
        elif pilih == "3":
            if databarang: 
                total = cetak_transaksi(databarang)
                pembayaran_amount, kembalian = pembayaran(total)
                print(f"Total pembayaran: {format_currency(pembayaran_amount)}")
                print(f"Kembalian: {format_currency(kembalian)}")
            else:
                print("Belum ada barang yang dimasukkan!")
        elif pilih == "4":
            print("Terima kasih, selesai!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih sesuai nomor.")

menu()
