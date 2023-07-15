import tkinter as tk

def hitung_imt(berat, tinggi):
    tinggi_m = tinggi / 100  # Mengkonversi tinggi dari cm menjadi meter
    imt = berat / (tinggi_m ** 2)  # Menghitung IMT dengan rumus IMT = berat / (tinggi^2)
    return imt

def kategori_imt(imt):
    if imt < 18.5:
        return "Kurus"
    elif 18.5 <= imt < 25:
        return "Normal"
    elif 25 <= imt < 30:
        return "Gemuk"
    else:
        return "Obesitas"

def hitung_button_click():
    berat_badan = float(entry_berat.get())
    tinggi_badan = float(entry_tinggi.get())

    imt = hitung_imt(berat_badan, tinggi_badan)
    kategori = kategori_imt(imt)

    label_imt.config(text="Indeks Massa Tubuh (IMT): {:.2f}".format(imt))
    label_kategori.config(text="Kategori IMT: {}".format(kategori))

def clear_button_click():
    entry_berat.delete(0, tk.END)
    entry_tinggi.delete(0, tk.END)
    label_imt.config(text="Indeks Massa Tubuh (IMT):")
    label_kategori.config(text="Kategori IMT:")

# Membuat window utama
window = tk.Tk()
window.title("Kalkulator IMT")
window.geometry("300x200")

# Membuat label dan entry untuk berat badan
label_berat = tk.Label(window, text="Berat Badan (kg):")
label_berat.pack()
entry_berat = tk.Entry(window)
entry_berat.pack()

# Membuat label dan entry untuk tinggi badan
label_tinggi = tk.Label(window, text="Tinggi Badan (cm):")
label_tinggi.pack()
entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

# Membuat tombol hitung
hitung_button = tk.Button(window, text="Hitung", command=hitung_button_click)
hitung_button.pack()

# Membuat tombol clear
clear_button = tk.Button(window, text="Clear", command=clear_button_click)
clear_button.pack()

# Membuat label untuk hasil IMT dan kategori IMT
label_imt = tk.Label(window, text="Indeks Massa Tubuh (IMT):")
label_imt.pack()
label_kategori = tk.Label(window, text="Kategori IMT:")
label_kategori.pack()

# Menjalankan event loop
window.mainloop()
