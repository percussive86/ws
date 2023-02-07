# common/util.py
def id_generator():
    count = 0
    while True:
        count += 1
        yield count