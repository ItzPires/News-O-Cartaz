docker build -t news-api .
docker run -p 8000:8000 news-api
docker run -p 8000:8000 -v $(pwd)/app:/app news-api
