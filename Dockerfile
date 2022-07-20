FROM python:3.6-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip uninstall requests && pip install requests &&\
pip install -r requirements.txt &&\
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list &&\
apt update -y &&\
apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils &&\
apt install -y google-chrome-stable

COPY ./evolutio /code/




