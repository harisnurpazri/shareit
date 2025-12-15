"""
Main Entry Point - Aplikasi Sistem Manajemen Perpustakaan

Demonstrasi lengkap konsep:
- OOP: Abstraction, Inheritance, Polymorphism, Encapsulation
- MVC: Model-View-Controller Architecture
- Database Integration dengan MySQL
"""

from views.console_view import ConsoleView
from controllers.library_controller import LibraryController


def main():
    """
    Function utama untuk menjalankan aplikasi
    
    Alur kerja:
    1. Buat instance View
    2. Buat instance Controller dengan View
    3. Jalankan Controller (yang akan handle semua logic)
    """
    
    print("""
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║      SISTEM MANAJEMEN PERPUSTAKAAN SEDERHANA      ║
    ║              OOP & MVC Architecture                ║
    ║                                                    ║
    ║  Demonstrasi:                                      ║
    ║  ✓ Abstraction  ✓ Inheritance                     ║
    ║  ✓ Polymorphism ✓ Encapsulation                   ║
    ║  ✓ Model-View-Controller Pattern                  ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """)
    
    try:
        # Inisialisasi View
        view = ConsoleView()
        
        # Inisialisasi Controller dengan View
        # Controller akan mengelola Model dan komunikasi View-Model
        controller = LibraryController(view)
        
        # Jalankan aplikasi
        controller.run()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Aplikasi dihentikan oleh user (Ctrl+C)")
    except Exception as e:
        print(f"\n\n❌ Terjadi error: {e}")
        print("Pastikan MySQL sudah berjalan dan database sudah dibuat!")
    finally:
        print("\n👋 Sampai jumpa!\n")


if __name__ == "__main__":
    main()