import random, time, queue

from multiprocessing.managers import BaseManager

task_queue = queue.Queue()

result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

manager = QueueManager(address=('', 5000), authkey=b'abc')

manager.start()

task = manager.get_task_queue()
 9