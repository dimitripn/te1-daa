import random

# Generate a list of 1000 random numbers between 0 and 1000
randomNumber1000 = [random.randint(0, 1000) for i in range(1000)]
sortedNumber1000 = randomNumber1000.copy()
sortedNumber1000.sort()
reversedNumber1000 = sortedNumber1000.copy()
reversedNumber1000.sort(reverse=True)

# Generate a list of 10000 random numbers between 0 and 10000
randomNumber10000 = [random.randint(0, 10000) for i in range(10000)]
sortedNumber10000 = randomNumber10000.copy()
sortedNumber10000.sort()
reversedNumber10000 = sortedNumber10000.copy()
reversedNumber10000.sort(reverse=True)

# Generate a list of 100000 random numbers between 0 and 100000
randomNumber100000 = [random.randint(0, 100000) for i in range(100000)]
sortedNumber100000 = randomNumber100000.copy()
sortedNumber100000.sort()
reversedNumber100000 = sortedNumber100000.copy()
reversedNumber100000.sort(reverse=True)

# Small list
with open('smallRandomNumber.txt', 'w') as f:
    for item in randomNumber1000:
        f.write("%s\n" % item)

with open('smallSortedNumber.txt', 'w') as f:
    for item in sortedNumber1000:
        f.write("%s\n" % item)

with open('smallReversedNumber.txt', 'w') as f:
    for item in reversedNumber1000:
        f.write("%s\n" % item)

# Medium list
with open('mediumRandomNumber.txt', 'w') as f:
    for item in randomNumber10000:
        f.write("%s\n" % item)

with open('mediumSortedNumber.txt', 'w') as f:
    for item in sortedNumber10000:
        f.write("%s\n" % item)

with open('mediumReversedNumber.txt', 'w') as f:
    for item in reversedNumber10000:
        f.write("%s\n" % item)


# Large list
with open('largeRandomNumber.txt', 'w') as f:
    for item in randomNumber100000:
        f.write("%s\n" % item)

with open('largeSortedNumber.txt', 'w') as f:
    for item in sortedNumber100000:
        f.write("%s\n" % item)

with open('largeReversedNumber.txt', 'w') as f:
    for item in reversedNumber100000:
        f.write("%s\n" % item)
