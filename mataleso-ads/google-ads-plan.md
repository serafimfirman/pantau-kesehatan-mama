# Google Ads Plan: Mataleso Coffee Canggu

**Bisnis:** Mataleso Coffee, specialty coffee shop
**Lokasi:** Jalan Padang Linjong, Canggu, Bali
**Jam buka:** setiap hari, 07.00 sampai 21.00 WITA
**Tagline:** Specialty Coffee, Indonesian Soul.
**Status website:** belum ada, jadi pakai landing page di `landing-page/index.html`

> Catatan: hasil pencarian web juga menemukan listing "Mataleso Coffee" di Labuan Bajo (Jl. Soekarno Hatta). Rencana ini khusus untuk outlet Canggu. Pastikan iklan ditautkan ke lokasi GBP Canggu, bukan Labuan Bajo.

---

## 1. Tujuan dan KPI

| Tujuan | Metrik utama | Sumber data |
|---|---|---|
| Orang datang ke kedai | Klik "Get directions" (landing page + GBP) | GA4 event `click_directions`, local actions di Google Ads |
| Orang bertanya/pesan | Klik WhatsApp, telepon | GA4 event `click_whatsapp`, call asset |
| Efisiensi | Biaya per aksi (CPA) | Google Ads |
| ROI riil | Transaksi dari iklan (kode ref WhatsApp / tanya di kasir) | Offline conversion upload |

Target awal 30 hari pertama: kumpulkan data dulu. Target CPA baru ditetapkan setelah ada 15 sampai 30 conversion.

---

## 2. Struktur akun

```
Akun: Mataleso Coffee Canggu (di bawah MCC)
│
├── Campaign 1: Search | Canggu Coffee | Proximity        (70% budget)
│   ├── AG1 Coffee shop Canggu (generic lokal)
│   ├── AG2 Specialty coffee & cold brew
│   ├── AG3 Matcha & tea
│   ├── AG4 Indonesian coffee / kopi susu
│   └── AG5 Brand (Mataleso)
│
└── Campaign 2: Performance Max | Store goals              (30% budget, mulai minggu ke-3)
    └── Asset group: Mataleso Canggu (location asset dari GBP + foto + copy)
```

### Pengaturan campaign 1 (Search)

| Setting | Nilai |
|---|---|
| Network | Google Search saja (matikan Search Partners dan Display) |
| Lokasi | Radius 5 km dari alamat GBP (Padang Linjong). Opsi "Presence: People in or regularly in", bukan "interest" |
| Bahasa | Tidak diset manual (sejak 30 Sep 2026 Google mencocokkan dari bahasa iklan). Copy dalam bahasa Inggris |
| Jadwal iklan | 06.30 sampai 20.30 WITA (berhenti 30 menit sebelum tutup) |
| Bidding minggu 1 sampai 3 | Maximize clicks, max CPC cap (lihat bagian budget) |
| Bidding setelah 15+ conversion/bulan | Maximize conversions, lalu Target CPA |
| Conversion goal | `click_directions` dan `click_whatsapp` (primary). `view_menu` (secondary) |

### Pengaturan campaign 2 (Performance Max, store goals)

| Setting | Nilai |
|---|---|
| Goal | Store visits / local actions (directions, calls) |
| Lokasi | Location asset dari GBP Canggu, radius 5 km |
| Final URL | Landing page. Matikan "Final URL expansion" |
| Assets wajib | 5+ foto asli (kopi, ruangan, klepon), logo persegi & landscape, headline dan deskripsi dari bagian 4 |
| Mulai | Minggu ke-3, setelah tracking terbukti jalan |

---

## 3. Keyword

Volume dan CPC **belum diverifikasi**. Tarik dari `KeywordPlanIdeaService.GenerateKeywordHistoricalMetrics` (lokasi: Bali / Badung, bahasa: Inggris) sebelum launch. Keyword dengan volume 0 tetap boleh dipertahankan di ad group lokal karena pencarian "near me" sering tidak tercatat per keyword.

### AG1 Coffee shop Canggu
- [coffee shop canggu]
- [canggu coffee]
- [cafe canggu]
- "coffee near me"
- "coffee shop near me"
- "cafe near me"
- "best coffee canggu"
- "coffee padang linjong"

### AG2 Specialty coffee & cold brew
- [specialty coffee canggu]
- "specialty coffee bali"
- "cold brew canggu"
- "espresso canggu"
- "flat white canggu"
- "third wave coffee canggu"

### AG3 Matcha & tea
- "matcha canggu"
- "pistachio matcha"
- "matcha latte canggu"
- "tea canggu"
- "chai canggu"

### AG4 Indonesian coffee / kopi susu
- "kopi susu canggu"
- "indonesian coffee canggu"
- "kopi canggu"
- "klepon canggu"
- "local coffee canggu"

### AG5 Brand
- [mataleso]
- [mataleso coffee]
- [mataleso canggu]

