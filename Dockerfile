FROM python:3.9
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
ENV PORT=5000
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
CMD ["python", "app.py"]
