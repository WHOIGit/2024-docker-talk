from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.environ.get('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    visitor_count = r.incr('visitors')
    return f'Hello, Docker! You are visitor number {visitor_count}.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
