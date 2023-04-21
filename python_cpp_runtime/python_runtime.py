import time

start_time = time.time()

# Calculate the sum of the first 10 million numbers
total = 0
for i in range(10000000):
    total += i

end_time = time.time()

print("Total:", total)
print("Time:", end_time - start_time)
