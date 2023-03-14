list = []
max = 0
words = 0
filename = input("Dose onoma arxeio: ")
arxeio = open(filename, "r")
for line in arxeio:
    count = 0
    for char in line:
        if char == " ":
            words += 1
            
        if char == ".":
            words += 1
            count += 1
        
    if count > max:
        max = count
        
    list.append(line)
    
print (words , "plithos lekseon")
print (max , "megalutero plithos")
for item in list:
    print (list.pop())
    
