FROM python:alpine3.15

WORKDIR /usr/src/app

COPY requirements.txt .

COPY hello.py .

RUN pip install -r requirements.txt

CMD [ "python", "hello.py" ]
