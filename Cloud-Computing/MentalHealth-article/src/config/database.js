const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('articles_db', 'root', '', {
    host: 'localhost',
    dialect: 'mysql'
});

module.exports = sequelize;