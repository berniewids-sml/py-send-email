docker build -t py-send-email .
docker run --env-file .env --rm py-send-email