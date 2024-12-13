const mongoose = require('mongoose');
require('dotenv').config();

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI);
    console.log('MongoDB terhubung berhasil');
  } catch (error) {
    console.error('Koneksi MongoDB gagal:', error.message);
    process.exit(1);
  }
};

module.exports = connectDB;