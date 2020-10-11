numbers_list_chars = "1 2 3 4 5 6".split()
print(numbers_list_chars)

numbers_list_int = [int(x) for x in numbers_list_chars]
print(numbers_list_int)

for i in numbers_list_int:
    if i == 1:
        print("bulbasaur")
    elif i == 2:
        print("pikachu")
    elif i == 3:
        print("charmeder")
    else:
        print("invalid")

hash_map = {1: "bulbasaur", 2: "pikachu", 3: "charmeder"}
if hash_map.get(2) is None:
    print("invalid character")
else:
    print(hash_map.get(2))
