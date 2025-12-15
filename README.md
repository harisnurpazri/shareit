# Library Management System - Project Tutorial

## 📚 Deskripsi Project
Aplikasi manajemen perpustakaan sederhana yang dibangun menggunakan Python dengan konsep **Object-Oriented Programming (OOP)** dan arsitektur **Model-View-Controller (MVC)**.

---

## 🎯 Tujuan Pembelajaran
1. Memahami 4 pilar OOP (Abstraction, Inheritance, Polymorphism, Encapsulation)
2. Memahami arsitektur MVC (Model-View-Controller)
3. Implementasi database MySQL dengan Python
4. Menulis kode yang modular dan mudah dimaintain

---

## 📖 Pengenalan OOP (Object-Oriented Programming)

### Apa itu OOP?
OOP adalah paradigma pemrograman yang mengorganisir kode berdasarkan **objek** yang memiliki data (attributes) dan perilaku (methods). OOP membantu kita menulis kode yang lebih terstruktur, reusable, dan mudah dipahami.

### 4 Pilar OOP

#### 1. **Abstraction (Abstraksi)**
Menyembunyikan detail implementasi yang kompleks dan hanya menampilkan fitur penting kepada user.

**Contoh dalam project:**
```python
from abc import ABC, abstractmethod

class Item(ABC):  # Class abstract
    @abstractmethod
    def display_info(self):
        pass  # Method harus diimplementasikan di child class
```

**Analogi:** Seperti mengendarai mobil, Anda hanya perlu tahu cara menggunakan kemudi, gas, dan rem tanpa perlu tahu detail mesin di dalamnya.

#### 2. **Inheritance (Pewarisan)**
Child class mewarisi properties dan methods dari parent class.

**Contoh dalam project:**
```python
class Book(Item):  # Book mewarisi dari Item
    def __init__(self, title, author):
        self.title = title
        self.author = author
```

**Analogi:** Seperti anak mewarisi ciri-ciri dari orang tua.

#### 3. **Polymorphism (Polimorfisme)**
Kemampuan objek berbeda untuk merespons method yang sama dengan cara berbeda.

**Contoh dalam project:**
```python
class Book(Item):
    def display_info(self):
        return f"Book: {self.title}"

class Magazine(Item):
    def display_info(self):
        return f"Magazine: {self.title}"
```

Kedua class punya method `display_info()` tapi implementasinya berbeda.

**Analogi:** Tombol "play" - di TV memutar channel, di music player memutar lagu, tapi tombolnya sama.

#### 4. **Encapsulation (Enkapsulasi)**
Menyembunyikan data internal dan mengaksesnya melalui method tertentu.

**Contoh dalam project:**
```python
class Book:
    def __init__(self, title):
        self.__title = title  # Private attribute (__)
    
    def get_title(self):  # Getter
        return self.__title
    
    def set_title(self, title):  # Setter
        self.__title = title
```

**Analogi:** Seperti ATM, Anda tidak bisa langsung ambil uang dari brankas, tapi harus melalui mesin ATM (interface).

---

## 🏗️ Arsitektur MVC (Model-View-Controller)

MVC adalah pola desain yang memisahkan aplikasi menjadi 3 komponen utama:

### **1. Model**
- **Tugas:** Mengelola data dan logika bisnis
- **Isi:** Class yang berinteraksi dengan database
- **Contoh:** `BookModel`, `MagazineModel`

```python
class BookModel:
    def get_all_books(self):
        # Query database untuk mengambil semua buku
        pass
    
    def add_book(self, book):
        # Insert data buku ke database
        pass
```

**Analogi:** Model seperti gudang data, tempat semua data disimpan dan dikelola.

### **2. View**
- **Tugas:** Menampilkan informasi kepada user dan menerima input
- **Isi:** Interface/UI untuk berinteraksi dengan user
- **Contoh:** `ConsoleView`

```python
class ConsoleView:
    def show_menu(self):
        print("1. Tampilkan Buku")
        print("2. Tambah Buku")
    
    def get_user_input(self):
        return input("Pilih menu: ")
```

**Analogi:** View seperti kasir di toko, yang berinteraksi langsung dengan pelanggan.

### **3. Controller**
- **Tugas:** Menghubungkan Model dan View, mengatur alur aplikasi
- **Isi:** Logika untuk memproses input user dan memanggil Model/View
- **Contoh:** `LibraryController`

```python
class LibraryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def run(self):
        choice = self.view.get_user_input()
        if choice == "1":
            books = self.model.get_all_books()
            self.view.display_books(books)
```

**Analogi:** Controller seperti manajer toko yang menerima pesanan dari kasir, mengambil barang dari gudang, lalu memberikannya ke kasir untuk diberikan ke pelanggan.

---

## 📂 Struktur Project

```
library_management/
│
├── models/
│   ├── __init__.py
│   ├── base_model.py        # Abstract class Item
│   ├── book_model.py        # Model untuk Book
│   └── magazine_model.py    # Model untuk Magazine
│
├── views/
│   ├── __init__.py
│   └── console_view.py      # View untuk console interface
│
├── controllers/
│   ├── __init__.py
│   └── library_controller.py  # Controller utama
│
├── database/
│   ├── __init__.py
│   └── db_connection.py     # Koneksi database
│
├── main.py                  # Entry point aplikasi
├── requirements.txt         # Dependencies
└── README.md               # Dokumentasi
```

---

## 🔧 Setup & Instalasi

### 1. Install Dependencies
```bash
pip install mysql-connector-python
```

### 2. Setup Database MySQL
```sql
CREATE DATABASE library_db;

USE library_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT,
    isbn VARCHAR(50)
);

CREATE TABLE magazines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publisher VARCHAR(255),
    issue_number INT
);
```

### 3. Konfigurasi Database
Edit file `database/db_connection.py` dengan kredensial MySQL Anda:
```python
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'library_db'
}
```

### 4. Jalankan Aplikasi
```bash
python main.py
```

---

## 🎓 Alur Kerja MVC dalam Project Ini

1. **User** memilih menu di **View** (ConsoleView)
2. **View** mengirim pilihan ke **Controller** (LibraryController)
3. **Controller** memproses pilihan dan meminta data ke **Model** (BookModel/MagazineModel)
4. **Model** mengambil/menyimpan data dari/ke **Database**
5. **Model** mengembalikan data ke **Controller**
6. **Controller** mengirim data ke **View** untuk ditampilkan
7. **View** menampilkan hasil kepada **User**

---

## 💡 Tips untuk Mentor

### Konsep yang Perlu Ditekankan:
1. **Separation of Concerns:** Setiap komponen punya tanggung jawab berbeda
2. **Reusability:** Code bisa digunakan ulang karena modular
3. **Maintainability:** Mudah diubah karena terstruktur
4. **Single Responsibility:** Satu class satu tugas

### Latihan untuk Siswa:
1. Tambahkan fitur edit dan delete
2. Buat class baru (DVD, Journal) yang inherit dari Item
3. Tambahkan validasi input
4. Implementasikan pencarian berdasarkan kriteria
5. Buat View berbeda (GUI dengan Tkinter)

---

## 📚 Resources Tambahan
- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [MVC Pattern Explained](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [MySQL Python Connector](https://dev.mysql.com/doc/connector-python/en/)

---

**Selamat Belajar! 🚀**
