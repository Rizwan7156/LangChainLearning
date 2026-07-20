from harness import execute


def failing_task():
    raise Exception("Test Error")


execute(failing_task)