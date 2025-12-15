"""
Console View - Interface untuk berinteraksi dengan user
Bagian VIEW dari MVC
"""


class ConsoleView:
    """
    Class untuk menampilkan UI dan menerima input dari user
    
    Tanggung jawab VIEW:
    1. Menampilkan menu dan informasi ke user
    2. Menerima input dari user
    3. TIDAK mengandung logika bisnis (itu tugas Controller dan Model)
    """
    
    def clear_screen(self):
        """Clear console screen"""
        print("\n" * 2)
    
    def show_header(self):
        """Tampilkan header aplikasi"""
        print("=" * 50)
        print("📚 SISTEM MANAJEMEN PERPUSTAKAAN 📚".center(50))
        print("=" * 50)
        print()
    
    def show_main_menu(self):
        """Tampilkan menu utama"""
        print("\n" + "─" * 50)
        print("MENU UTAMA:")
        print("1. Kelola Buku")
        print("2. Kelola Majalah")
        print("0. Keluar")
        print("─" * 50)
    
    def show_book_menu(self):
        """Tampilkan menu buku"""
        print("\n" + "─" * 50)
        print("MENU BUKU:")
        print("1. Tampilkan Semua Buku")
        print("2. Tambah Buku Baru")
        print("3. Cari Buku")
        print("0. Kembali ke Menu Utama")
        print("─" * 50)
    
    def show_magazine_menu(self):
        """Tampilkan menu majalah"""
        print("\n" + "─" * 50)
        print("MENU MAJALAH:")
        print("1. Tampilkan Semua Majalah")
        print("2. Tambah Majalah Baru")
        print("3. Cari Majalah")
        print("0. Kembali ke Menu Utama")
        print("─" * 50)
    
    def get_input(self, prompt="Pilih menu: "):
        """Mendapatkan input dari user"""
        return input(prompt).strip()
    
    def get_number_input(self, prompt):
        """Mendapatkan input angka dari user"""
        while True:
            value = input(prompt).strip()
            if not value:
                return None
            try:
                return int(value)
            except ValueError:
                self.show_error("Input harus berupa angka!")
    
    def display_items(self, items, title="DAFTAR ITEM"):
        """
        Menampilkan list of items (Book atau Magazine)
        Demonstrasi POLYMORPHISM: semua item punya method display_info()
        """
        print("\n" + "=" * 50)
        print(f" {title} ".center(50, "="))
        print("=" * 50)
        
        if not items or len(items) == 0:
            print("Tidak ada data.")
        else:
            for item in items:
                # POLYMORPHISM: display_info() berbeda untuk Book dan Magazine
                print(item.display_info())
                print("-" * 50)
        
        print(f"Total: {len(items) if items else 0} item")
    
    def get_book_input(self):
        """Mendapatkan input untuk buku baru"""
        print("\n" + "─" * 50)
        print("TAMBAH BUKU BARU")
        print("─" * 50)
        
        title = input("Judul Buku: ").strip()
        if not title:
            self.show_error("Judul tidak boleh kosong!")
            return None
        
        author = input("Penulis: ").strip()
        if not author:
            self.show_error("Penulis tidak boleh kosong!")
            return None
        
        year = self.get_number_input("Tahun Terbit (Enter untuk skip): ")
        isbn = input("ISBN (Enter untuk skip): ").strip() or None
        
        return {
            'title': title,
            'author': author,
            'year': year,
            'isbn': isbn
        }
    
    def get_magazine_input(self):
        """Mendapatkan input untuk majalah baru"""
        print("\n" + "─" * 50)
        print("TAMBAH MAJALAH BARU")
        print("─" * 50)
        
        title = input("Judul Majalah: ").strip()
        if not title:
            self.show_error("Judul tidak boleh kosong!")
            return None
        
        publisher = input("Penerbit (Enter untuk skip): ").strip() or None
        issue_number = self.get_number_input("Nomor Edisi (Enter untuk skip): ")
        
        return {
            'title': title,
            'publisher': publisher,
            'issue_number': issue_number
        }
    
    def get_search_keyword(self):
        """Mendapatkan keyword untuk pencarian"""
        return input("\nMasukkan kata kunci pencarian: ").strip()
    
    def show_success(self, message):
        """Tampilkan pesan sukses"""
        print(f"\n✅ {message}")
    
    def show_error(self, message):
        """Tampilkan pesan error"""
        print(f"\n❌ {message}")
    
    def show_info(self, message):
        """Tampilkan pesan informasi"""
        print(f"\nℹ️  {message}")
    
    def pause(self):
        """Pause dan tunggu user press enter"""
        input("\nTekan Enter untuk melanjutkan...")
    
    def confirm(self, message):
        """Konfirmasi yes/no dari user"""
        response = input(f"\n{message} (y/n): ").strip().lower()
        return response == 'y'