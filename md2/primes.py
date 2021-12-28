from random import randrange


def nBitRandom(n):
    return randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def isFermatPassed(x):
    return pow(2, x - 1, mod=x) == 1 and x % 2 != 0


def isMillerRabinPassed(mrc):
    """Run 20 iterations of Rabin Miller Primality test"""
    maxDivisionsByTwo = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert (2 ** maxDivisionsByTwo * ec == mrc - 1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True

        # Set number of trials here

    numberOfRabinTrials = 120
    for i in range(numberOfRabinTrials):
        round_tester = randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


def getPrime(n):
    p = nBitRandom(n)
    while not isFermatPassed(p) and not isMillerRabinPassed(p):
        p = nBitRandom(n)
    return p
