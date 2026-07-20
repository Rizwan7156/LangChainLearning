def execute(task_function):

    print("[LOG] Starting task")

    try:

        result = task_function()

        print("[LOG] Task completed")

        return result

    except Exception as ex:

        print("[ERROR]", ex)