testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


# ==========================
# applyToEach #1
# ==========================
applyToEach(testList, abs)



# =============================
# applyToEach #2
# =============================
def addOne(x):
    return x + 1
applyToEach(testList, addOne)



# =============================
# applyToEach #3
# =============================
def square(x):
    return abs(x) ** 2
    
applyToEach(testList, square)