FROM python:slim-buster	

WORKDIR /getUrl
COPY . /getUrl
RUN git clone https://github.com/sxbai/live-docker.git && mv live-docker/* ./getUrl/ && pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ -r /getUrl/requirements.txt \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
CMD ["python", "main.py"]
