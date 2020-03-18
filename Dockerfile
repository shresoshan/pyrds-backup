FROM laudio/pyodbc

WORKDIR /source

COPY ["src", "./src"]
COPY execute.py .
COPY setup.py .
COPY __init__.py .

#ENTRYPOINT ["python", "execute.py"]
