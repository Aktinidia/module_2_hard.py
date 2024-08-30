for k in range(3, 21):
    pairs = ''
    for i in range(1, k+1):
        for j in range(i+1, k):
            if k % (i+j) == 0:
                pairs += str(i)
                pairs += str(j)
    print(k, pairs)

