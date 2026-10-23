# Video animasi Pestra (voice over)

`pestra-video-animasi.mp4`: 1080x1920 (Reels/TikTok/Story), 30 fps, ~50 detik, voice over bahasa Indonesia + subtitle + musik latar.

Alur: hook risiko bisnis, logo reveal, cara kerja (terjadwal, teknisi tersertifikasi, bahan terdaftar Kemenkes), dokumentasi digital siap audit, komitmen (harga transparan, garansi tertulis, respons 24 jam), segmen klien, penutup "Bisnis bebas hama, reputasi terjaga. Tenang, Ada Pestra."

Voice over dibuat dengan TTS offline (eSpeak NG), jadi suaranya masih terdengar robotik. Untuk versi final, rekam ulang naskah di `vo.json` dengan voice actor atau TTS premium, lalu ganti audionya.

Render ulang:
1. `python3 tts.py id+m3 "<teks>" s1.wav 140 45` per adegan (butuh `pip install espeakng-loader`)
2. `NODE_PATH=$(npm root -g) node render.cjs` menghasilkan `silent.mp4` dari `anim.html`
3. Gabungkan audio dengan ffmpeg.
