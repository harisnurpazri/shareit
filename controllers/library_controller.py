"""
Library Controller - Pengatur alur aplikasi
Bagian CONTROLLER dari MVC
"""

from models.book_model import Book
from models.magazine_model import Magazine
from database.db_connection import DatabaseConnection


class LibraryController:
    """
    Controller yang menghubungkan Model dan View
    
    Tanggung jawab CONTROLLER:
    1. Menerima input dari View
    2. Memproses logika aplikasi
    3. Memanggil Model untuk operasi database
    4. Mengirim data ke View untuk ditampilkan
    """
    
    def __init__(self, view):
        """
        Initialize controller dengan view
        
        Args:
            view: Instance dari ConsoleView
        """
        self.view = view
        self.db = DatabaseConnection()
    
    def run(self):
        """Main loop aplikasi"""
        self.view.show_header()
        
        while True:
            self.view.show_main_menu()
            choice = self.view.get_input()
            
            if choice == '1':
                self.handle_book_menu()
            elif choice == '2':
                self.handle_magazine_menu()
            elif choice == '0':
                if self.view.confirm("Yakin ingin keluar?"):
                    self.view.show_info("Terima kasih telah menggunakan aplikasi!")
                    self.db.close_connection()
                    break
            else:
                self.view.show_error("Pilihan tidak valid!")
    
    def handle_book_menu(self):
        """Handle menu buku"""
        while True:
            self.view.show_book_menu()
            choice = self.view.get_input()
            
            if choice == '1':
                self.display_all_books()
            elif choice == '2':
                self.add_book()
            elif choice == '3':
                self.search_books()
            elif choice == '0':
                break
            else:
                self.view.show_error("Pilihan tidak valid!")
            
            if choice != '0':
                self.view.pause()
    
    def handle_magazine_menu(self):
        """Handle menu majalah"""
        while True:
            self.view.show_magazine_menu()
            choice = self.view.get_input()
            
            if choice == '1':
                self.display_all_magazines()
            elif choice == '2':
                self.add_magazine()
            elif choice == '3':
                self.search_magazines()
            elif choice == '0':
                break
            else:
                self.view.show_error("Pilihan tidak valid!")
            
            if choice != '0':
                self.view.pause()
    
    # ========== BOOK OPERATIONS ==========
    
    def display_all_books(self):
        """Menampilkan semua buku dari database"""
        query = "SELECT id, title, author, year, isbn FROM books ORDER BY title"
        rows = self.db.fetch_all(query)
        
        if rows:
            # Convert database rows menjadi Book objects
            books = [Book.from_db_row(row) for row in rows]
            self.view.display_items(books, "DAFTAR BUKU")
        else:
            self.view.show_info("Belum ada buku dalam database.")
    
    def add_book(self):
        """Menambahkan buku baru"""
        book_data = self.view.get_book_input()
        
        if book_data:
            # Buat object Book (demonstrasi OOP)
            book = Book(
                title=book_data['title'],
                author=book_data['author'],
                year=book_data['year'],
                isbn=book_data['isbn']
            )
            
            # Insert ke database
            query = """
                INSERT INTO books (title, author, year, isbn)
                VALUES (%s, %s, %s, %s)
            """
            data = book.to_dict()
            params = (data['title'], data['author'], data['year'], data['isbn'])
            
            if self.db.execute_query(query, params):
                self.view.show_success("Buku berhasil ditambahkan!")
            else:
                self.view.show_error("Gagal menambahkan buku!")
    
    def search_books(self):
        """Mencari buku berdasarkan keyword"""
        keyword = self.view.get_search_keyword()
        
        if keyword:
            query = """
                SELECT id, title, author, year, isbn 
                FROM books 
                WHERE title LIKE %s OR author LIKE %s
                ORDER BY title
            """
            search_param = f"%{keyword}%"
            rows = self.db.fetch_all(query, (search_param, search_param))
            
            if rows:
                books = [Book.from_db_row(row) for row in rows]
                self.view.display_items(books, f"HASIL PENCARIAN: '{keyword}'")
            else:
                self.view.show_info(f"Tidak ditemukan buku dengan keyword '{keyword}'")
    
    # ========== MAGAZINE OPERATIONS ==========
    
    def display_all_magazines(self):
        """Menampilkan semua majalah dari database"""
        query = "SELECT id, title, publisher, issue_number FROM magazines ORDER BY title"
        rows = self.db.fetch_all(query)
        
        if rows:
            # Convert database rows menjadi Magazine objects
            magazines = [Magazine.from_db_row(row) for row in rows]
            self.view.display_items(magazines, "DAFTAR MAJALAH")
        else:
            self.view.show_info("Belum ada majalah dalam database.")
    
    def add_magazine(self):
        """Menambahkan majalah baru"""
        magazine_data = self.view.get_magazine_input()
        
        if magazine_data:
            # Buat object Magazine (demonstrasi OOP)
            magazine = Magazine(
                title=magazine_data['title'],
                publisher=magazine_data['publisher'],
                issue_number=magazine_data['issue_number']
            )
            
            # Insert ke database
            query = """
                INSERT INTO magazines (title, publisher, issue_number)
                VALUES (%s, %s, %s)
            """
            data = magazine.to_dict()
            params = (data['title'], data['publisher'], data['issue_number'])
            
            if self.db.execute_query(query, params):
                self.view.show_success("Majalah berhasil ditambahkan!")
            else:
                self.view.show_error("Gagal menambahkan majalah!")
    
    def search_magazines(self):
        """Mencari majalah berdasarkan keyword"""
        keyword = self.view.get_search_keyword()
        
        if keyword:
            query = """
                SELECT id, title, publisher, issue_number 
                FROM magazines 
                WHERE title LIKE %s OR publisher LIKE %s
                ORDER BY title
            """
            search_param = f"%{keyword}%"
            rows = self.db.fetch_all(query, (search_param, search_param))
            
            if rows:
                magazines = [Magazine.from_db_row(row) for row in rows]
                self.view.display_items(magazines, f"HASIL PENCARIAN: '{keyword}'")
            else:
                self.view.show_info(f"Tidak ditemukan majalah dengan keyword '{keyword}'")