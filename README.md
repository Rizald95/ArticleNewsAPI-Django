# ArticleNewsAPI
ArticleNewsAPI adalah proyek Django yang mengambil berita dari **NewsAPI** dan menampilkannya di UI Django menggunakan **TailwindCSS**.

## 🚀 Fitur
- Menggunakan **Django** sebagai backend.
- Menggunakan **NewsAPI** untuk fetch berita.
- UI dibuat dengan **TailwindCSS**.
- Menggunakan **django-environ** untuk mengelola variabel lingkungan.
- Dapat dijalankan di local development dengan virtual environment.

---

## 📌 Persyaratan
Sebelum memulai, pastikan Anda telah menginstal:
- **Python** (>= 3.8)
- **Node.js & npm** (untuk TailwindCSS)
- **Virtual environment** (disarankan)

---

## 🛠 Instalasi & Konfigurasi

### 1️⃣ Clone Repository & Masuk ke Direktori Proyek
```bash
git clone https://github.com/username/ArticleNewsAPI.git
cd ArticleNewsAPI

2️⃣ Buat Virtual Environment & Install Dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
3️⃣ Buat File .env untuk API Key NewsAPI
Buat file .env di dalam folder root dan tambahkan:


NEWSAPI_KEY=your_api_key_here
Catatan: Jangan lupa mengganti your_api_key_here dengan API key dari NewsAPI.

🎨 Setup TailwindCSS
4️⃣ Install Node.js Dependencies

cd static
npm init -y
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
5️⃣ Konfigurasi tailwind.config.js
Edit file tailwind.config.js dan tambahkan:

javascript
Copy
Edit
module.exports = {
  content: [
    '../templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
6️⃣ Buat File CSS Tailwind
Di dalam folder static/css/, buat file tailwind.css dan tambahkan:


@tailwind base;
@tailwind components;
@tailwind utilities;
Jalankan perintah berikut untuk membangun Tailwind CSS:

bash
Copy
Edit
npx tailwindcss -i ./css/tailwind.css -o ./css/output.css --watch
Tambahkan konfigurasi di settings.py:


import os
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
Kemudian jalankan:


python manage.py collectstatic
🏃 Menjalankan Proyek Django
7️⃣ Jalankan Migrasi Database

python manage.py migrate
8️⃣ Jalankan Server Django

python manage.py runserver
Akses proyek di http://127.0.0.1:8000/news/.

