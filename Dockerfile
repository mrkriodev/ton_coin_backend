FROM python:3.7-alpine
RUN pip install Flask
COPY . .
EXPOSE 9001
CMD ["python", "main.py"]