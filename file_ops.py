def read_file_bytes(path):
    with open(path, "rb") as f:
        return f.read()

def write_file_bytes(path, bts):
    with open(path, "wb") as f:
        f.write(bts)
