import time


def retry():

    for i in range(3):

        print(f"Attempt {i + 1} failed")

        time.sleep(1)

    print("Maximum retries reached")


retry()