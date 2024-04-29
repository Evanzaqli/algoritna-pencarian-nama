def search_name(name_to_find, names_list):
    found_indices = []
    for i, name in enumerate(names_list):
        if name == name_to_find:
            found_indices.append(i)
    return found_indices

# Contoh penggunaan:
names = ["Apel", "Jeruk", "anggur", "alpukat", "salak","semangka", "melon"]
name_to_search = "salak"
result = search_name(name_to_search, names)

if result:
    print(f"Nama '{name_to_search}' ditemukan di indeks: {', '.join(map(str, result))}.")
else:
    print(f"Nama '{name_to_search}' tidak ditemukan.")