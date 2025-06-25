#  Image Gallery API

Це RESTful веб-застосунок на базі FastAPI, який дозволяє працювати з колекціями зображень. Сервіс реалізує функції додавання користувачів, створення колекцій, завантаження зображень та їх отримання.

---

##  Технології

- Python 3.12
- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic
- SQLite

---

## Запуск проєкту

### 1. Клонування репозиторію:
```
git clone https://github.com/your-username/image-gallery-api.git
cd image-gallery-api
```

### 2. Створення віртуального середовища (опціонально):
```
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Встановлення залежностей:
```
pip install -r requirements.txt
```

### 4. Запуск застосунку:
```
uvicorn main:app --reload
```

### 5. Документація API:
```
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
```

## Структура проєкту
```
ImageGalleryPractice2/
│
├── controllers/              # API маршрути
├── models/                   # SQLAlchemy моделі
├── repositories/             # Репозиторії для доступу до БД
├── services/                 # Бізнес-логіка
├── utils/                    # Допоміжні функції
├── database.py               # Ініціалізація БД
├── di_container.py           # DI-контейнер
├── main.py                   # Точка входу
├── requirements.txt          # Залежності
└── README.md                 # Документація
```
