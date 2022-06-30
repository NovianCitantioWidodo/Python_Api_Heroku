FROM python:3.9.13-slim-buster as builder
# RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc libpq-dev && apt-get install -y apt-utils

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --upgrade --user -r requirements.txt
COPY . .

# # # # #
FROM python:3.9.13-slim-buster
RUN mkdir /app
WORKDIR /app
COPY --from=builder /app .
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable:
ENV PATH=/root/.local/bin:$PATH

RUN chmod a+x gunicorn.sh
ENTRYPOINT ["sh","./gunicorn.sh"]