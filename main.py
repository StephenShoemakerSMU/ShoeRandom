from ShoeRandom import ShoeRandom
from ShoeRandom import ShoeRandomInPlace
from ShoeRandom import ShoeStandardRandom
import hashlib
import random
import time
import csv
def main():
    
    
    SEED = hashlib.md5(b"Dr. F").hexdigest()
    

    inplace = ShoeRandomInPlace(SEED)
    random = ShoeStandardRandom(SEED)

    values = [1,10,100,1000,10000,100000,1000000, 10000000, 100000000]

    f=open("outputStandard.txt","w+")


    with open("standardTimes.csv", mode="w") as outputFile:
        timeWriter = csv.writer(outputFile)
        header = [1,2,3,4,5,6,7,8,9,10]
        header.insert(0,"")
        timeWriter.writerow(header)
        for pos in values:
            times= []
            for x in range(10):
                f.write("Standard Random Tile :" + str(pos) + "\n" )
                start = time.time()

                tile = generateTile(random.getSeedLocation(pos))

                end = time.time()
                totalTime = end - start
                times.insert(len(times), totalTime)
                f.write("Time : " + str(totalTime) + " s \n")
                f.write(tile)
                f.write("\n")
            times.insert(0,pos)
            timeWriter.writerow(times)


    f=open("outputInPlace.txt","w+")

    with open("inPlaceTimes.csv", mode="w") as outputFile:
        timeWriter = csv.writer(outputFile)
        header = [1,2,3,4,5,6,7,8,9,10]
        header.insert(0,"")
        timeWriter.writerow(header)
        for pos in values:
            times= []
            for x in range(10):
                f.write("In Place Tile :" + str(pos) + "\n" )
                start = time.time()

                tile = generateTile(inplace.getSeedLocation(pos))

                end = time.time()
                totalTime = end - start
                times.insert(len(times), totalTime)
                f.write("Time : " + str(totalTime) + " s \n")
                f.write(tile)
                f.write("\n")
            times.insert(0,pos)
            timeWriter.writerow(times)




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