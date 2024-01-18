FROM python:3.8-slim

WORKDIR /rewards-serv

ENV FLASK_APP=app.py

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001", "--debugger"]
