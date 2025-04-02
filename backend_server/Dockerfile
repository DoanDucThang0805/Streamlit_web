FROM python:3.10-slim

WORKDIR /backend

COPY requirements.txt /backend/requirements.txt
COPY src /backend/src
COPY Models /backend/Models


RUN pip install --no-cache-dir -r /backend/requirements.txt

EXPOSE 3001

CMD ["python", "/backend/src/main.py"]
