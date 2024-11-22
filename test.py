def join_last_words(splitted: list):
    splitted.pop(0)
    print(" ".join(splitted))


a = "POST Stack Overflow Hi"
splitted = a.split(" ")
if splitted[0] == "POST":
    print(True)
    join_last_words(splitted=splitted)
