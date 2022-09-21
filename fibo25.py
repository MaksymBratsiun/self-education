first = 1
result = 0
for _ in range(0, 152):
    result += first
    first = result-first
        
print(result)
