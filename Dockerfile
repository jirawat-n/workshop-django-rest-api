FROM python:3.8
WORKDIR /api_workshop
COPY requirements.txt /api_workshop/
RUN pip install -r requirements.txt
COPY api_workshop/ /api_workshop/