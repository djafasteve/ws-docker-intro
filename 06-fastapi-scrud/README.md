# FastAPI CRUD example with SQLite

This small example demonstrates how to build a FastAPI application that stores
"cuisine" objects in a local SQLite database. Each cuisine has a name, a cooking
time in minutes and a JSON document containing the ingredients.

## Running locally

You need Python 3.8+ with `fastapi`, `uvicorn` and `sqlalchemy` installed:

```bash
pip install fastapi uvicorn sqlalchemy
```

Start the application with:

```bash
uvicorn app.main:app --reload
```

The API will be available on `http://localhost:8000`. FastAPI automatically
provides an interactive documentation under `/docs`.

## Available endpoints

- `POST /cuisines/` - create a new cuisine entry
- `GET /cuisines/` - list cuisines
- `GET /cuisines/{id}` - read a specific cuisine
- `PUT /cuisines/{id}` - update a cuisine
- `DELETE /cuisines/{id}` - remove a cuisine

The database is stored in the file `cuisines.db` inside this directory. The
schema is created automatically on startup.

## Running with Docker

You can also build a container image for this API. The repository contains a
`Dockerfile` that installs the dependencies and launches `uvicorn`. Build and
run the image:

```bash
docker build -t fastapi-scrud .
docker run -p 8000:8000 fastapi-scrud
```

If you want to persist the SQLite database, mount the current directory as a
volume:

```bash
docker run -p 8000:8000 -v $(pwd):/app fastapi-scrud
```
