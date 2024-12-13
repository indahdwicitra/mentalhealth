# __Mental Health Support App REST API Article Documentation__

## Overview
This documentation provides an overview of the REST API for Articles, including the setup, structure, and available endpoints. The API is designed to retrieve articles on mental health from specific URLs, which can be read and provide insights to readers through a GET request.

## Project Structure
mentalHealth-article/
├── src/
│   └── config/
|       └──database.js
|   └── models/
|       └── Article.js
|       └── index.js
|   └── app.js
├── node_modules/
├── package.json
├── package-lock.json

## File Descriptions

- database.js: Configures the database connection (Cloud SQL).
- Article.js: Defines the schema and model for articles, including fields and validation.
- index.js: Typically used to export models or functions, potentially aggregating them for easier imports elsewhere.
- app.js: The main application file that sets up the server, routes, and connects various components.
- node_modules/: A directory containing all the installed npm dependencies.
- package.json: Stores project metadata, scripts, and npm dependencies.
- package-lock.json: Records the exact versions of dependencies installed, ensuring consistency across environments.

## Setting Up the API
### Prerequisites
Node.js (version 18 or higher)

## Installation

```
### Install dependencies:
```
npm install
```
### Run the server:
```
npm start
The server will start on port 8080 by default.
```

## API Endpoint
###Get Articles
- URL: api/articles
- Method: GET
- Description: To view the article.
- Deployed URL: http://34.50.95.108:3000/api/articles

## Request
No request body or parameters are needed for this endpoint.

## Response
Status: 200 OK
Content-Type: application/json
Body: 
```
{
    "status": "success",
    "data": [
        {
            "id": 3,
            "title": "Cir Gangguan Kesehatan Mental yang Perlu Diwaspadai",
            "content": "Kesehatan mental merupakan bagian penting dari kesejahteraan secara keseluruhan. Namun, terkadang kita tidak menyadari adanya gangguan mental hingga gejalanya semakin parah. Mengenali ciri-ciri gangguan kesehatan mental sejak dini dapat membantu dalam mencari bantuan yang tepat. Beberapa ciri-ciri yang perlu diwaspadai adalah: 1. **Perubahan Mood yang Drastis**: Jika Anda sering merasa sangat cemas, marah, atau sedih tanpa alasan yang jelas, ini bisa menjadi tanda gangguan mood seperti depresi atau gangguan kecemasan. 2. **Kesulitan Beraktivitas Sehari-hari**: Jika Anda merasa kesulitan untuk melakukan aktivitas sehari-hari seperti bekerja, berinteraksi dengan orang lain, atau bahkan menjaga kebersihan diri, ini bisa menjadi tanda masalah mental yang lebih serius. 3. **Gangguan Tidur**: Baik itu tidur terlalu banyak atau terlalu sedikit, gangguan tidur yang berlangsung lama dapat menunjukkan adanya kecemasan atau depresi. 4. **Perasaan Terisolasi atau Tertutup**: Jika Anda mulai menghindari pertemuan sosial atau merasa terputus dari dunia luar, ini bisa menunjukkan gangguan sosial atau kecemasan sosial. 5. **Perubahan Pola Makan**: Perubahan nafsu makan yang drastis, baik itu makan berlebihan atau kehilangan selera makan, bisa menjadi gejala gangguan mental seperti bulimia atau anoreksia. Menyadari ciri-ciri gangguan kesehatan mental ini sangat penting agar kita bisa mencari bantuan profesional dengan segera. Jangan ragu untuk berbicara dengan seorang psikolog atau psikiater jika Anda merasa gejala ini mengganggu kehidupan Anda.",
            "createdAt": "2024-11-30T08:12:11.000Z",
            "updatedAt": "2024-11-30T08:12:11.000Z"
        }
    ]
}

