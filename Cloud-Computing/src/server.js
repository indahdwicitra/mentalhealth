// server.js
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connectDB = require('./config/database');

const app = express();

// Koneksi Database
connectDB();

// Middleware
console.log(typeof cors);
app.use(cors());
app.use(express.json());

// Rute
app.use('/api/auth', require('./routes/auth'));

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server berjalan di port ${PORT}`);
});