FROM python:3.7
COPY ./code/requirements.txt .
RUN python3 -m pip install --upgrade pip && pip install -r ./requirements.txt

COPY . /opt/ml/
WORKDIR /opt/ml/code

CMD ["main.py"]
