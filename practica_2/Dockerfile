# Dockerfile, Image, Container
FROM python:3.9

ADD recomendador_jugadores.py .
ADD fifa23players.csv .

RUN pip install pandas

CMD ["python", "./recomendador_jugadores.py"]





