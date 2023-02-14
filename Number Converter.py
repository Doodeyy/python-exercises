def decimalToBinOrHex(number , choice):
    hex = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    result = ""
    if choice == 1:
        while number > 0:
            result = str(number % 2) + result
            number = number // 2
            
        return result
        
    elif choice == 2:
        while number > 0:
            remain = number % 16
            item = hex[int(remain)]
            result = item + result
            number = number // 16
            
        return result
        
def binToDecOrHexToDec(number , choice):
    hex = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    result = 0
    if choice == 3:
        for i in range(len(number)):
            result = result * 2 + int(number[i])
            
        return  result        
        
    elif choice == 4:
        for i in range(len(number)):
            item = number[i]
            for j in range(len(hex)):
                if item == hex[j]:
                    result = result * 16 + j
        
        return result
            
      
choice = input("Επιλογες: 1)Απο δεκαδικο σε δυαδικο, 2)Απο δεκαδικο σε δεκαεξαδικο, 3)Απο δυαδικο σε δεκαδικο, 4)Απο δεκαεξαδικο σε δεκαδικο, 5)Εξοδος: ")
while choice != "5":
    
    if choice == "1":
        number = int(input("Δωσε δεκαδικο αριθμο: "))
        print (decimalToBinOrHex(number , 1))
        
    elif choice == "2":
        number = int(input("Δωσε δεκαδικο αριθμο: "))
        print (decimalToBinOrHex(number , 2))
        
    elif choice == "3":
        number = input("Δωσε δυαδικο αριθμο: ")
        print (binToDecOrHexToDec(number , 3))
    
    elif choice == "4":
        number = input("Δωσε δεκαεξαδικο αριθμο: ").upper()
        print (binToDecOrHexToDec(number , 4))
    
    else:
        print ("Λαθος επιλογη")
    
    choice = input("Επιλογες: 1)Απο δεκαδικο σε δυαδικο, 2)Απο δεκαδικο σε δεκαεξαδικο, 3)Απο δυαδικο σε δεκαδικο, 4)Απο δεκαεξαδικο σε δεκαδικο, 5)Εξοδος: ")
    
print ("Τελος προγραμματος")