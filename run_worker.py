from rq import Worker, Queue, Connection
from app.worker import conn, listen


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
