from ShoeRandom import ShoeRandom
from ShoeRandom import ShoeRandomInPlace
from ShoeRandom import ShoeStandardRandom
import hashlib
import random
import time
def main():
    
    
    SEED = hashlib.md5(b"Dr. F").hexdigest()
    

    inplace = ShoeRandomInPlace(SEED)
    random = ShoeStandardRandom(SEED)

    values = [1,10,100,1000,10000,100000,1000000, 1000000, 10000000, 100000000]

    f=open("outputStandard.txt","w+")

    for pos in values:
        f.write("Standard Random Tile :" + str(pos) + "\n" )
        start = time.time()

        tile = generateTile(random.getSeedLocation(pos))

        end = time.time()
        totalTime = end - start
        f.write("Time : " + str(totalTime) + " s \n")
        f.write(tile)
        f.write("\n")


    f=open("outputInPlace.txt","w+")

    for pos in values:
        f.write("Standard In Place Tile :" + str(pos) + "\n" )
        start = time.time()

        tile = generateTile(inplace.getSeedLocation(pos))

        end = time.time()
        totalTime = end - start
        f.write("Time : " + str(totalTime) + " s \n")
        f.write(tile)
        f.write("\n")




def generateTile(seed):

    random.seed(seed)

    output=""
    for x in range(20):
        for y in range(20):
            currRand = random.randint(0,10)
            if(currRand is 10):
                output +="|"
            elif (currRand > 7):
                output +="_"
            else:
                output +="*"
        output+="\n"
    return output


main()