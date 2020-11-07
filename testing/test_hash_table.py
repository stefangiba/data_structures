from hash_table.hash_table import HashTable

hash_table = HashTable(10)
hash_table.set(100, 1)
hash_table.set(25, 2)
hash_table.set(25, 3)

a = hash_table.get(25)
print(a)
print(hash_table.keys())
print(hash_table.values())
print(hash_table.contains_key(73))
print(hash_table.contains_value(5))

for key in hash_table.keys():
    print(key, hash_table.get(key))
