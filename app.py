import time

import redis
from flask import Flask
from flask import render_template

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/html')
def hello():
    '''
    doc string
    '''
    # count = get_hit_count()
    # return 'Hello World! new features will be added soon '
    message = "hello world!!"
    return render_template('index.html', message=message)

@app.route('/')
def base():
    '''
    doc string
    '''
    # count = get_hit_count()
    return 'Hello World! new features will be added soon. there is one more route /html v20'