### Negative keyword (level akun)
`job`, `jobs`, `lowongan`, `loker`, `barista course`, `training`, `kursus`, `wholesale`, `supplier`, `beans online`, `buy beans`, `machine`, `mesin`, `grinder`, `franchise`, `recipe`, `resep`, `plantation`, `luwak tour`, `coffee tour`, `farm`, `ubud`, `seminyak beach club`, `kuta`, `nusa dua`, `uluwatu`, `labuan bajo`

Negative lokasi (seperti `ubud`, `uluwatu`) mencegah klik dari orang yang mencari kopi di area lain Bali. Tambah lagi setiap minggu dari laporan search terms.

---

## 4. Ad copy (Responsive Search Ads)

Semua sudah dicek panjangnya (headline ≤ 30, deskripsi ≤ 90 karakter) dan mengikuti brand voice Mataleso: sentence case, tanpa em dash, tanpa tanda seru, tanpa kata "artisan/curated/premium".

### Headline pool

| # | Headline | Char | Pakai di |
|---|---|---|---|
| 1 | Mataleso Coffee Canggu | 22 | Semua (pin posisi 1 di AG5) |
| 2 | Specialty coffee in Canggu | 26 | AG1, AG2 |
| 3 | Open every day, 7am to 9pm | 26 | Semua |
| 4 | On Jalan Padang Linjong | 23 | Semua |
| 5 | Coffee shop near you | 20 | AG1 |
| 6 | Kopi Susu Mataleso Nusantara | 28 | AG4 |
| 7 | Si Hitam cold brew | 18 | AG2 |
| 8 | Try the Balinese Tangerine | 26 | AG1, AG2 |
| 9 | Pistachio matcha in Canggu | 26 | AG3 |
| 10 | Klepon with your coffee | 23 | AG4 |
| 11 | The room is simple | 18 | Semua (pin posisi 2 bersama #12 di posisi 3, opsional) |
| 12 | The coffee isn't | 16 | Semua |
| 13 | Named after the sun | 19 | AG5 |
| 14 | Get directions in one tap | 25 | Semua |
| 15 | Stay as long as you like | 24 | AG1 |
| 16 | Matcha and tea in Canggu | 24 | AG3 |
| 17 | Cold brew in Canggu | 19 | AG2 |
| 18 | Indonesian coffee in Canggu | 27 | AG4 |
| 19 | Kopi susu in Canggu | 19 | AG4 |
| 20 | Mango Kopyor and klepon | 23 | AG4 |
| 21 | Temple of Rose tea | 18 | AG3 |
| 22 | Open until 9pm | 14 | Semua |
| 23 | Coffee late in Canggu | 21 | AG1 |

Setiap ad group: ambil 12 sampai 15 headline (yang spesifik ad group + yang "Semua").

### Deskripsi pool

| # | Deskripsi | Char |
|---|---|---|
| 1 | The room is simple. The coffee isn't. Specialty coffee with Indonesian soul in Canggu. | 86 |
| 2 | Open every day, 7am to 9pm on Jalan Padang Linjong. Come in, sit down, stay a while. | 84 |
| 3 | Si Hitam cold brew, Balinese Tangerine, klepon. Drinks that taste like they belong here. | 88 |
| 4 | Mataleso is the Manggarai word for sun. We open early and close late. Come find us. | 83 |
| 5 | Pistachio matcha, Temple of Rose, Midnight in Paris. Not everything here is coffee. | 83 |
| 6 | Brewed last night, waiting quietly. Si Hitam cold brew on Jalan Padang Linjong, Canggu. | 87 |
| 7 | Coffee until 9pm. The last hour is usually the quietest one. Jalan Padang Linjong. | 82 |

AG3 pakai #5 sebagai deskripsi utama. AG2 pakai #6. AG5 pakai #4.

### Display path
`mataleso.../canggu/coffee` (AG1, AG2), `.../canggu/matcha` (AG3), `.../canggu/kopi-susu` (AG4)

---

## 5. Assets (extensions)

| Asset | Isi |
|---|---|
| Location | Tautkan GBP Canggu (AssetSet `LOCATION_SYNC`). **Paling penting**, karena memunculkan alamat, jarak, dan tombol arah |
| Call | Nomor kedai (perlu diisi). Aktifkan call reporting (Google forwarding number tersedia di Indonesia) |
| Sitelinks | "See the menu" → `#menu` · "Get directions" → `#visit` · "Opening hours" → `#visit` · "Chat on WhatsApp" → landing page |
| Callouts | Open 7am to 9pm daily · Jalan Padang Linjong · Indonesian pastry · Cold brew made daily · Matcha and tea |
| Structured snippet | Header "Types": Signature coffee, Espresso, Tea, Matcha, Juice, Indonesian pastry |
| Image | 3 sampai 5 foto asli (produk lebih penting dari ruangan, sesuai brand) |
| Message (opsional) | WhatsApp, kalau tersedia untuk akun |

Catatan: callout "Cold brew made daily" dan nomor telepon perlu dikonfirmasi pemilik dulu.

---

## 6. Budget

**Rekomendasi awal: Rp150.000/hari (±Rp4,5 juta/bulan)**, dibagi Search Rp105.000 dan PMax Rp45.000 (PMax mulai minggu ke-3; sebelum itu semua ke Search).

Asumsi yang **harus divalidasi** dengan Keyword Planner sebelum launch:

| Skenario | CPC rata-rata | Klik/hari (Rp105k) | Rate aksi* | Aksi/bulan | CPA |
|---|---|---|---|---|---|
| Murah | Rp2.000 | ~52 | 15% | ~235 | ~Rp13.000 |
| Tengah | Rp4.000 | ~26 | 12% | ~95 | ~Rp33.000 |
| Mahal | Rp8.000 | ~13 | 10% | ~40 | ~Rp80.000 |

\* Rate aksi = klik directions/WhatsApp ÷ klik iklan.

Max CPC cap minggu 1 sampai 3: set di sekitar batas "top of page bid (high)" dari Keyword Planner untuk AG1.

Aturan budget: jangan naik/turun lebih dari 20% per minggu. Kalau CPA tengah tercapai dan budget sering habis sebelum jam 15.00, naikkan 20%.

---

## 7. Tracking & conversion

| Event | Dari mana | Jenis di Google Ads |
|---|---|---|
| `click_directions` | Landing page (tombol) | Primary, value Rp25.000 (estimasi nilai kunjungan, sesuaikan dengan rata-rata transaksi) |
| `click_whatsapp` | Landing page | Primary, value Rp15.000 |
| `view_menu` | Landing page | Secondary (observasi saja) |
| Local actions: directions, calls | Location asset GBP | Otomatis, primary |
| Calls dari iklan | Call asset | Primary (durasi ≥ 30 detik) |
| Kunjungan terkonfirmasi | Kode ref WhatsApp (`M` + 6 karakter gclid) dicatat staf → upload | Offline conversion via `ConversionUploadService` |

Landing page sudah menyimpan `gclid` 90 hari dan menyisipkan kode ref ke pesan WhatsApp otomatis.

---

## 8. Checklist setup

### Manual (sekali, oleh pemilik)
- [ ] Pastikan GBP Canggu terverifikasi dan pemilik punya akses Owner/Manager
- [ ] Login Google, beri OAuth consent ke sistem (scope Ads + Business Profile)
- [ ] Setup pembayaran di Google Ads (kartu / transfer)
- [ ] Verifikasi pengiklan kalau diminta Google
- [ ] Beli domain (saran: `mataleso.coffee` atau `matalesocoffee.com`, cek ketersediaan) dan isi nomor WhatsApp
- [ ] Siapkan 5+ foto asli dan logo

### Otomatis (via API, oleh sistem)
- [ ] Buat akun di bawah MCC (`CustomerService.CreateCustomerClient`)
- [ ] Deploy landing page ke domain, isi ID GA4/Ads
- [ ] Buat GA4 property + web stream + link ke Ads (GA4 Admin API)
- [ ] Buat conversion actions (`ConversionActionService`), isi label ke landing page
- [ ] Tarik volume & CPC keyword (`KeywordPlanIdeaService`), buang keyword volume nol di luar AG1
- [ ] Buat budget, campaign, ad group, keyword, negative, RSA, assets
- [ ] Tautkan location asset dari GBP (`AssetSet` + `BusinessProfileLocationSet`)
- [ ] Monitor status review iklan (`policy_summary`), perbaiki yang disapproved

---

## 9. Aturan optimasi otomatis

| Frekuensi | Aksi | Mode |
|---|---|---|
| Harian | Cek budget pacing, status iklan disapproved, anomali (CTR/CPC naik >50%) | Alert |
| Mingguan | Search terms: tambah negative untuk istilah tidak relevan / di luar Canggu | Auto-apply |
| Mingguan | Pause keyword dengan biaya > 3× target CPA tanpa conversion | Auto-apply |
| Mingguan | Tambah keyword dari search terms yang menghasilkan conversion | Rekomendasi → approve |
| 2 mingguan | Ganti headline dengan rating "Low" (asset performance) pakai varian baru dari pool atau LLM, tetap lolos checklist brand voice | Rekomendasi → approve |
| Bulanan | Ubah budget (maks ±20%), ganti strategi bidding | Rekomendasi → approve |
| Bulanan | Laporan ke pemilik: biaya, directions, WhatsApp, CPA, estimasi kunjungan | Otomatis |

---

## 10. Data yang masih dibutuhkan dari pemilik

1. Nomor telepon dan WhatsApp kedai
2. Rata-rata nilai transaksi per orang (untuk conversion value dan ROI)
3. Konfirmasi menu dan harga yang aktif di Canggu (copy memakai menu dari brand guide)
4. Domain yang diinginkan
5. Budget bulanan yang nyaman
6. Apakah ada fasilitas yang layak diiklankan (wifi/tempat kerja, parkir motor, vegan options). Belum dipakai di copy karena belum terkonfirmasi
