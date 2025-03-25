
end = 100000
count = 0
for i in range(1, end):
    for j in range(i, end):
        a = i
        b = j
        c = (a**2) + (b**2)
        d = (a + b) ** 2
        k = a * b
        c = c % k
        d = d % k
        
        if c == d:
            print("Match: " + str(a) + " " + str(b) + " Modulo: " + str(c))
        else:
            print("Unmatched: " + str(a) + " " + str(b))
            break

        count += 1
end -= 1
sample = (end / 2) * (end + 1)
print("Count: ", count)
if (sample==count):
    print("Trust worthy")
else:
    print("Broken somewhere")


