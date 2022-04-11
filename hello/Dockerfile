FROM python:alpine3.15 as builder

COPY requirements.txt .

RUN pip install -r requirements.txt



FROM python:alpine3.15

COPY --from=builder /root/.cache /root/.cache

WORKDIR /usr/src/app

COPY hello.py .

CMD [ "python", "hello.py" ]
