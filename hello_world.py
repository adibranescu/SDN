print("Test")
originals = ["4. A New Hope", "5. Empire Strikes Back", "6. Return of the Jedi"]

prequel = []
prequel.append("1. The Phantom Menace")
prequel.append("2. Attack of the Clones")
prequel.append("3. Revenge of the Sith")

# print(originals)
# print(prequel)

for movie in originals:
    print(movie)

saga = originals + prequel

saga.sort()
print(saga)
