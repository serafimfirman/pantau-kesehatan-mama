# Import ke Google Ads Editor

File di folder ini membuat 1 campaign Search (status **Paused**) untuk Mataleso Canggu:
6 ad group, 39 keyword, 32 negative keyword, dan 6 responsive search ad.

| Ad group | Bahasa | Fokus |
|---|---|---|
| Coffee shop Canggu | EN | Pencarian kopi umum di sekitar Canggu |
| Specialty coffee & cold brew | EN | Si Hitam, specialty coffee |
| Matcha & tea | EN | Pistachio matcha, Temple of Rose |
| Indonesian food Canggu | EN | Se'i, rendang, nasi goreng, breakfast |
| Kopi Canggu (ID) | ID | "kopi", "tempat ngopi", "coffee shop terdekat" (pencarian terbesar di GBP) |
| Brand | EN | Orang yang sudah cari "mataleso" |

## Sebelum impor

1. Ganti `https://YOUR-DOMAIN/` di `5-responsive-search-ads.csv` dengan URL landing page yang sudah online.
   Iklan Search wajib punya URL di domain sendiri; link Google Maps tidak bisa dipakai.
2. Kedai tutup hari Selasa, jadi copy iklan sengaja tidak menyebut "every day" dan hanya menulis "Open from 7am".
   Jam tutup (20.00 atau 21.00) masih perlu dikonfirmasi sebelum ditambahkan ke iklan.

## Cara impor

1. Buka Google Ads Editor, login, lalu **Get recent changes** untuk akun Mataleso.
2. **Account → Import → From file**, impor berurutan: `1-campaign.csv`, `2-ad-groups.csv`,
   `3-keywords.csv`, `4-negative-keywords.csv`, `5-responsive-search-ads.csv`.
3. Kalau Ads Editor menanyakan pemetaan kolom, cocokkan nama kolom yang sama.
4. Review perubahan, lalu **Post**. Campaign tetap Paused sampai diaktifkan.

## Diatur manual setelah impor (sekali saja)

- **Lokasi:** campaign → Locations → Radius 5 km dari `-8.6397, 115.1408` (koordinat GBP Mataleso Bali).
  Location options: "Presence: people in or regularly in your targeted locations".
- **Location asset:** Assets → Location → tautkan Google Business Profile "Mataleso Bali".
- **Call asset:** 0823-6413-6150.
- **Callouts:** Open from 7am · Jalan Padang Linjong · Indonesian pastry · Se'i from Flores · Matcha and tea
- **Sitelinks** (setelah landing page online): See the menu · Get directions · Indonesian food · Chat on WhatsApp
- **Conversion:** buat conversion action untuk klik directions dan WhatsApp di landing page,
  lalu ganti bidding ke Maximize conversions setelah ada 15+ conversion per bulan.

Jadwal iklan Rabu sampai Senin 06.30–20.30 (Selasa kedai tutup, iklan mati). Budget awal Rp150.000/hari, Maximize clicks dengan batas CPC Rp6.000 (sesuaikan setelah data Keyword Planner masuk).
