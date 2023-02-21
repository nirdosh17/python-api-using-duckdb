from flask import Flask
import duckdb, json

app = Flask(__name__)
db = duckdb.connect(database='test.duckdb', read_only=True)

@app.route('/stats', methods=['GET'])
def stats():
  db.execute("""
    SELECT
        CAST(joined_date AS VARCHAR) as date,
        MAX(row_number) as users_joined
      FROM (
        SELECT
          joined_date,
          ROW_NUMBER() OVER (PARTITION BY joined_date) as row_number
        FROM users
        WHERE joined_date BETWEEN (now()::TIMESTAMP - INTERVAL '2 years') AND now()
      ) GROUP BY joined_date
      ORDER BY joined_date ASC;
  """)
  stats = db.fetchall()

  columns = ['date', 'users_joined']
  items = [dict(zip(columns, row)) for row in stats]
  return json.dumps(items)

if __name__ == '__main__':
  app.run(port=8080, host='0.0.0.0')
