<p align="center">
    <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://docs.pyrogram.org/_static/pyrogram.png" alt="Pyrogram" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://pyrogram.org">Homepage</a> •
    <a href="https://docs.pyrogram.org">Documentation</a> •
    <a href="https://docs.pyrogram.org/releases">Releases</a> •
    <a href="https://t.me/pyrogram">News</a>
</p>

## Pyrogram
> This Pyrogram code, Recode With BY <a href="https://t.me/bakuzaan">Bakuzaan</a>
___________________________________________

## Deploy to Heroku

### 1. **Fork/Clone Repo ini**

### 2. **Setting File Konfigurasi**
- Setelah fork/clone, buka file `.env` atau copy dari `sample.env`:
  ```bash
  cp sample.env .env
  ```
- Edit `.env` dengan variable Token, API_ID, API_HASH dan lain-lain.

### 3. **Deploy ke Heroku**
- Login ke [Heroku](https://heroku.com) dan buat new app.
- Jalankan command di terminal:
  ```bash
  git init
  git add .
  git commit -m "first deploy"
  heroku login
  heroku git:remote -a <nama-aplikasi-heroku-kamu>
  git push heroku main
  ```
  _(ganti `main` dengan `master` jika branch utama kamu bernama master)_

### 4. **Set Environment Variables (Config Vars)**
- Buka Heroku dashboard > App kamu > Settings > Reveal Config Vars.
- Masukkan semua variabel dari file `.env` (atau gunakan add-ons/import tools jika familiar).

### 5. **Selesai!**
- Heroku akan otomatis menginstall requirements dan menjalankan bot sesuai file `Procfile`.
- Untuk melihat log proses aplikasi:
  ```bash
  heroku logs --tail
  ```

---

## Tips

- **JANGAN** upload file `.env` ke repo public!
- Jika ada error dependency (kurang ffmpeg, dsb), tambahkan buildpack Heroku (lihat docs/FAQ atau tanya maintainer).

---

## Repo Asli
- [XwinkelsUbot](https://github.com/Danesiuu/XwinkelsUbot)
