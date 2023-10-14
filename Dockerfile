FROM svizor/zoomcamp-model:3.10.12-slim

RUN apt-get update && apt-get install -y gcc

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "app.py", "./"] /app/

RUN pipenv install --deploy --system 
#--ignore-pipfile

# EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "app:app"]
