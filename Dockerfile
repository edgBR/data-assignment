FROM python:3.7 AS build
COPY ./code/requirements.txt .
RUN python3 -m pip install --upgrade pip && pip install -r ./requirements.txt

FROM gcr.io/distroless/python3-debian10
COPY --from=build /usr/local/lib/python3.7/site-packages/  /usr/lib/python3.7/.

COPY . /opt/ml/
WORKDIR /opt/ml/code

CMD ["main.py"]
