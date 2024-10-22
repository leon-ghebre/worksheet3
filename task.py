seq_length = int(input("Please enter the length of the sequence: "))
sequence = []
a = 0
k = 0
sequence.append(a)
for k in range(seq_length-1):
    k += 1
    if ((a - k )>0) and ((a - k) not in sequence):
        a -= k
    else:
        a += k
    sequence.append(a)

print(sequence)