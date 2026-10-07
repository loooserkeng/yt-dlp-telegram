WORKDIR /app

ENV DATA_DIR="/app/data"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY config.py .

CMD ["python", "main.py"]
