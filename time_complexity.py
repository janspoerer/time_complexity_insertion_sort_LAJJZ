import random
import time
import matplotlib.pyplot as plt

results = []
decksizes = [10, 100, 1000, 10000]
repetition_limit = 100

for n in range(0, len(decksizes)):
    sum = 0
    for repetition in range( 1, repetition_limit ):
        state = list(range( 1, decksizes[n] ))
        random.shuffle( state )

        start = time.time()
        j = 1
        for j in range(j, len(state)):
            key = state[j]
            i = j - 1
            while i >= 0 and state[i] > key:
                state[i + 1] = state[i]
                i = i - 1
            state[i + 1] = key
        sum = sum + ( time.time() - start )
        # print (state)
        # print("operation took " + " {0:.9f}".format( time.time() - start ) + " seconds")
    average = sum / repetition_limit
    print(sum)
    results.append ( average )
    
plt.plot( results )
plt.ylabel('time complexity')
plt.show()