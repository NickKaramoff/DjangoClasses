import multiprocessing as mp


def run():
    for i in range(10):
        print(i)


t1 = mp.Process(target=run)
t1.start()
