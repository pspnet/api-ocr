FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./app app
COPY ./requirements.txt requirements.txt
RUN apt-get update && \
        apt-get install -y --no-install-recommends libgl1 libglib2.0-0 && \
	pip install --no-cache-dir -q -r requirements.txt
EXPOSE $PORT

