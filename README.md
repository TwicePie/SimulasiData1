# Simulasi Sistem Gerbang Tol Elektronik

## Deskripsi Proyek
Proyek ini merupakan simulasi sistem gerbang tol elektronik menggunakan Python dan library SimPy. Simulasi ini dibuat untuk menganalisis waktu tunggu dan efisiensi pelayanan di gerbang tol elektronik.

## Fitur
- Simulasi kedatangan kendaraan secara acak
- Perhitungan waktu tunggu kendaraan
- Analisis data statistik (waktu tunggu rata-rata, maksimum, minimum)
- Visualisasi hasil dengan grafik
- Penyimpanan data dalam format CSV

## Komponen Utama
1. **Parameter Simulasi**
   - Waktu simulasi: 1 jam (3600 detik)
   - Tingkat kedatangan: 27 kendaraan per menit
   - Waktu layanan: 4 detik per kendaraan
   - Jumlah gerbang tol: 2 unit

2. **Output yang Dihasilkan**
   - File CSV (toll_simulation_results.csv)
   - Grafik visualisasi (toll_simulation_graph.png)
   - Ringkasan statistik di console

## Cara Penggunaan
1. Pastikan sudah menginstall library yang diperlukan:
   ```bash
   pip install simpy matplotlib
   ```

2. Jalankan file Tol_Sistem.py:
   ```bash
   python Tol_Sistem.py
   ```

3. Hasil simulasi akan ditampilkan dalam:
   - Console: informasi real-time dan ringkasan statistik
   - File CSV: detail lengkap setiap kendaraan
   - File PNG: grafik waktu tunggu

## Interpretasi Hasil
- Grafik menunjukkan waktu tunggu setiap kendaraan (garis biru)
- Garis merah putus-putus menunjukkan waktu tunggu rata-rata
- Data CSV berisi informasi detail setiap kendaraan:
  - Nomor kendaraan
  - Waktu kedatangan
  - Metode pembayaran
  - Waktu keluar
  - Waktu tunggu

## Pengembangan Lebih Lanjut
Simulasi ini dapat dikembangkan dengan menambahkan:
- Variasi jenis kendaraan
- Variasi metode pembayaran
- Pengaruh jam sibuk (peak hours)
- Optimasi jumlah gerbang tol

## Skenario dan Hasil Analisis

### Skenario Weekday
1. **Konfigurasi 2 Gerbang**
   - Arrival rate: 27 kendaraan/menit
   - Hasil menunjukkan potensi antrian panjang
   - Waktu tunggu relatif tinggi

2. **Konfigurasi 4 Gerbang**
   - Arrival rate: 27 kendaraan/menit
   - Pengurangan signifikan pada waktu tunggu
   - Peningkatan efisiensi pelayanan
   - **Rekomendasi**: Lebih efektif untuk penanganan arus weekday

### Skenario Weekend
1. **Konfigurasi 3 Gerbang**
   - Arrival rate: 48 kendaraan/menit
   - Terjadi penumpukan antrian
   - Waktu tunggu di atas standar pelayanan

2. **Konfigurasi 6 Gerbang**
   - Arrival rate: 48 kendaraan/menit
   - Penanganan arus lebih optimal
   - Waktu tunggu lebih pendek
   - **Rekomendasi**: Sangat efektif untuk menangani lonjakan arus weekend

## Kesimpulan
- Penambahan jumlah gerbang terbukti efektif dalam mengurangi waktu tunggu
- Konfigurasi 4 gerbang optimal untuk weekday (arrival rate 27)
- Konfigurasi 6 gerbang optimal untuk weekend (arrival rate 48)
- Peningkatan jumlah gerbang berbanding lurus dengan efisiensi pelayanan
