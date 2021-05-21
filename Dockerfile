FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
CMD ["main.py"]
ENTRYPOINT ["python3"]
