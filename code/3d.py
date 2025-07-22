with open("./code/assets/laptop.txt") as file:
    f = file.read()

vertices = []
polygons = []
comments = []

print("1")

for line in f.split("\n"):
    if line == "\n" or line == "":
        continue
    if line[0:2] == "v ":
        vertices.append(line)
    elif line[0] == "f":
        polygons.append(line)
    elif line[0] == "#":
        comments.append(line)

print("2")

for index, vertex in enumerate(vertices):
    v = vertex.split()
    vertices[index] = f"\\left({v[1]}, {v[2]}, {v[3]}\\right)"

# print(vertices)

not_vertices_in_polygons = []

print("3")

for line in polygons:
    section = line.split(" ")
    v = []
    for s in section[1:-1]:
        v.append(s.split("/")[0])
    not_vertices_in_polygons.append(v)

vertices_in_polygons = []

print("4")

for thing in not_vertices_in_polygons:
    if len(thing) == 3:
        vertices_in_polygons.append(thing)
    elif len(thing) == 4:
        a = thing[0]
        b = thing[1]
        c = thing[2]
        d = thing[3]
        vertices_in_polygons.append([a, b, c])
        vertices_in_polygons.append([a, b, d])
    else:
        print(thing)

strings = ""

print("5")

for vertex_string in vertices_in_polygons:
    e1 = int(vertex_string[0])
    e2 = int(vertex_string[1])
    e3 = int(vertex_string[2])
    # s = f"\\operatorname\{triangle\}({vertices[e1-1]},{vertices[e2-1]},{vertices[e3-1]})\n"
    s = "\\operatorname{triangle}\\left(" + vertices[e1-1] + "," + vertices[e2-1] + "," + vertices[e3-1] + "\\right)\n"
    strings += s

print("6")

with open("./code/assets/output.txt", "w") as f:
    f.write(strings)

print("Done")