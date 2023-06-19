# Docker

## Test moi truong docker

docker run --name starlette_crawl_code -p 5001:8000 -it -v ${PWD}/app:/app:rw tiangolo/uvicorn-gunicorn-starlette:python3.11-slim /bin/bash

## Build image sau khi test ok, va day len gitlab

docker login registry.gitlab.com
docker build -t registry.gitlab.com/q347/starlette_crawl_code:v0.4 .

## Test image tren gitlab

docker run --name starlette_crawl_code -p 5001:8000 -it -v ${PWD}/app:/app:rw registry.gitlab.com/q347/starlette_crawl_code:v0.4 /bin/bash

## Test docker-compose

docker-compose -f docker-compose-test.yml up

## Push image len gitlab

docker push registry.gitlab.com/q347/starlette_crawl_code:v0.4

# Run starlette

uvicorn app:app --reload --host 0.0.0.0 --port 8000

vvZ2b&5z!nw9Le

anyio==3.6.2
click==8.1.3
colorama==0.4.6
dnspython==2.2.1
h11==0.14.0
idna==3.4
Jinja2==3.1.2
MarkupSafe==2.1.1
motor==3.1.1
pymongo==4.3.3
sniffio==1.3.0
starlette==0.22.0
uvicorn==0.20.0
multipart==0.2.4
