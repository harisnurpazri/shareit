"""
Database Connection Module
Mengelola koneksi ke MySQL database dengan ENCAPSULATION
"""

import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    """
    Singleton class untuk mengelola koneksi database
    
    Konsep OOP yang diterapkan:
    1. ENCAPSULATION: Private attributes untuk config dan connection
    2. Singleton Pattern: Hanya ada satu instance koneksi
    """
    
    _instance = None
    
    def __new__(cls):
        """Singleton pattern: hanya buat satu instance"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize database configuration"""
        if self.__initialized:
            return
        
        # Private configuration (ENCAPSULATION)
        self.__config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',  # Sesuaikan dengan password MySQL Anda
            'database': 'library_db'
        }
        self.__connection = None
        self.__initialized = True
    
    def get_connection(self):
        """
        Mendapatkan koneksi database
        Membuat koneksi baru jika belum ada atau sudah tertutup
        """
        try:
            if self.__connection is None or not self.__connection.is_connected():
                self.__connection = mysql.connector.connect(**self.__config)
                print("✅ Koneksi database berhasil")
            return self.__connection
        except Error as e:
            print(f"❌ Error koneksi database: {e}")
            return None
    
    def close_connection(self):
        """Menutup koneksi database"""
        if self.__connection and self.__connection.is_connected():
            self.__connection.close()
            print("✅ Koneksi database ditutup")
    
    def execute_query(self, query, params=None):
        """
        Execute query INSERT, UPDATE, DELETE
        Returns: True jika sukses, False jika gagal
        """
        try:
            connection = self.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query, params or ())
                connection.commit()
                cursor.close()
                return True
        except Error as e:
            print(f"❌ Error execute query: {e}")
            return False
    
    def fetch_all(self, query, params=None):
        """
        Execute query SELECT dan return semua hasil
        Returns: List of tuples atau None jika error
        """
        try:
            connection = self.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query, params or ())
                results = cursor.fetchall()
                cursor.close()
                return results
        except Error as e:
            print(f"❌ Error fetch data: {e}")
            return None
    
    def fetch_one(self, query, params=None):
        """
        Execute query SELECT dan return satu hasil
        Returns: Tuple atau None
        """
        try:
            connection = self.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query, params or ())
                result = cursor.fetchone()
                cursor.close()
                return result
        except Error as e:
            print(f"❌ Error fetch data: {e}")
            return None