import time
from queue import Queue

request_queue = Queue()

request_id = 0


def generate_request():
    global request_id
    request_id += 1
    request = f"Request #{request_id}"
    request_queue.put(request)
    print(f"Request {request} is added to queue")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Request {request} is processed.")
    else:
        print(f"There are no requests.")


for _ in range(10):
    generate_request()
    process_request()
    time.sleep(1)
