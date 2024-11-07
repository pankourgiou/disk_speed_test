import time
with open("test_file", "wb") as f:
    start = time.time()
    f.write(b"0" * (1024 * 1024 * 100))  # Write 100 MB
    end = time.time()
print(f"Write speed: {100 / (end - start)} MB/s")
