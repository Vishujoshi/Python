# Dictionary in python
tavel={"India": "live in India","South Africa": "1 time"}

# Neting Dictionary in python
travel={"India": {"city visted": "Jalandhar" , "total visit":"10times"},"South Africa": "1 time"}
print(travel)
for key in travel:
    print(key)
    print(travel[key])
    for innerkey in travel[key]:
        print(innerkey)

# Neting list in Dictionary in python
travel={"India": "Multiple time", "travel": {"city visted" :  ["jalandhar","Punjab"] }, "total visit":"10times","South Africa": "1 time"} 

# Neting  Dictionary in list in python
travel= [
            {"India": "Multiple time","city visted": ["jalandhar","Punjab"] , "total visit":"10times"},
            {"South Africa": "1 time"} 
        ]