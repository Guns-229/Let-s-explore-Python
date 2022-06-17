
try:
    with open("my_text.txt", "w+") as fp:
        fp.write(""""Context Managers are great,
Context Managers are our Friend.
So why not use them""")

    with open("my_text.txt") as file_handler:
        print("".join(file_handler.readlines()))
    print(file_handler.name)
    print(file_handler.readlines())
except Exception as e:
    print("* error:", e)
