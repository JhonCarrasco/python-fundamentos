
# Lists
l = ["Bob", "Rolf", "Anne"]
# Tuples
t = ("Bob", "Rolf", "Anne")
# Sets
s = {"Bob", "Rolf", "Anne"}

print("List:", l[1])
print("Tuple:", t[1])

l.append("Smith")
print("List:", l)

l.remove("Bob")
print("List:", l)

print("Tuple:", t)

s.add("Smith")
s.add("Smith")
print("Set:", s)

