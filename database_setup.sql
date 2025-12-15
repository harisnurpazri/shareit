-- =====================================================
-- DATABASE SETUP UNTUK LIBRARY MANAGEMENT SYSTEM
-- =====================================================

-- Buat database
CREATE DATABASE IF NOT EXISTS library_db;

-- Gunakan database
USE library_db;

-- Tabel untuk Buku
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT,
    isbn VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_title (title),
    INDEX idx_author (author)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabel untuk Majalah
CREATE TABLE IF NOT EXISTS magazines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publisher VARCHAR(255),
    issue_number INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_title (title),
    INDEX idx_publisher (publisher)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================
-- DATA SAMPLE UNTUK TESTING (OPSIONAL)
-- =====================================================

-- Insert sample books
INSERT INTO books (title, author, year, isbn) VALUES
('Clean Code', 'Robert C. Martin', 2008, '978-0132350884'),
('Design Patterns', 'Gang of Four', 1994, '978-0201633610'),
('The Pragmatic Programmer', 'Andrew Hunt', 1999, '978-0201616224'),
('Head First Design Patterns', 'Eric Freeman', 2004, '978-0596007126'),
('Python Crash Course', 'Eric Matthes', 2019, '978-1593279288');

-- Insert sample magazines
INSERT INTO magazines (title, publisher, issue_number) VALUES
('National Geographic', 'National Geographic Society', 202),
('Time Magazine', 'Time USA LLC', 45),
('Forbes Indonesia', 'Forbes Media', 98),
('Wired', 'Condé Nast', 156),
('Scientific American', 'Springer Nature', 234);

-- =====================================================
-- QUERY UNTUK VERIFIKASI
-- =====================================================

-- Cek jumlah buku
SELECT COUNT(*) as total_books FROM books;

-- Cek jumlah majalah
SELECT COUNT(*) as total_magazines FROM magazines;

-- Tampilkan semua buku
SELECT * FROM books ORDER BY title;

-- Tampilkan semua majalah
SELECT * FROM magazines ORDER BY title;