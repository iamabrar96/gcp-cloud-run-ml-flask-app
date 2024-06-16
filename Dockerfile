FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/
COPY ./deploy.py /app/
COPY ./templates /app/templates/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install gunicorn

COPY ./linear_regression_model.joblib /app/
COPY ./scaler.joblib /app/

# Set the FLASK_APP environment variable
# ENV FLASK_APP=deploy.py

# Run the Flask application locally 
# CMD ["flask", "run", "--host=0.0.0.0"]

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 deploy:app