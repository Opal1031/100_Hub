import sys

mapping = {
    "animal": "Panthera tigris",
    "tree": "Pinus densiflora",
    "flower": "Forsythia koreana"
}

while True:
    s = sys.stdin.readline().strip()
    
    if (s == "end"):
        break
        
    print(mapping[s])