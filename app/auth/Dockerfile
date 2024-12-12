FROM python:3.9-slim
WORKDIR /app
COPY auth.py requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python", "auth.py"]
