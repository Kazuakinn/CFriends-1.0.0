FROM python:3.10
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app/
ENV ENV_PATH=/app/.env
EXPOSE 5000
CMD ["python", "app.py"]
