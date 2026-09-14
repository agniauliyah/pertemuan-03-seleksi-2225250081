# Pertemuan 03 Seleksi Python

Nama: Agnia Ul Auliyah  
NIM: 2225250081  
Kelas: 3E  

## Tujuan

Menulis program seleksi menggunakan `if`, `if-else`, kondisi majemuk, dan nested `if`.

## Cara Menjalankan

Program dapat dijalankan melalui Terminal menggunakan Python.

Contoh menjalankan tugas:

    python tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas

Program digunakan untuk menganalisis persamaan kuadrat:

    ax² + bx + c = 0

Langkah-langkah:
1. Memasukkan nilai koefisien `a`, `b`, dan `c`.
2. Memeriksa apakah nilai `a` sama dengan 0.
3. Jika `a = 0`, maka program menampilkan bahwa input bukan persamaan kuadrat.
4. Jika `a ≠ 0`, program menghitung diskriminan dengan rumus `D = b² - 4ac`.
5. Jika `D > 0`, maka terdapat dua akar real yang berbeda.
6. Jika `D = 0`, maka terdapat satu akar real kembar.
7. Jika `D < 0`, maka tidak terdapat akar real.

## Hasil Pengujian

### Test Case 1

Input:
    a = 1
    b = -5
    c = 6

Keluaran yang diharapkan:
    Dua akar real, yaitu 3 dan 2.

Keluaran aktual:
    Diskriminan = 1.00
    Dua akar real: x1 = 3.00, x2 = 2.00

Status:
    Berhasil

### Test Case 2

Input:
    a = 1
    b = 2
    c = 1

Keluaran yang diharapkan:
    Akar real kembar, yaitu -1.

Keluaran aktual:
    Diskriminan = 0.00
    Akar real kembar: x = -1.00

Status:
    Berhasil

### Test Case 3

Input:
    a = 1
    b = 0
    c = 1

Keluaran yang diharapkan:
    Tidak ada akar real.

Keluaran aktual:
    Diskriminan = -4.00
    Tidak ada akar real.

Status:
    Berhasil

### Test Case 4

Input:
    a = 0
    b = 2
    c = 3

Keluaran yang diharapkan:
    Bukan persamaan kuadrat.

Keluaran aktual:
    Bukan persamaan kuadrat.

Status:
    Berhasil

## Refleksi

Pada praktikum ini saya mempelajari penggunaan `if`, `if-else`, kondisi majemuk, dan nested `if` dalam Python. Saya juga belajar bahwa indentasi sangat penting dalam penulisan program Python.

Kesalahan yang saya temukan adalah kesalahan indentasi yang menyebabkan `IndentationError`. Kesalahan tersebut diperbaiki dengan merapikan indentasi pada setiap blok kode agar program dapat dijalankan dengan benar.