collection = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while True:
    count = 0
    sentence = input()
    
    if sentence == "#":
        break
        
    for i in sentence:
        if i in collection:
            count += 1
            
    print(count)