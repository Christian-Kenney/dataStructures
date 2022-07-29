def bubbleSort(listOfNums): 
  for i in range(len(listOfNums)):
    
    swapped = False
    
    for j in range(0, len(listOfNums) - i - 1):
        
      if listOfNums[j] > listOfNums[j+1]:

        temp = listOfNums[j]
        listOfNums[j] = listOfNums[j+1]
        listOfNums[j+1] = temp

        swapped = True
          
    if not swapped:
      break

def selectionSort(listOfNums):  
    for i in range(len(listOfNums)):
        minNum = i

        for j in range(i + 1,len(listOfNums)):
         
            if listOfNums[j] < listOfNums[minNum]:
                minNum = j
         
        (listOfNums[i], listOfNums[minNum]) = (listOfNums[minNum], listOfNums[i])

def insertionSort(listOfNums): 

    for i in range(1, len(listOfNums)):
        key = listOfNums[i]
        j = i - 1
            
        while j >= 0 and key < listOfNums[j]:
            listOfNums[j + 1] = listOfNums[j]
            j = j - 1
            
        listOfNums[j + 1] = key

def dictSearch(nameOfBook):
    dictOfBooks = {"Hamlet":"Shakespeare", "Great Expectations":"Charles Dickens", "The Grapes of Wrath":"John Steinbeck"}
    output = dictOfBooks[nameOfBook]
    return output

def listSearch(i):
    listOfMovies = ["The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump"]
    return listOfMovies[i]
    

if __name__== '__main__':
    bubbleNums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubbleSort(bubbleNums)
    print("bubble: ", bubbleNums)
    
    sortNums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    selectionSort(sortNums)
    print("sort: ", sortNums)
    
    inserNums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertionSort(inserNums)
    print("insertion: ", inserNums)
    
    
    print(dictSearch("Hamlet"))
    print(listSearch(1))
    
   