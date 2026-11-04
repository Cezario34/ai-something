# Автописатель

Каркас веб-приложения для проверки и будущего автодополнения текста.
Сейчас это одна страница: поле для фрагмента, счётчик символов в браузере
и кнопка «Проверить текст», которая отвечает заглушкой.

База данных, авторизация и вызовы моделей не используются. Это отдельное
приложение рядом с чатом персонажей в `backend/` и `frontend/`.

## Требования

- Python 3.10+

## Установка и запуск

```bash
cd autowriter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

На Windows виртуальное окружение включается так: `.venv\Scripts\activate`.

Страница: http://127.0.0.1:8000

## Проверки

Из каталога `autowriter`, с установленными зависимостями:

```bash
pytest
```

## Структура

```
autowriter/
├── app/
│   ├── main.py                 # FastAPI отдаёт страницу
│   ├── routers/check.py        # заглушка «Проверить текст»
│   └── services/completion.py  # место для будущей логики
├── templates/index.html
├── static/                     # стили и счётчик символов
└── tests/
```
