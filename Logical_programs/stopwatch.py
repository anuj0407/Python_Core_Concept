import time
start = input("Press enter to start -- >")
start_time = time.time()
end =  input("Press enter to end -- >")
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")