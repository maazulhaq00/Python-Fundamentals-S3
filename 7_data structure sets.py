# --------- sets: unordered, unindexed, unique items

courses = { "JS", "BSJQ", "PHP", "MySQL", "JS" }
print(courses)

courses.add("ASP.NET")
print(courses)

# remove & discard

# courses.remove("ASP.NET")
courses.discard("ASP.NET")

# courses.remove("Flutter") # error 
courses.discard("Flutter")
print(courses)


for c in courses:
    print(c)

print("JS" in courses)
print("Flutter" in courses)


courses2 = {"R prog", "Python", "JS", "MySQL", "Tableau"}

print(courses | courses2) # union
print(courses & courses2) # intersection
print(courses - courses2) # difference
print(courses2 - courses) # difference