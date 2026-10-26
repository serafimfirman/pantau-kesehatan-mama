# Aturan untuk Claude

## Privasi: perangkat kerja dikelola kantor
Pemilik repo sering mengakses project ini dari laptop kantor yang dikelola MDM.
Agent MDM di laptop itu bisa membaca semua file di disk. Project ini berisi data
kesehatan keluarga, jadi tidak boleh ada file yang tersimpan ke laptop tersebut.

- **Jangan kirim file ke user** (jangan pakai SendUserFile, jangan buat file untuk di-download).
- **Jangan sarankan user download, export, atau menyimpan file** apa pun ke perangkatnya.
- Simpan semua hasil kerja di repo ini (commit & push) atau tampilkan langsung di chat.
- Kalau user minta file untuk di-download, ingatkan dulu aturan ini dan tanyakan
  apakah dia sedang memakai perangkat pribadi.
- Sesekali ingatkan: pakai jendela Incognito, logout setelah selesai.
