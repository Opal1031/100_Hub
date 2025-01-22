Subject = ["Algorithm", "DataAnalysis", "ArtificialIntelligence", "CyberSecurity", "Network", "Startup", "TestStrategy"]
Classroom = ["204", "207", "302", "B101", "303", "501", "105"]

N = int(input())

for i in range(N):
    idx = Subject.index(input())
    print(Classroom[idx])