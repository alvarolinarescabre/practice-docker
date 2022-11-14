# Primer Stage
FROM python:alpine3.16 as builder
WORKDIR /app
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt


# Segundo Stage
FROM python:alpine3.16
WORKDIR /app
COPY --from=builder /app/venv ./venv
COPY hello.py .
ENV PATH="/app/venv/bin:$PATH"
CMD ["python", "hello.py"]
