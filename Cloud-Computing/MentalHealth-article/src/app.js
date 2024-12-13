const express = require('express');
const sequelize = require('./config/database');
const { Article } = require('./models');

const app = express();
app.use(express.json());

// 1. CREATE - Membuat artikel baru
app.post('/api/articles', async (req, res) => {
    try {
        const article = await Article.create(req.body);
        res.status(201).json({
            status: 'success',
            data: article
        });
    } catch (error) {
        res.status(500).json({
            status: 'error',
            message: error.message
        });
    }
});

// 2. READ - Mendapatkan semua artikel
app.get('/api/articles', async (req, res) => {
    try {
        const articles = await Article.findAll();
        res.json({
            status: 'success',
            data: articles
        });
    } catch (error) {
        res.status(500).json({
            status: 'error',
            message: error.message
        });
    }
});

// 3. READ - Mendapatkan artikel by ID
app.get('/api/articles/:id', async (req, res) => {
    try {
        const article = await Article.findByPk(req.params.id);
        if (!article) {
            return res.status(404).json({
                status: 'error',
                message: 'Artikel tidak ditemukan'
            });
        }
        res.json({
            status: 'success',
            data: article
        });
    } catch (error) {
        res.status(500).json({
            status: 'error',
            message: error.message
        });
    }
});

// 4. UPDATE - Mengupdate artikel
app.put('/api/articles/:id', async (req, res) => {
    try {
        const article = await Article.findByPk(req.params.id);
        if (!article) {
            return res.status(404).json({
                status: 'error',
                message: 'Artikel tidak ditemukan'
            });
        }
        await article.update(req.body);
        res.json({
            status: 'success',
            data: article
        });
    } catch (error) {
        res.status(500).json({
            status: 'error',
            message: error.message
        });
    }
});

// 5. DELETE - Menghapus artikel
app.delete('/api/articles/:id', async (req, res) => {
    try {
        const article = await Article.findByPk(req.params.id);
        if (!article) {
            return res.status(404).json({
                status: 'error',
                message: 'Artikel tidak ditemukan'
            });
        }
        await article.destroy();
        res.json({
            status: 'success',
            message: 'Artikel berhasil dihapus'
        });
    } catch (error) {
        res.status(500).json({
            status: 'error',
            message: error.message
        });
    }
});

const start = async () => {
    try {
        await sequelize.sync({ force: true });
        console.log('Database synced');
        
        app.listen(3000, () => {
            console.log('Server running on port 3000');
        });
    } catch (error) {
        console.error(error);
    }
};

start();
