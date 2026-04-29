Copy env into .env
```
cp env .env
```

Edit .env according to your needs.

- Port 465 -> use USE_SSL=True
- Port 587 -> use USE_SSL=False

Build docker
```
docker build -t py-send-email .
```

Run docker
```
docker run --env-file .env --rm py-send-email
```