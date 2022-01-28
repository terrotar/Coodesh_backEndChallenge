release: apt-get update && apt-get -y install cron && crontab app/crontab/root
web: uvicorn app.main:api --host=0.0.0.0 --port=${PORT:-5000}