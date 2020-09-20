import pickle

# Guardar la lista [1, 2, 3, 4] en el archivo "obj.pickle".
obj = [1, 2, 3, 4]
with open("obj.pickle", "wb") as f:
    pickle.dump(obj, f)
with open("obj.pickle", "rb") as f:
    obj = pickle.load(f)
# Imprime [1, 2, 3, 4].
print(obj)
