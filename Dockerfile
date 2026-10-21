FROM python:3.13.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/tmp/poetry-cache \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Poetry ставится в отдельное окружение и удаляется в том же слое:
# его зависимости не смешиваются с зависимостями сервиса и не попадают в образ
RUN python -m venv /opt/poetry \
    && /opt/poetry/bin/pip install --no-cache-dir "poetry==1.8.0" \
    && python -m venv /opt/venv \
    && /opt/poetry/bin/poetry install --no-interaction --no-ansi --without dev --no-root \
    && rm -rf /opt/poetry "$POETRY_CACHE_DIR"

COPY . .

RUN useradd --create-home --uid 1000 app
USER app

EXPOSE 8000

CMD ["uvicorn", "--factory", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
