Build docker
```
docker build -t py-send-email .
```

Run docker
```
docker run --env-file .env --rm py-send-email
```