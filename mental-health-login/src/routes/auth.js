const express = require('express');
const router = express.Router();
const { register, login } = require('../controllers/authController');
const authMiddleware = require('../middleware/authMiddleware');

// Rute registrasi
router.post('/register', register);

// Rute login
router.post('/login', login);

// Contoh rute yang memerlukan autentikasi
router.get('/profile', authMiddleware, (req, res) => {
  res.json({ message: 'Akses profil berhasil' });
});
module.exports = router;
