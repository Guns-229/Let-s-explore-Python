filename = "my_text.txt"
with open(filename) as f:
    lines = (line.strip('\n') for line in f)

for l in lines:
    print(l)
