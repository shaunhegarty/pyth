FROM fkrull/multi-python

WORKDIR /app

RUN apt update && apt install pdftohtml -y

COPY tox.ini .

RUN tox -v; exit 0

COPY . .
