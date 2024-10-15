FROM python:3.12.1-slim-bullseye
WORKDIR /usr/src/app
COPY . .
RUN apt update && apt install -y gcc ffmpeg && pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./bot.py" ]
