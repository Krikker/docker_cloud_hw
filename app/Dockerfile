FROM python:3.11-slim
RUN pip install psycopg2-binary
COPY docker_test.py /app/docker_test.py
WORKDIR /app
CMD ["python", "docker_test.py"]
