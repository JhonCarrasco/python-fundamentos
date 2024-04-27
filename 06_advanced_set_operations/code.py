# Set operations
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

differences = friends.difference(abroad)
print("difference: ", differences)


unions = friends.union(abroad)
print("union: ", unions)


intersections = friends.intersection(abroad)
print("intersection: ", intersections)