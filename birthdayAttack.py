import random
import hashlib

def generateRandomHex():
    randomInt = int(random.random()*100000000)
    return hex(randomInt).encode('utf-8')

def generateRandomHash():
    hexStr = generateRandomHex()
    return hashlib.sha1(hexStr).hexdigest(), hexStr

def birthdayAttack():
    callsToSHA1 = 0
    SHA1Dict = {}
    
    matched = False
    while not matched:
        callsToSHA1 += 1
        randomHash, asciiStr = generateRandomHash()

        # Check if the SHA-1 hash has already been stored
        if SHA1Dict.get(randomHash[:10]) != None:
            # But it only counts if it was for another ascii string
            matched = SHA1Dict.get(randomHash[:10]).ascii != asciiStr

        # Store the 40-bits/first 10 hex chars
        SHA1Dict[ randomHash[:10] ] = {"hash": randomHash, "ascii":asciiStr}

        # Sanity check counter
        if (callsToSHA1 % 1000000) == 0:
          print("At {:,} million SHA-1 calls.".format(callsToSHA1 / 1000000))
        
    print("It took %i SHA-1 calls." % callsToSHA1)
    print("Matched %s to %s" % (hashToMatch, randomHash))

    return (asciiStr1, asciiStr2, callsToSHA1)

birthdayAttack()
