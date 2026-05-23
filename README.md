# library-api

# Endpoints

GET /books – получить список книг
GET /books/{id} – получить книгу по id
POST /books – добавить книгу

# Запуск 

docker build -t library-api .

docker run -p 5050:5050 library-api

# Примеры запросов

Получить список книг:

curl http://localhost:5050/books

Получить книгу по id: 

curl http://localhost:5050/books/id

Добавить книгу:

curl -X POST http://localhost:5050/books
-H "Content-Type: application/json"
-d '{"title":"Dune","author":"Frank Herbert"}'