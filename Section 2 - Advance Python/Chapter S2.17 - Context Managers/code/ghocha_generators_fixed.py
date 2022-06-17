file_name = "my_text.txt"

# Fix 1: Using list instead of generator
with open(file_name) as f:
    lines = [line.strip('\n') for line in f]

for l in lines:
    print(l)

print("~^" * 16)
# Fix 2: moving access within the context
with open(file_name) as f:
    lines = (line.strip('\n') for line in f)

    for l in lines:
        print(l)

print("~^" * 16)


# Fix 3: Encapsulating it with generator
def send_lines(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip('\n')


for l in send_lines(file_name):
    print(l)
