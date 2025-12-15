"""
Book Model - Model untuk data Buku
Demonstrasi INHERITANCE dan POLYMORPHISM
"""

from models.base_model import Item


class Book(Item):
    """
    Class Book yang inherit dari Item
    
    Konsep OOP yang diterapkan:
    1. INHERITANCE: Mewarisi dari class Item
    2. POLYMORPHISM: Mengimplementasi display_info() dengan cara berbeda
    3. ENCAPSULATION: Menggunakan private attributes
    """
    
    def __init__(self, title, author, year=None, isbn=None):
        super().__init__(title)  # Memanggil constructor parent (INHERITANCE)
        self.__author = author
        self.__year = year
        self.__isbn = isbn
    
    # Getter dan Setter (ENCAPSULATION)
    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        if author and len(author.strip()) > 0:
            self.__author = author
        else:
            raise ValueError("Author tidak boleh kosong")
    
    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        if year is None or (isinstance(year, int) and year > 0):
            self.__year = year
        else:
            raise ValueError("Year harus berupa angka positif")
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    # Implementasi abstract method dari parent (POLYMORPHISM)
    def display_info(self):
        """
        Override method dari parent class
        Ini contoh POLYMORPHISM
        """
        info = f"📚 Buku: {self.get_title()}\n"
        info += f"   Penulis: {self.__author}\n"
        if self.__year:
            info += f"   Tahun: {self.__year}\n"
        if self.__isbn:
            info += f"   ISBN: {self.__isbn}\n"
        return info
    
    def to_dict(self):
        """Convert object ke dictionary untuk database"""
        return {
            'title': self.get_title(),
            'author': self.__author,
            'year': self.__year,
            'isbn': self.__isbn
        }
    
    @staticmethod
    def from_db_row(row):
        """
        Factory method untuk membuat object Book dari hasil query database
        row format: (id, title, author, year, isbn)
        """
        book = Book(
            title=row[1],
            author=row[2],
            year=row[3],
            isbn=row[4]
        )
        book.set_id(row[0])
        return book