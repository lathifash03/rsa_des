### Nama: Lathifah Sahda
### NRP: 5025221159

# Sistem Enkripsi RSA dan DES

Proyek ini mendemonstrasikan sistem komunikasi aman yang mengintegrasikan enkripsi RSA untuk pertukaran kunci dan enkripsi DES (Data Encryption Standard) untuk komunikasi data. Proyek ini melibatkan tiga komponen utama:
1. **Server (Public Key Authority - PKA)**
2. **Initiator (Klien A)**
3. **Responder (Klien B)**

## Ikhtisar Proyek

Sistem ini mengikuti serangkaian langkah untuk komunikasi yang aman:
1. **Pertukaran Kunci** menggunakan enkripsi RSA.
2. **Verifikasi Identitas** antara Initiator A dan Server.
3. **Enkripsi Pesan** menggunakan RSA dan enkripsi data menggunakan DES untuk komunikasi yang aman.
4. **Integritas Komunikasi** dijaga melalui enkripsi dan dekripsi menggunakan kunci masing-masing.

## Komponen

### 1. **Server (PKA)**
Server berfungsi sebagai Public Key Authority (PKA). Server ini bertanggung jawab untuk memberikan kunci publik dari Initiator dan Responder serta memverifikasi identitas Initiator.

### 2. **Initiator (Klien A)**
Initiator A meminta kunci publik dari server, mengirim pesan terenkripsi ke Responder B menggunakan enkripsi RSA, dan memverifikasi identitas dengan server. Setelah pertukaran pesan terenkripsi, Initiator menggunakan enkripsi DES untuk mengirim data secara aman.

### 3. **Responder (Klien B)**
Responder B mendekode pesan dari Initiator A, memprosesnya, dan mengirimkan respons yang terenkripsi kembali menggunakan enkripsi RSA.

### 4. **Implementasi RSA dan DES**
- **RSA** digunakan untuk pertukaran kunci secara aman dan enkripsi potongan data kecil (misalnya kunci enkripsi simetris).
- **DES** digunakan untuk enkripsi data yang lebih besar yang dikirim selama komunikasi.

## Persyaratan

- Python 3.x
- `pycryptodome` untuk enkripsi DES dan utilitas RSA
- `cryptography` untuk menangani operasi kunci publik/privat

Untuk menginstal dependensi:
```bash
pip install pycryptodome cryptography
```


# Cara Menggunakan

### **1. Menghasilkan Kunci RSA**
Sebelum memulai sistem, Anda perlu menghasilkan pasangan kunci RSA (private dan public) untuk server dan klien.

Untuk server:

```bash
openssl genrsa -out server_private.pem 2048
openssl rsa -in server_private.pem -outform PEM -pubout -out server_public.pem
```

Untuk initiator dan responder, ulangi langkah-langkah berikut untuk menghasilkan pasangan kunci:

```bash
openssl genrsa -out initiator_private.pem 2048
openssl rsa -in initiator_private.pem -outform PEM -pubout -out initiator_public.pem

openssl genrsa -out responder_private.pem 2048
openssl rsa -in responder_private.pem -outform PEM -pubout -out responder_public.pem
```
### **2. Menjalankan Server**
Untuk menjalankan server (Public Key Authority - PKA), navigasikan ke direktori yang berisi skrip server.py dan jalankan:

```bash
python server.py
```

### **3. Menjalankan Initiator (Klien A)**
Setelah server berjalan, Anda dapat menjalankan Initiator A dengan menjalankan:

```bash
python initiator_a.py
```

### **4. Menjalankan Responder (Klien B)**
Terakhir, untuk menjalankan Responder B (yang menunggu pesan terenkripsi dari Initiator A), jalankan:

```bash
python responder_b.py
```

# **Proses Langkah-demi-Langkah**

1. Initiator A mengirimkan permintaan kepada server untuk mendapatkan kunci publik dari Initiator A dan Responder B.
2. Server merespons dengan kunci publik dari kedua klien.
3. Initiator A menghasilkan ID unik dan mengirimkannya ke server untuk verifikasi.
4. Server memverifikasi ID dan mengirimkan konfirmasi kembali ke Initiator A.
5. Initiator A mengenkripsi pesan menggunakan kunci publik Responder B (RSA) dan mengirimkannya ke Responder B.
6. Responder B menerima pesan terenkripsi, mendekodekannya menggunakan kunci privatnya, dan memproses pesan tersebut.
7. Responder B mengenkripsi respons menggunakan kunci publik Initiator A (RSA) dan mengirimkannya kembali ke Initiator A.
8. Initiator A mendekodekan respons menggunakan kunci privatnya.
9. Untuk komunikasi lebih lanjut, Initiator A dan Responder B sekarang dapat bertukar data secara aman menggunakan enkripsi DES.

# **Alur Enkripsi RSA dan DES**

1. Enkripsi RSA: Digunakan untuk mengenkripsi potongan data kecil (misalnya, kunci simetris, pesan) dan untuk pertukaran kunci yang aman antara klien dan server.
2. Enkripsi DES: Setelah pertukaran RSA, DES digunakan untuk enkripsi dan dekripsi data selama fase komunikasi. Kunci simetris yang dihasilkan dari RSA digunakan untuk mengenkripsi dan mendekripsi pesan menggunakan DES.


## **Struktur Kode**

Proyek ini terstruktur sebagai berikut:

```bash
rsa_des_encryption_system/
├── initiator_a.py            # Kode Initiator A untuk menangani komunikasi dan enkripsi
├── responder_b.py            # Kode Responder B untuk menerima dan mendekode pesan
├── server.py                 # Kode Server (PKA) untuk menyediakan kunci publik dan memverifikasi identitas
├── rsa_utility.py            # Fungsi utilitas untuk memuat dan menyimpan kunci, operasi RSA dan DES
├── initiator_private.pem     # Kunci privat Initiator A
├── initiator_public.pem      # Kunci publik Initiator A
├── responder_private.pem     # Kunci privat Responder B
├── responder_public.pem      # Kunci publik Responder B
├── server_private.pem        # Kunci privat Server (PKA)
├── server_public.pem         # Kunci publik Server (PKA)
└── README.md                 # Dokumentasi Proyek (file ini)
```

## **Pertimbangan Keamanan**

1. RSA aman untuk pertukaran kunci dan enkripsi data kecil, tetapi lebih lambat untuk set data yang besar. Untuk transmisi data yang sebenarnya, DES (atau AES) lebih disarankan.
2. DES adalah algoritma enkripsi yang lebih lama. Walaupun digunakan di sini untuk demonstrasi, itu tidak dianggap aman untuk tujuan kriptografi modern. Untuk lingkungan produksi, AES (Advanced Encryption Standard) lebih disarankan.

## **Lisensi**

Proyek ini adalah sumber terbuka dan tersedia di bawah Lisensi MIT.
