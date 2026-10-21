# Subscription Service

## Что внутри

| Путь                 | Что это |
|----------------------| --- |
| `app/main.py`        | Фабрика приложения `create_app`, lifespan и `GET /health` |
| `app/settings.py`    | Настройки из переменных окружения (pydantic-settings) |
| `migrations/`        | Alembic с async-окружением и пустой начальной ревизией |
| `Dockerfile`         | Образ сервиса |
| `docker-compose.yml` | PostgreSQL, применение миграций и сервис |
| `.env.example`       | Пример конфигурации |

