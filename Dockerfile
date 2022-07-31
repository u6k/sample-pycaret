FROM python:3.8-slim
LABEL maintainer="u6k.apps@gmail.com"

# Install
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libgomp1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -U pip && \
    pip install pipenv

# Install python packages
WORKDIR /var/myapp
VOLUME /var/myapp

COPY Pipfile Pipfile.lock ./
RUN pipenv sync --dev

CMD ["pipenv", "run", "python", "sample_pycaret.py"]
