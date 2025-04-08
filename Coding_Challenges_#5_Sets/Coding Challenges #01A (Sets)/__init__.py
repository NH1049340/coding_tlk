# Create the sets
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4}

# Check if set_b is a subset of set_a
is_subset = set_b.issubset(set_a)
print(f"Is set_b a subset of set_a? {is_subset}")

# Check if set_a is a superset of set_b
is_superset = set_a.issuperset(set_b)
print(f"Is set_a a superset of set_b? {is_superset}")