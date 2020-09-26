import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv(
    'REDISTOGO_URL', 'redis://redistogo:3dd68954d06aca596e12a0b8a863a5ae@pike.redistogo.com:10842/')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
