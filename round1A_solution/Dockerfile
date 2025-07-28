FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY extract_outline.py main.py ./
RUN mkdir -p /app/app/input /app/app/output

CMD ["python", "main.py"]
