# Menggunakan image dasar Node.js
FROM node:16

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file package.json dan package-lock.json terlebih dahulu untuk caching dependencies
COPY package*.json ./

# Menyalin file .env (pastikan file .env ada di root proyek)
COPY .env .env

# Install dependencies
RUN npm install

# Menyalin sisa file proyek ke dalam container
COPY . .

# Meng-expose port yang digunakan oleh aplikasi
EXPOSE 8080

# Menjalankan aplikasi dengan perintah 'npm start'
CMD ["node", "src/server.js"]