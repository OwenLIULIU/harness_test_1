FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV COMMIT_SHA="unknown"
EXPOSE 8090
CMD ["python", "app.py"]
