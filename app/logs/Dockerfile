FROM python:3.9-slim
WORKDIR /app
COPY log_collector.py requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python", "log_collector.py"]
