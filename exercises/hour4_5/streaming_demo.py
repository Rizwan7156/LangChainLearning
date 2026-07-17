import time

response = "LangChain enables developers to build AI powered applications."

for word in response.split():
    print(word, end=" ", flush=True)
    time.sleep(0.4)

print()