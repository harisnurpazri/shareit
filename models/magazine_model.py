"""
Magazine Model - Model untuk data Majalah
Demonstrasi INHERITANCE dan POLYMORPHISM
"""

from models.base_model import Item


class Magazine(Item):
    """
    Class Magazine yang inherit dari Item
    Menunjukkan bahwa child class berbeda bisa inherit dari parent yang sama
    
    Konsep OOP yang diterapkan:
    1. INHERITANCE: Mewarisi dari class Item
    2. POLYMORPHISM: display_info() berbeda dengan Book
    3. ENCAPSULATION: Private attributes
    """
    
    def __init__(self, title, publisher=None, issue_number=None):
        super().__init__(title)
        self.__publisher = publisher
        self.__issue_number = issue_number
    
    # Getter dan Setter (ENCAPSULATION)
    def get_publisher(self):
        return self.__publisher
    
    def set_publisher(self, publisher):
        self.__publisher = publisher
    
    def get_issue_number(self):
        return self.__issue_number
    
    def set_issue_number(self, issue_number):
        if issue_number is None or (isinstance(issue_number, int) and issue_number > 0):
            self.__issue_number = issue_number
        else:
            raise ValueError("Issue number harus berupa angka positif")
    
    # Implementasi abstract method dari parent (POLYMORPHISM)
    def display_info(self):
        """
        Override method dari parent class
        Implementasi berbeda dengan Book (POLYMORPHISM)
        """
        info = f"📰 Majalah: {self.get_title()}\n"
        if self.__publisher:
            info += f"   Penerbit: {self.__publisher}\n"
        if self.__issue_number:
            info += f"   Edisi: #{self.__issue_number}\n"
        return info
    
    def to_dict(self):
        """Convert object ke dictionary untuk database"""
        return {
            'title': self.get_title(),
            'publisher': self.__publisher,
            'issue_number': self.__issue_number
        }
    
    @staticmethod
    def from_db_row(row):
        """
        Factory method untuk membuat object Magazine dari hasil query database
        row format: (id, title, publisher, issue_number)
        """
        magazine = Magazine(
            title=row[1],
            publisher=row[2],
            issue_number=row[3]
        )
        magazine.set_id(row[0])
        return magazine