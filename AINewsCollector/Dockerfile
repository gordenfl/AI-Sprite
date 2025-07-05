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

   
# docker buildx build --platform linux/amd64 -t gordenfl/ainewscollector:latest . 
# 这个命令就可以将我的项目build 一个docker image, 在本地就会有一个image, 
# 然后你需要 login 到远程的docker hub上, 就是   docker login
# 按照步骤就可以登录上上去, 然后:
# 推送镜像: docker push gordenfl/ainewscollector:latest

#服务器端 pull镜像
# 

