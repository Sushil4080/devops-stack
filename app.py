from flask import Flask, jsonify
import os
import redis
import psycopg2

app = Flask(__name__)

# Redis connection
cache = redis.Redis(host="redis", port=6379)

# PostgreSQL connection
def get_db():
    return psycopg2.connect(
        host="db",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

@app.get("/")
def home():
    return jsonify({"message": "DevOps Stack Running 🚀"})

@app.get("/cache")
def cache_example():
    cache.incr("hits")
    return jsonify({"hits": cache.get("hits").decode()})

@app.get("/db")
def db_example():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    conn.close()
    return jsonify({"db_version": version[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
