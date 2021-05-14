
listOfValues = [0,3,2,3,4,5,6,7,8,9,10]
bestIndex = []


def findBestFirst():
    x = 1
    while(x<=10):
        best = min(listOfValues[x],listOfValues[x+1])
        if (best == listOfValues[x]):
            bestIndex.append(x)
            x = 2*x+1
        else:
            bestIndex.append(x+1)
            x = x+1
            x = 2*x+1
            
        

        
            
        
def printBestFirst():
    length = len(bestIndex)
    for x in range(length):
        index = bestIndex[x]
        print(listOfValues[index])


findBestFirst()

printBestFirst()


         
        
        
    
