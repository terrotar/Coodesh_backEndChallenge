FROM python:3.9

RUN apt-get update && apt-get -y install cron

WORKDIR /Coodesh_backEndChallenge

COPY ./requirements.txt /Coodesh_backEndChallenge/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Coodesh_backEndChallenge/requirements.txt

COPY ./app /Coodesh_backEndChallenge/app

COPY ./run.py /Coodesh_backEndChallenge/run.py

COPY ./run.sh /Coodesh_backEndChallenge/run.sh

COPY ./README.md /Coodesh_backEndChallenge/README.md

ADD ./app/crontab/root /etc/cron.d/root

RUN chmod +x /Coodesh_backEndChallenge/app/crontab/update_articles.py

CMD ["bash", "./run.sh"]
