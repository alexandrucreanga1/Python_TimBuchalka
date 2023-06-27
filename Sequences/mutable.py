shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

print("look for spam: ", shopping_list.count("spam"))


another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(id(another_list))

another_list += ["carrot"]
print(id(shopping_list))
print(id(another_list))
print(shopping_list)
print(another_list)

a = b = c = d = e = f = another_list
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)
print(shopping_list)


