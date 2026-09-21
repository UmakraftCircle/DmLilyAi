FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m lily && mkdir -p /app/data && chown -R lily /app/data /app/LilyAiGroqSupport
USER lily
ENV LILYAI_DATA_DIR=/app/data
EXPOSE 8000
CMD ["python", "-m", "LilyAiMain.main"]
