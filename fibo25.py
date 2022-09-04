first = 1
result = 0
for _ in range(0, 25):
    result += first
    first = result-first
        
print(result)
