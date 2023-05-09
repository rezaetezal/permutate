FROM python:3.11-alpine
WORKDIR /app

COPY requirements.txt permutate.py ./
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "permutate.py" ]
