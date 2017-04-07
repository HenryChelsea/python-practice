import threading
import Queue
import sys
import random
import string

FILE_PATH = 'word.txt'


def random_generate_big_file(word_len):
    with open(FILE_PATH, 'wb') as f:
        for _ in xrange(100000):
            word = ''.join((random.choice(string.letters) for _ in range(word_len)))
            f.write(word)
            f.write('\n')

            # t0 = time.time()
            # open("bla.txt", "wb").write(''.join(random.choice(string.ascii_lowercase) for i in xrange(10 ** 7)))
            # d = time.time() - t0
            # print "duration: %.2f s." % d
# def do_work(in_queue, out_queue):
#     while True:
#         item = in_queue.get()
#         # process
#         result = item
#         out_queue.put(result)
#         in_queue.task_done()
#
# if __name__ == "__main__":
#     work = Queue.Queue()
#     results = Queue.Queue()
#     total = 20
#
#     # start for workers
#     for i in xrange(4):
#         t = threading.Thread(target=do_work, args=(work, results))
#         t.daemon = True
#         t.start()
#
#     # produce data
#     for i in xrange(total):
#         work.put(i)
#
#     work.join()
#
#     # get the results
#     for i in xrange(total):
#         print results.get()
#
#     sys.exit()

# import array
# import os
#
# fn = 'data.bin'
# a = array.array('h')
# a.fromfile(open(fn, 'rb'), os.path.getsize(fn)/a.itemsize)

import itertools
import io






if __name__ == '__main__':