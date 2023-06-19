FROM tiangolo/uvicorn-gunicorn-starlette:python3.11-slim

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install -r requirements.txt
# RUN pip install python-multipart
# RUN pip install multipath
# RUN pip3 install requests