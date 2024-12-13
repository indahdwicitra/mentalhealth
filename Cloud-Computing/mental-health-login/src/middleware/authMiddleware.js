const jwt = require('jsonwebtoken');

module.exports = (req, res, next) => {
  // Dapatkan token dari header
  const token = req.header('Authorization')?.replace('Bearer ', '');

  // Cek apakah token ada
  if (!token) {
    return res.status(401).json({ message: 'Tidak ada token, otorisasi ditolak' });
  }

  try {
    // Verifikasi token
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ message: 'Token tidak valid' });
  }
};