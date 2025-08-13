FROM python:3.13.5

WORKDIR /terminal-chatbot
COPY . /terminal-chatbot

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "cli.py"]