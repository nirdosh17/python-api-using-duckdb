# Containerized Python API using DuckDB
Sample Containerized Python API using [DuckDB](https://duckdb.org/)

## Flask API
The service exposes `GET http://localhost:8080/stats` api which returns aggregated user count from DuckDB database `test.duckdb`.

**API response:**
```json
[
	{
		"date": "2021-02-20",
		"users_joined": 2598
	},
	{
		"date": "2021-02-21",
		"users_joined": 2578
	}
]
```

## Running without docker
```bash
make run
```

## Running as a container
```bash
# builds docker image
make docker.build

# runs docker image
make docker.run
```

## Test Data
Test data is coming from database file `test.duckdb`. It contains a table called `users` which has following fields with ~1 million randomly generated rows:

| id (int32)| joined_date (date) | name (varchar)|    email (varchar)      |
|-----------|--------------------|---------------|-------------------------|
|      1    |     2021-09-14     |  Jarret Kuhn  |  carsondooley@wolf.name |
