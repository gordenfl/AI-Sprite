FROM python:3.12-slim AS base

WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ENABLECORS=false

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

#-----UI 镜像 ----------
EXPOSE 8501
CMD ["streamlit", "run", "app/worker.py"]


# docker build -t gordon/ainewscollector:latest . 
# 这个命令就可以将我的项目build 一个docker image
