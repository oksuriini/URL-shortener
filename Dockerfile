FROM python:3.12.1

RUN useradd python

USER python

WORKDIR /home/python/programfiles

COPY . .

RUN python -m venv .venv
RUN . .venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5050

CMD [ "flask", "run", "--host=0.0.0.0" ]
