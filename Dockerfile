# Stage 1: Builder
FROM python:3.12-slim AS builder

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

RUN poetry export --without-hashes -f requirements.txt > requirements.txt \
    && pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /app

# Copy virtualenv from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY sugarvany_api ./sugarvany_api
COPY uvicorn_config.py ./

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

ENV ENVIRONMENT=production
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "sugarvany_api.interface.api.app:app", \
     "--host", "0.0.0.0", \
     "--port", "8000", \
     "--workers", "4", \
     "--log-level", "info", \
     "--proxy-headers", \
     "--forwarded-allow-ips", "*", \
     "--timeout-keep-alive", "120"]
