"""
Base Model - Abstract Class untuk Item Perpustakaan
Demonstrasi ABSTRACTION dan ENCAPSULATION
"""

from abc import ABC, abstractmethod


class Item(ABC):
    """
    Abstract Base Class untuk semua item di perpustakaan
    
    Konsep OOP yang diterapkan:
    1. ABSTRACTION: Class abstract yang memaksa child class mengimplementasi method tertentu
    2. ENCAPSULATION: Attribute private (__id) yang diakses via getter/setter
    """
    
    def __init__(self, title):
        self.__id = None  # Private attribute (ENCAPSULATION)
        self._title = title  # Protected attribute
    
    # Getter dan Setter untuk ENCAPSULATION
    def get_id(self):
        """Getter untuk mengakses private attribute __id"""
        return self.__id
    
    def set_id(self, item_id):
        """Setter untuk mengubah private attribute __id"""
        self.__id = item_id
    
    def get_title(self):
        """Getter untuk title"""
        return self._title
    
    def set_title(self, title):
        """Setter untuk title dengan validasi"""
        if title and len(title.strip()) > 0:
            self._title = title
        else:
            raise ValueError("Title tidak boleh kosong")
    
    @abstractmethod
    def display_info(self):
        """
        Abstract method yang HARUS diimplementasi oleh child class
        Ini adalah contoh ABSTRACTION
        """
        pass
    
    @abstractmethod
    def to_dict(self):
        """
        Abstract method untuk convert object ke dictionary
        Berguna untuk insert/update database
        """
        pass
    
    def __str__(self):
        """String representation dari object"""
        return f"{self.__class__.__name__}: {self._title}"