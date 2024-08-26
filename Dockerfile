# Use a base Python image
FROM python:3.11-slim

WORKDIR /decoder

COPY . .

CMD ["python", "encryptor.py"]